import pytest

from handle_page import get_continual_page

continual_page_data = [([2, 4, 5, 8], [[2, 2], [4, 5], [8, 8]]),
                       ([1, 4, 5, 6, 8], [[1, 1], [4, 6], [8, 8]]),
                       ([1, 2, 3, 4], [[1, 4]]),
                       ([1, 3, 4], [[1, 1], [3, 4]])
                       ]


@pytest.mark.parametrize('input_con, output_con', continual_page_data)
def test_continual_page(input_con, output_con):
    input_result = get_continual_page(input_con)
    assert input_result == output_con
