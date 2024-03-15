from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


record = Blueprint('record', __name__, url_prefix='/record')


@record.context_processor
def loader():
    pass


@record.route('/', methods=['GET', 'POST'])
def patients():
    return render_template('/home/records/patients.html')
