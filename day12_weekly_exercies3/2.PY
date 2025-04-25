alpha = {
    'A': '1','B': '2','C': '3','D': '4','E': '5','F': '6','G': '7','H': '8','I': '9','J': '01',
        'K': '02','L': '03','M': '04','N': '05','O': '06','P': '07','Q': '08','R': '09','S': '10',
        'T': '11','U': '12','V': '13','W': '14','X': '15','Y': '16','Z': '17',' ': '*',
    'a':'Z','b': 'Y','c': 'X','d':'W','e': 'V','f': 'U','g': 'T','h': 'S','i': 'R','j': 'Q',
        'k': 'P','l': 'O','m': 'N','n': 'M','o': 'L','p': 'K','q': 'J','r': 'I','s': 'H',
        't': 'G','u': 'F','v': 'E','w': 'D','x': 'C','y': 'B','z': 'A',}
plain_text = input("Enter single character: ")
coded_name = ""

for x in plain_text:
    if x in alpha:
        coded_name += alpha[x]
    else:
        coded_name += "?"
print("Coded text: ", coded_name)