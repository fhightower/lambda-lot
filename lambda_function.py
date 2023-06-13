import os

import newrelic.agent
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

newrelic.agent.initialize()
sentry_sdk.init(
    dsn=f"{os.getenv('sentry_dsn')}",
    integrations=[
        AwsLambdaIntegration(timeout_warning=True),
    ],
    traces_sample_rate=1.0,
)


@newrelic.agent.lambda_handler()
def lambda_handler(event, context):
    query_strings = event.get('queryStringParameters') or {}
    count = 1
    if qs_count := query_strings.get('count'):
        try:
            count = int(qs_count)
        except ValueError as e:
            print("Capturing exception!")
            sentry_sdk.capture_exception(e)
            newrelic.agent.record_custom_event('Error', {'foo': 'bar'})

    response = {
        'statusCode': 200,
        'body': 'λ' * count
    }
    return response

