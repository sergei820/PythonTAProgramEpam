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

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

db_engine = create_engine("sqlite:///films_db.db")

Base.metadata.create_all(db_engine)

