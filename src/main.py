from flask import Flask, jsonify, request
from task_manager import TaskManager

app = Flask(__name__)
gerenciador_tarefas = TaskManager()

# Adicionar algumas tarefas de exemplo
gerenciador_tarefas.adicionar_tarefa("Reunião de Sprint", "Planejamento semanal da equipe", "alta")
gerenciador_tarefas.adicionar_tarefa("Documentar API", "Criar documentação dos endpoints", "media")

@app.route('/')
def home():
    return jsonify({
        "mensagem": "Bem-vindo ao TaskMind API",
        "versao": "1.0.0",
        "endpoints": {
            "obter_tarefas": "GET /tarefas",
            "criar_tarefa": "POST /tarefas",
            "atualizar_tarefa": "PUT /tarefas/<id>",
            "excluir_tarefa": "DELETE /tarefas/<id>"
        }
    })

@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    """Retorna todas as tarefas"""
    return jsonify(gerenciador_tarefas.obter_todas_tarefas())

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    """Cria nova tarefa"""
    dados = request.json
    
    if not dados or 'titulo' not in dados:
        return jsonify({"erro": "Título é obrigatório"}), 400
    
    tarefa = gerenciador_tarefas.adicionar_tarefa(
        titulo=dados['titulo'],
        descricao=dados.get('descricao', ''),
        prioridade=dados.get('prioridade', 'media')
    )
    return jsonify(tarefa), 201

@app.route('/tarefas/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    """Atualiza tarefa existente"""
    dados = request.json
    tarefa = gerenciador_tarefas.atualizar_tarefa(tarefa_id, dados)
    
    if tarefa:
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
def excluir_tarefa(tarefa_id):
    """Remove tarefa"""
    gerenciador_tarefas.excluir_tarefa(tarefa_id)
    return '', 204

@app.route('/tarefas/prioridade/<string:prioridade>', methods=['GET'])
def obter_tarefas_por_prioridade(prioridade):
    """Filtra tarefas por prioridade"""
    prioridades_validas = ['baixa', 'media', 'alta']
    if prioridade not in prioridades_validas:
        return jsonify({"erro": "Prioridade inválida"}), 400
    
    tarefas = gerenciador_tarefas.obter_tarefas_por_prioridade(prioridade)
    return jsonify(tarefas)

if __name__ == '__main__':
    app.run(debug=True, port=5000)