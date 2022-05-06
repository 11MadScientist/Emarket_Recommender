from flask import Flask
from flask_restful import Api, Resource
from resources.svd_recommender import SVDRecommender as svd_recommend
from recommender.popularity_model import PopularityRecommender as popularity_recommender
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
api.add_resource(svd_recommend, "/recommend/<int:user_id>")
api.add_resource(popularity_recommender, "/recommend")

app.config['SQLALCHEMY_DATABASE_URI']= "mysql://Hustle:teamhustle@localhost/emarketdb"  
db = SQLAlchemy(app)
item = db.Table('item', db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/')
def index():
    return "hello"

if __name__== "__main__":
    app.run(debug=True)