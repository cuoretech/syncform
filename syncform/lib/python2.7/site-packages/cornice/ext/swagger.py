# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


def generate_swagger_spec(services, name, base_url, version, **kwargs):
    """Utility to turn cornice web services into a Swagger-readable file.

    See https://helloreverb.com/developers/swagger for more information.
    """

    doc = {
        'apiVersion': version,
        'swaggerVersion': '1.2',
        'basePath': base_url,
        'apis': [],
        'info': {
            'title': name
        }
    }

    for service in services:
        api = {
            'path': service.path,
            'operations': []
        }
        if service.description:
            api['description'] = service.description

        for method, view, args in service.definitions:
            operation = {
                'method': method,
                'produces': service.get_contenttypes(method) or 'application/json',
                'consumes': service.get_acceptable(method) or 'application/json'
            }

            if getattr(view, '__doc__'):
                operation['summary'] = view.__doc__

            if 'schema' in args:
                schema = args['schema']
                operation['parameters'] = []
                parameter = {}

                # We want to get all the attributes which aren't specifically
                # for the body, because swagger deserves them a special
                # treatment (see after).
                attributes = schema.as_dict(
                    schema.get_attributes(location=('path', 'querystring', 'header'))
                )

                for name, values in attributes.items():
                    paramType = values['location']
                    if paramType == 'querystring':
                        if '{%s}' % name in service.path:
                            paramType = 'path'
                        else:
                            paramType = 'query'
                    parameter['paramType'] = paramType
                    parameter['name'] = name
                    if values['description']:
                        parameter['description'] = values['description']
                    parameter['required'] = values['required']

                    # If the type is a primitive one, just put in in the "type"
                    # field.
                    primitive_values = {'str': 'string'}
                    type_ = ''
                    if values['type'] in primitive_values:
                        type_ = primitive_values[values['type']]
                    else:
                        # Otherwise, we need to create a model and link to it.
                        pass
                    parameter['type'] = type_

                # Get the parameters for the body.
                attributes = schema.as_dict(
                    schema.get_attributes(location=('body'))
                )

                operation['parameters'].append(parameter)

        api['operations'].append(operation)
        doc['apis'].append(api)
    return doc
