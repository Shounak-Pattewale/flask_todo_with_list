from flask import Flask
from flask import render_template, redirect, request, url_for, flash

todo = Flask(__name__)
data = []
todo.secret_key = b'_9#wsL"F4Q8z\qx!ec]/'

@todo.route('/')
def home():
    return render_template('todo.html')

@todo.route('/add_todo', methods=['POST'])
def add_todo():
    req = request.form
    print('ADDING : ',req.get('add-list'))
    data.append(req.get('add-list'))
    flash('Data Inserted Successfully','success')
    return render_template('todo.html',data=data)
    
    
@todo.route('/remove_todo', methods=['POST'])
def remove_todo():
    try:
        req = request.form
        print('REMOVING : ',req.get('rm-list'))
        data.remove(req.get('rm-list'))
        flash('Data Removed Successfully','warning')
        return render_template('todo.html',data=data)
    except Exception as error:
        print(error)
        flash('List is already empty','danger')
        return render_template('todo.html',data=data)
