from behave import given, when, then
import time
import random

@given("que o cliente está logado")
def step_cliente_logado(context):
    context.cliente_logado = True
    print("Cliente logado com sucesso.")

@given("que o cliente está na página de produtos")
def step_cliente_na_pagina_produtos(context):
    context.pagina_produtos = True
    print("Cliente na página de produtos.")

@when("o cliente adiciona um produto ao carrinho")
def step_adiciona_produto(context):
    context.produto_adicionado = True
    print("Produto adicionado ao carrinho.")

@when("o cliente finaliza o pedido")
def step_finaliza_pedido(context):
    context.tempo_inicio = time.time()
    context.pedido_realizado = random.choice([True, False])  
    context.tempo_fim = time.time()
    print("Pedido finalizado.")

@then("o pedido é realizado com sucesso")
def step_verifica_pedido_sucesso(context):
    assert context.pedido_realizado, "Erro: O pedido não foi realizado com sucesso."
    print("Pedido realizado com sucesso!")

@then("o pedido deve ser confirmado em menos de 2 segundos")
def step_verifica_tempo_pedido(context):
    tempo_total = context.tempo_fim - context.tempo_inicio
    assert tempo_total < 2, f"Erro: O pedido demorou {tempo_total:.2f} segundos, excedendo o limite."
    print(f"Pedido confirmado em {tempo_total:.2f} segundos.")
