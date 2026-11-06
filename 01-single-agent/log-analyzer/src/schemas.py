from pydantic import BaseModel, Field
from enum import StrEnum
from typing import List

class ConfidenceEnum(StrEnum):
    low = "low"
    mid = "mid"
    high = "high"

class Incident(BaseModel):
    patterns: List[str]
    counts: int
    evidence_lines: List[int] = Field(description="Number of lines where the errors and warnings are.")
    confidence: ConfidenceEnum

class Report(BaseModel):
    summary: str
    incidents: List[Incident]
    recommended_actions: List[str]