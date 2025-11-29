# 🎓 Sistema de Gestão Escolar Comunitária

> **Projeto Acadêmico** | CESAR School | Fundamentos da Programação | Python 🐍

Sistema de gestão escolar desenvolvido em Python com interface CLI para gerenciamento de **alunos**, **professores** e **turmas**. Implementa operações CRUD completas com persistência de dados em JSON.

## 👥 Equipe de Desenvolvimento

- Caio Catão
- Caio Martins
- Gustavo Cassemiro
- Kelvia Santos (Líder)
- Luís Felipe
- Mateus Henrique
- Priscila Pontes

## 📋 Características

- ✅ **Sistema CLI Interativo**: Menu completo no terminal
- ✅ **CRUD Completo**: Gerenciamento de alunos, professores e turmas
- ✅ **Persistência em JSON**: Dados salvos automaticamente
- ✅ **Relatórios**: Geração de relatórios por módulo

## ⚠️ Requisitos

- **Python 3.10 ou superior**
- Verificar versão: `python3 --version`

## 🚀 Como Executar

**Primeiro acesso** (dar permissão ao script):

```bash
chmod +x executar.sh
```

**Executar o sistema:**

```bash
./executar.sh
# ou
python3 main.py
# ou
python main.py
```

## 🎯 Funcionalidades

### Gestão de Alunos

- Matricular novos alunos
- Listar e buscar alunos
- Atualizar informações
- Gerar relatórios
- Excluir registros

### Gestão de Professores

- Cadastrar professores
- Listar por turno e matéria
- Atualizar dados
- Remover professores

### Gestão de Turmas

- Criar turmas por período
- Controlar capacidade e sala
- Buscar e atualizar turmas
- Excluir turmas

## 💾 Dados

Os dados são salvos em arquivos JSON na pasta `modulos/`:

- `modulos/alunos/alunos.json`
- `modulos/professores/professores.json`
- `modulos/turmas/turmas.json`

## 🏗️ Estrutura do Projeto

```
gestao-escolar-comunitaria-api/
├── main.py                    # Sistema CLI principal
├── executar.sh               # Script de execução
├── modulos/                   # Módulos de dados
│   ├── alunos/
│   ├── professores/
│   └── turmas/
├── backend/                   # API REST (extra)
└── frontend/                  # Interface Web (extra)
```

## 🐛 Solução de Problemas

### Erro: "SyntaxError: invalid syntax" próximo a "match"

**Causa**: Python 3.9 ou inferior.

**Solução**: Use `python3` ao invés de `python`:

```bash
python3 main.py
```

### Instalar Python 3.10+ (se necessário)

Verifique qual Python está instalado:

```bash
python3 --version
```

**macOS (Homebrew)**:

```bash
brew install python@3.10
```

**Linux (Ubuntu/Debian)**:

```bash
sudo apt update
sudo apt install python3.10
```

**Windows**:

1. Baixe em [python.org/downloads](https://www.python.org/downloads/)
2. ✅ Marque "Add Python to PATH" no instalador
3. Verifique: `python --version`

## 🎨 Tecnologias

- Python 3.10+
- JSON (Persistência de dados)

---

## 🌐 Extras: Sistema Web (Backend + Frontend)

O projeto também inclui uma **API REST** e **interface web** como extensões do sistema CLI.

### 🚀 Como executar o sistema web

**Primeiro acesso:**

```bash
chmod +x start-backend.sh start-frontend.sh
```

**Executar (2 terminais):**

```bash
# Terminal 1 - Backend (porta 5000)
./start-backend.sh

# Terminal 2 - Frontend (porta 8000)
./start-frontend.sh
```

Acesse: `http://localhost:8000`

### 🛠️ Tecnologias Web

**Backend:** Flask, Flask-CORS  
**Frontend:** HTML5, CSS3, JavaScript (Vanilla)

### 📡 Endpoints da API REST

A API REST está disponível em `http://localhost:5000/api`

#### 👨‍🎓 Alunos

- `GET /api/alunos` - Lista todos os alunos
- `GET /api/alunos/<matricula>` - Busca aluno por matrícula
- `POST /api/alunos` - Adiciona novo aluno
- `PUT /api/alunos/<matricula>` - Atualiza aluno
- `DELETE /api/alunos/<matricula>` - Exclui aluno
- `GET /api/alunos/buscar?termo=<texto>` - Busca por nome ou matrícula
- `GET /api/alunos/relatorio` - Relatório geral de alunos

#### 👨‍🏫 Professores

- `GET /api/professores` - Lista todos os professores
- `GET /api/professores/<id>` - Busca professor por ID
- `POST /api/professores` - Adiciona novo professor
- `PUT /api/professores/<id>` - Atualiza professor
- `DELETE /api/professores/<id>` - Exclui professor

#### 📚 Turmas

- `GET /api/turmas` - Lista todas as turmas
- `GET /api/turmas/<cod_turma>` - Busca turma por código
- `POST /api/turmas` - Adiciona nova turma
- `PUT /api/turmas/<cod_turma>` - Atualiza turma
- `DELETE /api/turmas/<cod_turma>` - Exclui turma
- `GET /api/turmas/relatorio` - Relatório geral de turmas

#### 📊 Relatório Geral

- `GET /api/relatorio-geral` - Relatório integrado (alunos por turma, médias, estatísticas)

### 📝 Exemplos de Uso da API

**Adicionar Aluno:**

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

**Adicionar Professor:**

```json
POST /api/professores
{
  "nome": "Maria Santos",
  "turno": "Manhã",
  "materia": "Matemática"
}
```

**Adicionar Turma:**

```json
POST /api/turmas
{
  "periodo": "2025.1",
  "sala": "101",
  "turno": "MANHÃ",
  "capacidade": 30
}
```

### ⚙️ Instalação do Backend (Detalhes)

```bash
# Criar ambiente virtual
python3 -m venv backend/venv

# Ativar ambiente virtual
# macOS/Linux:
source backend/venv/bin/activate
# Windows:
backend\venv\Scripts\activate

# Instalar dependências
pip install -r backend/requirements.txt
```

### 🐛 Troubleshooting Web

- **Flask não encontrado**: `cd backend && source venv/bin/activate && pip install -r requirements.txt`
- **CORS Error**: Certifique-se que o backend está rodando na porta 5000
- **Dados não carregam**: Backend deve estar ativo antes de acessar o frontend
- **Porta 5000 em uso**: Altere a porta no arquivo `backend/app.py` (última linha)
- **Porta 8000 em uso**: Pare outros servidores ou use `python3 -m http.server 8080` (porta diferente)

---
