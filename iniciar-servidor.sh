#!/usr/bin/env bash

echo " Iniciando servidor da Gestão Escolar..."
echo ""

OS_NAME="$(uname -s)"
if [ "$OS_NAME" = "Linux" ]; then
    if [ -f "/etc/debian_version" ]; then
        dpkg -s python3-venv &> /dev/null
        VENV_OK=$?
        dpkg -s python3-pip &> /dev/null
        PIP_OK=$?
        if [ $VENV_OK -ne 0 ] || [ $PIP_OK -ne 0 ]; then
            echo "[INFO] Dependências do sistema não encontradas:"
            if [ $VENV_OK -ne 0 ]; then
                echo "  - python3-venv"
            fi
            if [ $PIP_OK -ne 0 ]; then
                echo "  - python3-pip"
            fi
            echo "Deseja instalar automaticamente? (requer sudo) [s/N]"
            read -r INSTALAR
            if [ "$INSTALAR" = "s" ] || [ "$INSTALAR" = "S" ]; then
                sudo apt update
                sudo apt install -y python3-venv python3-pip
            else
                echo "Instale manualmente com: sudo apt install python3-venv python3-pip"
                exit 1
            fi
        fi
    fi
fi

cd servidor

VENV_DIR="venv"

if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python3 não está instalado. Instale o Python 3 antes de continuar."
    exit 1
fi

python3 -m venv --help &> /dev/null
if [ $? -ne 0 ]; then
    echo "[ERRO] O módulo 'venv' não está disponível."
    echo "No Linux, instale com: sudo apt install python3-venv"
    echo "No MacOS, instale o Python pelo site oficial: https://www.python.org/downloads/"
    exit 1
fi

if [ ! -f "$VENV_DIR/bin/python" ]; then
    echo " Criando ambiente virtual..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "[ERRO] Falha ao criar o ambiente virtual. Veja as mensagens acima."
        exit 1
    fi
fi

echo "Usando ambiente virtual..."


if [ ! -f "$VENV_DIR/bin/pip" ]; then
    echo "[INFO] pip não encontrado no ambiente virtual. Tentando instalar com ensurepip..."
    "$VENV_DIR/bin/python" -m ensurepip --upgrade
    "$VENV_DIR/bin/python" -m pip install --upgrade pip
    if [ ! -f "$VENV_DIR/bin/pip" ]; then
        echo "[ERRO] O pip não foi encontrado ou não pôde ser instalado no ambiente virtual."
        echo "Verifique se o Python está completo (com ensurepip) ou instale manualmente."
        exit 1
    fi
fi

echo " Instalando dependências..."
"$VENV_DIR/bin/pip" install -r requisitos.txt --quiet
if [ $? -ne 0 ]; then
    echo "[ERRO] Falha ao instalar dependências. Veja as mensagens acima."
    exit 1
fi

echo " Servidor pronto!"
echo " Servidor rodando em: http://localhost:5000"
echo ""
echo " Para parar o servidor, pressione Ctrl+C"
echo ""

"$VENV_DIR/bin/python" app.py