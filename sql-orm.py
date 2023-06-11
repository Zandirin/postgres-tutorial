from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# execute instructions from chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Create instance of sessionmaker
Session = sessionmaker(db)
# Create an actual session | call Session subclass defined at line 14
session = Session()

# Create the database using declaritive_base subclass
base.metadata.create_all(db)

# First Query - Select all record in Artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Second Query - Select the name column from artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Third Query - Find Queen in Artist table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Fourth Query - Select specified artistid from artist table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Fifth Query - Select only the albums from the album list with artist ID of 51
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Sixth Query - Select all tracks composed by Queen
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, sep=" | ")
