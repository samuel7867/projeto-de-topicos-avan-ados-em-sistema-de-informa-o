# Relatório técnico — Modalidade A / RF-03

**Disciplina:** Engenharia de Software Avançada com IA  
**Sistema:** Rota 2 Motopeças  
**Equipe:** preencher integrantes antes da entrega  
**Modalidade:** A — Workflow de Engenharia de Software

## 1. Problema e escopo
O filtro existente em `GET /api/products?category=` realizava comparação exata com a categoria cadastrada. Assim, `Freios` retornava dois produtos, mas `freios`, `FREIOS` e `  Freios  ` não produziam o mesmo resultado. Escopo restrito ao repositório didático e ao banco de testes.

## 2. Requisito e critérios de aceitação
**RF-03 (melhoria):** o filtro de categoria deve ignorar diferenças de caixa e espaços externos, sem modificar os nomes armazenados. Critérios: (CA1) três grafias equivalentes retornam os mesmos SKUs; (CA2) categoria inexistente retorna lista vazia; (CA3) combinação com busca textual mantém resultado correto; (CA4) testes anteriores não sofrem regressão.

## 3. RED → GREEN → revisão
**RED:** adicionados `tests/test_rf03_categoria.py` com três casos. Antes da correção, falharam os testes de normalização e de combinação com busca; o caso de categoria inexistente passou. Registro: `docs/evidence/rf03-red.txt`.

**GREEN:** em `app/main.py`, a comparação `p.category = ?` passou a `LOWER(TRIM(p.category)) = ?`, usando `category.strip().casefold()` no parâmetro SQL. A consulta continua parametrizada, sem concatenação de entrada do usuário.

**Regressão:** execução local `python -m pytest -q`: **19 testes passaram**. Gate `python scripts/gate.py`: **GATE PASS**, incluindo compilação e pytest. Registros em `docs/evidence/rf03-green.txt` e `docs/evidence/rf03-gate.txt`.

## 4. Segurança e limites
Não foram usados dados pessoais, credenciais ou pagamentos reais. A alteração não muda o banco de dados e mantém SQL parametrizado. A normalização atende às categorias demonstrativas; equivalências linguísticas mais amplas e testes de interface em navegador não foram verificados.

## 5. Rastreabilidade
| Requisito | Teste | Arquivo alterado | Evidência | Estado |
|---|---|---|---|---|
| RF-03 / CA1 | test_rf03_categoria_normalizada | app/main.py | rf03-red.txt, rf03-green.txt | PASS |
| RF-03 / CA2 | test_rf03_categoria_desconhecida | tests/test_rf03_categoria.py | rf03-green.txt | PASS |
| RF-03 / CA3 | test_rf03_combinacao_categoria_e_busca | app/main.py | rf03-red.txt, rf03-green.txt | PASS |
| RF-03 / CA4 | suíte completa | app/main.py | rf03-gate.txt | PASS |

## 6. Revisão e publicação
Revisão independente: **PENDENTE** — deve ser realizada por integrante distinto, registrando parecer. Branch, commits, Pull Request e CI remota: **NÃO VERIFICADOS**; o ZIP entregue não inclui histórico Git. Publicar o código em branch própria, registrar commit, obter revisão humana e anexar URL do PR antes da entrega.

## 7. Conclusão
O comportamento de filtragem foi melhorado e validado por testes automatizados locais. Não se afirma execução de revisão independente ou CI no GitHub.
