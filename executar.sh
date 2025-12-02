echo "🔍 Verificando versão do Python..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Python 3 não encontrado!"
    echo "Por favor, instale Python 3.10 ou superior"
    exit 1
fi

echo "🚀 Iniciando Sistema de Gestão Escolar Comunitária..."
python3 main.py