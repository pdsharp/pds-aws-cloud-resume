import boto3
from moto import mock_dynamodb2


@mock_dynamodb2   
def test_counter():
        from counter.app import lambda_handler

        client = boto3.resource("dynamodb", region_name='us-west-2')
        table = client.Table("counter")
        client.create_table(
            TableName="counter",
            KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"},
            ],
            AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "N"},
            ]
        )
        table.put_item(Item = {'id': 1, 'visitCount': 1})
        response = lambda_handler(None, None)
        counter = table.get_item(Key={'id': 1})
        newcount = counter['Item']['visitCount']
        assert newcount == 2
        assert response['statusCode'] == 200
       






        

