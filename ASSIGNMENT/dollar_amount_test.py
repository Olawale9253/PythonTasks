def test_usd_to_naira():
  
    assert usd_to_naira(1) == 1550.00
    assert usd_to_naira(2.5) == 3875.00

    assert usd_to_naira(0.333) == 516.15

    assert usd_to_naira(0) == 0.00

    try:
        usd_to_naira(-5)
        assert False  
    except ValueError:
        assert True

    try:
        usd_to_naira("abc")
        assert False
    except ValueError:
        assert True
