class Link:
    sourceURL: str
    otherArgs: list

    def __init__(self, sourceURL: str, otherArguments: list) -> None:
        self.sourceURL = sourceURL
        self.otherArguments = otherArguments
