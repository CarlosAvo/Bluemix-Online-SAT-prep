"""Cloud Foundry test"""
import requests
from flask import Flask , render_template,request 
import os
import random
from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '1a238bb54cd623442091b118a4b0ceb8d325f2247a5c71ae8'
client = swagger.ApiClient(apiKey, apiUrl)

##Call api to be used in WordApi
wordApi = WordApi.WordApi(client)

app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
    port = int(os.getenv("VCAP_APP_PORT"))
else:
    port = 8080

@app.route("/")
def main():
    
    cssCall="<HTML> <HEAD><TITLE>SAT Vocabulary</TITLE> <style media=\"screen\" type=\"text/css\"> #bigbutton {width:230px;\
background: #00CC00; padding: 8px 14px 10px; border:1px solid #3e9cbf; cursor:pointer; font-size:1.5em;font-family:Oswald, sans-serif; \
letter-spacing:.1em;text-shadow: 0 -1px 0px rgba(0, 0, 0, 0.3); color: #fff;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #00CC00, 0px 10px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-border-radius: 10px;-webkit-border-radius: 10px;border-radius: 10px;}#bigbutton:hover, #bigbutton:focus {color:#dfe7ea;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, \
0px 2px 0px 0px #205c73, 0px 2px 5px #999;-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;\
box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;} #bigbutton{\
position: fixed;    left: 580px;    top: 250px;} #leader {width:230px;background: #00CC00; padding: 8px 14px 10px; border:1px solid #3e9cbf; cursor:pointer; font-size:1.5em;\
font-family:Oswald, sans-serif; letter-spacing:.1em;text-shadow: 0 -1px 0px rgba(0, 0, 0, 0.3); color: #fff;\
-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;-moz-border-radius: 10px;-webkit-border-radius: 10px;border-radius: 10px;}\
#leader:hover, #leader:focus {color:#dfe7ea;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, \
0px 2px 0px 0px #205c73, 0px 2px 5px #999;}#leader{position: fixed;    left: 580px;    top: 350px;}</style> </HEAD><BODY bgcolor=\" #F1F1F1\">"
       
        
    return  cssCall+"<p style=\"text-align:center;font-size:35px;\">SAT Vocabulary Review<p/><form action=\"../Start\" method=\"POST\"><input id=\"bigbutton\" type=\"submit\" value=\"Start reviewing\" /></form><form action=\"../LeaderBoards\" ><input id=\"leader\" type=\"submit\" value=\"Leaderboards\" /></form><body/><html/> "

@app.route("/LeaderBoards")


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
    people=showScore.readlines()
    for i in people:
        a+=i+"<br/>"

    return cssCall+"<p style=\"text-align:center;font-size:40px;\">Scores<p/><p style=\"position: fixed;left: 600px;top: 100px;font-size:25px; \">"+a+"<p/><form action=\"../\" ><input id=\"bigbutton\" type=\"submit\" value=\"Main Menu\" /><body/><html/>"


    

@app.route("/Start", methods=['POST'])

