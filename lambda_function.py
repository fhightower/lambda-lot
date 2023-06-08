import os

import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

sentry_sdk.init(
    dsn=os.getenv('sentry_dsn'),
    integrations=[
        AwsLambdaIntegration(timeout_warning=True),
    ],
    traces_sample_rate=1.0,
)

print(os.getenv('sentry_dsn'))


def lambda_handler(event, context):
    query_strings = event.get('queryStringParameters') or {}
    count = 1
    if qs_count := query_strings.get('count'):
        try:
            count = int(qs_count)
        except ValueError as e:
            print("Capturing exception!")
            sentry_sdk.capture_exception(e)

    response = {
        'statusCode': 200,
        'body': 'λ' * count
    }
    return response

