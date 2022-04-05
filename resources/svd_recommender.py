from flask_restful import Api, Resource
from recommender.loadRecommender import recommend

class SVDRecommender(Resource):

    def get(self):
        return {"data":"Hello World"}
    
    def get(self, user_id):
        return recommend(user_id)


