import pytest

from handle_page import get_continual_page
from deque_con_page import deal_con_page_deque

continual_page_data = [([2, 4, 5, 8], [[2, 2], [4, 5], [8, 8]]),
                       ([1, 4, 5, 6, 8], [[1, 1], [4, 6], [8, 8]]),
                       ([1, 2, 3, 4], [[1, 4]]),
                       ([1, 3, 4], [[1, 1], [3, 4]])
                       ]


@pytest.mark.skip(reason='doesnt need to test it')
@pytest.mark.parametrize('input_con, output_con', continual_page_data)
def test_continual_page(input_con, output_con):
    input_result = get_continual_page(input_con)
    assert input_result == output_con


@pytest.mark.parametrize('input_con, output_con', continual_page_data)
def test_continual_page_queue(input_con, output_con):
    input_result = deal_con_page_deque(input_con)
    assert input_result == output_con
