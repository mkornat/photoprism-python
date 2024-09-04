from pydantic import BaseModel


class Resources(BaseModel):
    class Memory(BaseModel):
        free: int
        info: str
        reserved: int
        total: int
        used: int

    cores: int
    memory: Memory
    routines: int
