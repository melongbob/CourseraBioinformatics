#find positions where skew array value is minimum
#input: string Genome
#output: list skew (list of positions where skew array value is minimum)
def MinimumSkew(Genome):
        positions = []
        skew = SkewArray(Genome)
        minimum = min(skew.values())
        for i in range(len(Genome)):
                if skew[i] == minimum:
                        positions.append(i)
        return positions

#Find G-C value upto each position
#input: string Genome
#output: dictionary skew (G-C in each position)
def SkewArray(Genome):
        skew = {}
        skew[0] = 0
        for i in range(len(Genome)):
                if Genome[i] == 'C':
                        skew[i+1] = skew[i] - 1
                elif Genome[i] == 'G':
                        skew[i+1] = skew[i] + 1
                else:
                        skew[i+1] = skew[i]
        return skew

#Gives number of occurrences of a symbol in a given window
#input: string Genome, char symbol
#output: dictionary array (occurrences of each symbol in each position)
def SymbolArray(Genome, symbol):
        array = {}
        n = len(Genome)
        ExtendedGenome = Genome + Genome[0:n//2]

        array[0] = PatternCount(symbol, Genome[0:n//2])
        
        for i in range(1, n):
                array[i] = array[i-1]
                if ExtendedGenome[i-1] == symbol:
                        array[i] = array[i] - 1
                if ExtendedGenome[i+(n//2)-1] == symbol:
                        array[i] + 1
        return array

#Find all positions where the pattern occurs in the genome
#input: string Pattern, string Genome
#output: list positions (list of positions in Genome where Pattern occurs)
def PatternMatching(Pattern, Genome):
        positions = []
        for i in range(len(Genome)-len(Pattern)):
                if Genome[i:i+len(Pattern)] == Pattern:
                        positions.append(i)
        return positions

#returns reverse complement of a string
#input: string Pattern
#output: string revComp (reverse complement of Pattern)
def ReverseComplement(Pattern):
        revComp = ""
        rev = reverse(Pattern)
        revComp = complement(rev)
        return revComp

#return complement of the input string
#input: string Pattern
#output: string complement (complement of Pattern)
def complement(Pattern):
        complement = ""
        for i in range(len(Pattern)):
                if Pattern[i] == 'A':
                        complement += 'T'
                elif Pattern[i] == 'C':
                        complement += 'G'
                elif Pattern[i] == 'G':
                        complement += 'C'
                else:
                        complement += 'A'
        return complement

#reverses the input string
#input: string Pattern
#output: string rev (reverse of Pattern)
def reverse(Pattern):
        reverse = ""
        for i in range(len(Pattern)):
                reverse = Pattern[i] + reverse
        return reverse

#Output a list of most frequent k-mers in Text
#input: string Text, int k
#output: list FrequentPatternsNoDuplicates (list of patterns in Text that appear most frequently)
def FrequentWords(Text, k):
	FrequentPatterns = []
	freq = FrequencyMap(Text, k)
	m = max(freq.values())
	for i in freq:
		if freq[i] == m:
			FrequentPatterns.append(Text[i:i+k])
	FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
	return FrequentPatternsNoDuplicates

#Output a list of objects from Items without duplicates
#input: list Items
#output: list ItemsNoDuplicates (list of items without duplicates)
def remove_duplicates(Items):
	ItemsNoDuplicates = []
	for i in range(len(Items)):
		if Items[i] not in ItemsNoDuplicates:
			ItemsNoDuplicates.append(Items[i])
	return ItemsNoDuplicates

#Count k-mers in Text
#input: string Text, int k
#output: dictionary count (number of times each k-mer appears in Text)
def FrequencyMap(Text, k):
    freq = {} 
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        freq[i] = PatternCount(Text, Pattern)
    return freq

#Counts number of 'Patterns' in the 'Text'
#input: string Text, string Pattern
#output: int count (number of times Pattern appears in Text)
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

#Given 'Pattern' and the 'Text'
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

Pattern = "TGATCA"

k = 10

#Print the result
print(FrequentWords(Text, k))
print(ReverseComplement(Pattern))
