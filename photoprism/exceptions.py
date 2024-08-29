class PhotoprismError(Exception):
    pass


class PhotoprismUnauthorizedError(PhotoprismError):
    pass


class PhotoprismNotFoundError(PhotoprismError):
    pass


class PhotoprismTimeoutError(PhotoprismError):
    pass


class PhotoprismBadRequestError(PhotoprismError):
    pass
