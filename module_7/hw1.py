# Create a new database named "films_db".
# Use the SQLAlchemy library to create the database and tables in Python.
# Part 1: Setting up the Database
# Create one table for films, with the following columns:
#     films table:
#         id (integer, primary key)
#         title (string)
#         director (string)
#         release year (integer)
# Part 2: Manipulating with Database
#     Create script that:
#         Add 3 film to the film table.
#         Update 1 film
#         Print data from table
#         Delete all data from table

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)


db_engine = create_engine("sqlite:///films_db.db")

Base.metadata.create_all(db_engine)

Session = sessionmaker(bind=db_engine)
session = Session()

new_data = Film(id=1, title='title 1', director='director 1', release_year=1986)
session.add(new_data)
session.commit()

result = session.query(Film).filter_by(id=1).first()

session.close()



# Create a session
Session = sessionmaker(bind=db_engine)
session = Session()

# Select all rows from a table
result = session.query(Film).all()
for row in result:
    print(row.name)

# Create a session
Session = sessionmaker(bind=db_engine)
session = Session()

# Select all rows from a table
result = session.query(Film).all()
for row in result:
    print(row.name)

# Close the session when done
session.close()




