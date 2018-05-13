#------------------------- Week 4 ----------------------------------

# Returns a list of the Profile-most probable k-mers in each string from Dna
# Input:  list Profile, list Dna
# Output: list Motif
def Motifs(Profile, Dna):
    Text = Dna
    k = 4
    Profile = Profile
    MostProbableMotifs = []
    
    for i in range(len(Dna)):
        MostProbableMotifs.append(ProfileMostProbablePattern(Text[i], k, Profile))
    return MostProbableMotifs
                                 
#Returns best motifs calculated with pseudocounts (to use, functions
#need to be edited to integrate count, profile with pseudocounts
#Input: list Dna, int k, int t
#Output: list BestMotifs
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [] 
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i + k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    
    return BestMotifs

# Returns profile calculated with pseudocounts
# Input:  list Motifs
# Output: dictionary profile (calculated with pseudocounts)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    
    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] /= (t + 4)
    
    return profile

# Returns count with pseudocounts (adds 1 to every entity initially)
# Input: list Motifs
# Output: dictionary count (count with pseudocounts)

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count


#------------------------- Week 3 ----------------------------------

#Finds best Motifs
#input: list Dna, int k, int t
#output: list BestMotifs

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i + k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
                          
#Find a profile-most probable k-mer in a string
#input: str Text, int k, dict Profile
#output: str mostProbableKmer

def ProfileMostProbablePattern(Text, k, Profile):
    probability = 0
    mostProbableKmer = Text[0:k]
    for i in range(len(Text) - k + 1):
        kmer = Text[i:k + i]
        if Pr(kmer, Profile) > probability:
            probability = Pr(kmer, Profile)
            mostProbableKmer = kmer
    return mostProbableKmer
    
#Calculate score of given string with given profile
#input: string Text, list Motifs
#output: double p 

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
 
#Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]

#print(Count(Motifs))

#print(Profile(Motifs))

#print(Consensus(Motifs))

#print(Score(Motifs))

Text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
Profile = { 
  'A': [0.2, 0.2, 0.3, 0.2, 0.3],
  'C': [0.4, 0.3, 0.1, 0.5, 0.1],
  'G': [0.3, 0.3, 0.5, 0.2, 0.4],
  'T': [0.1, 0.2, 0.1, 0.1, 0.2]
}
k = 5

#Profile = {'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0], 'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6], 'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0], 'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}

#print(Pr(Text, Profile))

print(ProfileMostProbablePattern(Text, k, Profile))
