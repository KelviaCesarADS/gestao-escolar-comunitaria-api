# 🔧 Backend - API REST

API REST desenvolvida com Flask para o Sistema de Gestão Escolar Comunitária.

## 📦 Instalação

```bash
# Criar ambiente virtual (recomendado)
python3 -m venv venv

# Ativar ambiente virtual
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

## 🚀 Executar

```bash
# Ativar ambiente virtual (se não estiver ativo)
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows

# Executar o servidor
python app.py
```

O servidor estará disponível em: `http://localhost:5000`

## 📡 Endpoints da API

### Alunos

- `GET /api/alunos` - Lista todos os alunos
- `GET /api/alunos/<matricula>` - Busca aluno por matrícula
- `POST /api/alunos` - Adiciona novo aluno
- `PUT /api/alunos/<matricula>` - Atualiza aluno
- `DELETE /api/alunos/<matricula>` - Exclui aluno
- `GET /api/alunos/buscar?termo=<texto>` - Busca por nome ou matrícula
- `GET /api/alunos/relatorio` - Relatório geral

### Professores

- `GET /api/professores` - Lista todos os professores
- `GET /api/professores/<id>` - Busca professor por ID
- `POST /api/professores` - Adiciona novo professor
- `PUT /api/professores/<id>` - Atualiza professor
- `DELETE /api/professores/<id>` - Exclui professor

### Turmas

- `GET /api/turmas` - Lista todas as turmas
- `GET /api/turmas/<cod_turma>` - Busca turma por código
- `POST /api/turmas` - Adiciona nova turma
- `PUT /api/turmas/<cod_turma>` - Atualiza turma
- `DELETE /api/turmas/<cod_turma>` - Exclui turma

## 📝 Exemplos de Requisições

### Adicionar Aluno

```json
POST /api/alunos
{
  "Nome": "João Silva",
  "Idade": "20",
  "Genero": "Masculino",
  "Curso": "Engenharia",
  "Periodo": "2025.1"
}
```

### Adicionar Professor

```json
POST /api/professores
{
  "nome": "Maria Santos",
  "turno": "Manhã",
  "materia": "Matemática"
}
```

### Adicionar Turma

```json
POST /api/turmas
{
  "periodo": "2025.1",
  "sala": "101",
  "turno": "MANHÃ",
  "capacidade": 30
}
```
