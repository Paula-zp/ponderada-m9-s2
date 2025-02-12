Feature: Tempo de Onboarding dos Entregadores

  Scenario Outline: Verificar tempo médio de cadastro
    Given um grupo de novos entregadores iniciou o processo de cadastro
    When verificamos o tempo total de conclusão para cada entregador
    Then pelo menos <percentual>% dos entregadores devem ter concluído o cadastro em até <tempo_limite> minutos

  Examples:
    | percentual | tempo_limite |
    | 90        | X           |
