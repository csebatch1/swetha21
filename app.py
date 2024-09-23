#!/user/bin/python
#-*-coding: utf-8 -*-
from flask import Flask, request, render-template
app = Flask(_name_)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
            name = request.from['name']
            email = request.form['email']
            password = request.form['password']