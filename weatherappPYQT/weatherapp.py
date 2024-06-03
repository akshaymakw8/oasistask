import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import requests
import os

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.location_label = QLabel('Enter Location:')
        layout.addWidget(self.location_label)

        self.location_edit = QLineEdit()
        layout.addWidget(self.location_edit)

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_weather)
        layout.addWidget(self.search_button)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def search_weather(self):
        location = self.location_edit.text()
        weather_data = self.fetch_weather(location)
        self.display_weather(weather_data)

    def fetch_weather(self, location):
        api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual weather API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def display_weather(self, weather_data):
        if weather_data:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            self.result_label.setText(f'Temperature: {temperature}°C\nDescription: {description}')
        else:
            QMessageBox.warning(self, 'Error', 'Failed to fetch weather data')

if __name__ == '__main__':

    os.environ["QT_LOGGING_RULES"] = "qt.qpa.*=false"

    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
