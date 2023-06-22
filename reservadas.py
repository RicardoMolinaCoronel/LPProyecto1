def crear(palabras):
  reservadas = {}
  for i in palabras:
    reservadas.update({i:i.upper()})
  return reservadas