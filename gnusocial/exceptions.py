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
    def __init__(self, server_url, username, password):
        self.server_url = server_url
        self.username = username
        self.password = password
        super().__init__(self)

    def __repr__(self):
        return 'AuthenticationError(%r, %r, %r)' % (self.server_url,
                                                    self.username,
                                                    self.password)

    def __str__(self):
        return 'Invalid credentials for (%s, %s)' % (self.username,
                                                     self.server_url)
