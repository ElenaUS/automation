from sys import maxsize


class Base:
    def __init__(self, username=None, id=None, amount=None):
        self.id = id
        self.amount = amount
        self.username = username

    def __repr__(self):
        return "%s:%s;%s" % (self.id, self.amount, self.username)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.amount == other.amount and self.username == other.username

    """def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize"""
