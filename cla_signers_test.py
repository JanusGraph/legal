#!/usr/bin/python
#
# Copyright 2019 JanusGraph Authors
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

import unittest
import cla_signers


class ClaSignersTest(unittest.TestCase):

    def _ValidateData(self, data):
        return cla_signers.ValidateData(cla_signers.ParseYamlString(data))

    def testValidData(self):
        data = """\
people:
  - name: foo
    email: bar
    github: baz

bots:
  - name: foo1
    email: bar1
    github: baz1

companies:
  - name: Foo
    people:
     - name: foo2
       email: bar2
       github: baz2
"""
        self.assertEqual(0, self._ValidateData(data))

    def testEmptyStringInvalid(self):
        data = """\
people:
  - name:
    email:
    github:

bots:
  - name:
    email:
    github:

companies:
  - name:
    people:
     - name:
       email:
       github:
"""
        self.assertNotEqual(0, self._ValidateData(data))


if __name__ == '__main__':
    unittest.main()
