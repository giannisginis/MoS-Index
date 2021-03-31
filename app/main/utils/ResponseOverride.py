import json


class ResponseOverride(Exception):
    def __init__(self, status_code: int = None, sequence: str = None,
                 message: str = None):
        self.status_code = status_code
        self.sequence = sequence
        self.message = message
        self.attributes = {"status_code": self.status_code, "text": self.sequence,
                           "message": self.message}
        self.attributes_str = json.dumps(self.attributes)

    def get_status_code(self):
        return self.status_code

    def get_sequence(self):
        return self.sequence

    def get_message(self):
        return self.message

    def json(self):
        return json.loads(self.attributes_str)

    def to_dict(self):
        return {"status_code": self.status_code, "text": self.sequence, "message": self.message}
