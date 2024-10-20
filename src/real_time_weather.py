import requests
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# Define the cities
CITIES = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai']

# Your OpenWeatherMap API key
API_KEY = 'aa0d00371370dc6bf56bee581b7b4da8'

def create_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_summary (
        city TEXT,
        date TEXT,
        avg_temp REAL,
        max_temp REAL,
        min_temp REAL,
        condition TEXT,
        PRIMARY KEY (city, date)
    )
    ''')
    conn.commit()
    conn.close()

def fetch_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def save_weather_data(city, temp, max_temp, min_temp, condition):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    today_date = datetime.now().date()

    try:
        cursor.execute('''
            INSERT INTO daily_summary (city, date, avg_temp, max_temp, min_temp, condition)
            VALUES (?, ?, ?, ?, ?, ?)''', (city, today_date, temp, max_temp, min_temp, condition))
    except sqlite3.IntegrityError:
        cursor.execute('''
            UPDATE daily_summary
            SET avg_temp = ?, max_temp = ?, min_temp = ?, condition = ?
            WHERE city = ? AND date = ?''', (temp, max_temp, min_temp, condition, city, today_date))

    conn.commit()
    conn.close()

def calculate_daily_summary(city):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT AVG(avg_temp), MAX(max_temp), MIN(min_temp), MAX(condition)
        FROM daily_summary
        WHERE city = ?
    ''', (city,))
    
    avg_temp, max_temp, min_temp, condition = cursor.fetchone()

    save_daily_summary(city, avg_temp, max_temp, min_temp, condition)
    conn.close()

def save_daily_summary(city, avg_temp, max_temp, min_temp, condition):
    print(f"Daily summary saved for {city}: Avg Temp={avg_temp}, Max Temp={max_temp}, Min Temp={min_temp}, Condition={condition}")

def generate_visualization(city):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT date, avg_temp, max_temp, min_temp FROM daily_summary WHERE city = ?
    ''', (city,))
    data = cursor.fetchall()

    dates = [row[0] for row in data]
    avg_temps = [row[1] for row in data]
    max_temps = [row[2] for row in data]
    min_temps = [row[3] for row in data]

    plt.plot(dates, avg_temps, marker='o', label='Avg Temp', color='blue')
    plt.plot(dates, max_temps, marker='o', label='Max Temp', color='orange')
    plt.plot(dates, min_temps, marker='o', label='Min Temp', color='green')

    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Daily Weather Summary for {city}')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'visualizations/{city}_weather_summary.png')
    plt.close()

    conn.close()

def main():
    create_db()

    for city in CITIES:
        weather_data = fetch_weather_data(city)
        if weather_data['cod'] == 200:
            temp = weather_data['main']['temp']
            max_temp = weather_data['main']['temp_max']
            min_temp = weather_data['main']['temp_min']
            condition = weather_data['weather'][0]['description']
            
            save_weather_data(city, temp, max_temp, min_temp, condition)
            calculate_daily_summary(city)
            generate_visualization(city)
            print(f"Weather data saved for {city}: Temp={temp}°C, Max Temp={max_temp}°C, Min Temp={min_temp}°C, Condition={condition}")
        else:
            print(f"Error fetching data for {city}: {weather_data['message']}")

if __name__ == "__main__":
    main()