def giveDef():
    
    tokens=['adversity', 'aesthetic', 'amicable', 'anachronistic', 'anecdote', 'anonymous', 'antagonist', 'arid', 'assiduous', 'asylum', 'benevolent', 'camaraderie', 'censure', 'circuitous', 'clairvoyant', 'collaborate', 'compassion', 'compromise', 'condescending', 'conditional', 'conformist', 'congregation', 'convergence', 'deleterious', 'demagogue', 'digression', 'diligent', 'discredit', 'disdain', 'divergent', 'emulate', 'enervating', 'enhance', 'ephemeral', 'evanescent', 'exasperation', 'exemplary', 'extenuating', 'florid', 'fortuitous', 'frugal', 'haughty', 'hedonist', 'hypothesis', 'impetuous', 'impute', 'incompatible', 'inconsequential', 'inevitable', 'integrity', 'intrepid', 'intuitive', 'jubilation', 'lobbyist', 'longevity', 'mundane', 'nonchalant', 'novice', 'opulent', 'orator', 'ostentatious', 'perfidious', 'precocious', 'pretentious', 'procrastinate', 'prosaic', 'prosperity', 'provocative', 'prudent', 'querulous', 'rancorous', 'reclusive', 'reconciliation', 'renovation', 'resilient', 'reverence', 'sagacity', 'scrutinize', 'spontaneity', 'spurious', 'submissive', 'substantiate', 'subtle', 'superficial', 'superfluous', 'suppress', 'surreptitious', 'tactful', 'tenacious', 'transient', 'venerable', 'vindicate', 'wary']

    
    #Empty list were all random words will be appended
    global randomList

    randomList=[]

    ##Keep running as long as number of words in list are < 20

    
    spot=random.randint(1,len(tokens))

    definitions = wordApi.getDefinitions(tokens[spot],sourceDictionaries='webster',limit=3)


        ## If value of definition is None then skip that word
    if definitions is None :
        pass


        ## If randomW has a definition and related words then append to list
    else:
        randomList.append(tokens[spot])
        tokens.remove(tokens[spot])
            ##Make list global to call in other functions
    definitions = wordApi.getDefinitions(randomList[0],sourceDictionaries='webster',limit=3)


    ##Should run because None was purged in randomWords function
    if definitions is not None:
        ##Get the first definition from a list of definitions created from randomList[place]
        global randomDefinition
        randomDefinition=definitions[0].text

        ## Print random definition that has to be solved
        

        cssCall="<HTML> <HEAD><TITLE>SAT Vocabulary</TITLE> <style media=\"screen\" type=\"text/css\"> #bigbutton {width:230px;\
background: #00CC00; padding: 8px 14px 10px; border:1px solid #3e9cbf; cursor:pointer; font-size:1.5em;font-family:Oswald, sans-serif; \
letter-spacing:.1em;text-shadow: 0 -1px 0px rgba(0, 0, 0, 0.3); color: #fff;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #00CC00, 0px 10px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-border-radius: 10px;-webkit-border-radius: 10px;border-radius: 10px;}#bigbutton:hover, #bigbutton:focus {color:#dfe7ea;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;} #bigbutton{\
position: fixed;    left: 580px;    top: 250px;} #text{position: fixed;left: 550px;top: 220px;padding: 1px 20px; border: 0;    height: 25px;\
width: 275px;    border-radius: 10px;    -moz-border-radius: 10px; -webkit-border-radius: 10px;    box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset;\
-moz-box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset;    -webkit-box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset; -webkit-background-clip: padding-box;\
outline: 0;</style> </HEAD><BODY bgcolor=\" #F1F1F1\">"

        middle="<p style=\"position: fixed;left: 600px;top: 150px;font-size:25px;\"> Hint: "+wordHint(randomList[0])+"<p/>"

        first="<p style=\"text-align:center;font-size:40px;\">"+randomDefinition+"<p/>"
        
        

        
        return  cssCall+first+middle+"<form action=\"../GiveAnswer\" method=\"POST\"><input type=\"text\" id=\"text\" name=\"answer\"/> <input id=\"bigbutton\" type=\"submit\" value=\"Submit answer\" /></form><body/><html/> "


@app.route("/GiveAnswer", methods=['POST'])

