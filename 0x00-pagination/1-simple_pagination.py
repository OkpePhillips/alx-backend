#!/usr/bin/env python3
'''
A helper function to return start and end index of a range.
'''
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''
    Returning a tuple of start and end index of a range of indexes
    '''
    if not isinstance(page, int) or not isinstance(page_size, int) \
            or page < 1 or page_size < 1:
        raise ValueError("0Value cannot be less than 1")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns the requested page if exists """
        try:
            start, end = index_range(page, page_size)
        except ValueError:
            return []
        dataset = self.dataset()
        if start >= len(dataset):
            return []
        return dataset[start:end]
