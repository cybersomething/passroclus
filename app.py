# app.py

#Most current working version as of 07/03/2021, 23:07
import os
import subprocess
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
   
@app.route('/breachCheckerRedirect', methods = ['POST', 'GET'])
def breachCheckerRedirect():
   if request.method == 'POST':
      return redirect (url_for('breachChecker'))

@app.route('/breachChecker')
def breachChecker():
   subprocess.call(["g++", "/breachChecker/BreachChecker/Source.cpp"]) 
   tmp=subprocess.call("./a.out") 
   print "printing result" 
   print tmp 
   return render_template ('breachChecker.html')
    
@app.route('/checker', methods = ['POST', 'GET'])
def checker():
    if request.method == 'POST':
        password = request.form['password']
        return redirect (url_for('success',passWord = password))
    else:
        password = request.args.get('password')
        return redirect (url_for('success',passWord = password))
    
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
