import pytest
from task_manager import TaskManager

class TestTaskManager:
    def test_adicionar_tarefa(self):
        """Testa adição de nova tarefa"""
        gerenciador = TaskManager()
        tarefa = gerenciador.adicionar_tarefa("Tarefa Teste", "Descrição Teste", "alta")
        
        assert tarefa['titulo'] == "Tarefa Teste"
        assert tarefa['prioridade'] == "alta"
        assert len(gerenciador.obter_todas_tarefas()) == 1
    
    def test_excluir_tarefa(self):
        """Testa remoção de tarefa"""
        gerenciador = TaskManager()
        tarefa = gerenciador.adicionar_tarefa("Tarefa Teste", "Descrição Teste", "media")
        gerenciador.excluir_tarefa(tarefa['id'])
        
        assert len(gerenciador.obter_todas_tarefas()) == 0
    
    def test_atualizar_tarefa(self):
        """Testa atualização de tarefa"""
        gerenciador = TaskManager()
        tarefa = gerenciador.adicionar_tarefa("Título Original", "Descrição Original", "baixa")
        
        atualizada = gerenciador.atualizar_tarefa(tarefa['id'], {'titulo': 'Título Atualizado'})
        assert atualizada['titulo'] == 'Título Atualizado'
    
    def test_obter_tarefas_por_prioridade(self):
        """Testa filtro por prioridade"""
        gerenciador = TaskManager()
        gerenciador.adicionar_tarefa("Tarefa Alta", "Descrição", "alta")
        gerenciador.adicionar_tarefa("Tarefa Baixa", "Descrição", "baixa")
        
        tarefas_altas = gerenciador.obter_tarefas_por_prioridade("alta")
        assert len(tarefas_altas) == 1
        assert tarefas_altas[0]['prioridade'] == 'alta'