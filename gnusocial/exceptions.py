class GNUSocialAPIError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message
        super().__init__(Exception)

    def __repr__(self):
        return 'GNUSocialAPIError(%r)' % self.error_message

    def __str__(self):
        return 'API error: %s' % self.error_message


class ServerURLError(Exception):
    def __init__(self, server_url):
        self.server_url = server_url
        super().__init__(Exception)

    def __repr__(self):
        return 'ServerURLError(%r)' % self.server_url

    def __str__(self):
        return 'Invalid server URL %s' % self.server_url


class AuthenticationError(Exception):
    def __init__(self, server_url, username=''):
        self.server_url = server_url
        self.username = username
        super().__init__(self)

    def __repr__(self):
        msg = 'AuthenticationError(%r' % self.server_url
        if self.username:
            return msg + ', %r)' % self.username
        else:
            return msg + ')'

    def __str__(self):
        msg = 'Invalid credentials'
        if self.username:
            return msg + ' for (%s, %s)' % (self.username, self.server_url)
        return msg
