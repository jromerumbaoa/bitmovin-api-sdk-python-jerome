class AacAudioConfigurationListQueryParams(dict):
    def __init__(self, offset=None, limit=None, name=None):
        # type: (int, int, string_types) -> None
        super(AacAudioConfigurationListQueryParams, self).__init__()

        self.offset = offset
        self.limit = limit
        self.name = name
