def lambda_handler(event, context):
    query_strings = event.get('queryStringParameters', {})
    count = int(query_strings.get('count') or 1)

    response = {
        'statusCode': 200,
        'body': 'λ' * count
    }
    return response

