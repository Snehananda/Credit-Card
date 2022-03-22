from fcntl import F_SETFL
import pytest
from CreditCard import CreditCardValidator


def test_card_num():
  
    #Test case for Validating Card number
    assert CreditCardValidator().validate_card_num("4263982640269299")==True
    assert CreditCardValidator().validate_card_num("4917484589197107")==False

    #Test case for Validating Card Holder Name
    assert CreditCardValidator().validate_card_holder_name("John Wick1")==False
    assert CreditCardValidator().validate_card_holder_name(" Darshan")==False
    assert CreditCardValidator().validate_card_holder_name(" Gagan ")==False
    assert CreditCardValidator().validate_card_holder_name("Rashmi R")==True

    #Test case for Validating Card Validity
    assert CreditCardValidator().validate_card_validity("01/22")==False
    assert CreditCardValidator().validate_card_validity("03/22")==True
    assert CreditCardValidator().validate_card_validity("11/26")==True

    #Test case for Validating Card CVV
    assert CreditCardValidator().validate_card_cvv("12367")==False
    assert CreditCardValidator().validate_card_cvv("645#")==False
    assert CreditCardValidator().validate_card_cvv("756")==True
    assert CreditCardValidator().validate_card_cvv("0896")==True