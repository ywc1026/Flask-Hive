from flask import Blueprint, g, jsonify, render_template


page = Blueprint('page', __name__, url_prefix='/page')


@page.route('/main/')
def main():

    return render_template("main.html")