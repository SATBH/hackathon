import sqlite3 as sql
from fastapi import FastAPI, WebSocket
import schema
import jwt
from security import obtener_hash_clave, verificar_clave
import store


app = FastAPI()



@app.post("/login")
async def login(info: schema.LoginInfo):
    usuario = store.obtener_usuario(info.correo).data
    if usuario and verificar_clave(info.clave, usuario.hash_clave):
        if type(usuario).__name__ == 'Doctor':
            doctor = usuario
            return jwt.encode({
                "correo": doctor.correo,
                "nombre": doctor.nombre,
                "especialidad": doctor.especialidad,
                "pacientes": doctor.pacientes,
                "numero_telefono": doctor.numero_telefono,
                "tipo_usuario": "doctor"
            }, 'secret-key')
        else:
            paciente = usuario
            return jwt.encode({
                "correo": paciente.correo,
                "nombre": paciente.nombre,
                "peso": paciente.peso,
                "fecha_nacimiento": paciente.fecha_nacimiento.isoformat(),
                "fecha_registro": paciente.fecha_registro.isoformat(),
                "edad": paciente.edad,
                "numero_telefono": doctor.numero_telefono,
                "tipo_usuario": "paciente"
            }, 'secret-key')
    return {"error": "El usario o la contraseña son incorrectos"}


@app.post("/registro_paciente")
async def registro_paciente(info: schema.InfoRegistroPaciente): 
    if store.obtener_usuario(info.correo):
        return {"error": "El correo ya está en uso"}
    hash_clave = obtener_hash_clave(info.clave)
    paciente = schema.Paciente(
        correo=info.correo,
        nombre=info.nombre,
        numero_telefono=info.numero_telefono,
        hash_clave=hash_clave,
        fecha_nacimiento=info.fecha_nacimiento,
        peso=info.peso,
        fecha_registro=info.fecha_registro,
        doctores=info.doctores
    )
    return store.guardar_usuario(schema.Usuario(paciente)) or {"mensaje": "Registro exitoso"}


@app.post("/registro_doctor")
async def registro_doctor(info: schema.InfoRegistroDoctor): 
    if store.obtener_usuario(info.correo):
        return {"error": "El correo ya está en uso"}
    hash_clave = obtener_hash_clave(info.clave)
    paciente = schema.Doctor(
        correo=info.correo,
        nombre=info.nombre,
        numero_telefono=info.numero_telefono,
        hash_clave=hash_clave,
        especialidad=info.especialidad,
    )
    return store.guardar_usuario(schema.Doctor(paciente)) or {"mensaje": "Registro exitoso"}

@app.websocket("/registro_datos")
async def websocket_endpoint(websocket: WebSocket):
    while True:
        data = await websocket.receive_text()
        medicion = schema.Medicion(**data)
        store.agregar_medicion(medicion)
        # TODO: guardar la medición en la db
        print(medicion)

@app.websocket("/leer_mediciones_tiempo_real")
async def websocket_endpoint(websocket: WebSocket, correo_usuario: str):
    # TODO
    pass
    #usuario = store.obtener_usuario(correo_usuario).data

