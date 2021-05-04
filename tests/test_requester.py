from app.requester import Request
from app.config import config as c

test1 = Request("mulhouse")
test2 = Request("nicolas cage")
# test3 = Request("")
# test4 = Request("eugnegnegneugneuuu")


def test_unit_1_first_request_wiki_method():
    result = test1.first_request_wiki()
    assert result == {'batchcomplete': '', 'continue': {'sroffset': 1, 'continue': '-||'}, 'query': {'searchinfo': {'totalhits': 8991}, 'search': [
        {'ns': 0, 'title': 'Mulhouse', 'pageid': 3338790, 'size': 325248, 'wordcount': 32511, 'snippet': 'Pour les articles homonymes, voir <span class="searchmatch">Mulhouse</span> (homonymie). <span class="searchmatch">Mulhouse</span> (/myluz/Écouter) est une commune française située dans la collectivité européenne d\'Alsace', 'timestamp': '2021-05-04T13:28:01Z'}]}}

def test_unit_2_first_request_wiki_method():
    result = test2.first_request_wiki()
    assert result == {'batchcomplete': '', 'continue': {'sroffset': 1, 'continue': '-||'}, 'query': {'searchinfo': {'totalhits': 2122}, 'search': [
        {'ns': 0, 'title': 'Nicolas Cage', 'pageid': 69140, 'size': 58561, 'wordcount': 5631, 'snippet': 'les articles homonymes, voir <span class="searchmatch">Cage</span> (homonymie). <span class="searchmatch">Nicolas</span> <span class="searchmatch">Cage</span> <span class="searchmatch">Nicolas</span> <span class="searchmatch">Cage</span> au Festival de Deauville en 2013. <span class="searchmatch">Nicolas</span> <span class="searchmatch">Cage</span> [ˈnɪkələs keɪdʒ] est un acteur', 'timestamp': '2021-04-19T21:52:35Z'}]}}


# def test2_unit_first_request_wiki_method():
#     result = test3.first_request_wiki()
#     assert result ==
