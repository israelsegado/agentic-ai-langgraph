from pydantic import BaseModel
from typing import Optional

class Readme(BaseModel):
    description: str
    instalation: str
    usage: str
    structure: str

class Docstring(BaseModel):
    proposed: str
    file_name: str
    function_name: str
    function_line: int

class Proposal(BaseModel):
    readme: Readme
    docstrings: Optional[Docstring]