
import csv
import sys

param = sys.argv


print("limite")
print(csv.field_size_limit())
csv.field_size_limit(100000000)

arquivo = open(param[1])
corpus = open(param[2], 'w')

linhas = csv.reader(arquivo)
artigos = csv.DictReader(arquivo)
count = 0

for artigo in artigos:
    count += 1
    print("--------------------------------------------------------------------------------------")
    print(count, "- Resumo: ", artigo["Abstract"])
    corpus.writelines("**** *" + "Artigo_" + str(count))
    corpus.writelines("\n")

    if(artigo["Abstract"]=="[No abstract available]"):
        corpus.writelines("")
    else:
        corpus.writelines(artigo["Abstract"])

    corpus.writelines("\r\n")
    print("--------------------------------------------------------------------------------------")


corpus.close()