def sayHello():
    cssCall="<HTML> <HEAD><TITLE>SAT Vocabulary</TITLE> <style media=\"screen\" type=\"text/css\"> .bigbutton {width:230px;\
background: #00CC00; padding: 8px 14px 10px; border:1px solid #3e9cbf; cursor:pointer; font-size:1.5em;font-family:Oswald, sans-serif; \
letter-spacing:.1em;text-shadow: 0 -1px 0px rgba(0, 0, 0, 0.3); color: #fff;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #00CC00, 0px 10px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-border-radius: 10px;-webkit-border-radius: 10px;border-radius: 10px;}.bigbutton:hover, .bigbutton:focus {color:#dfe7ea;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;} .bigbutton{\
position: fixed;    left: 580px;    top: 250px;} #text{position: fixed;left: 550px;top: 220px;padding: 1px 20px; border: 0;    height: 25px;\
width: 275px;    border-radius: 10px;    -moz-border-radius: 10px; -webkit-border-radius: 10px;    box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset;\
-moz-box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset;    -webkit-box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset; -webkit-background-clip: padding-box;\
outline: 0; </style> </HEAD><BODY bgcolor=\" #F1F1F1\">"
    someans= request.form['answer']
    if someans == randomList[0]:

        return cssCall+"<p style=\"text-align:center;font-size:35px;\">Answer is Correct!!!<p/><form action=\"../Restart\" method=\"POST\"><input type=\"submit\" class=\"bigbutton\" value=\"Continue\"\ style=\"\"/></form>"
    
    else:
        return cssCall+"<p style=\"text-align:center;font-size:35px;\"> Answer is incorrect, right answer is: <em>"+randomList[0]+"</em> <p/> "+"<form action=\"../Redo\" method=\"POST\"><input type=\"submit\" class=\"bigbutton\" value=\"Try Again\"\/></form><body/><html/>"

@app.route("/Redo", methods=['POST'])

def redo():
    definitions = wordApi.getDefinitions(randomList[0],sourceDictionaries='webster',limit=3)
    randomDefinition=definitions[0].text
    cssCall="<HTML> <HEAD><TITLE>SAT Vocabulary</TITLE> <style media=\"screen\" type=\"text/css\"> #bigbutton {width:230px;\
background: #00CC00; padding: 8px 14px 10px; border:1px solid #3e9cbf; cursor:pointer; font-size:1.5em;font-family:Oswald, sans-serif; \
letter-spacing:.1em;text-shadow: 0 -1px 0px rgba(0, 0, 0, 0.3); color: #fff;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #00CC00, 0px 10px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-border-radius: 10px;-webkit-border-radius: 10px;border-radius: 10px;}#bigbutton:hover, #bigbutton:focus {color:#dfe7ea;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;} #bigbutton{\
position: fixed;    left: 580px;    top: 250px;} #text{position: fixed;left: 550px;top: 220px;padding: 1px 20px; border: 0;    height: 25px;\
width: 275px;    border-radius: 10px;    -moz-border-radius: 10px; -webkit-border-radius: 10px;    box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset;\
-moz-box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset;    -webkit-box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset; -webkit-background-clip: padding-box;\
outline: 0;</style> </HEAD><BODY bgcolor=\" #F1F1F1\">"
    middle="<p style=\"position: fixed;left: 600px;top: 150px;font-size:25px;\"> Hint: "+wordHint(randomList[0])+"<p/>"

    first="<p style=\"text-align:center;font-size:40px;\">"+randomDefinition+"<p/>"
        
        

        
    return  cssCall+first+middle+"<form action=\"../GiveAnswer\" method=\"POST\"><input type=\"text\" id=\"text\" name=\"answer\"/> <input id=\"bigbutton\" type=\"submit\" value=\"Submit answer\" /></form><body/><html/> "


