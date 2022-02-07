import boto3
import botocore.exceptions

client = boto3.resource("dynamodb")
table = client.Table("counter")

def lambda_handler(event, context):
    try:
        table.put_item(
            Item = {
                'id': 1,
                'visitCount': 1,
            },
            ConditionExpression = 'attribute_not_exists(id)'
        )
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise
    counter = table.get_item(Key={'id': 1})
    newcounter = counter['Item']['visitCount'] + 1
    table.update_item(
        Key={'id': 1},
        UpdateExpression='SET visitCount = :value1',
        ExpressionAttributeValues={':value1': newcounter}
    )
    return {
	'body': newcounter,
	'statusCode': 200,
	'headers': {
		'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'application/json',
                'Access-Control-Allow-Methods': 'OPTIONS,GET',
	}
    }
