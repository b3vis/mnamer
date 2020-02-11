from mnamer.types import MessageType


class ResultCounter:
    success: int
    skip: int
    fail: int

    def __init__(self, total: int):
        self.success = 0
        self.skip = 0
        self.fail = 0
        self.total = total

    @property
    def remaining(self):
        return self.total - self.success + self.skip + self.fail

    @property
    def report(self) -> str:
        if self.total == 0:
            return "no media files found"
        return (
            f"{self.success} out of {self.total} files processed successfully"
        )

    @property
    def result(self) -> MessageType:
        if self.total == self.success:
            return MessageType.SUCCESS
        elif self.fail:
            return MessageType.ERROR
        else:
            return MessageType.ALERT
