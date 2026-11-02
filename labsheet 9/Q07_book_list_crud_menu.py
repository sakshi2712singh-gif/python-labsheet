def main():
    # Keep book records in a list for the duration of this menu session.
    books = [
        {"book_id": 1, "title": "Python Basics", "author": "A. Writer"},
        {"book_id": 2, "title": "Learning SQL", "author": "B. Reader"},
    ]
    while True:
        # Display the CRUD actions for book records.
        print("\nBook CRUD: 1 Add  2 View  3 Update  4 Delete  5 Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                book_id = int(input("Book ID: "))
                if any(book["book_id"] == book_id for book in books):
                    print("That book ID already exists.")
                    continue
                title = input("Book title: ").strip()
                author = input("Author: ").strip()
                if not title or not author:
                    print("Title and author cannot be empty.")
                    continue
                books.append({"book_id": book_id, "title": title, "author": author})
                print("Book added.")
            elif choice == "2":
                for book in sorted(books, key=lambda item: item["book_id"]):
                    print(f"{book['book_id']}: {book['title']} by {book['author']}")
                if not books:
                    print("No books found.")
            elif choice == "3":
                book_id = int(input("Book ID to update: "))
                book = next((item for item in books if item["book_id"] == book_id), None)
                if book is None:
                    print("No book has that ID.")
                    continue
                title = input("New title: ").strip()
                author = input("New author: ").strip()
                if not title or not author:
                    print("Title and author cannot be empty.")
                    continue
                book.update({"title": title, "author": author})
                print("Book updated.")
            elif choice == "4":
                book_id = int(input("Book ID to delete: "))
                remaining = [book for book in books if book["book_id"] != book_id]
                if len(remaining) == len(books):
                    print("No book has that ID.")
                else:
                    books = remaining
                    print("Book deleted.")
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Choose a number from 1 to 5.")
        except ValueError as error:
            print(f"Enter a valid whole-number book ID: {error}")


if __name__ == "__main__":
    main()
