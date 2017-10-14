from flask import Flask, g, request, session
from viewhandler.page_blueprint import page
from viewhandler.user_blueprint import user


app = Flask(__name__)

app.config.from_pyfile('config.py')


BLUEPRINT = [page, user]


@app.context_processor
def common():
    return {
        'isLogin': True  if session.get('fworkid', None) else False
    }


def boostrap_app(app):

    for view in BLUEPRINT:
        app.register_blueprint(view)



    @app.before_request
    def beforre():

        args = {k: v[0] for k, v in dict(request.args).items()}    # get
        args_form = {k: v[0] for k, v in dict(request.form).items()}    # post
        args.update(args_form)
        g.args = args


boostrap_app(app)


if __name__ == '__main__':

    app.run(host=app.config['WEB_HOST'], port=app.config['WEB_PORT'])