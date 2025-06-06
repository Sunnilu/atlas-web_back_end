#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List[Any]]:
        """Cached dataset.

        Returns:
            List[List[Any]]: The dataset loaded from CSV excluding header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[Any]]:
        """Dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List[Any]]: Indexed dataset up to 1000 entries.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: row for i, row in enumerate(dataset[:1000])
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Return a page of the dataset with deletion-resilience.

        Args:
            index (int, optional): Starting index. Defaults to 0.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: Dictionary with page data and metadata.
        """
        assert isinstance(index, int) and index >= 0, "Index must be a non-negative integer"

        indexed_data = self.indexed_dataset()
        dataset_size = len(indexed_data)
        assert index < dataset_size, "Index out of range"

        data = []
        current_index = index

        while len(data) < page_size and current_index < dataset_size:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data
        }
