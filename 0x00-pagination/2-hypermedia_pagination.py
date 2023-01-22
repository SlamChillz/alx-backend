import csv
import math
from typing import Dict, List, Tuple, Union


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

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Calculate start and end index range for a `page`, with `page_size`
        """
        nextPageStartIndex = page * page_size
        return nextPageStartIndex - page_size, nextPageStartIndex

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items for the given page number
        Args:
            page (int): page number
            page_size (int): number of items per page
        Returns:
            (List[List]): a list of list(row) if inputs are within range
            ([]) : an empty list if page and page_size are out of range
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]

    def get_hyper(self, page: int, page_size: int) -> Dict[str, Union[int, List[List], None]]:
        """
        Args:
            page (int): page number
            page_size (int): number of items per page
        Returns:
            A dictionary of the following:
                * page_size, page, data, next_page, prev_page, total_pages
        """
        data = self.get_page(page, page_size)
        totalRows = len(self.dataset())
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1
        if self.index_range(page, page_size)[1] >= totalRows:
            next_page = None
        total_pages = totalRows / page_size
        if total_pages % 1 != 0:
            total_pages += 1
        return {'page_size': len(data), 'page': page,
                'data': data, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': int(total_pages)}
