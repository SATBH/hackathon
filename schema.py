from __future__ import annotations
from dataclasses import dataclass, field 
from decimal import Decimal
from typing import Optional, Union
from datetime import date, datetime


@dataclass
class Paciente:
    correo: str
    nombre: str
    hash_clave: str
    fecha_nacimiento: date
    numero_telefono: str
    peso: Optional[int]
    fecha_registro: date
    doctores: list[str] = field(default_factory=list)
    @property
    def edad(self) -> int:
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))


@dataclass
class Usuario:
    data: Doctor | Paciente



@dataclass
class InfoRegistroPaciente:
    correo: str
    numero_telefono: str
    nombre: str
    clave: str
    fecha_nacimiento: date
    peso: Optional[int]
    fecha_registro: date
    id_doctor: str

@dataclass
class InfoRegistroDoctor:
    correo: str
    clave: str
    especialidad: List[str]


@dataclass
class LoginInfo:
    correo: str
    clave: str


@dataclass
class Doctor:
    correo: str
    nombre: str
    numero_telefono: str
    especialidad: str
    pacientes: list[str]


@dataclass
class Medicion:
    id_paciente: str
    temperatura: float
    ritmo_cardiaco: float
    movimiento: float
    sonido: float
    tiempo_medicion: datetime = field(default_factory=datetime.now)


