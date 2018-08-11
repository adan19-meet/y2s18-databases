from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):

   __tablename__ = 'Knowledge'
   article_id = Column(Integer, primary_key=True)
   title = Column(String)
   rating = Column(Integer)
   is_useful = Column(Boolean)

   def __repr__(self):
       return ("article_id: {}\n"
               "title: {} \n"
               "rating: {}\n"
               "is_useful: {}".format(
                    self.article_id,
                    self.title,
                    self.rating , self.is_useful))
x = Knowledge(article_id=4,title="cats",rating=10,is_useful= True)



	