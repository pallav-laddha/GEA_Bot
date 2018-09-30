import json
import boto3

dynamo = boto3.resource('dynamodb')


def close( fulfillment_state, message):
    response = {
        
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    return response



def lambda_handler(event, context):
    # TODO implement
    table= dynamo.Table('Service')  
    id=event['currentIntent']['slots']['ID']
    
    d1=event['currentIntent']['slots']['Date']
    d2=event['currentIntent']['slots']['Time']
    table.update_item(
    Key={
        'TrackId': id,
    },
    UpdateExpression='SET #ts = :val1',
    ExpressionAttributeValues={
    ":val1": d1
  },
  ExpressionAttributeNames={
    "#ts": "Date"
  }
    )
    table.update_item(
    Key={
        'TrackId': id,
    },
    UpdateExpression='SET #ds = :val1',
    ExpressionAttributeValues={
    ":val1": d2
  },
  ExpressionAttributeNames={
    "#ds": "Time"
  }
    )
    return close(
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content':'Your appointment has been modified to '+ d1 +' at '+ d2 + 
                '.Please let me know if you would like to cancel or modify your appointment '
                       
        }
    )
