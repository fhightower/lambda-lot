import logging
import os
import random

import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

sentry_sdk.init(
    dsn=f"{os.getenv('sentry_dsn')}",
    integrations=[
        AwsLambdaIntegration(timeout_warning=True),
    ],
    traces_sample_rate=1.0,
)


def lambda_handler(event, context):
    query_strings = event.get('queryStringParameters') or {}
    count = 1
    if qs_count := query_strings.get('count'):
        try:
            count = int(qs_count)
        except ValueError as e:
            logging.warning("Error converting to int!")
            sentry_sdk.capture_exception(e)

    # occassionally fail just to make life exciting
    if count == 1 and random.randint(1, 10) >= 8:
        logging.error("Random error!")
        raise RuntimeError("Oppps!")
    # occassionally fail just to make life exciting
    elif count != 1 and random.randint(1, 10) >= 9:
        unknown_quantity = 1 / 0

    response = {
        'statusCode': 200,
        'body': 'λ' * count
    }
    return response
