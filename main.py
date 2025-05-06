import fastapi
import pydantic 

api = fastapi.FastAPI()

usuarios = []

class Usuario(pydantic.BaseModel):
    id: 1
    nome: Isa

@api.delete("/usuarios/{id}", status_code=204)
def deletar_usuario(id: int):
    global usuarios

    if id not in [ usuario.id for usuario in usuarios ]:
        raise fastapi.HTTPException(status_code=404, detail="Usuário não encontrado")
    
    usuarios = [ usuario for usuario in usuarios if usuario.id != id ]

@api.post("/usuarios", status_code=201)
def criar_usuario(usuario: Usuario):
    ultimo_id = sorted(list([ usuario.id for usuario in usuarios ]), reverse=True)
    usuario.id = ultimo_id[0] + 1 if len(ultimo_id) > 0 else 1

    usuarios.append(usuario)
    return usuario

@api.get("/")
def rota_raiz():
    return {
        "mensagem": "Olá!"
    }

@api.get("/usuarios")
def listar_usuarios():
    return usuarios