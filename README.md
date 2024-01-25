# Web Scraping Project: Extracting Restaurant Data from Dineout (Chennai)
# Hotel Dineout Scraper

This web scraping project is designed to extract restaurant data from the Dineout website (https://www.dineout.co.in/chennai-restaurants) for restaurants located in Chennai. The script navigates through all 35 pages of the website, capturing essential information (Name, Address, Price for 2 people per day and Rating) about each restaurant / hotel and storing it in a CSV file.

## Table of Contents

- [Overview](#overview)
- [Project Workflow](#project-workflow)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


## Overview

The project consists of a Python script (`scraper.py`) that uses web scraping techniques to extract information from the Dineout website. The extracted data includes hotel names, addresses, ratings, and prices. The script saves the data in both Excel (`XL_Hotel_Dineout_Scrap.xlsx`) and CSV (`CSV_Hotel_Dineout_Scrap.csv`) formats.

## Project Workflow
### 1. Requesting Web Pages:
  The script uses the requests module to send HTTP requests to the Dineout website, simulating the process of visiting each page.
### 2. Parsing HTML Content:
  BeautifulSoup is employed to parse the HTML content retrieved from each web page.
  Allows the script to navigate through the HTML structure and locate the relevant data.
### 3. Extracting Restaurant Data:
  The script identifies and extracts key information about each restaurant, such as name, address, rating, etc., from the parsed HTML.
### 4. Writing to CSV File:
  The extracted data is then written to a CSV file using the csv module.
  Each restaurant's information is stored as a separate row in the CSV file.

## Getting Started

## Prerequisites

Make sure you have the following prerequisites installed on your system:

- ### BeautifulSoup (bs4):
BeautifulSoup is a powerful Python library for pulling data out of HTML and XML files.
Utilized for parsing the HTML content of the Dineout website, making it easy to extract relevant information such as restaurant names, addresses, ratings, and more.

- ### Requests:
The Requests module is employed to send HTTP requests to the Dineout website and retrieve the HTML content.
Essential for accessing and fetching the web pages that contain the desired restaurant data.

- ### CSV:
The CSV module is used for handling CSV files.
Allows the script to create and write data to a CSV file, providing a structured format for storing the extracted restaurant information.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/hotel-dineout-scraper.git
```
   
2. Navigate to the project directory:

``` bash
cd hotel-dineout-scraper
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt 
```

## Usage
Make a local copy of the repository on your computer.
``` bash
pip install requests beautifulsoup4
```
Use this command to install the necessary modules.
- Open the script in the Python environment of your choice.
- Run the script using the following command:
``` bash
python scraper.py
```
The script will scrape data from the Dineout website and save it in Excel and CSV formats.
