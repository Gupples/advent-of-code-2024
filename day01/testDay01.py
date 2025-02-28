'''Driver for Day01.py'''
from day01 import *
import pytest

# Create a standard list for testing
def setup_standard_list():
    list = [1, 2, 3, 4, 5]
    return list

# Create a list filled with 0's for testing
def setup_zero_list():
    list = [0, 0, 0, 0, 0]
    return list

def assert_standard_list(list):
    assert list == [1, 2, 3, 4, 5]

def assert_zero_list(list):
    assert list == [0, 0, 0, 0, 0]


'''    -------BEGIN TESTING-------    '''

'''Test read_file'''
# Test against nonexistant file
def test_read_file_nonexistant():
    # SETUP
    file_name = "not_here.txt"
    result = setup_standard_list()

    # EXERCISE
    result = read_file(file_name)

    # VERIFY
    assert file_name == "not_here.txt"
    assert result==[]

    # TEARDOWN

# Test against empty file
def test_read_file_empty():
    # SETUP
    file_name = "day01/test_files/empty.txt"
    result = setup_standard_list()

    # EXERCISE
    result = read_file(file_name)

    # VERIFY
    assert file_name == "day01/test_files/empty.txt"
    assert result==[]

    # TEARDOWN

# Test against the key
def test_read_file_key():
    # SETUP
    file_name = "day01/01Key.txt"
    result = setup_zero_list()

    # EXERCISE
    result = read_file(file_name)

    # VERIFY
    assert file_name == "day01/01Key.txt"
    assert result == ['3   4', '4   3', '2   5', '1   3', '3   9', '3   3']

    # TEARDOWN

# Test against uneven file (left longer)

# Test against uneven file (right longer)


'''Test parse_data'''
# Test an empty string
def test_parse_data_empty():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test one line
def test_parse_data_one_line():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test uneven lines
def test_parse_data_uneven():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# 
#  ...

'''Test get_similarity_score'''
# Test both lists empty
def test_get_similarity_score_both_empty():
    # SETUP
    list1 = []
    list2 = []
    result = 99

    # EXERCISE
    result = get_similarity_score(list1, list2)

    # VERIFY
    assert list1 == []
    assert list2 == []
    assert result == 0      # 0 * 0 = 0

    # TEARDOWN

# Test left list empty
def test_get_similarity_score_left_empty():
    # SETUP
    list1 = []
    list2 = setup_standard_list()
    result = 99

    # EXERCISE
    result = get_similarity_score(list1, list2)

    # VERIFY
    assert list1 == []
    assert_standard_list(list2)
    assert result == 0      # 0 * 0 = 0

    # TEARDOWN


# Test right list empty
def test_get_similarity_score_right_empty():
    # SETUP
    list1 = setup_standard_list()
    list2 = []
    result = 99

    # EXERCISE
    result = get_similarity_score(list1, list2)

    # VERIFY
    assert_standard_list(list1)
    assert list2 == []
    assert result == 0      # 0 * 0 = 0

    # TEARDOWN

# Test one small item one occurance
def test_get_similarity_score_one_to_one():
    # SETUP
    list1 = [1]
    list2 = setup_standard_list()
    result = 99

    # EXERCISE
    result = get_similarity_score(list1, list2)

    # VERIFY
    assert list1 == [1]
    assert_standard_list(list2)
    assert result == 1      # 1 * 1 = 1

    # TEARDOWN

# Test one small item many occurances
def test_get_similarity_score_one_to_many():
    # SETUP
    list1 = [1]
    list2 = [1, 1, 1, 1, 1]
    result = 99

    # EXERCISE
    result = get_similarity_score(list1, list2)

    # VERIFY
    assert list1 == [1]
    assert list2 == [1, 1, 1, 1, 1]
    assert result == 5      # 1 * 5 = 5

# Test many small items one occurance each
def test_get_similarity_score_many_to_one():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test many small items many occurances each 
def test_get_similarity_score_many_to_many():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

'''Test get_total_difference'''
# Test empty strings
def test_get_total_difference_empty():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test left string longer
def test_get_total_difference_left_longer():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return
# Test right string longer
def test_get_total_difference_right_longer():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test one element same value 
def test_get_total_difference_one_value():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test one element left larger value by a little
def test_get_total_difference_short_left_little_difference():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test one element left larger value by a lot
def test_get_total_difference_short_left_large_difference():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test one element right larger value by a little
def test_get_total_difference_short_right_little_difference():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return

# Test one element right larger value by a lot
def test_get_total_difference_short_right_large_difference():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return
#  

pytest.main(["-v", "--tb=line", "-rN", __file__])