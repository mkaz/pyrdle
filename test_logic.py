import pyrdle


def test_invalid_chars():
    assert pyrdle.has_valid_chars("state", "a") is False
    assert pyrdle.has_valid_chars("water", "te") is False
    assert pyrdle.has_valid_chars("state", "") is True
    assert pyrdle.has_valid_chars("state", "y") is True


def test_has_required_chars():
    assert pyrdle.has_required("stare", "re") is True
    assert pyrdle.has_required("stare", "") is True
    assert pyrdle.has_required("stare", "qu") is False
    assert pyrdle.has_required("stare", "ze") is False


def test_is_wrong_pos():
    # second param is word checking
    assert pyrdle.is_wrong_position("..a..", "stare") is True
    assert pyrdle.is_wrong_position(".a...", "stare") is False
    assert pyrdle.is_wrong_position("s...e", "stare") is True
    assert pyrdle.is_wrong_position("g...e", "stare") is True
    assert pyrdle.is_wrong_position(".....", "stare") is False
    assert pyrdle.is_wrong_position("arste", "stare") is True
    assert pyrdle.is_wrong_position("arset", "stare") is False
    assert pyrdle.is_wrong_position("..A..", "stare") is False


def test_is_right_pos():
    # second param is word checking
    assert pyrdle.is_right_position("..A..", "stare") is True
    assert pyrdle.is_right_position(".a...", "stare") is True
    assert pyrdle.is_right_position("A....", "stare") is False
    assert pyrdle.is_right_position(".T..A", "stare") is False
    assert pyrdle.is_right_position("..AR.", "stare") is True
    assert pyrdle.is_right_position("aSstE", "stare") is False
    assert pyrdle.is_right_position(".....", "stare") is True
    assert pyrdle.is_right_position(".h..E", "heavy") is False
