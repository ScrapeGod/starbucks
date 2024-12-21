# Starbucks

## Project Overview
This project is a Python-based application that scrapes data from Starbucks.

## Features
- Data scraping using requests.
- Provides functionalities to fetch menu details and store information.

## Functionality

### `starbucks/__init__.py`
- Sets the base URL for the Starbucks API.

### `starbucks/menu.py`
- `get_all_menu()`: Fetches the full Starbucks menu and removes unnecessary keys.
- `get_product_details(product_number, store_number=None)`: Retrieves details of a specific product using its product number.

### `starbucks/stores.py`
- `get_stores(lat=None, lng=None, place=None)`: Gets a list of Starbucks stores based on latitude, longitude, or place name.
- `get_store_by_number(store_number)`: Retrieves information about a specific Starbucks store by its store number.

### `starbucks/utils.py`
- `remove_keys_recursively(data, keys_to_remove)`: Removes specified keys from a nested dictionary or list of dictionaries.
- `search_for_key_value_recursively(data, key, value)`: Searches for a key-value pair in a nested structure.
- `get_product_uri_from_product_number(product_number)`: Gets the URI of a specific product using its product number by searching in a JSON file.

## Installation
To install the required dependencies, run:
```sh
pip install -r requirements.txt
```

## Usage
To use the application, install it:
```sh
pip install git@github.com:ScrapeGod/starbucks.git
```

## Configuration
Ensure to configure your environment variables in the `.env` file.

## License