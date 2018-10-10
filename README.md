# GEA_Bot

This is a service scheduler bot.The main code is in the GEA_ScheduleBot_Export.json
There are 3 supporting lambda funcion whis go in fulfillment code hook of their respective intent.I have tested it and posted a youtube video with 
all the funtionality-https://youtu.be/Eiv0HayoC4Y


I have made a validation function for validating serial number .Now i have transfered the given sample data into dynamodb
and i am reusing the code provided in webinar and added some more funtionality to it.But i have not used validation code as it is has some 
bugs in it.
There are some integration issues with validation function as i have build it in last minute and hence i have not deployed it in my code
as soon as i figure out the bugs i will fix it and update the code.Till then i am relying on the lex natural language processing to validate 
my data.the problem with this is the it allow similar serial number which might not be there hence this validaton function is required.

The problem with the validation funtion is that it is working fine in the lambda console but as soon as i put it in validation code hook
it gives me lambda error .i think it starts validating even before user has given input .i will rectify it and try to put up the code as soon as 
possible  



Future scope of the project:

1) personalize website
We can create a dedicated website for the use of chatbot where all customer can directly go to the website to create the service appointment.

2) Alexa skill
As you will notice that there is a lot of typing involve in order to book the service call .
We can integrate Alexa skill so that already existing details like name, address,phone number is not asked from the user and deliver a state of the art user interface.
As lex is build on the same technology as Alexa we can use the same code for building the alexa skill .

3)Amazon Connect
With Amazon Connect, we can quickly and easily create a cloud-based contact center, creating dynamic contact flows that provide personalized experiences for our customer.
Using Amazon Lex, a service that allows you to create intelligent conversational “chatbots”, you can turn your contact flows into natural conversations.
In simple terms, we can use the same code to create a call center where customers can directly call and book a service request.


Architecture:

facebook messenger-> lex -> lambda -> dynamoDB -> SES -> Email

This is the flow of the information for the chatbot. User interacts with the chatbot using the facebook messenger.The facebook messenger callback
lex for processing the information. Lex then calls lambda funtion which perform the necessary task like updating the dynamoDB table and calling AWS SES which 
sends an email confirmation to the user along with their "Track-Id" which user can use to 'modify' or 'cancel' their existing appointment.