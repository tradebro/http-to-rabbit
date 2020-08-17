from os import environ
from httptorabbit import create_app


if __name__ == '__main__':
    app = create_app()

    APP_HOST = environ.get('APP_HOST')
    APP_PORT = int(environ.get('APP_PORT'))
    APP_DEBUG = True if environ.get('APP_DEBUG') == 1 else False

    app.run(host=APP_HOST,
            port=APP_PORT,
            debug=APP_DEBUG)
