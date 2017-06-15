import json
import urllib.parse
import urllib.request


def clean_json_response(dirty_json):
    '''
    Takes the HTTPResponse that is actually JSON and makes it to a string
    so that it can be decoded by json.loads()
    :param dirty_json: HTTPResponse Object
    :return: json string
    '''

    encoding = dirty_json.info().get_content_charset('utf-8')
    return dirty_json.read().decode(encoding)

def get_ipv4():
    '''
    gets IPv6 address.
    :return: string
    '''
    try:
        clean_json = clean_json_response(
            urllib.request.urlopen('http://v4.ipv6-test.com/api/myip.php?json')
        )

        return json.loads(clean_json)['address']

    except urllib.error.HTTPError as e:
        return -1

    except urllib.error.URLError as e:
        return -1

def get_ipv6():
    '''
    gets IPv6 address.
    :return: string
    '''
    try:
        clean_json = clean_json_response(
            urllib.request.urlopen('http://v6.ipv6-test.com/api/myip.php?json')
        )

        return json.loads(clean_json)['address']

    except urllib.error.HTTPError as e:
        return -1

    except urllib.error.URLError as e:
        return -1


if __name__ == "__main__":
    print(get_ipv4())
    print(get_ipv6())