from flask import Blueprint, g, jsonify, render_template


page = Blueprint('page', __name__, url_prefix='/page')


@page.route('/index')
def index():
    print g.args.get('account', None)

    return jsonify({'number': 12})


@page.route('/main/')
def main():

    return render_template("main.html")