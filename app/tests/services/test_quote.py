import pytest

from app.services.quote import QuoteService


@pytest.fixture
def service() -> QuoteService:
    """
    It creates a new QuoteService object, loads the quotes from the file, and returns the object
    :return: A QuoteService object
    """
    s = QuoteService()
    s.load()
    return s


def test_quotes(service: QuoteService):
    """
    It asserts that the length of the quotes is greater than zero
    
    :param service: QuoteService - this is the service we want to test
    :type service: QuoteService
    """
    assert len(service.quotes), "Quotes are not provided."


def test_get_quote(service: QuoteService):
    """
    It tests that the quote returned by the service is in the list of quotes
    
    :param service: QuoteService - this is the fixture that we defined above
    :type service: QuoteService
    """
    quote = service.get_quote()

    assert quote in service.quotes
