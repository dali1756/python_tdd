### 筆記
https://hackmd.io/@JeterYu/HyZJWLacel

### 建立虛擬環境
```bash
uv init --no-workspace
uv venv --python=3.12
source .venv/bin/activate
```
### 安裝所需套件
```bash
uv pip install -r requirements.txt
```

### 資料結構
```
python_tdd
├─ README.md
├─ main.py
├─ pyproject.toml
├─ pytest.ini
├─ requirements.txt
├─ src
│  ├─ __init__.py
│  ├─ calculator.py
│  ├─ math_utils.py
│  └─ validator.py
├─ tests
│  ├─ __init__.py
│  ├─ test_basic_assert.py
│  ├─ test_calculator.py
│  ├─ test_calculator_structured.py
│  ├─ test_math_utils.py
│  ├─ test_number_assert.py
│  ├─ test_string_assert.py
│  ├─ test_validator.py
│  └─ 安裝必要套件.ini
└─ uv.lock

```