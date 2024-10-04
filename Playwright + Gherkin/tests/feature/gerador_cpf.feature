Feature: Geração de CPF sem pontuação
         Como um usuário
         Quero gerar um CPF sem pontuação do estado "AM"
         Para verificar se o CPF gerado começa com o dígito "7"

  Scenario: Gerar CPF sem pontuação e validá-lo
    Given que estou na pagina de geracao de CPF
    When marco a opcao para nao gerar pontuacao
    And escolho o estado de origem com "AM" e clico no botao "GERAR CPF"
    Then o CPF gerado deve comecar com "7"