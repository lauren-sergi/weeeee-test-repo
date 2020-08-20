# python script for sse activity

# for changing the output text colour in terminal
class bcolors:
    HEADER 	= 	'\033[95m'
    OKBLUE 	= 	'\033[94m'
    OKGREEN = 	'\033[92m'
    WARNING = 	'\033[93m'
    FAIL = 		'\033[91m'
    ENDC = 		'\033[0m'
    BOLD = 		'\033[1m'
    UNDERLINE = '\033[4m'

# the (almost complete) mapping of letters
mapping = {
	't': 's',
	'g': 'e',
	'd': 't',
	'n': 'a',
	'o': 'o',
	'x': 'r',
	'f': 'h',
	'z': 'g',
	'c': 'i',
	'j': 'd',
	'k': 'c',
	'w': 'w',
	'b': 'l',
	's': 'n',
	'p': 'p',
	'i': 'f',
	'q': 'y',
	'r': 'v',
	'a': 'u',
	'h': 'b',
	'l': 'm'
}


word = "fc hoh, fow ct grgxqdfcsz zocsz? nxg qoa ixgg dfct ixcjnq sczfd? wg nxg pbnsscsz do fnrg n pnxdq nd kfnxbcg't pbnkg. dfg cjgn ct do hxcsz wfnd qoa wnsd do gnd nsj znlgt dfnd qoa wnsd do pbnq. nsj fnrg n bod oi ias dozgdfgx! iggb ixgg do csrcdg loxg pgopbg. fopg do tgg qoa dfgxg! kfggxt, nbckg"

def get_frequency(string):
	all_freq = {} 
  
	for i in string: 
	    if i in all_freq: 
	        all_freq[i] += 1
	    else: 
	        all_freq[i] = 1

	return all_freq

def inverse_monoalpha_cipher(monoalpha_cipher, word):
	for letter in word:
		new = monoalpha_cipher.get(letter)
		if new is not None:	
			print(bcolors.FAIL + new, end = '')
		else:
			print(bcolors.ENDC + letter, end = '')

inverse_monoalpha_cipher(mapping, word)

print(bcolors.ENDC)

print("script run successfully, exiting...")

this will cause some errors oke
