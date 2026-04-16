import requests
import pytest
import jsonschema


BASE_URL = "https://dummyjson.com"
LOGIN_URL = f"{BASE_URL}/auth/login"
USERS_URL = f"{BASE_URL}/users"
AUTH_ME_URL = f"{BASE_URL}/auth/me"

SCHEMA_USUARIO = {
    "type": "object",
    "required": ["id", "firstName", "lastName", "email", "username"],
    "properties": {
        "id": {"type": "integer"},
        "firstName": {"type": "string", "minLength": 1},
        "lastName": {"type": "string", "minLength": 1},
        "email": {"type": "string", "minLength": 3},
        "username": {"type": "string", "minLength": 1},
    },
}


def _fazer_login():
    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30,
    }
    return requests.post(LOGIN_URL, json=payload, timeout=10)


@pytest.fixture
def recurso_criado():
    """Cria um usuario temporario antes do teste e remove ao final."""
    payload = {
        "firstName": "Teste",
        "lastName": "Automatizado",
        "age": 20,
        "email": "teste.automatizado@exemplo.com",
        "username": "testeautomatizado",
    }
    response = requests.post(f"{USERS_URL}/add", json=payload, timeout=10)
    assert response.status_code == 201
    recurso = response.json()

    yield recurso

    requests.delete(f"{USERS_URL}/{recurso['id']}", timeout=10)


def test_listar_recursos():
    """Valida GET na colecao retornando status 200 e lista de usuarios nao vazia."""
    response = requests.get(USERS_URL, timeout=10)

    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert len(data["users"]) > 0


def test_schema_recurso():
    """Valida que GET em recurso existente retorna schema compativel com jsonschema."""
    response = requests.get(f"{USERS_URL}/1", timeout=10)

    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=SCHEMA_USUARIO)


def test_recurso_inexistente():
    """Valida que GET em recurso inexistente retorna status 404."""
    response = requests.get(f"{USERS_URL}/999999", timeout=10)

    assert response.status_code == 404


def test_criar_recurso():
    """Valida que POST criando usuario retorna status 201 e inclui id na resposta."""
    payload = {
        "firstName": "Maria",
        "lastName": "Oliveira",
        "age": 24,
        "email": "maria.oliveira@exemplo.com",
        "username": "mariaoliveira",
    }
    response = requests.post(f"{USERS_URL}/add", json=payload, timeout=10)

    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["firstName"] == payload["firstName"]


def test_atualizar_recurso():
    """Valida que PUT atualiza um campo do recurso e retorna sucesso."""
    payload = {"lastName": "Atualizado"}
    response = requests.put(f"{USERS_URL}/1", json=payload, timeout=10)

    assert response.status_code == 200
    data = response.json()
    assert data["lastName"] == "Atualizado"


def test_deletar_recurso():
    """Valida que DELETE retorna status 200 ou 204 para a remocao simulada."""
    response = requests.delete(f"{USERS_URL}/1", timeout=10)

    assert response.status_code in (200, 204)


def test_dados_invalidos():
    """Valida que envio de credenciais invalidas gera resposta 4xx."""
    payload = {
        "username": "usuario-invalido",
        "password": "senha-invalida",
    }
    response = requests.post(LOGIN_URL, json=payload, timeout=10)

    assert 400 <= response.status_code < 500


def test_endpoint_autenticado_sem_credencial():
    """Valida que endpoint protegido sem token retorna erro de autenticacao."""
    response = requests.get(AUTH_ME_URL, timeout=10)

    assert response.status_code == 401


def test_endpoint_autenticado_com_credencial():
    """Valida que endpoint protegido com token retorna status 200."""
    login_response = _fazer_login()
    assert login_response.status_code == 200

    token = login_response.json()["accessToken"]
    response = requests.get(
        AUTH_ME_URL,
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )

    assert response.status_code == 200
    assert response.json()["username"] == "emilys"


def test_usar_fixture(recurso_criado):
    """Usa fixture para validar o recurso criado durante o setup do teste."""
    assert "id" in recurso_criado
    assert recurso_criado["firstName"] == "Teste"


def test_tempo_resposta():
    """Valida que o tempo de resposta do GET fica abaixo de 2 segundos."""
    response = requests.get(f"{USERS_URL}/1", timeout=10)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0
