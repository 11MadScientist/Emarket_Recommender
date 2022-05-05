from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= "mysql://Hustle:teamhustle@localhost/emarketdb"  
db = SQLAlchemy(app)
item = db.Table('item', db.metadata, autoload=True, autoload_with=db.engine)

class ItemRepository:
    def getItems():
        results = db.session.query(item.c.id, item.c.overallreview).all()
        for r in results:
            print(r)
            
        return results
