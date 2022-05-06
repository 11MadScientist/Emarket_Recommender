from flask_restful import Api, Resource
from recommender.svd_model import recommend

class SVDRecommender(Resource):
    
    def get(self, user_id):
        return recommend(user_id)


