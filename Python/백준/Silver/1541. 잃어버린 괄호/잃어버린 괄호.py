import sys
input=sys.stdin.readline

s=input().strip()
lst=s.split('-')
#print(lst)

result=0
if s[0]=='-':
    result-=map(int,lst[0].split('+'))
else:
    result += sum(map(int,lst[0].split('+')))

for l in lst[1:]:
    s=sum(map(int,l.split('+')))
    result-=s

print(result)