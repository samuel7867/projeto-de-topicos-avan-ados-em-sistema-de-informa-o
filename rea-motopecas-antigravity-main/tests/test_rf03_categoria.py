"""RF-03: filtro por categoria tolerante a caixa e espaços."""

def test_rf03_categoria_normalizada(client):
    referencia = client.get('/api/products', params={'category': 'Freios'}).json()
    assert len(referencia) == 2
    for categoria in ('freios', 'FREIOS', '  Freios  '):
        resposta = client.get('/api/products', params={'category': categoria})
        assert resposta.status_code == 200
        assert [p['sku'] for p in resposta.json()] == [p['sku'] for p in referencia]


def test_rf03_categoria_desconhecida(client):
    assert client.get('/api/products', params={'category': 'Categoria inexistente'}).json() == []


def test_rf03_combinacao_categoria_e_busca(client):
    resposta = client.get('/api/products', params={'category': ' filtros ', 'q': 'óleo'})
    assert resposta.status_code == 200
    assert len(resposta.json()) == 1
    assert resposta.json()[0]['name'] == 'Filtro de óleo cartucho'
