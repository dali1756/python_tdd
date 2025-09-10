# 基本語法
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

# 常用方法
def test_equal():
    assert 1 == 1
    assert "小明" == "小明"
    assert 1 != 2
    assert "小明" != "小華"

def test_check_null_and_undefined():
    is_null = None
    is_undefined = None
    is_defined = "exists"
    assert is_null is None
    assert is_undefined is None
    assert is_defined is not None

def test_check_data_type():
    assert isinstance(10, int)
    assert isinstance("小明", str)
    assert isinstance(3.14, float)
    assert isinstance([], list)
    assert isinstance({}, dict)