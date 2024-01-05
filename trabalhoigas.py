import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir as variáveis
desempenho_financeiro = ctrl.Antecedent(np.arange(0, 101, 1), 'desempenho_financeiro')
satisfacao_cliente = ctrl.Antecedent(np.arange(0, 101, 1), 'satisfacao_cliente')
eficiencia_operacional = ctrl.Antecedent(np.arange(0, 101, 1), 'eficiencia_operacional')
inovacao_crescimento = ctrl.Antecedent(np.arange(0, 101, 1), 'inovacao_crescimento')

tomar_medidas_corretivas = ctrl.Consequent(np.arange(0, 101, 1), 'tomar_medidas_corretivas')
aumentar_investimentos = ctrl.Consequent(np.arange(0, 101, 1), 'aumentar_investimentos')

# Mapear características para conjuntos difusos
desempenho_financeiro['baixo'] = fuzz.trimf(desempenho_financeiro.universe, [0, 0, 50])
desempenho_financeiro['medio'] = fuzz.trimf(desempenho_financeiro.universe, [0, 50, 100])
desempenho_financeiro['alto'] = fuzz.trimf(desempenho_financeiro.universe, [50, 100, 100])

satisfacao_cliente['baixa'] = fuzz.trimf(satisfacao_cliente.universe, [0, 0, 50])
satisfacao_cliente['media'] = fuzz.trimf(satisfacao_cliente.universe, [0, 50, 100])
satisfacao_cliente['alta'] = fuzz.trimf(satisfacao_cliente.universe, [50, 100, 100])

eficiencia_operacional['baixa'] = fuzz.trimf(eficiencia_operacional.universe, [0, 0, 50])
eficiencia_operacional['media'] = fuzz.trimf(eficiencia_operacional.universe, [0, 50, 100])
eficiencia_operacional['alta'] = fuzz.trimf(eficiencia_operacional.universe, [50, 100, 100])

inovacao_crescimento['baixo'] = fuzz.trimf(inovacao_crescimento.universe, [0, 0, 50])
inovacao_crescimento['medio'] = fuzz.trimf(inovacao_crescimento.universe, [0, 50, 100])
inovacao_crescimento['alto'] = fuzz.trimf(inovacao_crescimento.universe, [50, 100, 100])

tomar_medidas_corretivas['baixo'] = fuzz.trimf(tomar_medidas_corretivas.universe, [0, 0, 50])
tomar_medidas_corretivas['medio'] = fuzz.trimf(tomar_medidas_corretivas.universe, [0, 50, 100])
tomar_medidas_corretivas['alto'] = fuzz.trimf(tomar_medidas_corretivas.universe, [50, 100, 100])

aumentar_investimentos['baixo'] = fuzz.trimf(aumentar_investimentos.universe, [0, 0, 50])
aumentar_investimentos['medio'] = fuzz.trimf(aumentar_investimentos.universe, [0, 50, 100])
aumentar_investimentos['alto'] = fuzz.trimf(aumentar_investimentos.universe, [50, 100, 100])

# Definir regras
rule1 = ctrl.Rule(desempenho_financeiro['baixo'] & eficiencia_operacional['baixa'],
                  tomar_medidas_corretivas['alto'])

rule2 = ctrl.Rule(satisfacao_cliente['alta'] & inovacao_crescimento['alto'],
                  aumentar_investimentos['alto'])

# Adicionar mais regras conforme necessário

# Criar o sistema de controle
sistema_controle = ctrl.ControlSystem([rule1, rule2])

# Simular o sistema de controle
simulador = ctrl.ControlSystemSimulation(sistema_controle)

# Definir entradas
simulador.input['desempenho_financeiro'] = 30
simulador.input['satisfacao_cliente'] = 80
simulador.input['eficiencia_operacional'] = 20
simulador.input['inovacao_crescimento'] = 70

# Computar a saída
simulador.compute()

# Exibir resultados
print("Tomar Medidas Corretivas:", simulador.output['tomar_medidas_corretivas'])
print("Aumentar Investimentos:", simulador.output['aumentar_investimentos'])
