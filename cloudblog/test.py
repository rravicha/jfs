import boto3

AWSAccessKeyId='AKIAYWFUZJPF2K6QTOHU'
AWSSecretKey='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'
# boto_sess = Session(
#     region_name='us-east-1',
#     aws_access_key_id=AWSAccessKeyId,
#     aws_secret_access_key=AWSSecretKey
# )

dynamodb = boto3.resource('dynamodb', region_name = 'eu-central-1')
table = dynamodb.Table('userInformations')

Item={
    'username':'rrr',
    'password':'rrr'
}
response = table.put_item(Item=Item)

print(response)
