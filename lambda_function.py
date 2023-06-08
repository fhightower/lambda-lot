def lambda_handler(event, context):
    count = int(event.get('queryStringParameters', {}).get('count') or 1)

    response = {
        'statusCode': 200,
        'body': 'λ' * count
    }
    return response

