from terminal import Terminal
import pytest
import logging

@pytest.fixture
def candidates():
    terminal = Terminal(["conducting", "challenger", "approaches", "conclusion", "hyperlight", "activities", "vanquished", "remainders", "resistance"])
    
    return terminal.candidates

@pytest.fixture
def two_candidates():
    terminal = Terminal(["conducting", "conclusion"])
    
    return terminal


def test_words_length(candidates):
    try:
        for word in candidates:
          assert(len(word) == len(candidates[0]))

    except AssertionError as e:
        logging.error(f"The words are not the same length. Check '{word}'")


def test_total_matches(two_candidates):
    
    #Check data type of result
    assert type(two_candidates.total_matches(two_candidates.candidates[0], two_candidates.candidates[1])) == int

    #Check that it returns 4 based on the inputs
    assert two_candidates.total_matches(two_candidates.candidates[0], two_candidates.candidates[1]) == 4


def test_check_candidate_matches(candidates):
    pass

    

    

        


