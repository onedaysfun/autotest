
import time


class Base:
    def __init__(self):
        self.id: int = 0
        self.token: str = ""
        self.version: int = 0
        self.tenant_id: int = 0
        self.owner: int = 0
        self.blocks: list = []
        self.parent_id: int = 0
        self.parent_type: int = 0
        self.edited_time = time.time()
        self.creator: int = 0
        self.delete_flag = 0
        self.source: int = 0
        self.obj_type: int = 8


class Table:
    def __init__(self):
        self.id: int = 0
        self.token: str = ""
        self.parent_token: str = ""
        self.field_map: dict = {}
        self.localRev: int = 0


