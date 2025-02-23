import time
import random

class Pedido:
    def __init__(self):
        self.cliente_logado = False
        self.pagina_produtos = False
        self.produto_adicionado = False
        self.pedido_realizado = False
        self.tempo_inicio = None
        self.tempo_fim = None

    def logar_cliente(self):
        self.cliente_logado = True

    def acessar_pagina_produtos(self):
        self.pagina_produtos = True

    def adicionar_produto(self):
        self.produto_adicionado = True

    def finalizar_pedido(self):
        self.tempo_inicio = time.time()
        self.pedido_realizado = random.choice([True, False])  # Simula sucesso ou falha
        self.tempo_fim = time.time()

    def tempo_pedido(self):
        return self.tempo_fim - self.tempo_inicio if self.tempo_fim and self.tempo_inicio else None


def test_realizar_pedido_com_sucesso():
    pedido = Pedido()

    pedido.logar_cliente()
    pedido.acessar_pagina_produtos()
    pedido.adicionar_produto()
    pedido.finalizar_pedido()
    
    assert pedido.pedido_realizado, "Erro: O pedido não foi realizado com sucesso."
    print("✅ Pedido realizado com sucesso!")


def test_realizar_pedido_dentro_do_tempo():
    pedido = Pedido()
    
    pedido.logar_cliente()
    pedido.acessar_pagina_produtos()
    pedido.adicionar_produto()
    pedido.finalizar_pedido()
    
    tempo_total = pedido.tempo_pedido()
    assert tempo_total is not None and tempo_total < 2, f"Erro: O pedido demorou {tempo_total:.2f} segundos, excedendo o limite."
    print(f"✅ Pedido confirmado em {tempo_total:.2f} segundos.")
