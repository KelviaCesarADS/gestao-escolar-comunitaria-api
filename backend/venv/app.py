from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app) 

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) 
ALUNOS_FILE = os.path.join(BASE_DIR, 'modulos', 'alunos', 'alunos.json')
PROFESSORES_FILE = os.path.join(BASE_DIR, 'modulos', 'professores', 'professores.json')
TURMAS_FILE = os.path.join(BASE_DIR, 'modulos', 'turmas', 'turmas.json')

def carregar_json(arquivo):
    """Carrega dados de um arquivo JSON"""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_json(arquivo, dados):
    """Salva dados em um arquivo JSON"""
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

@app.route('/api/alunos', methods=['GET'])
def listar_alunos():
    """Lista todos os alunos"""
    alunos = carregar_json(ALUNOS_FILE)
    return jsonify(alunos), 200

@app.route('/api/alunos/<int:matricula>', methods=['GET'])
def buscar_aluno(matricula):
    """Busca um aluno por matrícula"""
    alunos = carregar_json(ALUNOS_FILE)
    aluno = next((a for a in alunos if a['Matricula'] == matricula), None)
    
    if aluno:
        return jsonify(aluno), 200
    return jsonify({"erro": "Aluno não encontrado"}), 404

@app.route('/api/alunos', methods=['POST'])
def adicionar_aluno():
    """Adiciona um novo aluno"""
    dados = request.json
    alunos = carregar_json(ALUNOS_FILE)
    
    if alunos:
        proxima_matricula = max(a['Matricula'] for a in alunos) + 1
    else:
        proxima_matricula = 1
    
    novo_aluno = {
        "Matricula": proxima_matricula,
        "Nome": dados.get('Nome'),
        "Idade": dados.get('Idade'),
        "Genero": dados.get('Genero'),
        "Curso": dados.get('Curso'),
        "Periodo": dados.get('Periodo')
    }
    
    alunos.append(novo_aluno)
    salvar_json(ALUNOS_FILE, alunos)
    
    return jsonify(novo_aluno), 201

@app.route('/api/alunos/<int:matricula>', methods=['PUT'])
def atualizar_aluno(matricula):
    """Atualiza dados de um aluno"""
    dados = request.json
    alunos = carregar_json(ALUNOS_FILE)
    
    aluno = next((a for a in alunos if a['Matricula'] == matricula), None)
    
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    if 'Nome' in dados:
        aluno['Nome'] = dados['Nome']
    if 'Idade' in dados:
        aluno['Idade'] = dados['Idade']
    if 'Genero' in dados:
        aluno['Genero'] = dados['Genero']
    if 'Curso' in dados:
        aluno['Curso'] = dados['Curso']
    if 'Periodo' in dados:
        aluno['Periodo'] = dados['Periodo']
    
    salvar_json(ALUNOS_FILE, alunos)
    return jsonify(aluno), 200

@app.route('/api/alunos/<int:matricula>', methods=['DELETE'])
def excluir_aluno(matricula):
    """Exclui um aluno"""
    alunos = carregar_json(ALUNOS_FILE)
    
    aluno = next((a for a in alunos if a['Matricula'] == matricula), None)
    
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    
    alunos.remove(aluno)
    salvar_json(ALUNOS_FILE, alunos)
    
    return jsonify({"mensagem": f"Aluno {aluno['Nome']} excluído com sucesso"}), 200

@app.route('/api/alunos/buscar', methods=['GET'])
def buscar_alunos():
    """Busca alunos por nome ou matrícula"""
    termo = request.args.get('termo', '').lower()
    alunos = carregar_json(ALUNOS_FILE)
    
    resultados = [
        a for a in alunos 
        if termo in a['Nome'].lower() or termo in str(a['Matricula'])
    ]
    
    return jsonify(resultados), 200

@app.route('/api/alunos/relatorio', methods=['GET'])
def relatorio_alunos():
    """Gera relatório dos alunos"""
    alunos = carregar_json(ALUNOS_FILE)
    
    if not alunos:
        return jsonify({
            "total": 0,
            "media_idade": 0,
            "cursos": {}
        }), 200
    
    total = len(alunos)
    idades = [int(a['Idade']) for a in alunos]
    media_idade = sum(idades) / total
    
    # Contagem por curso
    cursos = {}
    for aluno in alunos:
        curso = aluno['Curso']
        cursos[curso] = cursos.get(curso, 0) + 1
    
    return jsonify({
        "total": total,
        "media_idade": round(media_idade, 1),
        "cursos": cursos
    }), 200

@app.route('/api/professores', methods=['GET'])
def listar_professores():
    """Lista todos os professores"""
    professores = carregar_json(PROFESSORES_FILE)
    return jsonify(professores), 200

