# app.py

#Most current working version as of 07/03/2021, 23:07
import os
import subprocess
import hashlib
import requests
import argparse
import re
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

@app.route('/breachChecker/<passWord>')
def breachChecker(passWord):
   SHA1 = hashlib.sha1(passWord.encode('utf-8'))
   hash_string = SHA1.hexdigest().upper()
   prefix = hash_string[0:5]

   header = {
      'User-Agent': 'password checker'
   }

   url = "https://api.pwnedpasswords.com/range/{}".format(prefix)

   req = requests.get(url, headers=header).content.decode('utf-8')
   # split the result twice - each line into key, value pairs of hash-postfixes and the usage count.
   hashes = dict(t.split(":") for t in req.split('\r\n'))

   # add the prefix to the key values (hashes) of the hashes dictionary
   hashes = dict((prefix + key, value) for (key, value) in hashes.items())

   for item_hash in hashes:
       if item_hash == hash_string:
          print(json.dumps({"\nOh no — pwned!"}))
          print(json.dumps({"{} has previously appeared in a data breach, used {} times, and should never be used. ".format(passWord,hashes[hash_string])}))
          passwordOutput = command1 + command2
       break

   if hash_string != item_hash:
       print(json.dumps({\nGood news — no pwnage found!"}))
       print(json.dumps({"{} wasn't found in any of the Pwned Passwords loaded into Have I Been Pwned.".format(passWord)}))
                         
   exit()

   json.dumps(passwordOutput)
                         
   parser = argparse.ArgumentParser()
   parser.add_argument("-p", "--password", help="enter your password")
   args = parser.parse_args()

   argv = vars(args)
   passWord = argv['password']

   if args.password:
      check_leak(passWord)
   else:
      print("No password supplied\n")
      parser.print_help()
   return render_template('breachChecker.html', passwordOutput = passwordOutput)
    
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
