import sys
import random

def main():
	if len(sys.argv) < 3:
		print "Use: <.py file> <input file> <output file>"
		sys.exit(0)

	# input file
	filein = open(sys.argv[1], 'r')
	fin = filein.read()

	# output file
	fout = open(sys.argv[2], 'w')

	# define codons
	codons = [[["F"],["TTT","TTC"],[0,0]],[["L"],["TTA","TTG","CTT","CTC","CTA","CTG"],[0,0,0,0,0,0]],[["I"],["ATT","ATC","ATA"],[0,0,0]],[["M"],["ATG"],[0]],[["V"],["GTT","GTC","GTA","GTG"],[0,0,0,0]],[["S"],["TCT","TCC","TCA","TCG","AGT","AGC"],[0,0,0,0,0,0]],[["P"],["CCT","CCC","CCA","CCG"],[0,0,0,0]],[["T"],["ACT","ACC","ACA","ACG"],[0,0,0,0]],[["A"],["GCT","GCC","GCA","GCG"],[0,0,0,0]],[["Y"],["TAT","TAC"],[0,0]],[["H"],["CAT","CAC"],[0,0]],[["Q"],["CAA","CAG"],[0,0]],[["N"],["AAT","AAC"],[0,0]],[["K"],["AAA","AAG"],[0,0]],[["D"],["GAT","GAC"],[0,0]],[["E"],["GAA","GAG"],[0,0]],[["C"],["TGT","TGC"],[0,0]],[["W"],["TGG"],[0]],[["R"],["CGT","CGC","CGA","CGG","AGA","AGG"],[0,0,0,0,0,0]],[["G"],["GGT","GGC","GGA","GGG"],[0,0,0,0]],[["STOP"],["TAA","TAG","TGA"],[0,0,0]]]


# split genes by '>'
	lista1 = str.split(fin, '>')
	percentage = 0
	interface = 0
	for i in range(len(lista1)-1):
		nonsense = "false"
		percentage = 50*i/len(lista1)
		while interface < percentage:
			interface += 1
			print str(interface)+"% complete"
		newvalue = str.split(lista1[i+1], ']')


	names = []	
		#split the file's contents by '>'
	proteins = str.split(fin, '>')[1:] #the file header is discarded
	for prot in proteins:
		seq = []
		lista = str.split(prot, '\n') #split each protein 
		names.append(lista[0]) #salve the names
		#concatenate the sequences of amino acids of the protein
		for temp in lista[1:]:
			seq.append(temp[:])	
		seqfinal = ''.join(seq) 
		protName = str.split(lista[0]) #take the first name

		lista2 = list(seqfinal)

	for i in range(len(lista1)-1):
		nonsense = "false"
		percentage = 50+50*i/len(lista1)
		while interface < percentage:
			interface += 1
			print str(interface)+"% complete"
		newvalue = str.split(lista1[i+1], ']')

		names = []
		sequences = []
		try:
			for element in newvalue:
				e = element.split('\n',1)
				names.append(e[0]) # genes list
				sequences.append(e[1]) #nucleotides list

				#for gene_name in names:
				#	fout.write('>'+str(gene_name)+'ATG')

				# lista2 = list of each base in a gene
				lista2 = sequences[len(sequences)-1]
				lista2 = lista2.replace("\n", "")
				lista2 = lista2.replace("\r", "")
				lista2 = list(lista2)
		except IndexError:
			pass

		
		
		j = 0
		while j < len(lista2)/3:
			matched = "false"
			try:
				codon = lista2[j*3] + lista2[j*3+1] + lista2[j*3+2]
			except Exception:
				print str.split(name, ' ')[0]+": fragmented codon"
				break
			for k in range(len(codons)):
				for w in range(len(codons[k][1])):
					if matched == "false":
						if codon == codons[k][1][w]:
							matched = "true"
					if matched == "true":
						codons[k][2][w] += 1
				if matched == "true":
					break
			j+=1

		
		for i in range(len(names)):
			fout.write('>'+str(names[i]))
			j = 0
			while j < len(lista2)/3:
				try:
					codon = lista2[j*3] + lista2[j*3+1] + lista2[j*3+2]
				except Exception:
					print str.split(name, ' ')[0]+": fragmented codon"
					break
				for k in range(len(codons)):
					itsamatch = "false"
					for w in range(len(codons[k][1])):
						if codon == codons[k][1][w]:
							teste = random.random()*codons[k][2][len(codons[k][2])-1]
							for z in range(len(codons[k][1])):
								if teste <= codons[k][2][z]:
									if  itsamatch == "false":
										fout.write(codons[k][1][z])
										itsamatch = "true"
									codons[k][2][z] -= 1
							break
					if itsamatch == "true":
						break
				j+=1

		
main()
print "100% complete!\n"