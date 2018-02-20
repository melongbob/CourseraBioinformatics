#------------------------- Week 3 ----------------------------------
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

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}

    profile = Count(Motifs)
    
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] /= t

    return profile

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

print(Score(Motifs))
