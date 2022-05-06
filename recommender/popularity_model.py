from flask_restful import Api, Resource
from sqlalchemy import null
from dao.ItemRepository import ItemRepository as item_repo
import pandas as pd

class PopularityRecommender(Resource):
    def get(self):
        data =  item_repo.getItems()

        data.insert(0, ['ProductId', 'Rating'])

        df = pd.DataFrame(data[1:], columns=data[0])

        ratings_mean_count = pd.DataFrame(df.groupby('ProductId')['Rating'].mean())

        ratings_mean_count['rating_counts'] = df.groupby('ProductId')['Rating'].count()

        average_rating = df['Rating'].mean()
        average_rating = average_rating if average_rating >= 3.5 else 3.5

        ratings_mean_count['gtar'] = df.groupby('ProductId')['Rating'].mean() >= 4
        ratings_mean_count['gtac'] = ratings_mean_count['rating_counts'] >= ratings_mean_count['rating_counts'].mean()

        print("##################################################")
        print("Original DataFrame:")
        print(ratings_mean_count)

        ratings_mean_count = ratings_mean_count[ratings_mean_count['gtar'] == True]
        ratings_mean_count = ratings_mean_count[ratings_mean_count['gtac'] == True]

        print("##################################################")
        print("List of Popular ProductId")
        popularlist = ratings_mean_count.index.tolist()
        print(popularlist)

        if not popularlist:
            return [-1]

        return popularlist