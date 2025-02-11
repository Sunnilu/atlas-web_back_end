#!/usr/bin/env python3
'''method named get_page that takes two integer arguments'''


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two containing the start and end index
    corresponding to the requested page and page size."""
    assert isinstance(page, int) and page > 0, "Page must be positive integer"
    assert isinstance(page_size, int) and page_size > 0, "Page size pos int"

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
            self.__dataset = dataset[1:]  # Exclude the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page from the dataset."""
        assert isinstance(page, int) and page > 0, "Page must positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page pos int"

        dataset = self.dataset()  # Get the full dataset
        start, end = index_range(page, page_size)  # range using index_range

        if start >= len(dataset):
            return []  # return an empty list

        return dataset[start:end]  # Return data within the calculated range
