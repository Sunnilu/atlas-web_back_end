#!/usr/bin/env python3
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indices for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index for the items
               to display on the given page.

    Examples:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(2, 5)
        (5, 10)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the correct page of the dataset.

        Args:
            page (int): Page number (default is 1).
            page_size (int): Number of items per page (default is 10).

        Returns:
            List[List]: List of rows corresponding to the requested page.

        Raises:
            AssertionError: If page or page_size is not greater than 0.
        """
        assert isinstance(page, int) and page > 0, "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be an integer greater than 0"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
