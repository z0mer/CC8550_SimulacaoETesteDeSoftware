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
    """
    Função auxiliar que realiza o login com credenciais de teste.
    Envia requisição POST para o endpoint de autenticação com usuário e senha padrão.
    Retorna a resposta da requisição contendo o token de autenticação.
    """
    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30,
    }
    return requests.post(LOGIN_URL, json=payload, timeout=10)


@pytest.fixture
def recurso_criado():
    """
    Fixture que implementa o padrão setup-teardown.
    Cria um usuário de teste antes da execução do teste (setup)
    e remove esse usuário após a conclusão (teardown),
    garantindo que o banco de dados fica limpo após cada teste.
    """
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
    """
    Testa a listagem de todos os usuários (GET na coleção).
    Valida que o endpoint retorna status HTTP 200 (sucesso)
    e que a resposta contém uma lista não vazia de usuários.
    """
    response = requests.get(USERS_URL, timeout=10)

    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert len(data["users"]) > 0


def test_schema_recurso():
    """
    Testa a validação do schema de resposta da API.
    Recupera um usuário específico (GET) e valida que a estrutura
    da resposta está em conformidade com o schema JSON definido (SCHEMA_USUARIO).
    """
    response = requests.get(f"{USERS_URL}/1", timeout=10)

    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=SCHEMA_USUARIO)


def test_recurso_inexistente():
    """
    Testa a resposta da API ao acessar um recurso que não existe.
    Valida que o endpoint retorna status HTTP 404 (Not Found)
    quando tenta acessar um usuário com ID inexistente.
    """
    response = requests.get(f"{USERS_URL}/999999", timeout=10)

    assert response.status_code == 404


def test_criar_recurso():
    """
    Testa a criação de um novo usuário (POST).
    Valida que o endpoint retorna status HTTP 201 (Created)
    e que a resposta contém um ID gerado para o novo usuário.
    """
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
    """
    Testa a atualização de um usuário existente (PUT).
    Envia uma requisição de atualização parcial de um campo
    e valida que o servidor retorna status 200 com o valor atualizado.
    """
    payload = {"lastName": "Atualizado"}
    response = requests.put(f"{USERS_URL}/1", json=payload, timeout=10)

    assert response.status_code == 200
    data = response.json()
    assert data["lastName"] == "Atualizado"


def test_deletar_recurso():
    """
    Testa a exclusão de um usuário (DELETE).
    Valida que o endpoint retorna status HTTP 200 ou 204,
    indicando sucesso na operação de remoção.
    """
    response = requests.delete(f"{USERS_URL}/1", timeout=10)

    assert response.status_code in (200, 204)


def test_dados_invalidos():
    """
    Testa o comportamento da API com credenciais inválidas.
    Valida que o endpoint de autenticação rejeita credenciais incorretas
    retornando um código de erro 4xx (erro do cliente).
    """
    payload = {
        "username": "usuario-invalido",
        "password": "senha-invalida",
    }
    response = requests.post(LOGIN_URL, json=payload, timeout=10)

    assert 400 <= response.status_code < 500


def test_endpoint_autenticado_sem_credencial():
    """
    Testa a segurança do endpoint autenticado.
    Valida que ao tentar acessar um endpoint protegido sem fornecer um token,
    a API retorna status HTTP 401 (Unauthorized).
    """
    response = requests.get(AUTH_ME_URL, timeout=10)

    assert response.status_code == 401


def test_endpoint_autenticado_com_credencial():
    """
    Testa o acesso a endpoint protegido com token de autenticação.
    Realiza login para obter um token válido, depois usa esse token
    para acessar um endpoint protegido e valida que retorna status 200.
    """
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
    """
    Testa o funcionamento da fixture recurso_criado.
    Valida que a fixture criou corretamente um usuário com os dados esperados,
    verificando a presença do ID e do nome esperado na resposta.
    """
    assert "id" in recurso_criado
    assert recurso_criado["firstName"] == "Teste"


def test_tempo_resposta():
    """
    Testa o desempenho da API medindo o tempo de resposta.
    Valida que uma requisição GET retorna sucesso (status 200)
    e que o tempo total de resposta fica abaixo do limite de 2 segundos.
    """
    response = requests.get(f"{USERS_URL}/1", timeout=10)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0
