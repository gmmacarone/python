class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
         # Completa este método        
        return len(self.items) == 0

    def encolar(self, item):
        # Completa este método con el ítem que corresponde
        a->) self.items.append(item)
        b->) self.items.insert(0, item)
        c->) self.items.pop(0)
        d->) self.items.remove(item)

    def desencolar(self):
        # Completa este método
        a->) return self.items.append(0)
        b->) return self.items.insert(0)
        c->) return self.items.pop(0)
        d->) return self.items.remove(0)

    def tamano(self):
        return len(self.items)
