from src import cli


def test_always_passes():
    cli.main()
    assert True
