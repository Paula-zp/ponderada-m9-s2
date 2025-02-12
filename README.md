# Documentação e Validação de Requisitos de Negócio em Código

## Direcionadores de Negócio

Cada uma das regras de negócio selecionadas tem como objetivo melhorar a experiência do entregador e garantir a eficácia do processo. A tabela abaixo resume a dor associada a cada regra, a descrição da regra e o indicador de conformidade para garantir que a operação esteja alinhada com os objetivos de negócios:

| **Dor**                                       | **Regra de Negócio**                                                                 | **Indicador de Conformidade**                                                              | **Condição de Sucesso**                                                                 | **Critério de Aceitação** |
|-----------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------|
| **Retenção de entregadores no onboarding**    | Entregadores que aceitam o primeiro pedido devem completar ao menos 20 pedidos em até 8 dias. | Taxa de retenção de entregadores | Pelo menos 50% dos entregadores que iniciaram o onboarding devem completar 20 pedidos dentro de 8 dias. (Estimativa de exemplo) | Testes automatizados confirmam que a métrica de retenção atinge ou supera 50% no período analisado. |
| **Tempo de onboarding elevado**               | O tempo de cadastro dos entregadores deve ser otimizado para permitir que eles comecem a trabalhar rapidamente. | Percentual de entregadores que completam o onboarding dentro de um tempo limite estabelecido. | Pelo menos 90% dos entregadores devem concluir o onboarding dentro do tempo limite estipulado. (Estimativa de exemplo) | Testes automatizados verificam que a taxa de conclusão do onboarding atinge ou supera a porcentagem definida dentro do tempo estipulado. |

### Taxa de Retenção de Entregadores
A taxa de retenção de entregadores no onboarding deve ser calculada com base na porcentagem de entregadores que completam pelo menos X pedidos no prazo de X dias após aceitarem o primeiro pedido.

Esse cenário pode ocorrer devido a possível falta de incentivos aos RTs, baixa previsibilidade de ganho, dificuldades nos primeiros passos na plataforma ou problemas com suporte durante o onboarding e lentidão do sistema. 

O impacto de uma baixa taxa de retenção de entregadores pode ser crucial nas atividades da Rappi, uma vez que resilta em um maior custo para a captação de novos entregadores e na falta de disponibilidade de entregadores para atender a demanda. Esses fatores podem resultar em uma experiência ruim para os usuários e na perda de oportunidades de negócio.

#### Cenário de teste (BDD)
```
Feature: Taxa de Retenção de Entregadores

  Scenario Outline: Verificar taxa de retenção de entregadores
    Given um grupo de entregadores aceitou o primeiro pedido
    When verificamos quantos completaram pelo menos <min_pedidos> pedidos em até <periodo>
    Then pelo menos <taxa_esperada>% dos entregadores devem ter atingido essa meta
```

#### Testes Implementados:
O teste verifica quantos entregadores completaram o número mínimo de pedidos dentro do período estabelecido (exemplo: 20 pedidos em 8 dias). Para isso, é considerado o número de entregadores que aceitaram o primeiro pedido e o número desses RTs que conseguiram alcançar a meta de onboarding dentro do período estipulado. O resultado esperado é que a taxa de retenção seja igual ou superior à taxa esperada (50%).


### Tempo de Cadastro

O tempo de cadastro dos entregadores é o período necessário para que eles completem o processo de registro na plataforma e consigam realizar as primeiras entregas. O objetivo é que uma alta porcentagem de entregadores finalize esse processo rapidamente para conseguir começar a trabalhar na plataforma.

O tempo de cadastro elevado pode ser causado por um processo de registro complexo, falta de clareza nas instruções, suporte ineficiente e lentidão do sistema ou da verificação de documentos. 

Esse cenário pode impactar negativamente a experiência do entregador, pois ele pode desistir de se cadastrar na plataforma e procurar outras oportunidades de trabalho, aumentando a taxa de churn. Dessa forma, a disponibilidade de entregadores pode ser afetada, resultando em atrasos nas entregas, principalmente durante alta demanda, e na insatisfação dos usuários.

#### Cenário de teste (BDD)
```
Feature: Tempo de Cadastro dos Entregadores

  Scenario Outline: Verificar tempo médio de onboarding
    Given um grupo de novos entregadores iniciou o processo de cadastro
    When verificamos o tempo total de conclusão para cada entregador
    Then pelo menos <percentual>% dos entregadores devem ter concluído o cadastro em até <tempo_limite> minutos
```

#### Testes Implementados
O teste verifica o tempo total de conclusão do cadastro para cada entregador, garantindo que não existam atrasos significativos no processo. Para isso, é considerado o tempo em que o cadastro foi iniciado e o tempo em que foi concluído por cada entregador, comparando com uma média de tempo considerada normal para o fluxo. O resultado esperado é que pelo menos 90% dos entregadores tenham concluído o cadastro dentro do tempo limite estabelecido.


## Validação de Requisitos de Negócio

Os testes foram projetados para simular a validação de uma regra de negócio chamando uma API inexistente, resultando na reprovação dos cenários. No entanto, toda a lógica foi construída pensando em um cenário real, onde a chamada para a API seria realizada com sucesso, obtendo os dados que foram simulados no teste e a validação correta das regras de negócio.