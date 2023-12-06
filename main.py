from loading import load_directory
from kmers import stream_kmers, kmer2str

def my_method(text,ia,ib,k):
    """
    Takes 2 sequences and returns the kmers present in each sequence.
    
    Parameters : 
    text : (array) each 
    ia,ib : (int) the index of the sequences to compare 
    k : (int) length of the kmers

    Returns : 
    U : (int) kmer union of the 2 sequences 
    I : (int) kmer intersection of the 2 sequences
    """
    Dkmer = {} #Dictionnary containing kmers
    U = 0 #Kmer union
    I = 0 #Kmer intersection
    for kmer in stream_kmers(text[ia],k): #génère les kmer de la séquence A et les stocke dans un dictionnaire
        if kmer in Dkmer:
            Dkmer[kmer]+=1
        else:
            Dkmer[kmer]=1
        U+=1
    
    for kmer2 in stream_kmers(text[ib],k):
        #génère les kmer de la séquence B et les compares avec ceux déjà  #présents dans le dictionnaire
        if kmer2 in Dkmer.keys() :
            I+=1
            Dkmer[kmer2]-=1
            if Dkmer[kmer2]==0:
                del Dkmer[kmer2]
        else :
            #Dkmer[kmer]+=1
            U+=1
        return U,I


def similarity(A,B):
    """
    Calcule la similarité entre les deux séquences
    """
    intersection_size = len(A.intersection(B))    
    return intersection_size/len(A),intersection_size/len(B)


def jaccard(A, B):
    """
    Calcule la distance de jaccard entre ecs 
    """
    intersection_size = len(A.intersection(B))
    union_size = len(A.union(B))
    
    return intersection_size/union_size


if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    
    filenames = list(files.keys())
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            
            # --- Complete here ---

            A, inter, B = my_method(indexes[filenames[i]], files[filenames[j]], k)
            print(filenames[i], filenames[j], jaccard(A, inter, B), similarity(A, inter, B))
