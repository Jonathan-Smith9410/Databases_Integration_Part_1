from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# NOTE - below section commented out for ease when working with application layer in Databses Part 3 Section 3, beginning with application class

# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")



# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# # Retrieve all albums and list them out
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()
# for album in albums:
#     print(album)

# # Retrieve the album with id=1 and print it
# album_repository = AlbumRepository(connection)
# album = album_repository.find(1)
# print(album)

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the Music Library Manager!")
        print("")
        print("What would you like to do?")
        print("1 - List all albums")
        print("2 - List all artists")
        print("")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            for album in albums:
                print(f"Album({album.id}, {album.title}, {album.release_year}, {album.artist_id}")
        elif choice == 2:
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        else:
            print("Not an option. Bye!")
            quit()

# "Runs" the terminal application.
# It might:
#   * Ask the user to enter some input
#   * Make some decisions based on that input
#   * Query the database
#   * Display some output
# We're going to print out the artists!



if __name__ == '__main__':
    app = Application()
    app.run()