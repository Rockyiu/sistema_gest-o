import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis do universo
Lucro_Liquido_Trimestral = ctrl.Antecedent(np.arange(0, 11, 1), 'Lucro_Liquido_Trimestral')
Nivel_Satisfacao_Cliente = ctrl.Antecedent(np.arange(0, 11, 1), 'Nivel_Satisfacao_Cliente')
Eficiencia_Operacional = ctrl.Antecedent(np.arange(0, 11, 1), 'Eficiencia_Operacional')
Numero_Novos_Clientes = ctrl.Antecedent(np.arange(0, 11, 1), 'Numero_Novos_Clientes')
Desempenho = ctrl.Consequent(np.arange(0, 26, 1), 'Desempenho')

# Definindo as funções de pertinência
Lucro_Liquido_Trimestral['poor'] = fuzz.trimf(Lucro_Liquido_Trimestral.universe, [0, 0, 5])
Lucro_Liquido_Trimestral['average'] = fuzz.trimf(Lucro_Liquido_Trimestral.universe, [0, 5, 10])
Lucro_Liquido_Trimestral['good'] = fuzz.trimf(Lucro_Liquido_Trimestral.universe, [5, 10, 10])

Nivel_Satisfacao_Cliente['poor'] = fuzz.trimf(Nivel_Satisfacao_Cliente.universe, [0, 0, 5])
Nivel_Satisfacao_Cliente['average'] = fuzz.trimf(Nivel_Satisfacao_Cliente.universe, [0, 5, 10])
Nivel_Satisfacao_Cliente['good'] = fuzz.trimf(Nivel_Satisfacao_Cliente.universe, [5, 10, 10])

Eficiencia_Operacional['poor'] = fuzz.trimf(Eficiencia_Operacional.universe, [0, 0, 5])
Eficiencia_Operacional['average'] = fuzz.trimf(Eficiencia_Operacional.universe, [0, 5, 10])
Eficiencia_Operacional['good'] = fuzz.trimf(Eficiencia_Operacional.universe, [5, 10, 10])

Numero_Novos_Clientes['poor'] = fuzz.trimf(Numero_Novos_Clientes.universe, [0, 0, 5])
Numero_Novos_Clientes['average'] = fuzz.trimf(Numero_Novos_Clientes.universe, [0, 5, 10])
Numero_Novos_Clientes['good'] = fuzz.trimf(Numero_Novos_Clientes.universe, [5, 10, 10])

Desempenho['ruim'] = fuzz.trimf(Desempenho.universe, [0, 0, 13])
Desempenho['bom'] = fuzz.trimf(Desempenho.universe, [0, 13, 25])
Desempenho['muito bom'] = fuzz.trimf(Desempenho.universe, [13, 25, 25])


# Definindo as regras
regra1 = ctrl.Rule(Lucro_Liquido_Trimestral['good'] & Nivel_Satisfacao_Cliente['good'], Desempenho['muito bom'])
regra2 = ctrl.Rule(Eficiencia_Operacional['poor'] | Numero_Novos_Clientes['poor'], Desempenho['ruim'])
regra3 = ctrl.Rule(Lucro_Liquido_Trimestral['average'] & Nivel_Satisfacao_Cliente['average'], Desempenho['bom'])
regra4 = ctrl.Rule(Eficiencia_Operacional['average'] | Numero_Novos_Clientes['average'], Desempenho['bom'])

# Criando e simulando um controlador fuzzy
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3, regra4])
simulacao = ctrl.ControlSystemSimulation(sistema_controle)

# Definindo um conjunto de casos de teste
casos_teste = [
    {'Lucro_Liquido_Trimestral': 6.5, 'Nivel_Satisfacao_Cliente': 9.8, 'Eficiencia_Operacional': 4.2, 'Numero_Novos_Clientes': 9.1},
    {'Lucro_Liquido_Trimestral': 5.0, 'Nivel_Satisfacao_Cliente': 5.0, 'Eficiencia_Operacional': 5.0, 'Numero_Novos_Clientes': 5.0},
    {'Lucro_Liquido_Trimestral': 2.5, 'Nivel_Satisfacao_Cliente': 2.5, 'Eficiencia_Operacional': 2.5, 'Numero_Novos_Clientes': 2.5},
    # Adicione mais casos de teste conforme necessário
]
#Métricas para avaliar o desempenho de uma empresa:
    #Ruim: 0 - 8;
    #Médio: 9 - 16;
    #Bom: 17 - 25;
# Executando os casos de teste
for i, caso_teste in enumerate(casos_teste):
    simulacao.input['Lucro_Liquido_Trimestral'] = caso_teste['Lucro_Liquido_Trimestral']
    simulacao.input['Nivel_Satisfacao_Cliente'] = caso_teste['Nivel_Satisfacao_Cliente']
    simulacao.input['Eficiencia_Operacional'] = caso_teste['Eficiencia_Operacional']
    simulacao.input['Numero_Novos_Clientes'] = caso_teste['Numero_Novos_Clientes']

    # Computando o desempenho
    simulacao.compute()

    # Imprimindo o resultado
    print(f"Caso de teste {i+1}: {simulacao.output['Desempenho']}")
