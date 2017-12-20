import fetch


def test_fetchHeader():
    header = fetch('h1')
    assert header == '天天基金网'
