# Atividade 08 - Suite de Testes para API REST

## 1. API escolhida e documentacao

- API escolhida: DummyJSON
- Documentacao oficial: [https://dummyjson.com/docs](https://dummyjson.com/docs)
- Documentacao de usuarios: [https://dummyjson.com/docs/users](https://dummyjson.com/docs/users)
- Documentacao de autenticacao: [https://dummyjson.com/docs/auth](https://dummyjson.com/docs/auth)

## 2. Justificativa da escolha

A DummyJSON foi escolhida porque e uma API publica documentada e atende aos requisitos da atividade. Ela possui endpoints para consulta de colecao e recurso individual, criacao, atualizacao, remocao e autenticacao com token Bearer, o que permite montar uma suite completa cobrindo status codes, schema, validacao, CRUD, autenticacao, fixture e tempo de resposta.

## 3. Instrucoes de instalacao

```bash
pip install -r requirements.txt
```

## 4. Instrucao de execucao

```bash
pytest test_api.py -v
```

Para salvar a saida em arquivo:

```bash
pytest test_api.py -v > resultado.txt
```

## 5. Descricao dos testes implementados

O arquivo `test_api.py` implementa os seguintes testes:

1. `test_listar_recursos`
Verifica `GET /users` com status `200` e lista nao vazia.

2. `test_schema_recurso`
Verifica `GET /users/1` com status `200` e valida o schema do usuario com `jsonschema`.

3. `test_recurso_inexistente`
Verifica `GET /users/999999` retornando `404`.

4. `test_criar_recurso`
Verifica `POST /users/add` retornando `201` e `id` na resposta.

5. `test_atualizar_recurso`
Verifica `PUT /users/1` alterando um campo e retornando sucesso.

6. `test_deletar_recurso`
Verifica `DELETE /users/1` retornando `200` ou `204`.

7. `test_dados_invalidos`
Verifica envio de credenciais invalidas com retorno `4xx`.

8. `test_endpoint_autenticado_sem_credencial`
Verifica que endpoint autenticado sem token retorna `401`.

9. `test_endpoint_autenticado_com_credencial`
Verifica que endpoint autenticado com token valido retorna `200`.

10. `test_usar_fixture`
Usa `@pytest.fixture` para criar um recurso temporario antes do teste.

11. `test_tempo_resposta`
Verifica que o tempo de resposta de um `GET` fica abaixo de `2.0` segundos.

