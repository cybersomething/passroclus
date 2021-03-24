# app.py

#Most current working version as of 07/03/2021, 23:07
import os
import subprocess
import json
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

@app.route('/securityChecker')
def securityChecker():
   return render_template ('securityChecker.html')
   
@app.route('/breachCheckerRedirect/<passWord>', methods = ['POST', 'GET'])
def breachCheckerRedirect(passWord):
   if request.method == 'POST':
      return redirect (url_for('breachChecker/<passWord>'))

#@app.route('/breachChecker/<passWord>')
#def breachChecker(passWord):
#   strengthCheck = passwordCheck.validate_password(passWord)
#   return render_template('breachChecker.html', strengthCheck = strengthCheck)

@app.route('/breachChecker/<passWord>')
def breachChecker(passWord):
   fileName = "ncscTop100k.txt"
   with open(fileName) as temp_f:
      breachFile = temp_f.readlines()
   for line in breachFile:
      if passWord in line:
         breachedPassword = "This password has been found in a breach, we suggest changing this password anywhere you use it.";
   breachedPassword = "This password was not found in a breach, however we suggest checking the strength of this password."
   #fileName = "ncscTop100k.txt"
  # breachFile = open(fileName, 'r')
   #for line in breachFile:
  #    line = str(line)
   #   line = line.strip()
   #   if line == passWord:
  #       breachedPassword = "This password has been found in a breach, we suggest changing this password anywhere you use it.";
  #    else:
  #       breachedPassword = "This password was not found in a breach, however we suggest checking the strength of this password."
   return render_template('breachChecker.html', breachedPassword = breachedPassword)
    
@app.route('/checker', methods = ['POST', 'GET'])
def checker():
    if request.method == 'POST':
        password = request.form['password']
        return redirect (url_for('breachChecker',passWord = password))
    else:
        password = request.args.get('password')
        return redirect (url_for('breachChecker',passWord = password))
    
@app.route('/creator', methods = ['POST', 'GET'])
def creator():
    if request.method == 'POST':
        return redirect(url_for('creatorHome'))
      
@app.route('/creatorHome')
def creatorHome():
   return render_template ('creator.html')
    
# A welcome message to test our server
@app.route('/')#, methods=['POST'])
def index():
    return render_template('index.html')
   
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))
