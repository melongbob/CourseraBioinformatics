#------------------------- Week 3 ----------------------------------

#Calculate score of given string with given profile
#input: string Text, list Motifs
#output: return 

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        base = Text[i]
        p *= Profile[base][i]
    return p

#Calculates score that indicates how different Motifs are from consensus string
#input: list Motifs
#output: int score (the more different Motifs are from consensus, the bigger the score)

def Score(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    consensus = Consensus(Motifs)
    score = 0
    
    for i in range(t):
        for j in range(k):
             if Motifs[i][j] != consensus[j]:
                 score += 1

    return score

#Formulates consensus string with most probable nucleotide in each position
#input: list Motifs
#output: string consensus (most probable consensus string)

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)

    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    
    return consensus

#Return probabilities of each nucleotide appearing in the position
#input: list Motifs
#output: dictionary profile (dictionary of probabilities of each nucleotide in the position)

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}

    profile = Count(Motifs)
    
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] /= t

    return profile

#Return number of occurrences of each nucleotide 
#input: list Motifs
#output: dictionary count (number of each nucleotides in dictionary format)

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count
 
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]

#print(Count(Motifs))

#print(Profile(Motifs))

#print(Consensus(Motifs))

#print(Score(Motifs))

Text = "ACGGGGATTACC"
Profile = {'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0], 'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6], 'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0], 'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}

print(Pr(Text, Profile))
