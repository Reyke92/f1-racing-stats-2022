# F1 Racing Stats

A Django web application for displaying Formula 1 racing statistics through a relational database-backed website.

This project was built to present F1 race data in a clean, browser-based format while strengthening skills in:

- data processing
- SQL and relational data modeling
- Django web development
- HTML templating and UI layout
- integrating backend data with frontend presentation

## Overview

F1 Racing Stats is a statistics-focused web application that displays Formula 1 information such as:

- current-year race winners
- driver standings by points
- Grand Prix-specific race results
- qualifying results
- sprint results for sprint weekends

The project uses Django for the web framework and a MySQL database backend for storing and querying racing data. It also uses Bootstrap for layout and styling, along with Django templates for rendering dynamic content.

## Project Goal

The goal of this project was to build a website that could present F1 racing statistics in an organized and user-friendly way while reinforcing practical backend and frontend development skills.

In particular, this project helped strengthen experience with:

- designing relational models for real-world data
- querying and aggregating racing results
- processing data into rankings and standings
- building dynamic web pages with Django views and templates
- structuring a multi-page website with reusable layouts

## Features

### Current implemented features

- Homepage showing Formula 1 race winners for the current year
- Driver rankings page showing yearly standings by total points
- Grand Prix detail page showing:
  - race results
  - qualifying results
  - sprint results when applicable
- Navigation between major ranking views
- Bootstrap-based layout and styling
- Custom Python utility logic for ranking and sorting race data

### In-progress / partially implemented areas

- Team rankings page scaffold exists but appears unfinished
- Race list route exists in the views, but the repository appears focused more strongly on rankings and Grand Prix detail displays than on a completed race-list page

## Tech Stack

- **Backend:** Django
- **Database:** MySQL
- **Frontend:** HTML, Django Templates, Bootstrap, CSS
- **Language:** Python
- **Other tools:** requests, sqlparse, pipreqs

## How the Application Works

The application is centered around a relational F1 data model and a set of helper functions that process database records into rankings for display.

### Data model

The project defines models for core F1 entities such as:

- `GP`
- `Track`
- `Event`
- `Qualifying`
- `Sprint`
- `Race`
- `Driver`
- `Team`

This structure allows the application to represent a Grand Prix weekend, connect drivers to teams, and store multiple types of race-related results.

### Ranking logic

Ranking and data-processing logic lives in `f1site/f1utils.py`.

This utility layer is responsible for tasks such as:

- collecting Grand Prix events for a given year
- summing driver points across races
- including sprint points when applicable
- sorting rankings by points or finishing position
- handling DNF-style placement logic through a special sentinel value

This design keeps business logic separate from the view layer and makes the ranking process easier to understand and maintain.

### Views and pages

The site currently includes routes for:

- `/` - homepage
- `/drivers/` - driver rankings
- `/drivers/<int:year>` - driver rankings by year
- `/races/` - race-related view
- `/gp/<int:gpID>` - Grand Prix detail page
- `/teams/` - team rankings page

## Project Structure

```text
.
|-- README.md
|-- requirements.txt
|-- Lib/                         # Committed virtual environment contents
|-- Scripts/
|   |-- website/
|   |   |-- manage.py
|   |   |-- db.sqlite3
|   |   |-- f1site/             # Main Django app
|   |   |   |-- models.py
|   |   |   |-- views.py
|   |   |   |-- urls.py
|   |   |   `-- f1utils.py
|   |   |-- templates/
|   |   |   |-- base.html
|   |   |   |-- index.html
|   |   |   |-- drivers.html
|   |   |   |-- gp.html
|   |   |   `-- teams.html
|   |   |-- static/
|   |   |   `-- static_dirs/
|   |   |       `-- css/
|   |   |           `-- styles.css
|   |   `-- website/            # Django project configuration
|   |       |-- settings.py
|   |       |-- urls.py
|   |       |-- asgi.py
|   |       `-- wsgi.py
|   `-- ...                     # Virtual environment executables
`-- pyvenv.cfg
