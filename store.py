from schema import Usuario, Paciente, Medicion, FiltrosMediciones
from datetime import date
from security import obtener_hash_clave
from typing import Callable, Any


subscriptions: list[(str, Callable[Medicion, Any])] = []

mediciones = []

usuarios = [
    Usuario(data=Paciente(nombre="Carlos Fernando Arcia Castro",
                          correo="cfarcia@gmail.com",
                          fecha_nacimiento=date(1980, 12, 25),
                          numero_telefono="75300295",
                          peso=80,
                          fecha_registro=date(2021, 1, 1),
                          hash_clave=obtener_hash_clave("clave123"))),
]

def obtener_usuario(correo: str):
    # TODO: usar una db
    for usuario in usuarios:
        if usuario.data.correo == correo:
            return usuario
    return None

def guardar_usuario(usuario: Usuario):
    usuarios.append(usuario)

def registrar_medicion(medicion: Medicion):
    mediciones.append(medicion)
    for correo_usuario, callback in subscriptions:
        if medicion.correo_paciente == correo_usuario:
            callback(medicion)

def agregar_subscripcion(correo_usuario, callback):
    subscriptions.push((correo_usuario, callback))


def obtener_mediciones(filtros: FiltrosMediciones):
    return [i for i in filter(lambda x: filtros.predicado(x), mediciones)]
