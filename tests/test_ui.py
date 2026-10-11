import pytest
from ass1.ui import Decoder

@pytest.fixture
def decoder():
    return Decoder()

def test_decoder_instantiates(decoder):
    assert isinstance(decoder, Decoder)

def test_decoder_handles_push_pop_with_reals(decoder):
    decoder.decode("push 1")
    n = decoder.decode("pop")
    assert n == 1

    decoder.decode("push -1")
    n = decoder.decode("pop")
    assert n == -1

    decoder.decode("push - 1")
    n = decoder.decode("pop")
    assert n == -1
