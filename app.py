# app.py

#Most current working version as of 24/03/2021
import os
import subprocess
import re
import random
import json
import math
from flask import Flask, request, jsonify, render_template, url_for, redirect, flash
app = Flask(__name__)

@app.route('/success/<passWord>')
def success(passWord):
   message = ('The password you entered was ' + passWord)
   return render_template ('success.html', message = message)

@app.route('/securityCheckerRedirect', methods = ['POST', 'GET'])
def securityCheckerRedirect():
   if request.method == 'POST':
      return redirect (url_for('securityChecker'))

@app.route('/securityChecker/<passWord>')
def securityChecker(passWord):
   symbols = [' ', '!', '#', '$', '%', '&', "'", '?', '@']
   lowercase = 0
   uppercase = 0
   num = 0
   ASCII = 0
   uniqueChar = 0
   
   length = len(passWord)
   
   if (len(passWord) >= 1):
      for i in passWord:
         if (i.islower()):
            lowercase += 1
         if (i.isupper()):
            uppercase += 1
         if (i.isdigit()):
            num += 1
         if (i == symbols):
            ASCII += 1
      
   if lowercase == 1:
      uniqueChar = uniqueChar + 26
   if uppercase == 1:
      uniqueChar = uniqueChar + 26
   if num == 1:
      uniqueChar = uniqueChar + 10
   if ASCII == 1:
      uniqueChar = uniqueChar + 30
      
   entropy = math.log2(uniqueChar * length)
   
   return render_template ('securityChecker.html', entropy)

@app.route('/breachCheckerRedirect/<passWord>', methods = ['POST', 'GET'])
def breachCheckerRedirect(passWord):
   if request.method == 'POST':
      return redirect (url_for('breachChecker/<passWord>'))

@app.route('/breachChecker/<passWord>')
def breachChecker(passWord):
   result = open('ncscTop100k.txt', 'r')
   if passWord in result.read():
      breachedPassword = "This password has been found in a breach, we suggest changing this password anywhere you use it.";
      return render_template('breachChecker.html', breachedPassword = breachedPassword)
   else:
      breachedPassword = "This password was not found in a breach, however we suggest checking the strength of this password."
      return render_template('breachChecker.html', breachedPassword = breachedPassword)
    
@app.route('/checker', methods = ['POST', 'GET'])
def checker():
    if request.method == 'POST':
        password = request.form['password']
        return redirect (url_for('securityChecker',passWord = password))
    else:
        password = request.args.get('password')
        return redirect (url_for('securityChecker',passWord = password))
    
@app.route('/creator', methods = ['POST', 'GET'])
def creator():
   return render_template('creator.html')

@app.route('/generatorRedirect', methods = ['POST', 'GET'])
def generatorRedirect():
    if request.method == 'POST':
        length = request.form['length']
        return redirect (url_for('generator', length = length))
    else:
        length = request.args.get('length')
        return redirect (url_for('generator', length = length))

@app.route('/generator/<length>')
def generator(length):  
   length = int(length)
   textFile = open('randomWords.txt', 'r')
   textFile = textFile.read()
   words = list(map(str, textFile.split()))
   passphrase = []
   
   for i in range(length):
      temp = int(random.random()*len(words))
      passphrase.append(words[temp])
         
   return render_template ('generator.html', passphrase = passphrase)
    
# A welcome message to test our server
@app.route('/')#, methods=['POST'])
def index():
    return render_template('index.html')
   
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))
