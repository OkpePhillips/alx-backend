#!/usr/bin/env python3
'''
A helper function to return start and end index of a range.
'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    Returning a tuple of start and end index of a range of indexes
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
