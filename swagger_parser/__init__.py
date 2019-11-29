from .json_parser import *
from .mock_generator import *
import os
import sys
sys.path.append('../')


base_dir = '%s/static/mocks' % os.getcwd()

file_to_path = os.path.dirname(os.path.abspath('swagger.json')) + '/static/swagger.json'

parser = JsonParser(file_to_path)
ENDPOINTS = parser.parse_json()

mock_generator = MockGenerator(ENDPOINTS)

if not os.path.exists(base_dir):
    mock_generator.create_mock()


