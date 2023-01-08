import urllib
from urllib.parse import urlparse


def parse(query: str) -> dict:
    parser = urlparse(query)

    return dict(urllib.parse.parse_qsl(parser.query))


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://py.checkio.org/en/mission/just-fizz/') == {}
    assert parse('https://www.codewars.com/kata/57a0885cbb9944e24c00008e/solutions/python') == {}
    assert parse('https://translate.google.de/?hl=ru&tab=rT&sl=en&tl=ru&op=translate') == {'hl': 'ru', 'tab': 'rT',
                                                                                           'sl': 'en', 'tl': 'ru',
                                                                                           'op': 'translate'}
    assert parse('https://lms.ithillel.ua/groups/634317c22fa78f4b3a6fd66c/homeworks/63ab49bedd0ec14f08fb1d8f') == {}
    assert parse('https://ru.wikipedia.org/wiki/Python') == {}
    assert parse('https://github.com/Pashatishinin/Hillel_Pro') == {}
    assert parse('https://www.youtube.com/') == {}
    assert parse('https://itvdn.com/ru/subscriptions') == {}
    assert parse('https://www.youtube.com/watch?v=vou0HS2EXos') == {"v": "vou0HS2EXos"}
    assert parse('https://www.youtube.com/watch?v=z5lo2_mMZ3E') == {"v": "z5lo2_mMZ3E"}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}