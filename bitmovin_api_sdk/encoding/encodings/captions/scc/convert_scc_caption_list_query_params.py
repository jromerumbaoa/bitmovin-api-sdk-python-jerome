class ConvertSccCaptionListQueryParams(dict):
    def __init__(self, offset=None, limit=None):
        # type: (int, int) -> None
        super(ConvertSccCaptionListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
