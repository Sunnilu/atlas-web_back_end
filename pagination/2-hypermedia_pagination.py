#!/usr/bin/env python3
'''Method that takes get_hyper'''


import csv
import math
from typing import List, Dict

# Using index_range is defined in the module 0-simple_helper_function
index_range = __import__('0-simple_helper_function').index_range

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data"""
        # Assert that both page and page_size are positive integers
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        # Get the indices for the requested page
        start, end = index_range(page, page_size)

        # Get the dataset
        dataset = self.dataset()

        # Return the slice of dataset for the page, or an empty list if out of range
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieve a dictionary with pagination information"""
        # Get the page data
        data = self.get_page(page, page_size)

        # Total number of rows in the dataset
        total_rows = len(self.dataset())

        # Calculate the total number of pages
        total_pages = math.ceil(total_rows / page_size)

        # Determine next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return the dictionary with pagination information
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
