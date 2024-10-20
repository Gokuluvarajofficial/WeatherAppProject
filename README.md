# Weather Data Monitoring Application

## Project Overview
This project is designed to retrieve real-time weather data from the OpenWeatherMap API for multiple cities and store the data in a local SQLite database. It processes this data to generate daily summaries and visualizations that highlight the trends in temperature and weather conditions.

## Features
- Fetches real-time weather data for several cities using the OpenWeatherMap API.
- Stores data in an SQLite database.
- Generates individual visualizations for each city's weather data.
- Provides an overall weather summary comparison across all cities.

## Technologies Used
- **Python 3.12**
- **SQLite**: To store weather data.
- **Matplotlib**: For generating visualizations.
- **Requests**: For fetching data from the OpenWeatherMap API.

## How to Run the Project

### Step 1: Install Dependencies
Install the necessary Python libraries by running:
```bash
pip install -r requirements.txt
