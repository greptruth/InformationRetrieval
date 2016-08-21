import json

# Dynamic programming implementation of LCS problem
 
# Returns length of LCS for X[0..m-1], Y[0..n-1] 
def lcs(X, Y, m, n):
    L = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] 
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # Following code is used to print LCS
    index = L[m][n]
 
    # Create a character array to store the lcs string
    lcs = [""] * (index+1)
    lcs[index] = "\0"
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1 
    return lcs 

# Driver program to test the above function
fout = open('output3.txt','w+');
config = json.loads(open('dump.json').read())
print type(config);

#X = config['industry-led']
#Y = config['industry-specific']
#print>>fout, X
#print>>fout, Y
#m = len(X)
#n = len(Y)
#print 'loaded'
#k = lcs(X, Y, m, n)
#print>>fout, k
#m = len(k)
#print>>fout, lcs(k,Y,m,n)

l = 0
fin = open('query.txt','r');
for line in fin:
    k = line.split('  ');
    query_id = k[0];
    print query_id
    term = k[1].split(' ');
    term[len(term)-1]=term[len(term)-1][:-1]
    print term
    try:
        X = config[term[0]]
    except:
        Y = 'ABC'
    try:
        Y = config[term[1]]
    except:
        Y = 'ZZZ'
    X = lcs(X,Y,len(X),len(Y))
    for i in range(2,len(term)):
        try:
            Y = config[term[i]]
        except:
            Y = 'ZZZ'
        X = lcs(X,Y,len(X),len(Y))
    print>>fout, X
    #l+=1
    #if l>5:
    #    l = input("something")


