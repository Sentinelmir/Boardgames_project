# Boardgame World

Boardgame World is a small Django web application for cataloging board games, writing reviews, and grouping games into curated collections.

The idea for the project comes from my personal interest in board games. I wanted to build a simple and cozy place where different games can be added, described, reviewed, and organized by theme.

## Features

- Home page with latest games and featured collections
- Full CRUD for games
- Full CRUD for reviews
- Collections list and collection details
- Multiple genres per game
- Filtering games by genre and player count
- Sorting games by title or duration
- Custom 404 page
- Reusable partial templates and shared base layout

## Project structure

The project contains three Django apps:

- `games` — game catalog, game details, genres, create/edit/delete pages
- `games_collections` — curated game collections
- `reviews` — review list, create/edit/delete review pages

## Models and relationships

- `Game`
- `Collection`
- `Review`

Relationships:
- One `Game` can have many `Review` objects
- One `Collection` can contain many `Game` objects
- One `Game` can belong to many `Collection` objects

## Tech stack

- Python
- Django
- PostgreSQL
- Bootstrap 5
- django-unfold

## Environment variables

Create a `.env` file in the project root and add:

```env
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432