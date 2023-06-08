import sentry_sdk


def lambda_handler(event, context):
    query_strings = event.get('queryStringParameters') or {}
    count = 1
    if qs_count := query_strings.get('count'):
        count = int(qs_count)

    response = {
        'statusCode': 200,
        'body': 'λ' * count
    }
    return response

