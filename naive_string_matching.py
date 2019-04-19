
#!/usr/bin/python

T = raw_input("Enter the text \n");
P = raw_input("Enter the pattern \n");

n = len(T);
m = len(P);

def naivematcher(T,P) :
    for s in range(0,n-m) :
        j = 0;
        while T[s+j] == P[j] :
            j = j + 1;
            if j == m :
                return s;
    return -1;


print naivematcher(T,P);
