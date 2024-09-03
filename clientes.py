class Cliente:
    def __init__(self, nombre, correo, direccion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"Dirección actualizada a: {self.direccion}")

    def realizar_compra(self):
        print(f"{self.nombre} ha realizado una compra.")
