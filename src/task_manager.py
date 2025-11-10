class TaskManager:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1
    
    def adicionar_tarefa(self, titulo, descricao, prioridade='media'):
        """Adiciona nova tarefa ao sistema"""
        tarefa = {
            'id': self.proximo_id,
            'titulo': titulo,
            'descricao': descricao,
            'prioridade': prioridade,
            'status': 'pendente',
            'criado_em': '2024-11-15'
        }
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        return tarefa
    
    def obter_todas_tarefas(self):
        """Retorna todas as tarefas"""
        return self.tarefas
    
    def obter_tarefa_por_id(self, tarefa_id):
        """Busca tarefa por ID"""
        for tarefa in self.tarefas:
            if tarefa['id'] == tarefa_id:
                return tarefa
        return None
    
    def atualizar_tarefa(self, tarefa_id, atualizacoes):
        """Atualiza tarefa existente"""
        tarefa = self.obter_tarefa_por_id(tarefa_id)
        if tarefa:
            tarefa.update(atualizacoes)
            return tarefa
        return None
    
    def excluir_tarefa(self, tarefa_id):
        """Remove tarefa do sistema"""
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa['id'] != tarefa_id]
    
    def obter_tarefas_por_prioridade(self, prioridade):
        """Filtra tarefas por prioridade"""
        return [tarefa for tarefa in self.tarefas if tarefa['prioridade'] == prioridade]