# Abrindo um arquivo

file1 = open("file1.csv", mode = "a", encoding = "utf-8" )

# Abrindo um arquivo com o 'with'

file2 = "file2.csv"

with open(file2, mode = "a", encoding = "utf-8") as f:
    f.write('linha 1\n')

# Abrindo um arquivo com 'with' e usando o writelines para escrever

text_to_write = ["linha 2 ","linha 3"]

with open(file2, mode="a", encoding = "utf-8" ) as f:
    f.writelines(text_to_write)  

# Lendo os dados de um arquivo
    # Its necessary to use mode = r 

with open(file2, mode="r", encoding = "utf-8" ) as f:
    text_to_read = f.read()
    #print(text_to_read)

with open(file2, mode="r", encoding = "utf-8" ) as f:
    text_to_read2 = f.readlines()
    print(text_to_read2)
