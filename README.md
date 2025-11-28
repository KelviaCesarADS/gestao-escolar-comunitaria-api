# 🎓 Sistema de Gestão Escolar Comunitária

> **Projeto Acadêmico** | CESAR School | Fundamentos da Programação | CESAR School | Python 🐍

Sistema completo de gestão escolar desenvolvido em Python, com módulos independentes para gerenciamento de **alunos**, **professores** e **turmas**. Projeto colaborativo que implementa operações CRUD completas com persistência de dados em JSON.

## 👥 Equipe de Desenvolvimento

- Caio Catão
- Caio Martins
- Gustavo Cassemiro
- Kelvia Santos
- Luís Felipe
- Mateus Henrique
- Priscila Pontes

### Nome da Líder

- Kelvia Santos

## 📋 Características

- ✅ **CRUD Completo de Alunos**: Matrícula, listagem, atualização, busca, relatórios e exclusão
- ✅ **CRUD Completo de Professores**: Cadastro, listagem, atualização e remoção
- ✅ **CRUD Completo de Turmas**: Cadastro, listagem, busca, atualização e exclusão
- ✅ **Persistência de Dados**: Todos os dados são salvos em arquivos JSON
- ✅ **Módulos Independentes**: Cada sistema pode funcionar de forma autônoma

## ⚠️ Requisitos

- **Python 3.10 ou superior** (devido ao uso de `match/case`)
- Sistema testado com Python 3.14.0

### Verificar versão do Python

```bash
python3 --version
```

## 🚀 Como Executar

### Opção 1: Usando o script auxiliar (Mais fácil)

Primeiro, dê permissão de execução ao script:

```bash
chmod +x executar.sh
```

Depois execute:

```bash
./executar.sh
```

### Opção 2: Usando python3 (Recomendado)

```bash
python3 main.py
```

### Opção 3: Usando python (se configurado para 3.10+)

```bash
python main.py
```

## 📁 Estrutura do Projeto

```
gestao-escolar-comunitaria-api/
├── main.py                    # Arquivo principal (orquestrador)
├── executar.sh               # Script auxiliar para execução
├── modulos/
│   ├── alunos/
│   │   ├── crud_alunos.py   # Sistema de gestão de alunos
│   │   └── alunos.json      # Dados dos alunos
│   ├── professores/
│   │   ├── crud_professores.py  # Sistema de gestão de professores
│   │   └── professores.json     # Dados dos professores
│   └── turmas/
│       ├── crud_turmas.py   # Sistema de gestão de turmas
│       └── turmas.json      # Dados das turmas
└── README.md
```

## 🎯 Navegação no Sistema

```
╔═══════════════════════════════════════╗
║   GESTÃO ESCOLAR COMUNITÁRIA         ║
╠═══════════════════════════════════════╣
║  1 - Gestão de Alunos                ║
║  2 - Gestão de Professores           ║
║  3 - Gestão de Turmas                ║
║  4 - Sair do Sistema                 ║
╚═══════════════════════════════════════╝
```

### Sistema de Alunos

- Matricular aluno
- Listar alunos matriculados
- Atualizar cadastro
- Buscar aluno (por matrícula ou nome)
- Gerar relatório geral
- Excluir matrícula

### Sistema de Professores

- Adicionar professor
- Listar professores
- Atualizar dados do professor
- Gerar relatório geral
- Deletar professor

### Sistema de Turmas

- Cadastrar nova turma
- Listar todas as turmas
- Buscar uma turma específica
- Atualizar dados da turma
- Gerar relatório geral
- Deletar turma

## 🔧 Solução de Problemas

### Erro: "SyntaxError: invalid syntax" próximo a "match"

**Causa**: Você está usando Python 3.9 ou inferior.

**Solução**: Use `python3` ao invés de `python`:

```bash
python3 main.py
```

### Verificar qual Python está sendo usado

```bash
which python
which python3
```

### Instalar Python 3.14 (se necessário)

**macOS (usando Homebrew)**:

```bash
brew install python@3.14
```

**Linux (Ubuntu/Debian)**:

```bash
sudo apt update
sudo apt install python3.14
```

**Windows**:

1. Baixe o instalador oficial: [python.org/downloads](https://www.python.org/downloads/)
2. Execute o instalador
3. ✅ **IMPORTANTE**: Marque a opção "Add Python to PATH"
4. Clique em "Install Now"
5. Após a instalação, abra o CMD ou PowerShell e verifique:
   ```bash
   python --version
   ```

## 💾 Dados Persistentes

Todos os dados são automaticamente salvos em arquivos JSON:

- `modulos/alunos/alunos.json`
- `modulos/professores/professores.json`
- `modulos/turmas/turmas.json`
