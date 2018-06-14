class Status(object):

    __instance = None
    OriginalDB = None
    CopyDB = None

    def __new__(cls):
        if Status.__instance is None:
            Status.__instance = object.__new__(cls)
        return Status.__instance
