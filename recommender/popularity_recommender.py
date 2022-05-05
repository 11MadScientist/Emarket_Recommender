from flask_restful import Api, Resource
from dao.ItemRepository import ItemRepository as item_repo
import pandas as pd

class PopularityRecommender(Resource):
    def get(self):
        data =  item_repo.getItems()
        return "hello"

        # df = pd.read_csv('ratings_Emerkado.csv')

        # df.drop('Timestamp', axis=1, inplace=True)

        # ratings_mean_count = pd.DataFrame(df.groupby('ProductId')['Rating'].mean())

        # ratings_mean_count['rating_counts'] = df.groupby('ProductId')['Rating'].count()

        # average_rating = df['Rating'].mean()
        # average_rating = average_rating if average_rating >= 3.5 else 3.5

        # ratings_mean_count['gtar'] = df.groupby('ProductId')['Rating'].mean() >= 4
        # ratings_mean_count['gtac'] = ratings_mean_count['rating_counts'] >= ratings_mean_count['rating_counts'].mean()

        # print("##################################################")
        # print("Original DataFrame:")
        # print(ratings_mean_count)

        # # print("##################################################")
        # # print("Removed False GTAR DataFrame:")
        # ratings_mean_count = ratings_mean_count[ratings_mean_count['gtar'] == True]
        # # print(ratings_mean_count)

        # # print("##################################################")
        # # print("Removed False GTAC DataFrame:")
        # ratings_mean_count = ratings_mean_count[ratings_mean_count['gtac'] == True]
        # # print(ratings_mean_count)

        # print("##################################################")
        # print("List of Popular ProductId")
        # popularlist = ratings_mean_count.index.tolist()
        # print(popularlist)


