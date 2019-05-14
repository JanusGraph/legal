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

VERB = @
ifeq ($(VERBOSE),1)
	VERB =
endif

PYTHON_DIR = third_party/python
CLA_SCRIPT = ./cla_signers.py
CLA_SIGNERS = CLA_SIGNERS.yaml

default:
	$(VERB) echo "Available actions: stats, validate, pip-install, test"

stats:
	$(VERB) $(CLA_SCRIPT) stats $(CLA_SIGNERS)

pip-install:
	$(VERB) pip install -r requirements.txt -t $(PYTHON_DIR)

validate:
	$(VERB) $(CLA_SCRIPT) validate $(CLA_SIGNERS)

test: validate
	$(VERB) python -m unittest discover -p '*_test.py'
