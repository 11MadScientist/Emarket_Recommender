from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= "mysql://Hustle:teamhustle@localhost/emarketdb"  
db = SQLAlchemy(app)
item = db.Table('item', db.metadata, autoload=True, autoload_with=db.engine)

class ItemRepository:
    def getItems():
        results = db.session.query(item.c.id, item.c.overallreview).all()

        # results = [(1, 4),
        # (2, 5),
        # (3, 3),
        # (4, 3),
        # (5, 3)]
        
        results = [list(x) for x in results]

        for x in results:
            x[1] = float(x[1])

        print(results)

        return results
