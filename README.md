# 🎓 Sistema de Gestão Escolar Comunitária

> **Projeto Acadêmico** | CESAR School | Fundamentos da Programação | Python 🐍

Sistema completo de gestão escolar desenvolvido em Python com **API REST (Flask)** e **Frontend Web (HTML/CSS/JavaScript)**, incluindo módulos para gerenciamento de **alunos**, **professores** e **turmas**. Projeto colaborativo que implementa operações CRUD completas com persistência de dados em JSON.

## 👥 Equipe de Desenvolvimento

- Caio Catão
- Caio Martins
- Gustavo Cassemiro
- Kelvia Santos (Líder)
- Luís Felipe
- Mateus Henrique
- Priscila Pontes

## 📋 Características

- ✅ **API REST com Flask**: Backend completo com endpoints para todas as operações
- ✅ **Frontend Web Moderno**: Interface amigável e responsiva
- ✅ **CRUD Completo de Alunos**: Matrícula, listagem, atualização, busca, relatórios e exclusão
- ✅ **CRUD Completo de Professores**: Cadastro, listagem, atualização e remoção
- ✅ **CRUD Completo de Turmas**: Cadastro, listagem, busca, atualização e exclusão
- ✅ **Persistência de Dados**: Todos os dados são salvos em arquivos JSON
- ✅ **Sistema CLI Original**: Mantido para compatibilidade

## 🏗️ Arquitetura do Projeto

```
gestao-escolar-comunitaria-api/
├── backend/                    # API REST
│   ├── app.py                 # Servidor Flask
│   ├── requirements.txt       # Dependências Python
│   ├── venv/                  # Ambiente virtual
│   └── README.md             # Documentação da API
│
├── frontend/                  # Interface Web
│   ├── index.html            # Página inicial
│   ├── css/
│   │   └── style.css         # Estilos
│   ├── js/
│   │   ├── alunos.js         # Lógica de alunos
│   │   ├── professores.js    # Lógica de professores
│   │   └── turmas.js         # Lógica de turmas
│   └── pages/
│       ├── alunos.html
│       ├── professores.html
│       └── turmas.html
│
├── modulos/                   # Dados compartilhados (CLI + API)
│   ├── alunos/
│   │   ├── alunos.json
│   │   └── crud_alunos.py
│   ├── professores/
│   │   ├── professores.json
│   │   └── crud_professores.py
│   └── turmas/
│       ├── turmas.json
│       └── crud_turmas.py
│
├── main.py                    # Sistema CLI
├── executar.sh               # Script CLI
├── start-backend.sh          # Script para iniciar API
├── start-frontend.sh         # Script para iniciar Frontend
└── README.md                  # Este arquivo
```

## ⚠️ Requisitos

- **Python 3.10 ou superior** (devido ao uso de `match/case`)
- **pip** (gerenciador de pacotes Python)
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

### Verificar versão do Python

```bash
python3 --version
```

## 🚀 Como Executar

### ⚡ Início Rápido

Para começar rapidamente, consulte o **[QUICKSTART.md](QUICKSTART.md)**

**Resumo:**

```bash
# Terminal 1 - Backend
./start-backend.sh

# Terminal 2 - Frontend
./start-frontend.sh
```

Acesse: `http://localhost:8000`

⚠️ **IMPORTANTE**: O frontend requer que o backend esteja rodando!

---

### 🖥️ Sistema CLI Original

```bash
./executar.sh
# ou
python3 main.py
```

---

### 📚 Documentação Detalhada

- **[QUICKSTART.md](QUICKSTART.md)** - Guia rápido de início
- **[backend/README.md](backend/README.md)** - Documentação completa da API
  - Instalação detalhada
  - Lista completa de endpoints
  - Exemplos de requisições

## 🎯 Funcionalidades

### 🌐 Sistema Web (API + Frontend)

**Dashboard Principal**

- Acesso rápido aos módulos de Alunos, Professores e Turmas
- Interface intuitiva e responsiva

**Gestão de Alunos**

- ✅ Visualização de estatísticas (total, média de idade)
- ✅ Busca por nome ou matrícula
- ✅ Adicionar/Editar/Excluir alunos
- ✅ Geração de relatórios

**Gestão de Professores**

- ✅ Listagem completa de professores
- ✅ Adicionar/Editar/Excluir professores
- ✅ Visualização por turno e matéria

**Gestão de Turmas**

- ✅ Cadastro de turmas por período
- ✅ Controle de capacidade e sala
- ✅ Adicionar/Editar/Excluir turmas

### 🖥️ Sistema CLI (Terminal)

- Menu interativo completo
- CRUD de Alunos, Professores e Turmas
- Mesmos dados compartilhados com a API

### 📡 API REST

**18 endpoints disponíveis** para gerenciamento completo. Veja a lista completa em [backend/README.md](backend/README.md)

## 💾 Dados Persistentes

Todos os dados são automaticamente salvos em arquivos JSON na pasta `modulos/` (compartilhada entre CLI e API):

- `modulos/alunos/alunos.json`
- `modulos/professores/professores.json`
- `modulos/turmas/turmas.json`

**✨ Vantagem**: O sistema CLI e a API compartilham os mesmos dados! Qualquer alteração feita em um é refletida no outro.

## 🐛 Solução de Problemas

### Backend não inicia

**Erro**: `ModuleNotFoundError: No module named 'flask'`

**Solução**:

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### CORS Error no Frontend

**Erro**: `Access to fetch has been blocked by CORS policy`

**Solução**: Certifique-se de que o backend está rodando (`./start-backend.sh`)

### Frontend não carrega dados

**Causa**: Backend não está rodando

**Solução**: Execute `./start-backend.sh` antes de abrir o frontend

### Erro: "SyntaxError: invalid syntax" próximo a "match" (Sistema CLI)

**Causa**: Você está usando Python 3.9 ou inferior.

**Solução**: Use `python3`:

```bash
python3 main.py
```

## 🎨 Tecnologias Utilizadas

### Backend

- Python 3.10+
- Flask (Framework Web)
- Flask-CORS (Cross-Origin Resource Sharing)
- JSON (Persistência de dados)

### Frontend

- HTML5
- CSS3 (Design responsivo)
- JavaScript (Vanilla JS)
- Fetch API (Requisições HTTP)

## 📚 Documentação Adicional

- [Documentação do Backend](backend/README.md) - Detalhes completos da API
- [Documentação Flask](https://flask.palletsprojects.com/)

## 🌟 Próximas Melhorias

- [ ] Autenticação e autorização de usuários
- [ ] Banco de dados (SQLite/PostgreSQL)
- [ ] Vinculação de alunos às turmas
- [ ] Upload de fotos de perfil
- [ ] Exportação de relatórios em PDF
- [ ] Dashboard com gráficos
- [ ] Testes automatizados

## 📝 Licença

Projeto acadêmico desenvolvido para fins educacionais - CESAR School 2025

---

**Desenvolvido com ❤️ pela equipe do projeto**
