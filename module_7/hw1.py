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
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


db_engine = create_engine("sqlite:///films_db.db")
Base = declarative_base()


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)


Base.metadata.create_all(db_engine)

Session = sessionmaker(bind=db_engine)
session = Session()

film1 = Film(title='Star Wars. Episode IV: A New Hope', director='George Lucas', release_year=1977)
film2 = Film(title='Star Wars: Episode VII: The Force Awakens', director='J.J. Abrams', release_year=2015)
film3 = Film(title='Star Wars: Episode VIII: The Last Jedi', director='Rian Johnson', release_year=2017)

session.add_all([film1, film2, film3])
session.commit()

film_to_update = session.query(Film).filter_by(title='Star Wars. Episode IV: A New Hope').first()
if film_to_update:
    film_to_update.director = 'George Lucas ft. Disney'
    session.commit()

films = session.query(Film).all()
for film in films:
    print(f'ID: {film.id},  Title: {film.title},  Director: {film.director},  Release Year: {film.release_year}')

session.query(Film).delete()
session.commit()

session.close()
