from flask import Flask

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAI_VERSION"] = "3.0.3"
app.config["OPENAI_URL_PREFIX"] = "/"
app.config["OPENAI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAI_SWAGGER_UI_URL"] = "https://cdn.jsdeliver.net/npm/swagger-ui-dist/"

if __name__ == '__main__':
    app.run(debug=True)
