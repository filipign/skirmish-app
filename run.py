from backend import create_app
from backend import c

if __name__ == "__main__":
    app = create_app()
    app.run(host=c.config['app']['host'], port=c.config['app']['port'])
