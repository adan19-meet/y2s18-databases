from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(title, rating, is_useful):
    article_object = Knowledge(
        
        title=title,
        rating=rating,
        is_useful=is_useful
        )
    session.add(article_object)
    session.commit()
add_article("fruits",5,True)
def query_all_articles():
    article = session.query(Knowledge).all()
    return article
print(query_all_articles())

def query_article_by_topic(article_title):
    article_two = session.query(Knowledge).filter_by(title=article_title).all
    return article_two
query_article_by_topic("fruits")
    

def delete_article_by_topic(topic):
    session.query(Knowledge).filter_by(title=topic).delete()
    session.commit()

delete_article_by_topic("cats")



    

def delete_all_articles():
    session.query(Knowledge).all().delete()
    session.commit()   
#delete_all_articles()

def edit_article_rating(update_rating , article_tirle):
#    """
#    Update a student in the database, with
#    whether or not they have finished the lab
#    """
    article_object = session.query(
        Knowledge).filter_by(
        title=article_tirle).all()
    article_object.rating= update_rating
    session.commit()
edit_article_rating(6 ,"fruits" )



# def bbs(number):
#     article=session.query(Knowledge).filter_by(article_id = number)
#     return article

# #print(bbs(4))
# edit_article_rating(5,"dogs")

    
