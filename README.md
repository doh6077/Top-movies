# Movie Collection Manager with Flask 🎬

This project is designed to help users manage their movie collections effortlessly. 
It enables users to perform actions like viewing, adding, updating, and deleting movies from their personal collection.

<img src="https://github.com/doh6077/Top-movies/assets/134092191/25b7a705-e03d-4398-9d64-c046f587acc7">

## Key Features 🌟

- **Browse Movies**: Users can easily browse through their curated list of top 10 favorite movies, accessing detailed information such as title, release year, rating, review, and description.
- **Add New Movies**: Users have the capability to expand their collection by adding new movies. The application integrates with the Movie Database API, allowing users to search for desired movies and select them from the search results.
- **Update Movie Details**: Users can modify existing movie entries by updating their rating and review.
- **Delete Movies**: Unwanted movies can be removed from the collection, providing users with full control over their movie database.

## Required Dependencies 🛠️

- Flask
- Flask-Bootstrap
- Flask-SQLAlchemy
- Flask-WTF
- WTForms
- Requests
- SQLAlchemy

## Movie Database Integration 🎥

This application leverages the [Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api) to retrieve movie information, including titles, release dates, overviews, and poster images. Through integration with this API, users can search for specific movies and access detailed information like description and posters.

## Installation Instructions ⚙️

1. Clone this repository to your local machine.

2. Install Virtual Environment:
   ```
    python -m venv venv 
    ```
3. Activate Virtual Environment
4. Install the necessary dependencies listed in the `requirements.txt` file using pip:

    ```
    pip install -r requirements.txt
    ```
5. Launch the Flask application:

    ```
    set FLASK_APP=main.py
    ```
    ```
    flask run 
    ```
4. Access the application via your web browser at `http://localhost:5000`.

## Usage Guidelines 🚀

- Upon accessing the application, users will immediately gain access to their top 10 favorite movies.
- To augment the collection, users can simply click the "Add Movie" button and utilize the provided search functionality to find and select desired movies.
- For existing entries, users have the option to update movie details, including ratings and reviews, by clicking the "Update" button adjacent to the respective movie.
- To declutter the collection, users can effortlessly delete unwanted movies by clicking the "Delete" button associated with each movie entry.


