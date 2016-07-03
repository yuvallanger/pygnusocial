from gnusocial import _get_request


def public_timeline(server_url: str) -> list:
    return _get_request(server_url, 'statuses/public_timeline')
