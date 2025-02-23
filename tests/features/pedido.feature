Feature: Realizar pedido

    Scenario: Realizar pedido com sucesso
        Given que o cliente está logado
        And que o cliente está na página de produtos
        When o cliente adiciona um produto ao carrinho
        And o cliente finaliza o pedido
        Then o pedido é realizado com sucesso

    Scenario: Realizar pedido dentro do tempo esperado
        Given que o cliente está logado
        And que o cliente está na página de produtos
        When o cliente adiciona um produto ao carrinho
        And o cliente finaliza o pedido
        Then o pedido deve ser confirmado em menos de 2 segundos

