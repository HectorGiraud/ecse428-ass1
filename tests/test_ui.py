import pytest
from ass1.ui import Decoder

@pytest.fixture
def decoder():
    return Decoder()

def test_decoder_instantiates(decoder):
    assert isinstance(decoder, Decoder)