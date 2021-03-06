import requests
from flask import Flask , render_template,request 
import os
import random
from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '##API key goes here'
client = swagger.ApiClient(apiKey, apiUrl)

##Call api to be used in WordApi
wordApi = WordApi.WordApi(client)

app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
    port = int(os.getenv("VCAP_APP_PORT"))
else:
    port = 8080


@app.route("/")

#Main menu from here you can access leaderboards and start the game
def main():
    #CSS code for design and button layout
           
    #Returns website with buttons  
    return  render_template("main.html")

#If leaderboard button clicked it redirects to that.  
@app.route("/LeaderBoards")

#Read file with names and scores and return them.
def leaderboards():
    showScore=open("LeaderbordScores.txt","r")
    cssCall="<HTML> <HEAD><TITLE>SAT Vocabulary</TITLE> <style media=\"screen\" type=\"text/css\"> #bigbutton {width:230px;\
background: #00CC00; padding: 8px 14px 10px; border:1px solid #3e9cbf; cursor:pointer; font-size:1.5em;font-family:Oswald, sans-serif; \
letter-spacing:.1em;text-shadow: 0 -1px 0px rgba(0, 0, 0, 0.3); color: #fff;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #00CC00, 0px 10px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-border-radius: 10px;-webkit-border-radius: 10px;border-radius: 10px;}#bigbutton:hover, #bigbutton:focus {color:#dfe7ea;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, \
0px 2px 0px 0px #205c73, 0px 2px 5px #999;-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;\
box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;} #bigbutton{\
position: fixed;    left: 580px;    top: 450px;} </style> </HEAD><BODY bgcolor=\" #F1F1F1\">"
    a=""
    #Read ech line in the file and create a variable that saves each name and score with a break between names and cores 
    people=showScore.readlines()
    for i in people:
        a+=i+"<br/>"

    return cssCall+"<p style=\"text-align:center;font-size:40px;\">Scores<p/><p style=\"position: fixed;left: 600px;top: 100px;font-size:25px; \">"+a+"<p/><form action=\"../\" ><input id=\"bigbutton\" type=\"submit\" value=\"Main Menu\" /><body/><html/>"


    
#If start review button is clicked in main menu redirect here 
@app.route("/Start", methods=['POST'])

#Return definition for random word that must be guessed, it also shows a hint for said word
def giveDef():
    
    tokens=['adversity', 'aesthetic', 'amicable', 'anachronistic', 'anecdote', 'anonymous', 'antagonist', 'arid', 'assiduous', 'asylum', 'benevolent', 'camaraderie', 'censure', 'circuitous', 'clairvoyant', 'collaborate', 'compassion', 'compromise', 'condescending', 'conditional', 'conformist', 'congregation', 'convergence', 'deleterious', 'demagogue', 'digression', 'diligent', 'discredit', 'disdain', 'divergent', 'emulate', 'enervating', 'enhance', 'ephemeral', 'evanescent', 'exasperation', 'exemplary', 'extenuating', 'florid', 'fortuitous', 'frugal', 'haughty', 'hedonist', 'hypothesis', 'impetuous', 'impute', 'incompatible', 'inconsequential', 'inevitable', 'integrity', 'intrepid', 'intuitive', 'jubilation', 'lobbyist', 'longevity', 'mundane', 'nonchalant', 'novice', 'opulent', 'orator', 'ostentatious', 'perfidious', 'precocious', 'pretentious', 'procrastinate', 'prosaic', 'prosperity', 'provocative', 'prudent', 'querulous', 'rancorous', 'reclusive', 'reconciliation', 'renovation', 'resilient', 'reverence', 'sagacity', 'scrutinize', 'spontaneity', 'spurious', 'submissive', 'substantiate', 'subtle', 'superficial', 'superfluous', 'suppress', 'surreptitious', 'tactful', 'tenacious', 'transient', 'venerable', 'vindicate', 'wary']

    
    #Empty list were all random words will be appended
    global randomList

    randomList=[]

    #spot is a random position inside the list tokens, it chooses a random place that will be later indexed
    spot=random.randint(1,len(tokens))

    #call api to get definition for a random word in token and save in variable definitions
    definitions = wordApi.getDefinitions(tokens[spot],sourceDictionaries='webster',limit=3)


        ## If value of definition is None then skip that word
    if definitions is None :
        pass


        ## If it has a definition then append to list and remove from tokens so it doesn't repeat
    else:
        randomList.append(tokens[spot])
        tokens.remove(tokens[spot])


    ##Should run because None was purged 
    if definitions is not None:
        ##Get the first definition from a list of definitions created from randomList[place]

        global randomDefinition
        randomDefinition=definitions[0].text
        
        #CSS styling for website
              

        #CSS HTML and python code is combined to display together
        return  render_template("Start.html",wordHint=wordHint(randomList[0]),hintNoLetter=wordHintNoLetter(randomList[0]),randomDef=randomDefinition);

