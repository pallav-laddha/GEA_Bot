import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def elicit_slot(intent_name, slots, slot_to_elicit, message):
    return {
       
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }
def confirm_intent(intent_name, slots, message):
    return {
        'dialogAction': {
            'type': 'ConfirmIntent',
            'intentName': intent_name,
            'slots': slots,
            'message': message
        }
    }

def validateModel(model_number):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('model')
    print("validateModel : model_number = "+str(model_number))
    #query_response = table.query(KeyConditionExpression=Key('Serial_number').eq(model_number))
    #query_response = table.scan(FilterExpression=Attr('Serial_number').eq(model_number))
    query_response = table.query(KeyConditionExpression=Key('Serial_number').eq(model_number))
    
    print("validateModel : query_response = "+str(query_response))
    return query_response


def MakeAppointment(event):
    # TODO implement
    if event['invocationSource'] == 'DialogCodeHook':
    
        add="\r"
        model_number=event['currentIntent']['slots']['Serial_Number']+add
        query_response=validateModel(model_number)
        if query_response['Count']>0:
            product_type = query_response['Items'][0]['Product Line']
            print("validateModel : we found the model_number & product type is "+str(product_type))
            return confirm_intent(
                event['currentIntent']['name'],
                event['currentIntent']['slots'],
                {
                    'contentType': 'PlainText',
                    'content': '{} is available, should I go ahead and book your appointment?'.format(
                        event['currentIntent']['slots']['Time'])
            }
            )
            
            
            
            
        else:
            print("validateModel : model_number Not Found in Table")
            return elicit_slot(
                event['currentIntent']['name'],
                event['currentIntent']['slots'],
                'Serial_Number',
                {
                    'contentType': 'PlainText',
                    'content': 'please enter a valid serial number '
                }
            
                )
def lambda_handler(event, context):
    intent='MakeAppointment'
    intentName=event['currentIntent']['name']
    
    if intentName == 'MakeAppointment':
        return MakeAppointment(event)
        
    raise Exception('Intent with name ' + intent_name + ' not supported')