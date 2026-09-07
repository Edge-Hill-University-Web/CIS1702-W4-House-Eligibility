from gryffindor_eligibility import check_gryffindor_eligibility


def test_bravery_and_loyalty_qualifies():
    assert check_gryffindor_eligibility(8, 6, 2) == "Gryffindor material!"


def test_bravery_and_ambition_qualifies():
    assert check_gryffindor_eligibility(9, 2, 6) == "Gryffindor material!"


def test_bravery_alone_is_not_enough():
    assert check_gryffindor_eligibility(8, 2, 2) == "Not Gryffindor material."


def test_loyalty_alone_is_not_enough():
    assert check_gryffindor_eligibility(5, 8, 2) == "Not Gryffindor material."


def test_ambition_alone_is_not_enough():
    assert check_gryffindor_eligibility(4, 2, 9) == "Not Gryffindor material."


def test_boundary_bravery_seven_loyalty_five_qualifies():
    assert check_gryffindor_eligibility(7, 5, 0) == "Gryffindor material!"


def test_boundary_bravery_six_fails_even_with_high_others():
    assert check_gryffindor_eligibility(6, 10, 10) == "Not Gryffindor material."


def test_both_loyalty_and_ambition_high_qualifies():
    assert check_gryffindor_eligibility(7, 9, 9) == "Gryffindor material!"


def test_maximum_scores_qualify():
    assert check_gryffindor_eligibility(10, 10, 10) == "Gryffindor material!"


def test_high_bravery_with_low_others_does_not_qualify():
    assert check_gryffindor_eligibility(10, 0, 0) == "Not Gryffindor material."


def test_score_above_ten_is_invalid():
    assert check_gryffindor_eligibility(11, 5, 5) == "Invalid score"


def test_negative_score_is_invalid():
    assert check_gryffindor_eligibility(7, -1, 5) == "Invalid score"
