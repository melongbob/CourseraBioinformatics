#Gives number of occurrences of a symbol in a given window
#input: string Genome, char symbol
#output: dictionary array (occurrences of each symbol in each position)
def SymbolArray(Genome, symbol):
        array = {}
        n = len(Genome)
        ExtendedGenome = Genome + Genome[0:n//2]
        for i in range(n):
                array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
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
