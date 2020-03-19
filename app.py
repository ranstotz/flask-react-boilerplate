import os
from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder='./client/dist',
            template_folder='./client/dist')

# api routes
@app.route('/api/items')
def items():
    '''Sample API route for data'''
    return jsonify([{'title': 'A'}, {'title': 'B'}])

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    ''' serve index.html for non-api routes '''
    return render_template("index.html")


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)
