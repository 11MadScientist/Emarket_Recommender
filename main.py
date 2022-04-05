from flask import Flask
from flask_restful import Api, Resource
from resources.svd_recommender import SVDRecommender as svd_recommend

# class HelloWorld(Resource):
#     def get(self):
#         return {"data":"Hello World"}

app = Flask(__name__)
api = Api(app)

api.add_resource(svd_recommend, "/recommend/<int:user_id>")


if __name__== "__main__":
    app.run(debug=True)