from flask import Blueprint, render_template, request, make_response
from flask_login import login_required, current_user
#from .KeyGeneration import encrypt_message, decrypt
from .models import User 
from . import db
from .newrsa import encrypt_message, decrypt ,import_public,import_private

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        user = User.query.get(current_user.id)
        mode = request.form.get('type')
        if mode == '1':
        #print(user.public_key)
            
            public=import_public(user.public_key)
            cipher = encrypt_message(public, message=note)
            return render_template("home.html", cipher=cipher, user=user)
        
        elif mode == '0':
            with open("private.txt",'r') as f:
                pri_key=f.read()
            private=import_private(pri_key)
            plain_text=decrypt(private, note)
            return render_template("home.html", plain_text=plain_text, user=user)        

    return render_template("home.html", user=current_user)

def index():
    response=make_response(render_template('home.html'))
    response.headers['Content-Security-Policy']="default-src 'self' "
    return response
