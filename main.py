from http.cookies import SimpleCookie


def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


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