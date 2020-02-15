from flask import Flask

import settings
from apis import api

app = Flask(settings.FLASK_APP)
api.init_app(app)


def config_app():
    app.config['ENV'] = settings.FLASK_ENVIRONMENT
    app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    app.config['RESTPLUS_VALIDATE'] = settings.FLASK_RESTPLUS_VALIDATE
    app.config['RESTPLUS_MASK_SWAGGER'] = settings.FLASK_RESTPLUS_MASK_SWAGGER


def main():
    config_app()
    app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG)


if __name__ == '__main__':
    main()
