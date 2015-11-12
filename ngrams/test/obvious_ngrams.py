input_list = ['having', 'made', 'a', 'preelection', 'pledge', 'of', 'not', 'another', 'cent', 'to', 'the', 'bondholders', 'the', 'taoiseach', 'made', 'a', 'postelection', 'uturn', 'proclaiming', 'that', 'he', 'would', 'not', 'wear', 'the', 'slogan', 'of', 'debt', 'defaulter', 'on', 'his', 'forehead', 'it', 'is', 'clear', 'that', 'the', 'slogan', 'of', 'indebtedness', 'will', 'be', 'marked', 'across', 'our', 'brows', 'for', 'many', 'years', 'because', 'of', 'the', 'cowardice', 'and', 'incompetence', 'of', 'this', 'Fine', 'Gael', 'and', 'Labour', 'Government',
'a', 'massive', 'burden', 'of', 'odious', 'debt', 'the', 'debts', 'of', 'bankers', 'speculators', 'and', 'developers', 'weighs', 'heavily', 'on', 'this', 'and', 'future', 'generations', 'all', 'the', 'while', 'the', 'taoiseach', 'has', 'busied', 'himself', 'currying', 'favour', 'with', 'the', 'troika', 'and', 'his', 'friend', 'chancellor', 'angela', 'merkel']

def find_bigrams(input_list):
	bigram_list = []
	for i in range(len(input_list)-1):
		bigram_list.append((input_list[i], input_list[i+1]))
	return bigram_list

print bigram_list