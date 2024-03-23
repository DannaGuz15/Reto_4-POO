class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity):
        return self.price * quantity
    
class Beverage:
    def __init__(self, name, price, size):
        self._name = name
        self._price = price
        self._size = size

    # Definir método get_price() para obtener el precio
    def get_price(self):
        return self._price

        

class Appetizer:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # Definir método get_price() para obtener el precio
    def get_price(self):
        return self._price
        
class MainCourse:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # Definir método get_price() para obtener el precio
    def get_price(self):
        return self._price

class Order:
    def __init__(self):
        self._items = []

    def add_item(self, item, quantity=1):
        self._items.append((item, quantity))

    def remove_item(self, item):
        self._items.remove(item)

    def calculate_total_price(self):
        total_price = 0
        has_main_course = False
        for item, quantity in self._items:
            if isinstance(item, MainCourse):
                has_main_course = True
            total_price += item.get_price() * quantity
        
        if has_main_course:
            for item, quantity in self._items:
                if isinstance(item, Appetizer):
                    total_price -= item.get_price() * 0.1 * quantity  # Aplicar un descuento del 10%
        
        return total_price

    
# Menu
water = Beverage("Agua", 2.5, "large")
coke = Beverage ("Sprite", 2.7, "large")
coke2 = Beverage("CocaCola", 3.0, "large")
vino = Beverage("Vino Tinto", 60.0, "large")
vino2 = Beverage("Vino Blanco", 55.0, "large")

wings = Appetizer("Alitas BBQ", 14.0)
wings2 = Appetizer("Alitas bufalo", 15.5)
wings3 = Appetizer("Alitas rellenas", 18.2)
wings4 = Appetizer("Alitas Ranch", 12.5)

pasta = MainCourse("Pasta Carbonara", 25.2)
pasta2 = MainCourse("Pasta Pesto", 24.0)
pasta3 = MainCourse("Pasta Boloñesa", 25.5)
pasta4 = MainCourse("Pasta con camarones", 26.0)  


my_order = Order ()
my_order.add_item(coke2, 2)
my_order.add_item(coke, 1)
my_order.add_item(wings, 3)
my_order.add_item(pasta, 1)
my_order.add_item(pasta3, 2)
total_amount = my_order.calculate_total_price()


print(f"Total bill amount: ${total_amount:.2f}")

class MedioPago:
  def __init__(self):
    pass

  def pagar(self, total_amount):
    raise NotImplementedError("Subclases deben implementar pagar()")

class Tarjeta(MedioPago):
  def __init__(self, numero, cvv):
    super().__init__()
    self.numero = numero
    self.cvv = cvv

  def pagar(self, total_amount):
    print(f"Pagando {total_amount} con tarjeta {self.numero[-4:]}")

class Efectivo(MedioPago):
  def __init__(self, monto_entregado):
    super().__init__()
    self.monto_entregado = monto_entregado

  def pagar(self, total_amount):
    if self.monto_entregado >= total_amount:
      print(f"Pago realizado en efectivo. Cambio: {self.monto_entregado - total_amount}")
    else:
      print(f"Fondos insuficientes. Faltan {total_amount - self.monto_entregado} para completar el pago.")

 #Ejemplo de uso
pago1 = Tarjeta("1234567890123456", 123)
pago2 = Efectivo(total_amount)

pago1.pagar(56)
pago2.pagar(74)



