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

def test_decoder_handles_push_pop_with_complex_and_weird_inputs(decoder):
    decoder.decode("push 2+3j")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push 2 + 3j")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push 2+ 3 j")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push 3 j+2")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push -3 j+2")
    n = decoder.decode("pop")
    assert n == 2-3j

    decoder.decode("push --3 j+2")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push - - 3 j+2")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push -3 j")
    n = decoder.decode("pop")
    assert n == -3j

    decoder.decode("push -+3 j")
    n = decoder.decode("pop")
    assert n == -3j

    decoder.decode("push - + - 3 j")
    n = decoder.decode("pop")
    assert n == +3j

    decoder.decode("push - - + - +-3j +- + - 4")
    n = decoder.decode("pop")
    assert n == 4+3j

    decoder.decode("push 2+j3")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push 2 + j3")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push 2+ j 3")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push j 3 +2")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push -j 3+2")
    n = decoder.decode("pop")
    assert n == 2-3j

    decoder.decode("push --j 3+2")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push - - j 3+2")
    n = decoder.decode("pop")
    assert n == 2+3j

    decoder.decode("push -j 3")
    n = decoder.decode("pop")
    assert n == -3j

    decoder.decode("push -+j 3")
    n = decoder.decode("pop")
    assert n == -3j

    decoder.decode("push - + - j 3")
    n = decoder.decode("pop")
    assert n == +3j

    decoder.decode("push - - + - +-j3 +- + - 4")
    n = decoder.decode("pop")
    assert n == 4+3j

    decoder.decode("push - - -1")
    n = decoder.decode("pop")
    assert n == -1

    decoder.decode("push - -1")
    n = decoder.decode("pop")
    assert n == 1

    decoder.decode("push + + + +1")
    n = decoder.decode("pop")
    assert n == 1

def test_decoder_handles_decimal(decoder):
    decoder.decode("push 1.4")
    n = decoder.decode("pop")
    assert n == pytest.approx(1.4)

    decoder.decode("push -1.4")
    n = decoder.decode("pop")
    assert n == pytest.approx(-1.4)

    decoder.decode("push -1.0")
    n = decoder.decode("pop")
    assert n == pytest.approx(-1.0)

    decoder.decode("push -j1.4 + 3.2")
    n = decoder.decode("pop")
    assert n == pytest.approx(3.2-1.4j)

def test_decoder_rejects_bad_number_inputs(decoder):
    with pytest.raises(SyntaxError):
        decoder.decode("push 3 4")
    with pytest.raises(SyntaxError):
        decoder.decode("push 3.")
    with pytest.raises(SyntaxError):
        decoder.decode("push .")
    with pytest.raises(SyntaxError):
        decoder.decode("push .2")
    with pytest.raises(SyntaxError):
        decoder.decode("push 3 .")
    with pytest.raises(SyntaxError):
        decoder.decode("push . 2")
    with pytest.raises(SyntaxError):
        decoder.decode("push 34 456 678")
    with pytest.raises(SyntaxError):
        decoder.decode("push 4j 3")
    with pytest.raises(SyntaxError):
        decoder.decode("push j4 3")
    with pytest.raises(SyntaxError):
        decoder.decode("push 4j3")
    with pytest.raises(SyntaxError):
        decoder.decode("push 4.5.6")
    with pytest.raises(SyntaxError):
        decoder.decode("push 0.+3")

def test_decoder_handles_sequence_of_inputs(decoder):
    decoder.decode("push 1.4 push 1.3")
    n = decoder.decode("pop")
    assert n == pytest.approx(1.3)
    n = decoder.decode("pop")
    assert n == pytest.approx(1.4)

    n = decoder.decode("push 1 push 4 push 3 + 3j-3 push 2 push 5 pop")
    assert n == 5
    n = decoder.decode("push 3.4 pop")
    assert n == pytest.approx(3.4)
    n = decoder.decode("pop")
    assert n == 2
    n = decoder.decode("pop")
    assert n == 3j
    n = decoder.decode("pop")
    assert n == 4
    n = decoder.decode("pop")
    assert n == 1
    with pytest.raises(IndexError):
        decoder.decode("pop")
    

    with pytest.raises(SyntaxError):
        decoder.decode("push 1.4 pop pop")

    with pytest.raises(SyntaxError):
        decoder.decode("push 1 pop push 3")

def test_decoder_handles_all_right_inputs_and_wrong_inputs(decoder):
    n = decoder.decode("push 1.4 push 4 mul push 2 add pop")
    assert n == pytest.approx(7.6)
    n = decoder.decode("push 3+4---5j push 6 sub push 2 mul push 2 div pop")
    assert n == pytest.approx(1-5j)

    with pytest.raises(IndexError):
        decoder.decode("add")
    with pytest.raises(IndexError):
        decoder.decode("push 1 add")

    with pytest.raises(IndexError):
        decoder.decode("sub")
    with pytest.raises(IndexError):
        decoder.decode("push 1 sub")

    with pytest.raises(IndexError):
        decoder.decode("mul")
    with pytest.raises(IndexError):
        decoder.decode("push 1 mul")

    with pytest.raises(IndexError):
        decoder.decode("div")
    with pytest.raises(IndexError):
        decoder.decode("push 1 div")


    with pytest.raises(SyntaxError):
        decoder.decode("a")
    with pytest.raises(SyntaxError):
        decoder.decode("a push 1.3")
    with pytest.raises(SyntaxError):
        decoder.decode("push 1.3 a")
    with pytest.raises(SyntaxError):
        decoder.decode("push 1 push 2 push 3 push 4 subadd")
    with pytest.raises(SyntaxError):
        decoder.decode("push 3j+1pop")
    with pytest.raises(SyntaxError):
        decoder.decode("push3j+1 pop")
    with pytest.raises(SyntaxError):
        decoder.decode("push 1 .pop")
            
        
        