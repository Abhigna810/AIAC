def recommend_book():
    genres = {
        "Horror": ["Devil Nights", "The Haunting of Hill House", "It", "Dracula"],
        "Science Fiction": ["Dune", "Neuromancer", "Ender's Game", "The Martian"],
        "Fantasy": ["The Hobbit", "Harry Potter and the Sorcerer's Stone", "Mistborn", "The Name of the Wind"],
        "Mystery": ["Gone Girl", "The Girl with the Dragon Tattoo", "Sherlock Holmes", "Big Little Lies"],
        "Romance": ["Pride and Prejudice", "The Notebook", "Outlander", "Me Before You"],
        "Non-Fiction": ["Sapiens", "Educated", "Becoming", "The Immortal Life of Henrietta Lacks"]
    }

    print("Select genre:")
    for idx, genre in enumerate(genres.keys(), 1):
        print(f"{idx}. {genre}")

    try:
        choice = int(input("Enter the number of your preferred genre: "))
        genre_list = list(genres.keys())
        if 1 <= choice <= len(genre_list):
            selected_genre = genre_list[choice - 1]
            import random
            book = random.choice(genres[selected_genre])
            print(f"Book: {book}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    recommend_book()

