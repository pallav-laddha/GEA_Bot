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