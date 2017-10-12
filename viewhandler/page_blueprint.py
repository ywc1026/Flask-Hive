from flask import Blueprint, render_template


page = Blueprint('page', __name__, url_prefix='/page')


@page.route('/main/')
def main():

    return render_template("main.html")