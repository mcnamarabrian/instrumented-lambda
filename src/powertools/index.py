import os

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
import requests

logger = Logger()

url = os.getenv('URL', 'https://www.google.com')

@logger.inject_lambda_context
def lambda_handler(event, context):
    result = requests.get(url)
    logger.info({"function_name": "powertools", "url": url, "http_status_code": result.status_code})
    return({"function_name": "powertools", "url": url, "http_status_code": result.status_code})
