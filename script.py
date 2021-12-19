

if __name__ == "__main__":
	diccionario_chr = {	"NC_000067.6": "1",	"NC_000068.7": "2",	"NC_000069.6": "3",	"NC_000070.6": "4",	"NC_000071.6": "5",	"NC_000072.6": "6",	"NC_000073.6": "7",	"NC_000074.6": "8",	"NC_000075.6": "9",	"NC_000076.6": "10", "NC_000077.6": "11", "NC_000078.6": "12", "NC_000079.6": "13", "NC_000080.6": "14", "NC_000081.6": "15", "NC_000082.6": "16", "NC_000083.6": "17", "NC_000084.6": "18", "NC_000085.6": "19", "NC_000086.7": "X",	"NC_000087.7": "Y"}
	archivo_tss = open("Mm_ucscTSS_mm10.sga","r")
	archivo_salida = open("tss.bed3cols","w")
	for linea in archivo_tss:
		datos = linea[:-1].split("\t") #separo los datos por tabulacion
		chr = diccionario_chr[datos[0]] # el 1er elemento de datos es el cromosoma en formato NC_0000XY.X, asi que en el diccionario tenemos que cromosoma es
		hebra = datos[3]
		cordenada_inicio = datos[2]
		cordenada_termino = datos[2]
		if hebra == "+":
			cordenada_termino = str(int(cordenada_termino) + 1)
		else: #hebra negativa
			cordenada_inicio = str(int(cordenada_inicio) - 1)
		archivo_salida.write(chr+"\t"+cordenada_inicio+"\t"+cordenada_termino+"\n")
	archivo_tss.close()
	archivo_salida.close()
