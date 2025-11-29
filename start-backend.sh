echo " Iniciando Backend da Gestão Escolar..."
echo ""

cd backend

if [ ! -d "venv" ]; then
    echo " Criando ambiente virtual..."
    python3 -m venv venv
fi

echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

echo " Instalando dependências..."
pip install -r requirements.txt --quiet

echo ""
echo " Backend pronto!"
echo " Servidor rodando em: http://localhost:5000"
echo ""
echo " Para parar o servidor, pressione Ctrl+C"
echo ""

python app.py
