# Weather Data Monitoring Application

This project retrieves real-time weather data from the OpenWeatherMap API for multiple cities and stores it in an SQLite database. The application processes the data to generate daily summaries and visualizations to highlight trends in temperature and weather conditions.

## Table of Contents

- [Objective](#objective)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [Fetching Weather Data](#fetching-weather-data)
  - [Visualizing Weather Data](#visualizing-weather-data)
- [Screenshots](#screenshots)
  - [1. Bangalore Weather Summary](#1-bangalore-weather-summary)
  - [2. Chennai Weather Summary](#2-chennai-weather-summary)
  - [3. Delhi Weather Summary](#3-delhi-weather-summary)
  - [4. Hyderabad Weather Summary](#4-hyderabad-weather-summary)
  - [5. Kolkata Weather Summary](#5-kolkata-weather-summary)
  - [6. Mumbai Weather Summary](#6-mumbai-weather-summary)
  - [7. Overall Weather Summary](#7-overall-weather-summary)
- [Conclusion](#conclusion)
- [License](#license)

## Objective

This project aims to showcase how real-time weather data can be fetched from the OpenWeatherMap API, stored in an SQLite database, and visualized to analyze temperature and weather trends across multiple cities.

## Features

- **Real-Time Data Fetching**: Fetches real-time weather data for multiple cities using the OpenWeatherMap API.
- **Data Storage**: Stores weather data in an SQLite database for persistent storage.
- **City-Specific Visualizations**: Generates weather visualizations for each city, including daily average, maximum, and minimum temperatures.
- **Overall Comparisons**: Provides a comparative visualization of weather data across all cities.

## Technologies Used

- **Python 3.12**: Used for backend processing.
- **SQLite**: Database used to store weather data.
- **Matplotlib**: Used to generate the weather visualizations.
- **Requests**: Used to fetch data from the OpenWeatherMap API.

## Setup and Installation

### Prerequisites

1. Python 3.x
2. `pip` for installing dependencies

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/Gokuluvarajofficial/WeatherAppProject.git
    cd WeatherAppProject
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Step 1: Start the Application

To fetch the weather data and generate visualizations, run the following command:
```bash
python src/real_time_weather.py
