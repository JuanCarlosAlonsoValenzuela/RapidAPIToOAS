import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', str(text)).strip()


def obtain_html(url):
    browser = webdriver.Firefox()
    browser.get(url)
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "api-page-body"))
        )
    finally:
        browser.quit
    bs = BeautifulSoup(browser.page_source, "html.parser")
    data = remove_tags(bs.find('script', {'id':'__NEXT_DATA__'}))
    return bs, data


def print_oas(version, endpoints):
    first_part = generate_first_part(version)
    print(first_part)

    endpoints_part = generate_paths(endpoints)
    print(endpoints_part)



def generate_first_part(version):
    res = {
        'swagger': '2.0',
        'info': {
            'description': 'Description placeholder',
            'title': 'Title placeholder',
            'version': 'Version placeholder'
        },
        'host': 'petstore.swagger.io',
        'basePath': '/',
        'schemes': ['https']
    }

    res['info']['description'] = version['description']
    res['info']['title'] = version['api']
    res['info']['version'] = version['id']

    res['host'] = version['publicdns'][0]['address']

    return yaml.dump(res)


# TODO: Regular expressions and datetime
def generate_paths(endpoints):
    res = {
        'paths': {}
    }

    for path in endpoints:

        route = path['route']
        method = path['method'].lower()

        p = {method: {
            'summary': "",
            'description': "",
            'operationId': "",
            'parameters': [],
            'responses': {
                '200': {
                    'description': 'Ok'
                },
                'default': {
                    'description': 'Unexpected error'
                }
            }

        }
        }

        p[method]['summary'] = path['summary'] if path['summary'] is not None else ""
        p[method]['description'] = path['description'] if path['description'] is not None else ""
        p[method]['operationId'] = path['id'] if path['id'] is not None else ""

        for parameter in path['params']['parameters'] if path['params'] is not None else []:
            param = {
                'name': '',
                'in': '',
                'required': True,
                'description': '',
            }

            inType = 'query' if parameter['querystring'] else 'path'
            requiredBool = True if parameter['condition'] == 'REQUIRED' else False

            param['name'] = parameter['name']
            param['in'] = inType
            param['required'] = requiredBool
            param['description'] = parameter['description'] if 'description' in list(parameter.keys()) else " "

            #             if 'value' in list(parameter.keys()):
            #                 param['example'] = parameter['value']

            # SCHEMA
            if parameter['paramType'] == 'DATE (YYYY-MM-DD)':
                typeList = parameter['paramType'].split(" ")
                param['type'] = 'string'
                param['pattern'] = 'date'
            elif parameter['paramType'] == 'ENUM':
                param['schema'] = {
                    'type': 'string',
                    'enum': parameter['options']
                }
            else:
                param['type'] = parameter['paramType'].lower()
                # Caso normal

            p[method]['parameters'].append(param)

        res['paths'][route] = p
    return yaml.dump(res)