# app.py
import os
from flask import Flask, request, jsonify, render_template, url_for, redirect, flash
app = Flask(__name__)

@app.route('/success/<passWord>')
def success(passWord):
   return render_template ('success.html')

#@app.route('/securityCheckerRedirect', methods = ['POST', 'GET'])
 #  if request.method == 'POST':
#      security = request.form['security']
 #     return redirect (url_for('securityChecker'))
 #  else
 #     security = request.args.get('security')
 #     return redirect (url_for('securityChecker'))
   
#@app.route('/breachCheckerRedirect', methods = ['POST', 'GET'])
#   if request.method == 'POST':
#      breach = request.form['breach']
#      return redirect (url_for('breachChecker'))
#   else
 #     security = request.args.get('breach')
#      return redirect (url_for('breachChecker'))
      
@app.route('/creatorHome')
def creatorHome():
   return render_template ('creator.html')

@app.route('/securityChecker')
def creatorHome():
   return render_template ('securityChecker.html')

@app.route('/breachChecker')
def creatorHome():
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
    
# A welcome message to test our server
@app.route('/')#, methods=['POST'])
def index():
    return render_template('index.html')
   
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))
