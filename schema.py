from __future__ import annotations
from dataclasses import dataclass, field 
from decimal import Decimal
from typing import Optional, Union
from datetime import date, datetime
from enum import Enum


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

class Subscripcion(Enum):
    GRATIS = 0
    BASICO = 1
    ESTANDAR = 2
    PREMIUM = 3


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
    doctores: list[str]

@dataclass
class InfoRegistroDoctor:
    correo: str
    clave: str
    nombre: str
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
    hash_clave: str
    especialidad: Optional[str] = field(default=None)
    pacientes: list[str] = field(default_factory=list)


@dataclass
class Medicion:
    correo_paciente: str
    temperatura: float
    ritmo_cardiaco: float
    movimiento: float
    sonido: float
    tiempo_medicion: datetime = field(default_factory=datetime.now)


@dataclass
class FiltrosMediciones:
    correo_paciente: str
    temperatura: Optional[(float, float)]
    ritmo_cardiaco: Optional[(float, float)]
    movimiento: Optional[(float, float)]
    sonido: Optional[(float, float)]
    tiempo_medicion: Optional[(datetime, datetime)]
    def predicado(self, medicion: Medicion):
        correo_filtro = medicion.correo_paciente == self.correo_paciente
        temperatura_filtro = (self.temperatura[0] < medicion.temperatura < self.temperatura[1]) if self.temperatura else True
        ritmo_cardiaco_filtro = (self.ritmo_cardiaco[0] < medicion.ritmo_cardiaco < self.ritmo_cardiaco[1]) if self.ritmo_cardiaco else True
        movimiento_filtro = (self.movimiento[0] < medicion.movimiento < self.movimiento[1]) if self.movimiento else True
        sonido_filtro = (self.temperatura[0] < medicion.temperatura < self.temperatura[1]) if self.temperatura else True
        tiempo_medicion_filtro = (self.tiempo_medicion[0] < medicion.tiempo_medicion < self.tiempo_medicion[1]) if self.tiempo_medicion else True
        return correo_filtro and temperatura_filtro and ritmo_cardiaco_filtro and sonido_filtro and tiempo_medicion_filtro
