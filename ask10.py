import json

def check(d):            # Με τη συνάρτηση check(d)
    if(len(d) == 0):     # ελέγχω εάν το λεξικό έχει βάθος 0,
        return 0         #  αν έχει βάθος 0 επιστρέφω την τιμή 0,
    return find_depth(d) # αλλιώς καλώ τη συνάρτηση find_depth(d).

def find_depth(d): # Αναδρομική συνάρτηση για την εύρεση του μέγιστου βάθους του λεξικού dictionary.
    if(isinstance(d, dict)): # Με τη συνάρτηση isinstance(d, dict) ελέγχω εάν η μεταβλητή d είναι λεξικό.
        return 1 + max(map(find_depth, d.values())) # Η συνάρτηση map(find_depth, d.values()) μου δίνει την δυνατότητα να καλέσω τη συνάρτηση find_depth(d), για όλες τις τιμές του λεξικού d.
    elif(isinstance(d, list)): # Με τη συνάρτηση isinstance(d, dict) ελέγχω εάν η μεταβλητή d είναι λίστα.
        return 1 + max(map(find_depth, d)) # Η συνάρτηση map(find_depth, d) μου δίνει την δυνατότητα να καλέσω τη συνάρτηση find_depth(d), για όλες τις τιμές της λίστας d.
    else:
        return 0

filename = input("Give file name/path: ")
f = open(filename, "r")
content = f.read()
dictionary = json.loads(content)
print("Το μεγαλύτερο βάθος του λέξικου είναι: ", check(dictionary))
