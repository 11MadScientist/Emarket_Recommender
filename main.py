from flask import Flask
from flask_restful import Api, Resource
from resources.HelloWorld import HelloWorld

# class HelloWorld(Resource):
#     def get(self):
#         return {"data":"Hello World"}

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, "/recommend/<int:user_id>")


if __name__== "__main__":
    app.run(debug=True)