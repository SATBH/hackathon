from schema import Usuario, Paciente
from datetime import date
from security import obtener_hash_clave

class SQlite:
    pass

mediciones = []

usuarios = [
    Usuario(data=Paciente(nombre="Carlos Fernando Arcia Castro",
                          correo="cfarcia@gmail.com",
                          fecha_nacimiento=date(1980, 12, 25),
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
    if store.obtener_usuario(info.correo):
        return {"error": "El correo ya está en uso"}
    usuarios.append(usuario)

def registrar_medicion(medicion: Medicion):

