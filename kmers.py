
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(text,k):
    """
    Fonction qui renvoie tous les mots de taille k contenus dans la séquence (appelés kmers)
    Ainsi que son réverse complément
    
    Parameters : 
    - text : (str) séquence nucléotidique
    - k : (int) longueur des kmers
    
    """
    kmer = 0
    rev_kmer = 0
    
    # Initialisation du kmer et de son reverse
    for letter in text[:k-1]:
        kmer <<= 2 #décalage de 2 vers la gauche
        nucl = (ord(letter)>>1) & 0b11 #encodage : masque binaire
        kmer += nucl # ajout du nucléotide
        #Reverse 
        rev_nucl = (nucl+2) & 0b11 #ajout de 2 bit pr trouver le nucléotide complémentaire puis encodahe
        rev_kmer += rev_nucl << (2*(k-1)) #décalage de (2*(k-1)) positions vers la gauche
    
    # Énumération des kmers
    mask = (1<<(2*k))-1 
    for letter in text[k-1:]:
        kmer <<=2
        nucl = (ord(letter)<<1) & 0b11
        kmer += nucl
        kmer &= mask #masque pour lire le kmer suivant
        #Reverse
        rev_nucl = (nucl+2) & 0b11
        rev_kmer += rev_nucl << (2*(k-1))
            
        yield min(kmer,rev_kmer)