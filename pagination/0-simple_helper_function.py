#!/usr/bin/env python3
'''function named index-range'''


def index_range(page, page_size):
    """
    Calculate the start and end index of a list slice for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end index for the page range
               (start_index, end_index), where the end index is exclusive.

    Example:
        index_range(1, 10)  # Returns (0, 10)
        index_range(2, 10)  # Returns (10, 20)
        index_range(3, 10)  # Returns (20, 30)
    """
    # Calculate the starting index (0-indexed)
    start_index = (page - 1) * page_size
    # Calculate the ending index (exclusive)
    end_index = start_index + page_size
    return (start_index, end_index)
