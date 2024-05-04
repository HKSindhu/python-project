class MovieDatabase:
    def __init__(self):
        self.movies = {}
        self.score = 0
        self.quiz_questions = {
            "What year was the movie 'KGF' released?": "2018",
            "Who directed the movie 'Kantara'?": "Rishab Shetty",
            "What is the genre of the kgf movie ?": "action"
        }

    def add_movie(self):
        title = input("Enter the movie title: ")
        director = input("Enter the director's name: ")
        year = input("Enter the release year: ")
        genre = input("Enter the genre: ")
        self.movies[title] = {"Director": director, "Year": year, "Genre": genre}
        print(f"{title} added to the movie database.")

    def display_movies(self):
        if self.movies:
            print("Movie database:")
            for title, info in self.movies.items():
                print(f"Title: {title}, Director: {info['Director']}, Year: {info['Year']}, Genre: {info['Genre']}")
        else:
            print("No movies found in the movie database.")

    def update_movie(self):
        title = input("Enter the title of the movie you want to update: ")
        if title in self.movies:
            print("Enter new information (leave blank to keep current value):")
            director = input(f"Director ({self.movies[title]['Director']}): ") or self.movies[title]['Director']
            year = input(f"Year ({self.movies[title]['Year']}): ") or self.movies[title]['Year']
            genre = input(f"Genre ({self.movies[title]['Genre']}): ") or self.movies[title]['Genre']
            self.movies[title] = {"Director": director, "Year": year, "Genre": genre}
            print(f"{title} updated in the movie database.")
        else:
            print(f"{title} not found in the movie database.")

    def delete_movie(self):
        title = input("Enter the title of the movie you want to delete: ")
        if title in self.movies:
            del self.movies[title]
            print(f"{title} deleted from the movie database.")
        else:
            print(f"{title} not found in the movie database.")

    def take_quiz(self):
        print("Welcome to the Movie Quiz!")
        for question, answer in self.quiz_questions.items():
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")
        print(f"You scored {self.score} out of {len(self.quiz_questions)}.")