import pyrdle


def test_invalid_chars():
    assert pyrdle.has_valid_chars("state", "a") == False
    assert pyrdle.has_valid_chars("water", "te") == False
    assert pyrdle.has_valid_chars("state", "") == True
    assert pyrdle.has_valid_chars("state", "y") == True


def test_has_required_chars():
    assert pyrdle.has_required("stare", "re") == True
    assert pyrdle.has_required("stare", "") == True
    assert pyrdle.has_required("stare", "qu") == False
    assert pyrdle.has_required("stare", "ze") == False


def test_is_wrong_pos():
    assert pyrdle.is_wrong_position("..a..", "stare") == True
    assert pyrdle.is_wrong_position(".a...", "stare") == False
    assert pyrdle.is_wrong_position("s...e", "stare") == True
    assert pyrdle.is_wrong_position(".....", "stare") == False
    assert pyrdle.is_wrong_position("arste", "stare") == True
    assert pyrdle.is_wrong_position("arset", "stare") == False
    assert pyrdle.is_wrong_position("..A..", "stare") == False
