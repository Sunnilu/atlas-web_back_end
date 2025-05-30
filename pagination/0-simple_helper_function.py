#!/usr/bin/env python3
"""Helper function for pagination index calculation.

This module provides a utility function `index_range`
used to determine the start and end index for paginated data.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return the start and end index for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
