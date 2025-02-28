'''Driver for Day01.py'''
from day01 import *
import pytest

# Create a standard list for testing
def setup_standard_list():
    list = [1, 2, 3, 4, 5]
    return list

# Create a list filled with 0's for testing
def setup_empty_list():
    list = [0, 0, 0, 0, 0]
    return list


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
    result = setup_empty_list()

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

# 
# 
# 
# 
#  

def test_parse_data_uneven():
    # SETUP
    # EXERCISE
    # VERIFY
    # TEARDOWN
    return
#
# 
# 
# 
#  ...

'''Test get_similarity_score'''
# Test empty strings
# 
#  ...

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