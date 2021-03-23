# app.py

#Most current working version as of 07/03/2021, 23:07
import os
import subprocess
#import passwordCheck
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

   def validate_password(password):
      VALIDATIONS = (
        (contains_upper, 'Password needs at least one upper-case character.'),
        (contains_lower, 'Password needs at least one lower-case character.'),
        (contains_digit, 'Password needs at least one number.'),
        (contains_special, 'Password needs at least one special character.'),
        (long_enough, 'Password needs to be at least 8 characters in length.'),
      )
      failures = [
        failMsg for validator, failMsg in VALIDATIONS if not validator(password)
      ]
      if not failures:
        return True
      else:
         print("Invalid password! Review below and change your password accordingly!\n")
         for failMsg in failures:
            msg = "Your password is insecure \n"
            strengthCheck = msg + failMsg
            return msg + failMsg
            break
           
      if __name__ == '__main__':
         while True:
            password = validate_password(password)
            if validate_password(password):
                strengthCheck = ("Password meets all requirements and may be used.\n")
                return strengthCheck
                break
   return render_template('breachChecker.html', strengthCheck = strengthCheck)
    
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
