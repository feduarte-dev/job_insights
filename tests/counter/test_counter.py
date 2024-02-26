from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "Design") == 3584
    assert count_ocurrences("data/jobs.csv", "design") == 3584
