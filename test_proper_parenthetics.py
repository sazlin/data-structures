from proper_parenthetics import check_parens


def test_check_parens_open1():
    assert check_parens(u'(((text))') == 1


def test_check_parens_open2():
    assert check_parens(u'((((((text') == 1


def test_check_parens_open3():
    assert check_parens(u'(') == 1


def test_check_parens_balanced1():
    assert check_parens(u'') == 0


def test_check_parens_balanced2():
    assert check_parens(u'(text)') == 0


def test_check_parens_balanced3():
    assert check_parens(u'(text(text(text())))') == 0


def test_check_parens_balanced4():
    assert check_parens(u'()') == 0


def test_check_parens_broken1():
    assert check_parens(u')') == -1


def test_check_parens_broken2():
    assert check_parens(u'(text))') == -1


def test_check_parens_broken3():
    assert check_parens(u'(text(text(text(text)text)text)text)text)') == -1


def test_check_parens_invalid1():
    assert check_parens(u')(') == -1


def test_check_parens_invalid2():
    assert check_parens(u'(dog(cat)),(foo(bar(baz)bar)foo))') == -1
