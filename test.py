from abc import ABC, abstractmethod

# Strategy Pattern: Cálculo de desconto

class DescontoStrategy(ABC):
    @abstractmethod
    def aplicar(self, total: float) -> float:
        pass

class SemDesconto(DescontoStrategy):
    def aplicar(self, total: float) -> float:
        return total

class DescontoPorcentagem(DescontoStrategy):
    def aplicar(self, total: float) -> float:
        return total * 0.9

class DescontoFixo(DescontoStrategy):
    def aplicar(self, total: float) -> float:
        return total - 20 if total >= 20 else 0

# Classe Produto

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

# Classe Carrinho de Compras

class Carrinho:
    def __init__(self):
        self.produtos = []
        self.desconto = SemDesconto()

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def definir_desconto(self, estrategia: DescontoStrategy):
        self.desconto = estrategia

    def total_sem_desconto(self) -> float:
        return sum(p.preco for p in self.produtos)

    def total_com_desconto(self) -> float:
        total = self.total_sem_desconto()
        return self.desconto.aplicar(total)

    def imprimir_recibo(self):
        print("Recibo de Compra:")
        for p in self.produtos:
            print(f"{p.nome}: R${p.preco:.2f}")
        print(f"Total: R${self.total_com_desconto():.2f}")

# Uso
carrinho = Carrinho()
carrinho.adicionar_produto(Produto("Camiseta", 50))
carrinho.adicionar_produto(Produto("Calça", 100))
carrinho.adicionar_produto(Produto("Tênis", 200))

# Aplicar desconto percentual

carrinho.definir_desconto(DescontoPorcentagem())
carrinho.imprimir_recibo()