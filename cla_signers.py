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

"""TODO: High-level file comment."""

import sys
try:
    import yaml
except:
    from third_party.python import yaml


def ParseYaml(filename):
    with open(filename) as yaml_input:
        return yaml.safe_load(yaml_input.read())


def Validate(filename):
    data = ParseYaml(filename)


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

    if command == 'validate':
        Validate(filename)
    else:
        sys.stderr.write('Invalid command: %s\n' % command)
        ShowSyntax(program)
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv)
