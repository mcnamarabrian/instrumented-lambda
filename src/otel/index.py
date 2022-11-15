import os

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
import requests
from opentelemetry.instrumentation.requests import RequestsInstrumentor

logger = Logger()

url = os.getenv('URL', 'https://www.google.com')

@logger.inject_lambda_context
def lambda_handler(event, context):
    result = requests.get(url)
    logger.info({"function_name": "otel", "url": url, "http_status_code": result.status_code})
    return({"function_name": "otel", "url": url, "http_status_code": result.status_code})
