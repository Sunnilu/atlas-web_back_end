def index_range(page: int, page_size: int) -> tuple:
   #!/usr/bin/env python3
    """
    Calculate start and end index for pagination.

    Parameters:
    page (int): The current page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
