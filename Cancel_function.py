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
    id=event['currentIntent']['slots']['Track_id']
    
    
    table.delete_item(
    Key={
        'TrackId': id,
    }
    )
    return close(
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content':'Your appointment has been canceled'
                '.Please let me know if you would like to cancel or modify your appointment '
                       
        }
    )
