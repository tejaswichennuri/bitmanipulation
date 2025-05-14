'''s="abcd"
n=input()
if len(n)<len(s):
    print("true")
else:
    print("false")'''
#3a4d5c 12a3d234c 12abcas4s
'''n=input()
x=input()
z=input()
print(n*3+x*4+z*5)'''
'''s="3a4d5c"
n=len(s)
res=""
for i in range(n):
    if s[i] in "123456789":
        res+=int(s[i])*s[i+1]
print(res)
string=input()
x={
    "a":3,
    "b":4,
    "c":5
}
print(x)'''
#looping
'''l=[1,2,3,4,5]
for i in range(5):
    print(l[i]**3,end=" ")
#print good numbers it is even AND POSITIVE
l=list(map(int,input().split()))
c=0
for i in l:
    if i>0 and i%2==0:
        c+=1
print(c)'''
#finding vowels
l=input()
c=0
for ch in l:
    if ch in "aeiou":
        c+=1
print(c)
#prime number
n=int(input())
f=0
for i in range(2,n//2):
    if n%i==0:
        f+=1
if f==0:
    print("prime")
else:
    print("not prime")
    

