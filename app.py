# app.py
import os
from flask import Flask, request, jsonify, render_template, url_for, redirect
app = Flask(__name__)
    
@app.route('/success/<pass>')
def success(passWord):
   return 'welcome %s' % passWord
    
@app.route('/checker', methods = ['POST', 'GET'])
def checker():
    if request.method == 'POST':
        password = request.form['pass']
        return redirect (url_for('success',passWord = password))
    else:
        password = request.args.get('pass')
        return redirect(url_for('success',passWord = password))
    
# A welcome message to test our server
@app.route('/')#, methods=['POST'])
def index():
    #if form.validate_on_submit():
       # if 'bruteForcer' in request.form:
       #     pass
       #     
       ## elif 'checker' in request.form:
        #    pass
            
            return render_template('index.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))
