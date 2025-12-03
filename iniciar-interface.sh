echo " Iniciando Interface da Gestão Escolar..."
echo ""

cd interface

echo " Interface pronta!"
echo " Servidor rodando em: http://localhost:8000"
echo ""
echo " Para parar o servidor, pressione Ctrl+C"
echo ""

python3 -m http.server 8000
