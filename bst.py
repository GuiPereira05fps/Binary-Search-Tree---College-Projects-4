import networkx as nx
import matplotlib.pyplot as pt

class Node:
    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade
        self.left = None
        self.right = None

    def insert(self, idade, nome):
        newNode = (idade, nome)
        currentNode = (self.idade, self.nome)

        if newNode < currentNode:
            if self.left is None:
                self.left = Node(idade, nome)
            else:
                self.left.insert(idade, nome)

        elif newNode > currentNode or newNode == currentNode:
            if self.right is None:
                self.right = Node(idade, nome)
            else:
                self.right.insert(idade, nome)

raiz = Node(20, "Raíssa")
raiz.insert(10, "Pedro")
raiz.insert(10, "Sabrina")
raiz.insert(10, "Sabrina")



print(raiz.left.right.right.nome)