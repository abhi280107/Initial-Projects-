import pytest
from Final import add_balance, withdraw, view_balance
def main():
    pass

def create_balance_file(tmp_path, amount=1000):
    file_path = tmp_path / "balance.csv"
    file_path.write_text(f"Balance,{amount}")
    return file_path

def test_add_balance(tmp_path):
    balance_file = create_balance_file(tmp_path, 1000)
    add_balance(500, balance_file)

    contents = balance_file.read_text()
    assert contents == "Balance,1500"

def test_withdraw_balance(tmp_path):
    balance_file = create_balance_file(tmp_path, 1000)
    withdraw(300, balance_file)

    contents = balance_file.read_text()
    assert contents == "Balance,700"

def test_withdraw_insufficient_balance(tmp_path):
    balance_file = create_balance_file(tmp_path, 200)
    with pytest.raises(ValueError):
        withdraw(300, balance_file)
main()