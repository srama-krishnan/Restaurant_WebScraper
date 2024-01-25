import requests
import pandas as pd
from bs4 import BeautifulSoup

def count_caps_and_digits(s):
    """
    Count the number of uppercase letters and digits in a string.
    Args: - s (str): Input string.
    Returns: - bool: True if the count is greater than or equal to 2 and the length is at least 4, False otherwise.
    """
    ct = 0
    for i in s:
        if i.isupper() or i.isdigit():
            ct += 1
    return ct >= 2 and len(s) >= 4

def extract_name(data):
    """
    Extract the hotel name from the data.
    Args:- data (list): List containing data for a restaurant.
    Returns: - str: Extracted hotel name.
    """
    namels = data[0].split(' ')
    hotel = ""
    temp = " "
    for part in namels:
        if count_caps_and_digits(part): 
            temp = part
            break
        else:
            hotel += part + " "

    count_upper = 0
    for char in temp:
        if char.isupper() or char.isdigit():
            count_upper += 1
        if count_upper == 2:
            break
        hotel += char
    return hotel.strip()

def extract_address(data):
    """
    Extract the address from the data.
    Args: - data (list): List containing data for a restaurant.
    Returns: - str: Extracted address.
    """
    addrls = data[0].split(' ')
    address = ""
    flag = False
    temp = " "
    for part in addrls:
        if flag:
            address += part + " "
        if count_caps_and_digits(part) and not flag:
            temp = part
            flag = True

    ct = 0
    temp_digits = ""
    for i in temp:
        if i.isupper() or i.isdigit():
            ct += 1
            temp_digits += i
        if ct == 2:
            break

    full_address = temp_digits + " " + address
    final_address = ""
    for ch in full_address:
        if ch != "₹":
            final_address += ch
        else:
            break
    return final_address.strip()

def extract_ratings(data):
    """
    Extract ratings from the data.
    Args: - data (list): List containing data for a restaurant.
    Returns: - str: Extracted rating or 'Not available'.
    """
    rating_value = data[1]
    if rating_value != 'Not available':
        return float(rating_value)
    else:
        return 0.0

def extract_prices(data):
    """
    Extract prices from the data.
    Args: - data (list): List containing data for a restaurant.
    Returns: - str: Extracted price.
    """
    rupee_list = ""
    rupee_flag = False
    for ch in data[0]:
        if rupee_flag:
            if ch.isdigit() or ch == "," or ch == " ":
                rupee_list += ch
            else:
                break
        if ch == "₹":
            rupee_flag = True
    
    rupees = ""
    for i in rupee_list:
        if i != ',' and i != " ":
            rupees += i
    return rupees

def scrape_dineout_data(base_url, total_pages):
    """
    Scrape data from Dineout website and return a list of lists.
    Args:
        - base_url (str): Base URL of the website.
        - total_pages (int): Total number of pages to scrape.
    Returns: - list: List of lists containing scraped data.
    """
    data = []
    for page_num in range(1, total_pages + 1):
        url = f"{base_url}{page_num}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            print(f"Success! Scraping data from page {page_num}")
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for the specific HTML tags that contain the restaurant info
            restaurants = soup.find_all('div', class_='restnt-main-wrap clearfix')

            for restaurant in restaurants:
                # Extract the restaurant's name
                name = restaurant.find('div', class_='restnt-detail-wrap').text 

                for rating_class in range(6):
                    rating_div = restaurant.find('div', class_=f'restnt-rating rating-{rating_class}')
                    if rating_div:
                        rating = rating_div.text.strip()
                        break  
                    else:
                        # If the rating div is not found, set rating to 'Not available'
                        rating = 'Not available'
                name = name[12:]
                data.append([name, rating])

        except requests.exceptions.HTTPError as errh:
            # The code inside the 'except' block is executed if an HTTPError occurs
            print(f"HTTP Error: {errh} for page {page_num}")
    return data

# Base URL for Dineout 
base_url = "https://www.dineout.co.in/chennai-restaurants/welcome-back?p="
Pages = 35

# Scrape data from Dineout
scraped_data = scrape_dineout_data(base_url, Pages)

# Extract data using defined functions
hotellist = []
addresses = []
ratings = []
prices = []

for item in scraped_data:
    hotellist.append(extract_name(item))
    addresses.append(extract_address(item))
    ratings.append(extract_ratings(item))
    prices.append(extract_prices(item))

# Create DataFrame
df = pd.DataFrame({
    'Hotel Name': hotellist,
    'Address': addresses,
    'Rating (5)': ratings,
    'Price (2)': prices
}, index=range(1, len(hotellist) + 1))

# Save the DataFrame to an Excel file
df.to_excel('XL_Hotel_Dineout_Scrap.xlsx', index=True)
df.to_csv('All_Restaurant_Details.csv', index=True)
high_rated_hotels = df[df['Rating (5)'] >= 4]
high_rated_hotels.reset_index(drop=True, inplace=True)

# Save the filtered DataFrame to a new CSV file
high_rated_hotels.to_csv('Best_Restaurants_of_Chennai.csv', index=True)
