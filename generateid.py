import uuid


class GenerateID:
    def __init__(self):
        pass

    @staticmethod
    def generate_id():
        return uuid.uuid4()
