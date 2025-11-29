#!/usr/bin/env bash

echo " Iniciando Backend da Gestão Escolar..."
echo ""

cd backend

# Use venv for the virtual environment
VENV_DIR="venv"

if [ ! -f "$VENV_DIR/bin/python" ]; then
    echo " Criando ambiente virtual..."
    python3 -m venv "$VENV_DIR"
fi

echo "🔧 Usando ambiente virtual..."

echo " Instalando dependências..."
"$VENV_DIR/bin/pip" install -r requirements.txt --quiet

echo ""
echo " Backend pronto!"
echo " Servidor rodando em: http://localhost:5000"
echo ""
echo " Para parar o servidor, pressione Ctrl+C"
echo ""

"$VENV_DIR/bin/python" app.py