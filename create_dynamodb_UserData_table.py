import boto3
import gifify_config

def main():
    dynamodb_client = boto3.client('dynamodb',
                        aws_access_key_id=gifify_config.ACCESS_KEY_ID,
                        aws_secret_access_key=gifify_config.ACCESS_SECRET_KEY,
                        aws_session_token=gifify_config.AWS_SESSION_TOKEN,
                        region_name=gifify_config.REGION)

    existing_tables = dynamodb_client.list_tables()['TableNames']

    if gifify_config.USERDATA_TABLE not in existing_tables:
        print(f"creating DynamoDB table={gifify_config.USERDATA_TABLE}")
        # Create the DynamoDB table.
        table = dynamodb_client.create_table(
            TableName=gifify_config.USERDATA_TABLE,
            AttributeDefinitions=[
                {
                    'AttributeName': 'user_id',
                    'AttributeType': 'S',
                },
                {
                    'AttributeName': 'timestamp',
                    'AttributeType': 'S',
                },
            ],
            KeySchema=[
                {
                    'AttributeName': 'user_id',
                    'KeyType': 'HASH',
                },
                {
                    'AttributeName': 'timestamp',
                    'KeyType': 'RANGE',
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5,
            },
        )

        # Wait until the table exists.
        print("waiting for table to be created...")
        dynamodb_client.get_waiter('table_exists').wait(TableName=gifify_config.USERDATA_TABLE)
        print(f"created table {gifify_config.USERDATA_TABLE}")
    else:
        print(f"table {gifify_config.USERDATA_TABLE} exists")

if __name__ == '__main__':
    main()



