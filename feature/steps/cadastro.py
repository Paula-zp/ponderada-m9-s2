import requests
from behave import given, when, then

API_URL = "https://api.com"

@given("um grupo de novos entregadores iniciou o processo de cadastro")
def step_impl(context):
    try:
        response = requests.get(f"{API_URL}/entregadores/cadastro/ativos")
        context.entregadores = response.json().get("total", 0)

        if context.entregadores <= 0:
            raise ValueError("Nenhum entregador iniciou o cadastro!")
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro na requisição para obter entregadores ativos: {e}")

@when("verificamos o tempo total de conclusão para cada entregador")
def step_impl(context):
    try:
        response = requests.get(f"{API_URL}/entregadores/cadastro/finalizados")

        context.tempo_conclusao = response.json().get("tempos", [])
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro na requisição para obter tempos de conclusão: {e}")

@then("pelo menos {percentual}% dos entregadores devem ter concluído o cadastro em até {tempo_limite} minutos")
def step_impl(context, percentual, tempo_limite):
    percentual = float(percentual)
    tempo_limite = int(tempo_limite)

    try:
        cadastros_concluidos = sum(1 for tempo in context.tempo_conclusao if tempo <= tempo_limite)
    
        if context.entregadores > 0:
            taxa_conclusao = (cadastros_concluidos / context.entregadores) * 100
        else:
            raise ValueError("Nenhum entregador para calcular taxa de conclusão!")
        
    except ValueError as e:
        raise Exception(f"Erro ao calcular a taxa de conclusão: {e}")  

    assert taxa_conclusao >= percentual, f"Apenas {taxa_conclusao}% concluíram dentro do tempo limite ({tempo_limite} min), esperado era {percentual}%!"
