#!/usr/bin/env python3
"""Module to paginate a database of popular baby names with hypermedia support."""

import csv
import math
from typing import List, Tuple, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end indices for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices for items
               on the given page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.

    Provides both simple pagination and hypermedia-style pagination.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with dataset set to None."""
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Load and cache the dataset.

        Returns:
            List[List[str]]: The cached dataset as a list of lists,
                             excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Get a specific page from the dataset.

        Args:
            page (int, optional): Page number. Defaults to 1.
            page_size (int, optional): Items per page. Defaults to 10.

        Returns:
            List[List[str]]: Rows corresponding to the requested page.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert isinstance(page, int) and page > 0, (
            "page must be an integer greater than 0"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be an integer greater than 0"
        )

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(
        self,
        page: int = 1,
        page_size: int = 10
    ) -> Dict[str, Optional[int]]:
        """Provide pagination details in a dictionary (hypermedia format).

        Args:
            page (int, optional): Page number. Defaults to 1.
            page_size (int, optional): Items per page. Defaults to 10.

        Returns:
            dict: A dictionary with pagination details, including:
                  - page_size: number of items returned
                  - page: current page number
                  - data: dataset page
                  - next_page: next page number or None
                  - prev_page: previous page number or None
                  - total_pages: total number of pages
        """
        dataset_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
