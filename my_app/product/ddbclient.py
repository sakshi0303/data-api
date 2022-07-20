from typing import Any
import boto3
import json

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
# Responsbile for upload, query, delete logic
class DDBClient:
    # attributes
    client: Any

    # constructor
    def __init__(self) -> None:
        self.client = boto3.client('dynamodb')
        pass

    def createTable(self, namespace, content):
        try:
            existing_tables = self.client.list_tables()['TableNames']
            if namespace in existing_tables:
                print(f'Table with name: {namespace} already exists')
                return

            attributeDefintions = []
            primaryKey = None
            firstItem = json.loads(content)[0]
            print(type(firstItem))
            for k in firstItem:
                print(k,firstItem[k])
                primaryKey = self._buildPrimaryKey(k)
                attributeDefintions.append(self._buildAttribute(k, 'S'))
                break

            response = self.client.create_table(
                    AttributeDefinitions=attributeDefintions,
                    TableName=namespace,
                    KeySchema=[primaryKey],
                    BillingMode='PAY_PER_REQUEST',
                    TableClass='STANDARD'
                )
            print(response)
        except Exception as e:
            print('Error:', e)


    # methods
    def upload(self, namespace, content):
        try:
            # put_item(TableName='fruitSalad', Item={'fruitName':{'S':'Banana'},'key2':{'N':'value2'}})
            items = json.loads(content)
            for item in items:
                print(item)
                response = self.client.put_item(
                    TableName=namespace,
                    Item=self._buildItem(item)
                )
                print(response)
            pass
        except Exception as e:
            print(e)


    # private functions
    # DDB expects the following format for an upload request
    # dynamodb.put_item(TableName='fruitSalad', Item={'fruitName':{'S':'Banana'},'key2':{'N':'value2'}})
    def _buildItem(self, item):
        result = {}
        for key in item:
            result[key] = {'S': str(item[key])}
        return result

    def _buildAttribute(self, key, datatype):
        return {
            'AttributeName': key,
            'AttributeType': datatype
        }

    def _buildPrimaryKey(self, key):
        return {
            'AttributeName': key,
            'KeyType': 'HASH'
        }
