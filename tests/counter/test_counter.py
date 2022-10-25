from src.counter import count_ocurrences


def test_counter():
    result_l = count_ocurrences('src/jobs.csv', 'test')
    result_u = count_ocurrences('src/jobs.csv', 'TEST')
    assert result_l == 2687
    assert result_u == 2687
