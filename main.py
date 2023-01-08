from http.cookies import SimpleCookie
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
    cookie = SimpleCookie()
    cookie.load(query)
    new_dict = {}
    for keys, values in cookie.items():
        new_dict[keys] = values.value
    return new_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('NAME=VALUE') == {'NAME': 'VALUE'}
    assert parse_cookie('ReturnUrl=%2Fru%2Fcabinet') == {'ReturnUrl': '%2Fru%2Fcabinet'}
    assert parse_cookie('NAME=VALUE; expires=DATE; path=PATH; domain=DOMAIN_NAME; secure') == {'NAME': 'VALUE'}
    assert parse_cookie('name=ferret;color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_cookie('PART_NUMBER=ROCKET_LAUNCHER_0001; path=/') == {'PART_NUMBER': 'ROCKET_LAUNCHER_0001'}
    assert parse_cookie('hl=ru;tab=rT;sl=en;tl=ru;op=translate') == {'hl': 'ru', 'tab': 'rT',
                                                                     'sl': 'en', 'tl': 'ru',
                                                                     'op': 'translate'}
    assert parse_cookie('NAME1=OPAQUE_STRING1; NAME2=OPAQUE_STRING2') == {'NAME1': 'OPAQUE_STRING1',
                                                                          'NAME2': 'OPAQUE_STRING2'}
    assert parse_cookie('q=python;sxsrf=ALiCzsa9oZN7AbKXeaqIiyf1ksT31sb3hg%3A1673021001209;'
                 'ei=SUa4Y4qPDMK-xc8PtpmN4Aw;ved=0ahUKEwjK1-nzqLP8AhVCX_EDHbZMA8wQ4dUDCA8;uact=5;oq=python;gs_lcp=Cgxnd'
                 '3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIECCMQJzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIFCAAQgAQ6Bw'
                 'gjELADECc6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQrQVYrQVgxQloAXABeACAAV-IAV-SAQExmAEAoAEByAEJwAEB'
                 ';sclient=gws-wiz-serp') == {'q': 'python',
                                              'sxsrf': 'ALiCzsa9oZN7AbKXeaqIiyf1ksT31sb3hg%3A1673021001209',
                                              'ei': 'SUa4Y4qPDMK-xc8PtpmN4Aw',
                                              'ved': '0ahUKEwjK1-nzqLP8AhVCX_EDHbZMA8wQ4dUDCA8',
                                              'uact': '5',
                                              'oq': 'python',
                                              'gs_lcp': 'Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIECCMQJzIECAAQQzIECA'
                                                        'AQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIFCAAQgAQ6BwgjELADECc6'
                                                        'CggAEEcQ1gQQsANKBAhBGABKBAhGGABQrQVYrQVgxQloAXABeACAAV-IAV-'
                                                        'SAQExmAEAoAEByAEJwAEB',
                                              'sclient': 'gws-wiz-serp'}
    assert parse_cookie('search_query=python+vs+javascript') == {'search_query': 'python+vs+javascript'}
    assert parse_cookie('ReturnUrl=%2Fru%2Fcabinet') == {'ReturnUrl': '%2Fru%2Fcabinet'}