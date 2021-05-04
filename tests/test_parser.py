""" 
    this module will test all the Parser's functions with pytest. The Parser
    class contain 5 methods what are executing each after other one with the 
    result of the previous one as paramater. Se execept the first 
    method 'regex', all the other methods will be mocked for test the next 
    method.

    """

from app.parser import Parser
import re
import unicodedata

test = Parser("Hi! I do a test with french word: l'éveil")

def test_unit_regex_method():

    result = test.regex()
    assert result == "Hi  I do a test with french word  l éveil"


def mock_regex():
    
    regexed = re.sub(r'[^\w\s]', ' ', test.message)
    return regexed


def test_unit_lower_letter_method():

    result = test.lower_letter(mock_regex())
    assert result == "hi  i do a test with french word  l éveil"


def mock_lower_letter(regexed):

    message_low = regexed.lower()
    return message_low


def test_unit_remove_accent_method():

    result = test.remove_accent(mock_lower_letter(mock_regex()))
    assert result == "hi  i do a test with french word  l eveil"


def mock_remove_accent(message_low):

    nk = unicodedata.normalize('NFKD', message_low)
    ascii = nk.encode('ASCII', 'ignore')
    strascii = ascii.decode('utf-8')  # convert byte data to string
    return strascii


def test_unit_split_reworked_message_method():
    result = test.split_reworked_message(
        mock_remove_accent(mock_lower_letter(mock_regex())))
    assert result == ['hi', 'i', 'do', 'a', 'test',
                      'with', 'french', 'word', 'l', 'eveil']


def mock_split_reworked_message(strascii):
    list_of_words = strascii.split()
    return list_of_words


def test_unit_check_stopwords_method():
    result = test.check_stopwords(mock_split_reworked_message(
        mock_remove_accent(mock_lower_letter(mock_regex()))))
    assert result == ['do', 'test', 'with', 'french', 'word', 'eveil']

#additional full test 
def test_full_class_parser():

    result = test.cleaned
    assert result == ['do', 'test', 'with', 'french', 'word', 'eveil']