@app.route("/Restart", methods=['POST'])
def restart():
    tokens=['adversity', 'aesthetic', 'amicable', 'anachronistic', 'anecdote', 'anonymous', 'antagonist', 'arid', 'assiduous', 'asylum', 'benevolent', 'camaraderie', 'censure', 'circuitous', 'clairvoyant', 'collaborate', 'compassion', 'compromise', 'condescending', 'conditional', 'conformist', 'congregation', 'convergence', 'deleterious', 'demagogue', 'digression', 'diligent', 'discredit', 'disdain', 'divergent', 'emulate', 'enervating', 'enhance', 'ephemeral', 'evanescent', 'exasperation', 'exemplary', 'extenuating', 'florid', 'fortuitous', 'frugal', 'haughty', 'hedonist', 'hypothesis', 'impetuous', 'impute', 'incompatible', 'inconsequential', 'inevitable', 'integrity', 'intrepid', 'intuitive', 'jubilation', 'lobbyist', 'longevity', 'mundane', 'nonchalant', 'novice', 'opulent', 'orator', 'ostentatious', 'perfidious', 'precocious', 'pretentious', 'procrastinate', 'prosaic', 'prosperity', 'provocative', 'prudent', 'querulous', 'rancorous', 'reclusive', 'reconciliation', 'renovation', 'resilient', 'reverence', 'sagacity', 'scrutinize', 'spontaneity', 'spurious', 'submissive', 'substantiate', 'subtle', 'superficial', 'superfluous', 'suppress', 'surreptitious', 'tactful', 'tenacious', 'transient', 'venerable', 'vindicate', 'wary']

    
    #Empty list were all random words will be appended
    global randomList

    randomList=[]

    ##Keep running as long as number of words in list are < 20

    
    spot=random.randint(1,len(tokens))

    definitions = wordApi.getDefinitions(tokens[spot],sourceDictionaries='webster',limit=3)


        ## If value of definition is None then skip that word
    if definitions is None :
        pass


        ## If randomW has a definition and related words then append to list
    else:
        randomList.append(tokens[spot])
        tokens.remove(tokens[spot])
            ##Make list global to call in other functions
    definitions = wordApi.getDefinitions(randomList[0],sourceDictionaries='webster',limit=3)


    ##Should run because None was purged in randomWords function
    if definitions is not None:
        ##Get the first definition from a list of definitions created from randomList[place]
        global randomDefinition
        randomDefinition=definitions[0].text

        ## Print random definition that has to be solved
        cssCall="<HTML> <HEAD><TITLE>SAT Vocabulary</TITLE> <style media=\"screen\" type=\"text/css\"> #bigbutton {width:230px;\
background: #00CC00; padding: 8px 14px 10px; border:1px solid #3e9cbf; cursor:pointer; font-size:1.5em;font-family:Oswald, sans-serif; \
letter-spacing:.1em;text-shadow: 0 -1px 0px rgba(0, 0, 0, 0.3); color: #fff;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #00CC00, 0px 10px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 5px 0px 0px #205c73, 0px 10px 5px #999;\
-moz-border-radius: 10px;-webkit-border-radius: 10px;border-radius: 10px;}#bigbutton:hover, #bigbutton:focus {color:#dfe7ea;-webkit-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;\
-moz-box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;box-shadow: inset 0px 1px 0px #3e9cbf, 0px 2px 0px 0px #205c73, 0px 2px 5px #999;} #bigbutton{\
position: fixed;    left: 580px;    top: 250px;} #text{position: fixed;left: 550px;top: 220px;padding: 1px 20px; border: 0;    height: 25px;\
width: 275px;    border-radius: 10px;    -moz-border-radius: 10px; -webkit-border-radius: 10px;    box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset;\
-moz-box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset;    -webkit-box-shadow: 1px 1px 0 0 #FFF, 5px 5px 40px 2px #BBB inset; -webkit-background-clip: padding-box;\
outline: 0;</style> </HEAD><BODY bgcolor=\" #F1F1F1\">"
        middle="<p style=\"position: fixed;left: 600px;top: 150px;font-size:25px;\"> Hint: "+wordHint(randomList[0])+"<p/>"

        first="<p style=\"text-align:center;font-size:40px;\">"+randomDefinition+"<p/>"
        
        

        
        return  cssCall+first+middle+"<form action=\"../GiveAnswer\" method=\"POST\"><input type=\"text\" id=\"text\" name=\"answer\"/> <input id=\"bigbutton\" type=\"submit\" value=\"Submit answer\" /></form><body/><html/> "




    

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port,debug=False)
