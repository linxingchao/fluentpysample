from dataclasses import dataclass,field
from typing import Optional
from enum import Enum,auto
from datetime import date
 
class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()
    
@dataclass
class Resource:
    identifier: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None
    description: str = ''
    type: ResourceType = ResourceType.BOOK
    language: str = ''
    subjects: list[str] = field(default_factory=list)
     
     