@app.route('/api/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    """Busca um professor por ID"""
    professores = carregar_json(PROFESSORES_FILE)
    
    if 0 <= id < len(professores):
        return jsonify(professores[id]), 200
    return jsonify({"erro": "Professor não encontrado"}), 404

@app.route('/api/professores', methods=['POST'])
def adicionar_professor():
    """Adiciona um novo professor"""
    dados = request.json
    professores = carregar_json(PROFESSORES_FILE)
    
    novo_professor = {
        "nome": dados.get('nome'),
        "turno": dados.get('turno'),
        "materia": dados.get('materia')
    }
    
    professores.append(novo_professor)
    salvar_json(PROFESSORES_FILE, professores)
    
    return jsonify(novo_professor), 201

@app.route('/api/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    """Atualiza dados de um professor"""
    dados = request.json
    professores = carregar_json(PROFESSORES_FILE)
    
    if id < 0 or id >= len(professores):
        return jsonify({"erro": "Professor não encontrado"}), 404
    
    professor = professores[id]
    
    if 'nome' in dados:
        professor['nome'] = dados['nome']
    if 'turno' in dados:
        professor['turno'] = dados['turno']
    if 'materia' in dados:
        professor['materia'] = dados['materia']
    
    salvar_json(PROFESSORES_FILE, professores)
    return jsonify(professor), 200

@app.route('/api/professores/<int:id>', methods=['DELETE'])
def excluir_professor(id):
    """Exclui um professor"""
    professores = carregar_json(PROFESSORES_FILE)
    
    if id < 0 or id >= len(professores):
        return jsonify({"erro": "Professor não encontrado"}), 404
    
    professor_removido = professores.pop(id)
    salvar_json(PROFESSORES_FILE, professores)
    
    return jsonify({"mensagem": f"Professor {professor_removido['nome']} excluído com sucesso"}), 200


@app.route('/api/turmas', methods=['GET'])
def listar_turmas():
    """Lista todas as turmas"""
    turmas = carregar_json(TURMAS_FILE)
    return jsonify(turmas), 200

@app.route('/api/turmas/<int:cod_turma>', methods=['GET'])
def buscar_turma(cod_turma):
    """Busca uma turma por código"""
    turmas = carregar_json(TURMAS_FILE)
    turma = next((t for t in turmas if t['cod_turma'] == cod_turma), None)
    
    if turma:
        return jsonify(turma), 200
    return jsonify({"erro": "Turma não encontrada"}), 404

@app.route('/api/turmas', methods=['POST'])
def adicionar_turma():
    """Adiciona uma nova turma"""
    dados = request.json
    turmas = carregar_json(TURMAS_FILE)
    
    # Gera próximo código
    if turmas:
        proximo_codigo = max(t['cod_turma'] for t in turmas) + 1
    else:
        proximo_codigo = 1
    
    nova_turma = {
        "cod_turma": proximo_codigo,
        "periodo": dados.get('periodo'),
        "sala": dados.get('sala'),
        "turno": dados.get('turno'),
        "capacidade": dados.get('capacidade')
    }
    
    turmas.append(nova_turma)
    salvar_json(TURMAS_FILE, turmas)
    
    return jsonify(nova_turma), 201

@app.route('/api/turmas/<int:cod_turma>', methods=['PUT'])
def atualizar_turma(cod_turma):
    """Atualiza dados de uma turma"""
    dados = request.json
    turmas = carregar_json(TURMAS_FILE)
    
    turma = next((t for t in turmas if t['cod_turma'] == cod_turma), None)
    
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404
    
    if 'periodo' in dados:
        turma['periodo'] = dados['periodo']
    if 'sala' in dados:
        turma['sala'] = dados['sala']
    if 'turno' in dados:
        turma['turno'] = dados['turno']
    if 'capacidade' in dados:
        turma['capacidade'] = dados['capacidade']
    
    salvar_json(TURMAS_FILE, turmas)
    return jsonify(turma), 200

@app.route('/api/turmas/<int:cod_turma>', methods=['DELETE'])
def excluir_turma(cod_turma):
    """Exclui uma turma"""
    turmas = carregar_json(TURMAS_FILE)
    
    turma = next((t for t in turmas if t['cod_turma'] == cod_turma), None)
    
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404
    
    turmas.remove(turma)
    salvar_json(TURMAS_FILE, turmas)
    
    return jsonify({"mensagem": f"Turma {turma['periodo']} excluída com sucesso"}), 200

@app.route('/')
def index():
    """Rota raiz da API"""
    return jsonify({
        "mensagem": "API Gestão Escolar Comunitária",
        "versao": "1.0.0",
        "endpoints": {
            "alunos": "/api/alunos",
            "professores": "/api/professores",
            "turmas": "/api/turmas"
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
