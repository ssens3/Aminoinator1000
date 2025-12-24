import os
considerMet = True
DNAcompBase = {"A":"T", "T":"A", "C":"G", "G":"C"} #dna to temp dna
RNAcompBase = {"A":"U", "U":"A", "C":"G", "G":"C"} #dna to rna
mRNAcompBase = {"A":"U", "T":"A", "C":"G", "G":"C"} #dna to rna
codonTable = {
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
    "AUG": "Met",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "AGU": "Ser", "AGC": "Ser",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "UAU": "Tyr", "UAC": "Tyr",
    "CAU": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "UGU": "Cys", "UGC": "Cys",
    "UGG": "Trp",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}
def translate(strand):
    x = 0; start = False; aminoList = []
    if considerMet:
        while x <= len(strand)-3:
            if strand[x] == 'A':
                if strand[x+1] == 'U':
                    if strand[x+2] == 'G':
                        start = True; break
            x += 1
    if start or (not considerMet):
        while x <= len(strand)-3:
            codon = strand[x:x+3]
            k = codonTable.get(codon, "?")
            if k == "STOP":
                break
            aminoList.append(k)
            x += 3
        print("Amino               : "," - ".join(aminoList))
    else:
        print("No start codon found")
    print("Enter anything to continue")
    o = input("> ")
    
def tomrna(strand):
    strand = "".join(mRNAcompBase[x] for x in strand)
    print("mRNA codon          : ", "5' ",strand," 3'")
    print("tRNA Anti-Codon     : ","3' ","".join(RNAcompBase[x] for x in strand)," 5'")
    translate(strand)
    
def interface():
    global considerMet
    print("\n"*20)
    os.system("clear")
    print("DNA/mRNA Translator")
    print("Where to start?")
    print("DNA")
    print("  Non-Temp        : 1")
    print("  Template        : 2")
    print("RNA")
    print("  mRNA Codon      : 3")
    print("  tRNA Anti-Codon : 4")
    print("Exit Program      : 0")
    mode = int(input("> "))
    print("Consider start codon? 0:No 1:Yes")
    considerMet = int(input("> "))
    if considerMet == 1:
        considerMet = True
    elif considerMet == 0:
        considerMet = False
    else:
        print("Invalid")
        considerMet = True
    return mode

#dna  will all be 3 to 5
#mrna will all be 5 to 3
while True:
    mode = interface()
    if mode == 0:
        break
    if mode == 1:
        print("Insert non-template DNA strand \nExample 5ATGCTC3")
        strand = input("> ").strip().upper()
        if strand[0] == '3': #turn to 5 to 3
            strand = strand[1:-1] #remove 3,5
            strand = strand[::-1] #reverse
        elif strand[0] == '5':
            strand = strand[1:-1] #remove 5,3
        else:
            continue #invalid
        strand = "".join(DNAcompBase[x] for x in strand)
        print("Template Strand     : ", "3' ",strand," 5'")
        tomrna(strand)
    elif mode == 2:
        print("Insert template DNA strand \nExample 5ATGCTC3")
        strand = input("> ").strip().upper()
        if strand[0] == '3':
            strand = strand[1:-1] #remove 3,5
        elif strand[0] == '5':
            strand = strand[1:-1] #remove 5,3
            strand = strand[::-1] #reverse
        else:
            continue #invalid
        print("Non-Template Strand : ", "5' ","".join(DNAcompBase[x] for x in strand)," 3'")
        tomrna(strand)
    elif mode == 3:
        print("Insert mRNA strand \nExample 5AUGCUC3")
        strand = input("> ").strip().upper()
        if strand[0] == '3': #turn to 5 to 3
            strand = strand[1:-1] #remove 3,5
            strand = strand[::-1] #reverse 
        elif strand[0] == '5':
            strand = strand[1:-1] #remove 5,3
        else:
            continue #invalid
    #   print("Non-Template Strand : ", "5' ","".join(DNAcompBase[x] for x in strand)," 3'") not working yet
    #   print("Template Strand     : ", "5' ","".join(DNAcompBase[x] for x in strand)," 3'") not working yet
        print("tRNA Anti-Codon     : ","3' ","".join(RNAcompBase[x] for x in strand)," 5'")
        translate(strand)
    elif mode == 4:
        print("Insert tRNA strand \nExample 5AUGCUC3")
        strand = input("> ").strip().upper()
        if strand[0] == '3': 
            strand = strand[1:-1] #remove 3,5
        elif strand[0] == '5': #turn to 3 to 5
            strand = strand[1:-1] #remove 5,3
            strand = strand[::-1] #reverse 
        else:
            continue #invalid
        strand = "".join(RNAcompBase[x] for x in strand)
        print("mRNA Codon          : ","3' ",strand," 5'")
        translate(strand)
#sample
#nont 5tacgatggattcacggaatggaaccagtac3
#temp 3atgctacctaagtgccttaccttggtcatg5
#mrna 5uacgauggauucacggaauggaaccaguac3
#trna 3augcuaccuaagugccuuaccuuggucaug5