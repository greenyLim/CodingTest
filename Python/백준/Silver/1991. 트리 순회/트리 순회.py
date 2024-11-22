import sys
 
n = int(sys.stdin.readline())
tree = {}
 
for n in range(n): #tree 생성
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]



def preorder(root): #왼->루트->오른
    if root!='.':
        print(root, end='')
        preorder(tree[root][0]) #현 루트의 왼쪽
        preorder(tree[root][1]) #현 루트의 오른쪽 



def inorder(root):
    if root!='.':
        inorder(tree[root][0]) #현 루트의 왼쪽 
        print(root, end='') #현 루트 출력
        inorder(tree[root][1]) # 현 루트의 오른쪽 

def postorder(root):
    if root!='.':
        postorder(tree[root][0]) #현 루트의 왼쪽 
        postorder(tree[root][1]) # 현 루트의 오른쪽 
        print(root, end='') #현 루트 출력

preorder('A')
print()
inorder('A')
print()
postorder('A')
                
    