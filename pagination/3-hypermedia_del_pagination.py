#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary containing a page of data, the current index, next index, and page size."""
        # Verify that index and page_size are valid
        assert isinstance(index, int) and index >= 0, "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        # Get the indexed dataset
        indexed_dataset = self.indexed_dataset()

        # Initialize a list to hold the data for the requested page
        data = []
        current_index = index

        # Retrieve the required page of data, even if rows were deleted
        while len(data) < page_size:
            # If the current index exists in the indexed dataset, add it to the data list
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            # Skip the current index if it's missing (deleted)
            current_index += 1

        # Calculate the next index, which is the first item after the last item on the current page
        next_index = current_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
