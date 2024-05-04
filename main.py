from movie_database import MovieDatabase

movie_database = MovieDatabase()

while True:
    print("\nWelcome to the Interactive Movie Guide!")
    print("1. Add a movie")
    print("2. display all movie")
    print("3. Update a movie")
    print("4. Delete a movie")
    print("5. Take the Quiz")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        movie_database.add_movie()
    elif choice == '2':
        movie_database.display_movies()
    elif choice == '3':
        movie_database.update_movie()
    elif choice == '4':
        movie_database.delete_movie()
    elif choice == '5':
        movie_database.take_quiz()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")