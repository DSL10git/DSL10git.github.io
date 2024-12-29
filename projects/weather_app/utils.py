import requests
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


if __name__ == "__main__":
    # Example usage
    latitude = 28.5364
    longitude = -81.0176
    address = get_address_from_coordinates(latitude, longitude)
    print(f"Address: {address}")