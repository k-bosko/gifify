import boto3
import gifify_config as keys

TABLE_NAME = 'Gifify-users'

def main():
    dynamodb_client = boto3.client('dynamodb',
                        aws_access_key_id=keys.ACCESS_KEY_ID,
                        aws_secret_access_key=keys.ACCESS_SECRET_KEY,
                        aws_session_token=keys.AWS_SESSION_TOKEN,
                        region_name=keys.REGION)

    existing_tables = dynamodb_client.list_tables()['TableNames']

    if TABLE_NAME not in existing_tables:
        print(f"creating DynamoDB table={TABLE_NAME}")
        # Create the DynamoDB table.
        table = dynamodb_client.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'user_id',
                    'KeyType': 'HASH'
                }

            ],
            AttributeDefinitions=[
                    {
                    'AttributeName': 'user_id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        # Wait until the table exists.
        print("waiting for table to be created...")
        dynamodb_client.get_waiter('table_exists').wait(TableName=TABLE_NAME)
        print(f"created table {TABLE_NAME}")
    else:
        print(f"table {TABLE_NAME} exists")

if __name__ == '__main__':
    main()



