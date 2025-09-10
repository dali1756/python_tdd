def test_equal():
    result = 1 + 1
    assert result == 2

def test_check_equal():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    # 檢查值是否相等
    assert a == b
    # 檢查是否為同一個物件
    assert a is c