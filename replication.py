#Output a list of most frequent k-mers in Text
def FrequentWords(Text, k):
	FrequentPatterns = []
	Count = CountDict(Text, k)
	m = max(Count.values())
	for i in Count:
		if Count[i] == m:
			FrequentPatterns.append(Text[i:i+k])
	FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
	return FrequentPatternsNoDuplicates

#Output a list of objects from Items without duplicates
def remove_duplicates(Items):
	ItemsNoDuplicates = []
	for i in range(len(Items)):
		if Items[i] not in ItemsNoDuplicates:
			ItemsNoDuplicates.append(Items[i])
	return ItemsNoDuplicates

#Count k-mers in Text
def CountDict(Text, k):
    Count = {} 
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

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
