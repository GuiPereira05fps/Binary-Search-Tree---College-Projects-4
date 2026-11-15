import networkx as nx

class Node:
    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade
        self.left = None
        self.right = None

    #nodes com idades iguais e nomes diferentes são inseridos de acordo com ordem alfabética.
    #letras menores para a esquerda, letras maiores para a direita.
    #nodes 100% iguais são alocados sempre à direita
    def insert(self, idade, nome):
        newNode = (idade, nome) #permite a verificação individual das idades e nomes em ordem alfabética.
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

    #in_order
    def travessia_inorder(self):
        if self.left:
            self.left.travessia_inorder()
        print(self.nome, "|", self.idade, "anos")
        
        if self.right:
            self.right.travessia_inorder()
            
    #in_order_reverse
    def travessia_inorder_reversa(self):        
        if self.right:
            self.right.travessia_inorder_reversa()
        print(self.nome, "|", self.idade, "anos")
    
        if self.left:
            self.left.travessia_inorder_reversa()
            
    #pre_order
    def travessia_preorder(self):
        print(self.nome, "|", self.idade, "anos")
        if self.left:
           self.left.travessia_preorder()
           
        if self.right:
           self.right.travessia_preorder()
           
    #post_order
    def travessia_postorder(self):
        if self.left:
           self.left.travessia_postorder()
           
        if self.right:
           self.right.travessia_postorder()
        
        print(self.nome, "|", self.idade, "anos")
        
#grafo criado para permitir implementação de BFS
def BT_para_grafo(root):
    grafo = nx.DiGraph()
    
    def insert_node(node):

        grafo.add_node(node, idade=node.idade, nome=node.nome)
        
        if node.left is not None:
            grafo.add_edge(node, node.left)
            insert_node(node.left)
            
        if node.right is not None:
            grafo.add_edge(node, node.right)
            insert_node(node.right)

    insert_node(root)
    return grafo

root = Node(35, "Rubem")
root.insert(61, "Evaristo")
root.insert(22, "Monica")
root.insert(16, "Tamires")
root.insert(50, "Cezar")
root.insert(43, "Álvaro")
root.insert(70, "Cleusa")
root.insert(60, "Quitéria")
root.insert(48, "Raul")
root.insert(33, "Juliana")

print("Travessia em Ordem:")
root.travessia_inorder()

print("\n\nTravessia Pré-Ordem:")
root.travessia_preorder()

print("\n\nTravessia Pós-Ordem:")
root.travessia_postorder()

print("\n\nTravessia em Ordem Inversa:")
root.travessia_inorder_reversa()

grafo = BT_para_grafo(root)
print("\n\nPercurso em Largura")
print(root.nome, "|" , root.idade, "anos")
for node_atual, node_seguinte in nx.bfs_edges(grafo, source=root):
    print(node_seguinte.nome, "|" , node_seguinte.idade, "anos")