#After definition is submitted check to see if word is right or wrong
@app.route("/GiveAnswer", methods=['POST'])

def giveAnswer():
   
    #Request answer from website and save as variable
    someans= request.form['answer']

    #If it's the same as the one in the global list then return a website saying that answer is correct and option to continue to another question 
    if someans == randomList[0]:

        return render_template("answerCorrect.html")
    #If it's not the correct answer display the correct one and button displayed redirects to page where same definition is given
    #to see if player remembers the mistake he made
    else:
        return render_template("answerWrong.html",word=randomList[0])

@app.route("/Redo", methods=['POST'])

#If answer was wrong show player the definition they got wrong and make player re-input answer
def redo():
    #get definitions for mistaken word again
    definitions = wordApi.getDefinitions(randomList[0],sourceDictionaries='webster',limit=3)
    #Store only one of the definitions in a variable
    randomDefinition=definitions[0].text
            

    #CSS HTML and python code is combined to display together
    return render_template("redo.html",hintNoletter=wordHintNoLetter(randomList[0]),hintFull=wordHint(randomList[0]),definition=randomDefinition)


#Gives a hint of the correct word with some letters    
def wordHint(word):

    ##List of all letters in alphabet to replace with _ _
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    ##Make the word lowercase to check list easier
    lowerWord=word.lower()

    ##Create an empty word that will be populated with a few letters and _ _ _
    newWord=""

    ##Get length of the word
    lenWord=len(lowerWord)

    ##The result of dividing the length of the word by 4(arbitrary number) and then rounding is the amount of letters that will be showed
    thingsToRemeove=round(lenWord/3)

    ##a counter for the FOR loop
    mover = 0
    ##make a statement with value true
    statement= True

    for i in lowerWord:
        ##Give the first and every other letter in an even place until thingToRemove limit is reached
        if statement == True and mover < thingsToRemeove:
            ##Change to false so it skips and removes word in next run
            statement = False
            mover+=1
            ##Add letter to newWord
            newWord+=i


        ##Remove the letters that are in the alphabet and then turn letters into underscore signs _ _
        elif (i in alphabet and statement==False) or (mover >= thingsToRemeove and i in alphabet):

            newWord+=i.replace(i,"_ ")
            ##Turn statement into True so it goes back up
            statement=True
        ##If word has any other type of sign or space then print it as is
        elif i not in alphabet or mover<thingsToRemeove:
            newWord+=i
    ##Print newWord created s_o_ e-_ _ _ _ _ (stone-sober)
    return newWord

#Gives hint without any letters only spaces and number of letters
def wordHintNoLetter(word):

    ##List of all letters in alphabet to replace with _ _
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    ##Make the word lowercase to check list easier
    lowerWord=word.lower()

    ##Create an empty word that will be populated with a few letters and _ _ _
    newWord=""

    for i in lowerWord:
        
        if i in alphabet  :

            newWord+=i.replace(i,"_ ")
        elif i not in alphabet :
            newWord+=i
    return newWord



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port,debug=False)
