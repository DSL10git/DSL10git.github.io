import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WeatherApp:
    def _get_weather(self, city):
        api_key = "a96d2b017a1a7133c7422d3e9c9f9ff3"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" 

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("400 Bad request: \nPlease Cheak your input! ")
                case 401:
                    self.display_error("401 Unauthourized: \nInvaild API Key!")
                case 403:
                    self.display_error("403 Forbidden: \nAccess is denied! ")
                case 404:
                    self.display_error("405 Not found: \nPlace not found! ")
                case 500:
                    self.display_error("500 Internal Server Error: \nPlease try again later! ")
                case 501:
                    self.display_error("501 Not Implemented: \nNot Supported! ")
                case 502:
                    self.display_error("Bad Gateway: \nInvalid response from the server! ")
                case 503:
                    self.display_error("Service Unavaliable: \nServer is down! ")
                case 504:
                    self.display_error("Gateway Timeout: \nNo response from the server! ")
                case _:
                    self.display_error(f"HTTP Error occured\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connnection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "⛆"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 500 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

def get_address_from_coordinates(lat, lon):
    """
    Get address from latitude and longitude using Nominatim API (OpenStreetMap).
    
    Args:
    lat (float): Latitude.
    lon (float): Longitude.
    
    Returns:
    str: Address corresponding to the coordinates.
    """
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        data = response.json()
        if "address" in data:
            return data["display_name"]
        else:
            return "No address found for these coordinates."
    else:
        return f"HTTP Error: {response.status_code}"


try:
    from pyscript import document, display
    class WeatherAppHTML(WeatherApp):
        def __init__(self):
            super().__init__()
            self.place = document.querySelector("#place")
            self.temperature_label = document.querySelector("#temperature")
            self.emoji_label = document.querySelector("#emoji")
            self.description_label = document.querySelector("#description")
            self.fahrenheit_button = document.querySelector("#fahrenheit")
            self.celsius_button = document.querySelector("#celsius")
            self.kelvin_button = document.querySelector("#kelvin")
            self.more_section = document.querySelector("#more_section")
            self.more_label = document.querySelector("#more")
            self.mph_button = document.querySelector("#mph")
            self.kmh_button = document.querySelector("#kmh")
            self.address_label = document.querySelector("#address")
            self.more_text = document.querySelector("#more_text")

        def display_error(self, message):
            self.temperature_label.innerText = message
            self.emoji_label.innerText = ""
            self.description_label.innerText = ""

        def display_weather(self, data):
            temperature_k = data["main"]["temp"]
            weather_id = data["weather"][0]["id"]
            if self.celsius_button.checked:
                temperature = temperature_k - 273.15
                self.temperature_label.innerText = f"{temperature:.1f} °C"
            elif self.fahrenheit_button.checked:
                temperature = (temperature_k * 9/5) - 459.67
                self.temperature_label.innerText = f"{temperature:.0f} °F"
            elif self.kelvin_button.checked:
                self.temperature_label.innerText = f"{temperature_k:.0f} K"
            weather_description = data["weather"][0]["description"]
            self.emoji_label.innerText = self.get_weather_emoji(weather_id)
            self.description_label.innerText = weather_description

        def display_more(self, data):
            if self.more_section.hidden:
                self.more_section.hidden = False
                self.more_text.innerText = "Hide More"


                more_info = ""
                feels_like_k = data["main"]["feels_like"]
                if self.celsius_button.checked:
                    feels_like = feels_like_k - 273.15
                    more_info += f"Feels like: {feels_like:.1f} °C"
                elif self.fahrenheit_button.checked:
                    feels_like = (feels_like_k * 9/5) - 459.67
                    more_info += f"Feels like: {feels_like:.0f} °F"
                elif self.kelvin_button.checked:
                    more_info += f"Feels like: {feels_like_k:.0f} K"

                wind_speed = data["wind"]["speed"]
                # Wind Speed
                if self.mph_button.checked:
                    wind_speed = wind_speed * 2.23694  # Convert m/s to mph
                    more_info += f"\nWind speed: {wind_speed:.1f} mph"
                elif self.kmh_button.checked:
                    wind_speed = wind_speed * 3.6  # Convert m/s to km/h
                    more_info += f"\nWind speed: {wind_speed:.1f} km/h"
                else:
                    pass

                latitude = data["coord"]["lat"]
                longitude = data["coord"]["lon"]
                address = get_address_from_coordinates(latitude, longitude)
                address = f"Address: {address}"
                self.more_label.innerText = more_info
                self.address_label.innerText = address

            else:
                self.more_section.hidden = True
                self.more_text.innerText = "Show More"

        def get_weather(self):
            place = self.place.value
            data = super()._get_weather(place)
            return data


    def display_weather(p):
        app = WeatherAppHTML()
        data = app.get_weather()
        if data and data['cod'] == 200:
            app.display_weather(data)


    def display_more(p):
        app = WeatherAppHTML()
        data = app.get_weather()
        if data and data['cod'] == 200:
            app.display_weather(data)
            app.display_more(data)


except:
    from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QRadioButton, QButtonGroup,
                                QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
    from PyQt5.QtCore import Qt

    class WeatherAppQt(QWidget, WeatherApp):
        def __init__(self):
            super().__init__()
            self.city_label = QLabel("Enter a place: ", self)
            self.city_input = QLineEdit(self)
            self.get_weather_button = QPushButton("Get Weather", self)
            self.celsius_button = QRadioButton("Celsius")
            self.fahrenheit_button = QRadioButton("Fahrenheit")
            self.kelvin_button = QRadioButton("Kelvin")
            self.celsius_button.setChecked(True)
            self.mph_button = QRadioButton("mph")  # Line for mph option
            self.kmh_button = QRadioButton("km/h")  # Line for km/h option
            self.kmh_button.hide()
            self.mph_button.setChecked(True)  # Default to mph
            self.mph_button.hide()

            self.wind_unit_group = QButtonGroup()
            self.wind_unit_group.addButton(self.mph_button)
            self.wind_unit_group.addButton(self.kmh_button)


            self.unit_group = QButtonGroup()
            self.unit_group.addButton(self.celsius_button)
            self.unit_group.addButton(self.fahrenheit_button)
            self.unit_group.addButton(self.kelvin_button)

            self.temperature_label = QLabel(self)
            self.emoji_label = QLabel(self)
            self.description_label = QLabel(self)
            self.more_label = QLabel(self)
            self.address_label = QLabel(self)

            # About and More buttons
            self.about_button = QPushButton("Learn More/How to use", self)
            self.about_button.clicked.connect(self.show_popup)

            self.more_button = QPushButton("Show more", self)  # Added "More" button
            self.more_button.clicked.connect(self.show_more)  # Connect to function

            self.weather_data = None  # Placeholder for weather data
            self.more_showed = False
            self.initUI()

        def initUI(self):
            self.setWindowTitle("Weather App")

            vbox = QVBoxLayout()
            vbox.addWidget(self.city_label)
            vbox.addWidget(self.city_input)
            vbox.addWidget(self.get_weather_button)

            hbox = QHBoxLayout()
            hbox.addWidget(self.celsius_button)
            hbox.addWidget(self.fahrenheit_button)
            hbox.addWidget(self.kelvin_button)
            
            vbox.addLayout(hbox)
            vbox.addStretch()


            vbox.addWidget(self.temperature_label)
            vbox.addWidget(self.emoji_label)
            vbox.addWidget(self.description_label)
            vbox.addWidget(self.more_label)  # Line to display wind speed
            hbox_wind = QHBoxLayout()
            hbox_wind.addWidget(self.mph_button)
            hbox_wind.addWidget(self.kmh_button)
            vbox.addLayout(hbox_wind)  # Line to add wind unit buttons to layout
            vbox.addWidget(self.address_label)
            vbox.addWidget(self.more_button)
            self.setLayout(vbox)

            self.city_label.setAlignment(Qt.AlignCenter)
            self.city_input.setAlignment(Qt.AlignCenter)
            self.temperature_label.setAlignment(Qt.AlignCenter)
            self.emoji_label.setAlignment(Qt.AlignCenter)
            self.description_label.setAlignment(Qt.AlignCenter)
            self.more_label.setAlignment(Qt.AlignCenter)

            self.address_label.setAlignment(Qt.AlignCenter)
            self.city_label.setObjectName("city_label")
            self.city_input.setObjectName("city_input")
            self.get_weather_button.setObjectName("get_weather_button")
            self.temperature_label.setObjectName("temperature_label")
            self.emoji_label.setObjectName("emoji_label")
            self.description_label.setObjectName("description_label")
            
            self.setStyleSheet("""
                QLabel, QPushButton, QRadioButton {
                    font-family: sans serif;         
                }
                QLabel#city_label {
                    font-size: 40px;
                    font-style: italic;         
                }
                QLineEdit#city_input {
                    font-size 40px:
                }
                QPushButton#get_weather_button {
                    min-height: 50px;
                    font-size: 30px;
                    font-weight: bold;
                }
                QLabel#temperature_label {
                    font-size: 75px;           
                }
                QLabel#emoji_label {
                    font-size: 100px;
                    font-family: Apple Color Emoji;
                }
                QLabel#description_label {
                    font-size: 50px; 
                    
                }  
                QLabel#more_label {
                    font-size: 50px;
                }        
                QLabel#address_label {
                    font-size: 10px;
                }            
            """)

            self.get_weather_button.clicked.connect(self.get_weather)

        def display_error(self, message):
            self.temperature_label.setStyleSheet("font-size: 30px;")
            self.temperature_label.setText(message)
            self.emoji_label.clear()
            self.description_label.clear()

        def show_more(self):
            if not self.more_showed:
                if self.weather_data:
                    data = self.weather_data
                    print(data)

                    more_info = ""
                    feels_like_k = data["main"]["feels_like"]
                    if self.celsius_button.isChecked():
                        feels_like = feels_like_k - 273.15
                        more_info += f"Feels like: {feels_like:.1f} °C"
                    elif self.fahrenheit_button.isChecked():
                        feels_like = (feels_like_k * 9/5) - 459.67
                        more_info += f"Feels like: {feels_like:.0f} °F"
                    elif self.kelvin_button.isChecked():
                        more_info += f"Feels like: {feels_like_k:.0f} K"

                    wind_speed = data["wind"]["speed"]
                    # Wind Speed
                    if self.mph_button.isChecked():
                        wind_speed = wind_speed * 2.23694  # Convert m/s to mph
                        more_info += f"\nWind speed: {wind_speed:.1f} mph"
                    elif self.kmh_button.isChecked():
                        wind_speed = wind_speed * 3.6  # Convert m/s to km/h
                        more_info += f"\nWind speed: {wind_speed:.1f} km/h"
                    else:
                        pass

                    latitude = data["coord"]["lat"]
                    longitude = data["coord"]["lon"]
                    address = get_address_from_coordinates(latitude, longitude)
                    address = f"Address: {address}"
                    
                    self.more_label.setStyleSheet("font-size: 50px;")
                    self.more_label.setText(more_info)
                    self.address_label.setText(address)
                    self.mph_button.show()
                    self.kmh_button.show()

                    ##############################
                    
                else:
                    self.more_label.setStyleSheet("font-size: 25px;")
                    self.more_label.setText("No data available. Fetch weather first.")

                self.more_showed = True
                self.more_button.setText("Hide more")
            else:
                self.more_label.setText("")
                self.mph_button.hide()
                self.kmh_button.hide()
                self.more_showed = False
                self.more_button.setText("Show more")

        def get_weather(self):
            city = self.city_input.text()
            data = self._get_weather(city)
            if data and data["cod"] == 200:
                self.display_weather(data)
                self.weather_data = data
            else:
                self.weather_data = None

        def display_weather(self, data):
            self.temperature_label.setStyleSheet("font-size: 75px;")
            temperature_k = data["main"]["temp"]
            weather_id = data["weather"][0]["id"]
            if self.celsius_button.isChecked():
                temperature = temperature_k - 273.15
                self.temperature_label.setText(f"{temperature:.1f} °C")
            elif self.fahrenheit_button.isChecked():
                temperature = (temperature_k * 9/5) - 459.67
                self.temperature_label.setText(f"{temperature:.0f} °F")
            elif self.kelvin_button.isChecked():
                self.temperature_label.setText(f"{temperature_k:.0f} K")
            weather_description = data["weather"][0]["description"]
            self.emoji_label.setText(self.get_weather_emoji(weather_id))
            self.description_label.setText(weather_description)
        def show_popup(self):
            # Create and show a message box
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("""
                    Weather App    By: Daniel
    1. place Input
    You can type the name of any place in a text
    input box to fetch its weather information.
                        
    2. Unit Selection                    
    This app allows you to view the temperature in Celsius, Fahrenheit, or Kelvin using radio buttons.  
                        
    3. Weather Information
    Displays:
        Temperature in the selected unit.
        Weather Description (e.g., sunny, cloudy, rainy, etc.).
        emoji-based weather icons.
                        
    4. Error Handling    
    Handles common API and connection errors, such as:
        City not found
        Invalid API key
        Server errors
        Internet connectivity issues
        Displays user-friendly error messages for each type of error.
            
    5. Responsive Design   
    The app dynamically adjusts the position of elements like the "About the Website" button based on the size of the window.


    How To Use
    Type in a zip code (e.g 12345), contry(e.g Russia), county(e.g Los angles), city(e.g Unalaska), and ect 
    It will give you the temperature(You can pick between K(Kelvin), F(fahrenheit), or C(celsius) KFC!), rain and ect, and weather emoji.
    If you click Show more it will give you the wind (You can pick between Mph or Km/h), what it feels like, and place(road, city, county, state, zip code, and contry)!                                  
    """)
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        def resizeEvent(self, event):
            super().resizeEvent(event)
            # Dynamically position the button in the top middle of the window
            button_width = self.about_button.width()
            button_height = self.about_button.height()
            button_x = (self.width() - button_width) // 2  # Center horizontally
            button_y = 10  # 10px margin from the top
            self.about_button.move(button_x, button_y)

    app = QApplication(sys.argv)
    weather_app = WeatherAppQt()
    weather_app.show()

    sys.exit(app.exec_())

    if __name__ == "__main__":
        main()
