# Rota 2 Motopeças — Modalidade A

### Engenharia de Software Avançada

**Integrantes:** Samuel Marinho e João Márcio  
**Professor:** Fernando Garcia  
**Curso:** Sistemas de Informação  
**Ano:** 2026

---

## Sobre o projeto

O projeto Rota 2 Motopeças consiste em uma aplicação web desenvolvida para simular uma loja virtual de peças para motocicletas.

Este trabalho foi realizado na **Modalidade A — Workflow de Engenharia de Software**, com foco no aperfeiçoamento do requisito **RF-03 — Filtro de Produtos por Categoria**.

O objetivo foi melhorar a consistência da busca de produtos e validar as alterações por meio de testes automatizados.

## Melhoria implementada

A melhoria realizada permite que o filtro reconheça diferentes formas de escrita de uma mesma categoria.

Por exemplo:

- `Freios`
- `FREIOS`
- `freios`
- ` Freios `

Todas essas entradas devem produzir resultados equivalentes.

Essa funcionalidade melhora a experiência do usuário e torna a filtragem mais consistente.

## Tecnologias utilizadas

- Python 3.12
- FastAPI
- SQLite
- HTML, CSS e JavaScript
- Pytest
- Git e GitHub
- Visual Studio Code

## Metodologia de desenvolvimento

Foi utilizada a metodologia **TDD (Test-Driven Development)**, organizada em três etapas:

**RED:** criação de testes para identificar o comportamento que precisava ser corrigido.

**GREEN:** implementação da melhoria para atender aos testes.

**REFACTOR:** revisão e organização do código, preservando o comportamento esperado.

## Como executar o projeto

### 1. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

No Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements-dev.txt
```

### 4. Executar a aplicação

```bash
python -m uvicorn app.main:app --reload
```

Acesse no navegador:

http://127.0.0.1:8000

## Testes automatizados

Para executar os testes:

```bash
python -m pytest -q
```

**Resultado registrado durante o desenvolvimento:**

- 19 testes aprovados.
- Melhoria do filtro por categoria validada.
- Gate técnico local aprovado.

Os resultados devem ser confirmados ao executar os testes na versão atual do repositório.

## Resultados e conclusão

A melhoria do requisito RF-03 tornou a filtragem por categoria mais consistente, permitindo reconhecer diferentes formas de escrita.

O projeto possibilitou aplicar conceitos de Engenharia de Software, testes automatizados e desenvolvimento assistido por Inteligência Artificial.

A experiência demonstrou a importância de validar alterações no código para manter a qualidade, a confiabilidade e a organização de uma aplicação.

---

**Projeto acadêmico — Sistemas de Informação | 2026**
