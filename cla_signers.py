#!/usr/bin/python
#
# Copyright 2017 JanusGraph Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Validator for the CLA signers YAML file."""

import sys
try:
    import yaml
except:
    from third_party.python import yaml


def ParseYamlString(data):
    return yaml.safe_load(data)


def ParseYamlFile(filename):
    with open(filename) as yaml_input:
        return ParseYamlString(yaml_input.read())


def PrintStatistics(data):
    individuals = len(data['people'])
    total_people = individuals

    print('Individuals: %d' % individuals)
    companies = data['companies']
    print('Companies: %d' % len(companies))
    for company in companies:
        # Several people appear more than once in the YAML config for a single
        # company to handle multiple email addresses per person for various
        # reasons.
        #
        # This eliminates overcounting by creating a set of all GitHub user ids,
        # such that duplicate entries for a single person will be eliminated
        # since their GitHub id is unique, even if the spelling of their name
        # varies.
        num_people = len(set([person['github'] for person in company['people']]))
        print('  %s: %s' % (company['name'], num_people))
        total_people += num_people

    print('Total signers: %d' % total_people)


def ValidateAccounts(accounts):
    """Returns whether given list of accounts are valid, with errors if not.

    This function works on a single set of accounts, whether people or bots.

    Args:
        accounts ([dict]): a list of accounts to validate

    Returns:
        (bool, [str]) or (bool, None): first element is whethe the data is
        valid; second parameter is list of error strings if data is not valid.
    """
    accounts_keys = ('name', 'email', 'github')
    for account in accounts:
        if not account:
            return (False, ['Invalid empty account found'])
        if sorted(account.keys()) != sorted(accounts_keys):
            return (False, ['The only allowed and required keys for people/bot accounts are: %s.' % str(accounts_keys),
                            'Invalid account record: %s' % account])
        for key in accounts_keys:
            # Covers value being either `None` or empty string.
            if not account[key]:
                return (False, 'The key "%s" is empty in account (%s)\n' % (key, account))
    return (True, None)


def ValidateData(data):
    """Returns whether data is valid, with errors if not.

    This function works on an entire config file, including individuals, bots,
    and companies.

    Args:
        data (dict): full config file

    Returns:
        (bool, [str]) or (bool, None): first element is whethe the data is
        valid; second parameter is list of error strings if data is not valid.
    """
    if 'people' in data:
        valid, errors = ValidateAccounts(data['people'])
        if not valid:
            return (False, errors)

    if 'bots' in data:
        valid, errors = ValidateAccounts(data['bots'])
        if not valid:
            return (False, errors)

    if 'companies' in data:
        company_keys = ('name', 'people')
        for company in data['companies']:
            if not company:
                return (False, ['Invalid company found'])
            if sorted(company.keys()) != sorted(company_keys):
                return (False, ['The only allowed and required keys for `company` are: %s.' % str(company_keys),
                                'Invalid company record: %s' % company])
            valid, errors = ValidateAccounts(company['people'])
            if not valid:
                return (False, errors)

    return (True, None)


def ShowSyntax(program):
    sys.stderr.write("""\
Syntax: %s [command] [file]

Commands:
  validate: verify invariants in given config file
""" % program)

def main(argv):
    program = argv[0]
    if len(argv) < 3:
        ShowSyntax(program)
        sys.exit(1)

    command = argv[1]
    filename = argv[2]
    data = ParseYamlFile(filename)

    if command == 'stats':
        sys.exit(PrintStatistics(data))
    elif command == 'validate':
        valid, errors = ValidateData(data)
        if not valid:
            for err in errors:
                sys.stderr.write('%s\n' % err)
                sys.exit(1)
    else:
        sys.stderr.write('Invalid command: %s\n' % command)
        ShowSyntax(program)
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv)
