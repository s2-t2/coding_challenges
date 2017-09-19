#!/usr/bin/python
import sys;

#s = '---'
#k = 3

global count;
global flips;
flips = 0;
count = 0

def reverse(sign) :
    if sign == '-' :
        sign = '+' 
    else :
        sign = '-'
    return sign;

def flip (s,k) :
    s = list(s)
    #print (s)
    #print (type(s))
    global count;
    global flips;
    if len(s) < k :
        res = 'Impossible'
        return res;
        #flips = "Impossible"

    if len(s) == k:
        if ( (s[0] == '+') and ( all(x == s[0] for x in s))):
            count = 0;
            #return 0;
        elif ( ( s[0] == '-' ) and (all(x == s[0] for x in s))):
            count = 1;
            flips = count + flips
            #return count + flips;
            #return 1;
        else :
            return None;
            #res = 'Impossible'
            #return res;
            #flips = "Impossible"
            
    if len(s) > k:
        if s[0] == '-' :
            flips = count + 1 + flips
            newList = [ reverse(x) for x in s[0:k] ]  + s[k:]
            #newList = reverse([x for x in s[1:k] ]) + s[k:]
                        
        elif s[0] == '+' :
            flips = count + 0 + flips
            newList = s[1:]
            
        #print (newList)
        flip(newList,k)
        return flips;


#print (flip(s,k))
#print (reverse('+'))

def main() :
    #s = '---+-++-'
    #k = 3
    #result = flip(s,k)
    #print(result)

    #return result;


    if len(sys.argv) > 1:
        inFile = sys.argv[1]
    else :
        inFile = 'test.in'
    
    with open(inFile) as f:
        content = f.readlines()
        content = [ x.strip() for x in content]
        print (content)
        casesNo = content[0]
        for i in range(1, len(content)) :
            test_s = content[i][0:(len(content[i])-1)]
            test_k = content[i][(len(content[i])-1):]
            test_k = int(test_k)
            result = flip(test_s,test_k)
            print (result)

    return result
            #print( ' Case # %d ' %(i) , flip(test_s,test_k) )
            #print( ' Case # %d %s %d' %(i,test_s,test_k) )
            #print ("test-s ", test_s)
            
            #print ( ' Case # %d: %s %s %d '%i+1, s,k, flip(s,k) )
    
    
    #result = flip (s,k)
    #print ( "No. of flips for " '%s  %d' " is"  %(s, k) )
    #print(result)
    #return result;

if __name__ == '__main__':
    main()


