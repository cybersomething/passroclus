# app.py

#Most current working version as of 24/03/2021
import os
import subprocess
import passwordGenerator
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

@app.route('/securityChecker/<passWord>')
def securityChecker(passWord):
   def contains(required_chars, s):
      return any(c in required_chars for c in s)

   def contains_upper(s):
      return contains(ascii_uppercase, s)

   def contains_lower(s):
      return contains(ascii_lowercase, s)

   def contains_digit(s):
      return contains(digits, s)

   def contains_special(s):
      return contains(r"""!@$%^&*()_-+={}[]|\,.></?~`"':;""", s)

   def long_enough(s):
      return len(s) >= 8

   def check_len(input):
      if len(input) >= 8:
         return True
      else:
         return False

   def validate_password(passWord):
      VALIDATIONS = (
      (contains_upper, 'Password needs at least one upper-case character.'),
      (contains_lower, 'Password needs at least one lower-case character.'),
      (contains_digit, 'Password needs at least one number.'),
      (contains_special, 'Password needs at least one special character.'),
      (long_enough, 'Password needs to be at least 8 characters in length.'),
      )
      failures = [
         msg for validator, msg in VALIDATIONS if not validator(password)]
      if failures:
         firstMessage = ("Invalid password! Review below and change your password accordingly!\n")
         for msg in failures:
            msg+=str(failures)
         return firstMessage
         return msg
      else:
         firstMessage = ("Password meets all requirements.")
         msg = ("To make a better password check out the password creator.")
         return firstMessage
         return msg
   return render_template ('securityChecker.html', firstMessage = firstMessage, msg = msg)

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

@app.route('/generator')
def generator(length):
   passwordGenerator.generate(length);
   return render_template ('generator.html', word = word, contains = contains)
    
# A welcome message to test our server
@app.route('/')#, methods=['POST'])
def index():
    return render_template('index.html')
   
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))
