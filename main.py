from flask import Flask
# https://github.com/johnwheeler/flask-ask/archive/master.zip
from flask_ask import Ask, statement, question, session
from common import *
import lotteryroutes

app = Flask(__name__)
ask = Ask(app, '/alexa')

supported_intents = ['check your lottery tickets']

@app.route('/ping', methods=['POST','GET'])
def ping():
    return "OK"


### 
### Basic Alexa routes
###

@ask.launch
def new_ask():
    message = "My Scribe here. How can I help you?"
    reprompt = "What can I do you for? I can {}".format(choose_from_list_as_str(supported_intents))
    return question(message) \
        .reprompt(reprompt)

@ask.intent('AMAZON.FallbackIntent')
def fallback_intent():
    message = "I'm not sure what you want me to do. Please try to ask me again. I can {}".format(choose_from_list_as_str(supported_intents))
    reprompt = "What can I do you for? I can {}".format(choose_from_list_as_str(supported_intents))
    return question(message) \
        .reprompt(reprompt)

@ask.intent('AMAZON.HelpIntent')
def fallback_intent():
    message = "Here are some things I can do: {}".format(choose_from_list_as_str(supported_intents, number=7, join_text="and"))
    reprompt = "What can I do you for? I can {}".format(choose_from_list_as_str(supported_intents))
    return question(message) \
        .reprompt(reprompt)

### 
### Lottery Routes
###

@ask.intent('CheckLotteryNumbersStart')
def checkNumbers(lottery_name):
    session.attributes['lottery_name'] = lottery_name
    return question("Okay. Checking {}. Go ahead and say your numbers.".format(lottery_name))

@ask.intent('CheckLotteryNumbers')
def checkNumbers(num_one, num_two, num_three, num_four, num_five, bonus_num):
    lottery_name = session.attributes['lottery_name']
    return question("You said {} {} {} {} {} and bonus {} for {}".format(num_one, num_two, num_three, num_four, num_five, bonus_num, lottery_name))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')
