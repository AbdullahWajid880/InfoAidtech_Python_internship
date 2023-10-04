import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextBrowser, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

# Replace with your OpenWeatherMap API key
API_KEY = "e3a5c6ae33503f7560b6db802845ca7d"

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("5-Day Weather Forecast")
        self.setGeometry(300, 300, 600, 600)

        # Create a custom color palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(100, 149, 237))  # Light Steel Blue background
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))  # White text
        palette.setColor(QPalette.Button, QColor(70, 130, 180))  # Steel Blue buttons
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))  # White button text
        palette.setColor(QPalette.Base, QColor(240, 248, 255))  # Alice Blue base color
        self.setPalette(palette)

        self.city_label = QLabel("Enter city:")
        self.city_label.setFont(QFont("Arial", 12))
        self.city_input = QLineEdit()
        self.city_input.setFont(QFont("Arial", 12))

        # Create a styled button
        self.fetch_button = QPushButton("Fetch Forecast")
        self.fetch_button.setFont(QFont("Arial", 12))
        self.fetch_button.setStyleSheet(
            """
            background-color: #4A90E2; /* Steel Blue */
            color: #FFFFFF; /* White text */
            border: 1px solid #357ABD; /* Darker Steel Blue border */
            border-radius: 10px; /* Rounded corners */
            """
        )

        self.result_display = QTextBrowser()
        self.result_display.setFont(QFont("Arial", 12))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.city_label)
        self.layout.addWidget(self.city_input)
        self.layout.addWidget(self.fetch_button)
        self.layout.addWidget(self.result_display)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.fetch_button.clicked.connect(self.fetch_weather)

    def fetch_weather(self):
        city = self.city_input.text()
        if not city:
            return

        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            self.display_weather(weather_data)
        else:
            self.result_display.setText("Error fetching weather data. Please check the city name.")

    def display_weather(self, weather_data):
        self.result_display.clear()

        if "list" not in weather_data:
            self.result_display.setText("No weather data available.")
            return

        self.result_display.append(f"Weather forecast for {weather_data['city']['name']}:\n")

        for forecast in weather_data["list"]:
            timestamp = forecast["dt"]
            date = forecast["dt_txt"].split()[0]
            time = forecast["dt_txt"].split()[1]
            temperature = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]

            self.result_display.append(f"{date} {time}:")
            self.result_display.append(f"Temperature: {temperature}°C")
            self.result_display.append(f"Description: {description.capitalize()}")
            self.result_display.append("-" * 30)

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
