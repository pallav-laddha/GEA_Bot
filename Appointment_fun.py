import json
import boto3
import uuid

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
   
    id=uuid.uuid4()
    id=str(id)
    event['currentIntent']['slots']['TrackId']=id
    
    
    s1 = event['currentIntent']['slots']['Name']
    s2 = event['currentIntent']['slots']['PhoneNumber']
    s3 = event['currentIntent']['slots']['email']
    s4 = event['currentIntent']['slots']['AppointmentType']
    s5 = event['currentIntent']['slots']['ModelId']
    s6 = event['currentIntent']['slots']['Serial_Number']
    s7 = event['currentIntent']['slots']['Issue']
    s8 = event['currentIntent']['slots']['Date']
    s9 = event['currentIntent']['slots']['Time']
    s10 = event['currentIntent']['slots']['PINcode']
    s11 = event['currentIntent']['slots']['Address']
    
    
    
    table.put_item(Item={'TrackId':id,'Address':s11,'AppointmentType':s4,'Date':s8,'Issue':s7,'ModelId':s5,'PINcode':s10,'PhoneNumber': s2,'Serial_Number':s6 ,'Time':s9,'email':s3,'Name':s1 })
    
    return close(
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content':'Your tracking id is '+event['currentIntent']['slots']['TrackId']+' We will send you an email confirmation on '+event['currentIntent']['slots']['email']+' shortly' 
                '  Please let me know if you would like to cancel or modify your appointment '
                       
        }
    )
    
