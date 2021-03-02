import urllib.request
import json

filename = input("Give file name/path: ")  # Ο χρήστης δίνει το αρχείο με τα κρυπτονομίσματα.
f = open(filename, "r")
dict = json.loads(f.read())   # Μετατρέπω το περιεχόμενο του αρχείου σε λεξικό.
f.close()

k = len(dict)
crypto = list(dict.keys())    # Βάζω τα κλειδία του λεξικού dict σε μια λίστα με όνομα crypto.
value = list(dict.values())   # Βάζω τις τιμές του λεξικού dict σε μια λίστα με όνομα value.

for i in range (k):
    str = crypto[i]    # Βάζω το i στοιχείο της λίστας crypto μέσα στο str.
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + str + "&tsyms=EUR"  # Χτίζω το url με το str.
    r = urllib.request.urlopen(url)
    page_content = r.read()              # Διαβάζω το περιεχόμενο της ιστοσελίδας και το αποθηκεύω στη μεταβλητή page_content.
    page_content = page_content.decode()
    dict2 = json.loads(page_content)     # Μετατρέπω το page_content σε λεξικό.
    output = str + " in euro:"
    amount = dict2[str]["EUR"] * value[i]
    print("\n", output, amount)
