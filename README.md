# Book_MS
A simple Django application that manages a list of books.
## Features
- Create, retrieve, update, and delete books
- Validates ISBN (must be 10 or 13 digits)
- Ensures publication date is not in the future.
# Installation
1. Clone the repository
   - git clone: https://github.com/Keithclinton/Book_MS.git
2. Run Migrations
   -Python manage.py makemigrations
   -Python manage.py migrate
3. Start the server
   -Python manage.py runserver
4. Run Unit test
   -python manage.py test     
