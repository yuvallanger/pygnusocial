import re

domain_regex = re.compile("http(s|)://(www\.|)(.+?)(/.*|)$")


class ServerURLError(Exception):
    def __init__(self, server_url: str):
        self.server_url = server_url

    def __repr__(self):
        return 'ServerURLError(%r)' % self.server_url

    def __str__(self):
        return 'Invalid server URL %s' % self.server_url


class AuthenticationError(Exception):
    def __init__(self, server_url: str, username: str, password: str):
        self.server_url = server_url
        self.username = username
        self.password = password

    @property
    def credentials(self):
        return (self.username, self.password)

    def __repr__(self):
        return 'AuthenticationError(%r, %r, %r)' % (self.server_url,
                                                    *self.credentials)

    def __str__(self):
        return 'Invalid credentials %s:%s for %s' % (*self.credentials,
                                                     self.server_url)
