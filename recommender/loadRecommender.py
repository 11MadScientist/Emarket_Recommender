import pandas as pd

from collections import defaultdict

def get_top_n(user_id, predictions, n):
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[user_id].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

def load_model(model_filename):
    print (">> Loading dump")
    from surprise import dump
    import os
    file_name = os.path.expanduser(model_filename)
    _, loaded_model = dump.load(file_name)
    print (">> Loaded dump")
    return loaded_model

import numpy as np


# function to get unique values
def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    return unique_list

def recommend(user_id):
    SVD_model = load_model('EmerkadoRecommender.pickle')

    df = pd.read_csv('ratings_Emerkado2.csv')
    df.drop('Timestamp', axis=1, inplace=True)

    # df = df.values.tolist()
    # from surprise import Reader, Dataset
    # from surprise.model_selection import train_test_split

    """
    userID = df.groupby('UserId').count()
    top_user = userID[userID['Rating'] >= 50].index
    topuser_ratings_df = df[df['UserId'].isin(top_user)]
    prodID = df.groupby('ProductId').count()
    top_prod = prodID[prodID['Rating'] >= 5].index
    top_ratings_df = topuser_ratings_df[topuser_ratings_df['ProductId'].isin(top_prod)]
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(top_ratings_df[['UserId', 'ProductId', 'Rating']], reader)
    trainset, testset = train_test_split(data, train_size=None, random_state=0)
    """

    df = df.values.tolist()

    test_pred = SVD_model.test(df)
    # test_pred = SVD_model.test(testset)

    top_n = get_top_n(user_id, test_pred, n=400)

    list_recommendations = list()
    userid = ''

    for uid, user_ratings in top_n.items():
        userid = uid
        list_recommendations += ([iid for (iid, _) in user_ratings])

        # print(uid, [iid for (iid, _) in user_ratings])

    # from surprise import accuracy

    # accuracy.rmse(test_pred)

    print("TOP 10")
    list_recommendations = unique(list_recommendations)

    data_to_send = list()
    data_to_send.append(userid)
    data_to_send.append(list_recommendations[0:10])

    #print(userid)
    #print(list_recommendations[0:5])

    print(data_to_send)
    return data_to_send[1]