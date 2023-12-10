from pydantic import BaseModel
from typing import Optional, List
from model.mulher import mulher
import json
import numpy as np

class MulherSchema(BaseModel):
    """ Define como um novo mulher a ser inserido deve ser representado
    """
    name: str = "Gabriela"
    rad_mean: float = 7.76
    tex_mean: float = 24.54
    perim_mean: float = 47.92
    area_mean: float = 181.0
    smoo_mean: float = 0.05263
    comp_mean: float = 0.04362
    concav_mean: float = 0.00000
    cp_mean: float = 0.00000
    sym_mean: float = 0.1587
    fd_mean: float = 0.05884

class MulherViewSchema(BaseModel):
    """Define como um mulher será retornado
    """
    id: int = 1
    name: str = "Gabriela"
    rad_mean: float = 7.76
    tex_mean: float = 24.54
    perim_mean: float = 47.92
    area_mean: float = 181.0
    smoo_mean: float = 0.05263
    comp_mean: float = 0.04362
    concav_mean: float = 0.00000
    cp_mean: float = 0.00000
    sym_mean: float = 0.1587
    fd_mean: float = 0.05884
    outcome: int = None

class MulherBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do mulher.
    """
    name: str = "Gabriela"

class ListaMulheresSchema(BaseModel):
    """Define como uma lista de mulheres será representada
    """
    mulheres: List[MulherSchema]

class MulherDelSchema(BaseModel):
    """Define como um mulher para deleção será representado
    """
    name: str = "Gabriela"

# Apresenta apenas os dados de um mulher
def apresenta_mulher(mulher: mulher):
    """ Retorna uma representação do mulher seguindo o schema definido em
        mulherViewSchema.
    """
    return {
        "id": mulher.id,
        "name": mulher.name,
        "rad_mean": mulher.rad_mean,
        "tex_mean": mulher.tex_mean,
        "perim_mean": mulher.perim_mean,
        "area_mean": mulher.area_mean,
        "smoo_mean": mulher.smoo_mean,
        "comp_mean": mulher.comp_mean,
        "concav_mean": mulher.concav_mean,
        "cp_mean": mulher.cp_mean,
        "sym_mean": mulher.sym_mean,
        "fd_mean": mulher.fd_mean,
        "outcome": mulher.outcome
    }

# Apresenta uma lista de mulheres
def apresenta_mulheres(mulheres: List[mulher]):
    """ Retorna uma representação do mulher seguindo o schema definido em
        mulherViewSchema.
    """
    result = []
    for mulher in mulheres:
        result.append({
            "id": mulher.id,
            "name": mulher.name,
            "rad_mean": mulher.rad_mean,
            "tex_mean": mulher.tex_mean,
            "perim_mean": mulher.perim_mean,
            "area_mean": mulher.area_mean,
            "smoo_mean": mulher.smoo_mean,
            "comp_mean": mulher.comp_mean,
            "concav_mean": mulher.concav_mean,
            "cp_mean": mulher.cp_mean,
            "sym_mean": mulher.sym_mean,
            "fd_mean": mulher.fd_mean,
            "outcome": mulher.outcome
        })

    return {"mulheres": result}