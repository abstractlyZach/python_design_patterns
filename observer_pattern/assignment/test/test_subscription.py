import pytest

from observer import magazines
from observer import subscribers

def test_single_subscriber():
    magazine_name = 'Example Magazine'
    subscriber = subscribers.Subscriber('Joe Schmoe')
    magazine = magazines.Magazine(magazine_name)
    magazine.attach(subscriber)
    magazine.release_edition('February 2018')
    assert subscriber.magazines_received[magazine_name] == 1

