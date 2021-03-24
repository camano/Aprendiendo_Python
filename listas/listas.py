milista=["maria","Pepe","Martha","Antonio"]
""" Se agrega un nuevo elemento """
milista.append("Jonathan")
""" Puede agregar en que posicion  """
milista.insert(2,"Sandra")
milista.extend(["Maricela","Gancha"])
milista.remove("maria")
print("listar todo :"+ str(milista[:]))
print("Solo muestra el indice 2 :" + str(milista[2]))
print("Muestra al revez :"+ str(milista[-1]))
print(milista[0:2])
print(milista[1:2])
print("Busca el indice :"+ str(milista.index("Gancha")))
print("Buscando si existe en la lista")
print("Jonathan" in milista)