from typing import Optional

from pydantic import BaseModel
from datetime import datetime

class StudentSchema(BaseModel):
    id: int
    nom: str
    prenom: str
    date_naissance: datetime
    adresse: str
    sexe: str
    classe_id: int

class StudentResponseSchema(StudentSchema):
    codcli: int

class StudentPatchSchema(BaseModel):
    id: Optional[int] = None
    nom: Optional[str] = None
    prenom: Optional[str] = None
    date_naissance: Optional[datetime] = None
    adresse: Optional[str] = None
    sexe: Optional[str] = None
    classe_id: Optional[int] = None

