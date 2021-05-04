#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © Her Majesty the Queen in Right of Canada, as represented
# by the Minister of Statistics Canada, 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest, json
from jsonschema import Draft7Validator, validate

class MetadataSchemaTestCase(unittest.TestCase):
    def setUp(self):
        print("+++++++++++++++++++++++++++++++++++++++")
        print("Beginning new TestCase %s" % self._testMethodName)
        print("+++++++++++++++++++++++++++++++++++++++")

    def test_SchemaValidation(self):
        with open("local-data-catalog-spec/jsonschema_metadata.json") as f:
            self.schema=json.load(f)

        print("Schema validator result:")
        result = Draft7Validator.check_schema(self.schema)
        if result is None:
            print("Schema is valid.")
        else:
            print(result)
