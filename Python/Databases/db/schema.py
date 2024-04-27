from dataclasses import dataclass

@dataclass
class DBSchema():
    column_name: str
    data_type: str
    is_nullable: bool
    character_maximum_length: int
    udt_name: str