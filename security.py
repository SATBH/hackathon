from passlib.context import CryptContext

llave = "87491a4613fc7ffaee1d30b00b954aec8b473db714ea8ec2b2a64c864a3db021"
algoritmo = "HS256"
tiempo_expiracion_token = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_clave(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def obtener_hash_clave(password):
    return pwd_context.hash(password)
