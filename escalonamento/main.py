import escalonamento_tarefas as EscalonamentoTarefas

custos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

(escalonamento, custo) = EscalonamentoTarefas.encontre_escalonamento_minimo(custos)
print(f'Escalonamento: {escalonamento}\nCusto mínimo: {custo}')
for i in range(len(escalonamento)):
    print(f'Pessoa #{i}: tarefa #{escalonamento[i]}')
