class Carrito:
  def __init__(self, request):
    self.request = request
    self.session = request.session
    carrito = self.session.get("carrito")
    if not carrito:
      self.session["carrito"] = {}
      self.carrito = self.session["carrito"]
    
    else:
      self.carrito = carrito


  def agregar(self,disco):
    id = str(disco.id)
    if id not in self.carrito.keys():
      self.carrito[id] = {
        "disco_id": disco.id,
        "disco_url":disco.url_imagen,
        "nombre": disco.nombre,
        "acumulado": disco.valor,
        "cantidad": 1,
      }
    else:
        self.carrito[id]["acumulado"] += disco.valor
        self.carrito[id]["cantidad"] += 1

    self.guardar_carrito()

  def guardar_carrito(self):
    self.session["carrito"] = self.carrito
    self.session.modified = True


  def eliminar(self, disco):
    id = str(disco.id)
    if id in self.carrito:
      del self.carrito[id]
      self.guardar_carrito()
    

  def restar(self,disco):
    id = str(disco.id)
    if id in self.carrito.keys():
      self.carrito[id]["acumulado"] -= disco.valor
      self.carrito[id]["cantidad"] -= 1
      if self.carrito[id]["cantidad"] <= 0 : self.eliminar(disco)
      self.guardar_carrito()

  def limpiar(self):
    self.session["carrito"] = {}
    self.session.modified = True