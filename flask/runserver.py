from notejam import app
from notejam.config import Config

app.config.from_object(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
