# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
from cornice.tests.support import TestCase
from cornice.service import Service
from cornice.ext.swagger import generate_swagger_spec
from cornice.tests.validationapp import FooBarSchema


class TestSwaggerGeneration(TestCase):

    def test_generate_spore_description(self):

        coffee = Service(name='coffee', path='/coffee/{bar}/{id}')

        @coffee.post()
        def create_coffee(req):
            """create a new coffee"""
            pass

        @coffee.delete(schema=FooBarSchema)
        def delete_coffee(req):
            """Removes a coffee"""
            pass

        doc = generate_swagger_spec(
            [coffee], name="oh yeah",
            base_url="http://localhost/", version="1.0")

        # Basic swagger fields should be present.
        self.assertEqual(doc['info']['title'], "oh yeah")
        self.assertEqual(doc['basePath'], "http://localhost/")
        self.assertEqual(doc['apiVersion'], "1.0")

        self.assertEqual(len(doc['apis']), 1)
        from pdb import set_trace; set_trace()
