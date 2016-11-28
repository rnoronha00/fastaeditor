#This program opens a txt file that has a fasta sequence and formats it
#The output are sequences that have a space every 10 nucleotides and a new line after 5 spaces
#The formatted file is saved with the same name followed by "Formatted.txt" and is stored it in the same directory

#open fasta file and read contents
#user should enter the name of the file
fastaFile = open("filename", 'r')
fastaSection = fastaFile.read().split("\n")
fastaFile.close()

#ignore the first line(> name) and store the sequence
fastaSequence = ""
for line in fastaSection:
    if (line[0] != ">"):
        fastaSequence += line

#add spaces and newlines to the fasta sequence
newLine = 0
formatFasta = ""
for i in range(0, len(fastaSequence)):
    if i % 10 == 0 and i > 0:
        if newLine == 5:
            formatFasta += fastaSequence[i-10: i] + "\n\n"
            newLine = 0
        else:
            formatFasta += fastaSequence[i-10: i] + " "
            newLine += 1

#add name of fasta sequence to formated sequence
formatFasta = fastaSection[0] + "\n\n" + formatFasta

#save the file
fastaText = open(fastaFile.name.split(".")[0] + "Formatted.txt", "w")
fastaText.write(formatFasta)
fastaText.close()
