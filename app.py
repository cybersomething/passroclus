# app.py
import os
from flask import Flask, request, jsonify, render_template, url_for, redirect, flash
app = Flask(__name__)

@app.route('/success/<passWord>')
def success(passWord):
   return render_template ('success.html')
  
@app.route('/creatorHome')
def creatorHome():
   return render_template ('creator.html')
    
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
