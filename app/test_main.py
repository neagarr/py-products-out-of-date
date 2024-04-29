import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture
def product_list() -> list:
    products = [
        {
            "name": "salmon",
            "expiration_date": "2022-02-10",
        },
        {
            "name": "chicken",
            "expiration_date": "2022-02-05",
        },
        {
            "name": "duck",
            "expiration_date": "2022-02-01",
        }
    ]
    return products


@pytest.mark.parametrize(
    "today_date,result",
    [
        ("2022-02-11", ["salmon", "chicken", "duck"]),
        ("2022-02-01", []),
        ("2022-02-05", ["duck"])
    ],
    ids=[
        "today date > expiration date",
        "today date = expiration date of 'oldest' product",
        "today date = expiration date of 'middle' product"
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mocked_date: mock,
        product_list: list,
        today_date: str,
        result: list
) -> None:
    mocked_date.today.return_value = today_date

    assert outdated_products(product_list) == result
