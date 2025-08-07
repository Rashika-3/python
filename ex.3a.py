MAX_SIZE=5
stack=[]
top=-1
def push(book_tilte):
    global top
    if top >= MAX_SIZE-1:
        print("stack overflow cannot push more books.")
    else:
        top+=1
        stack.append(book_tilte)
        print(f"Book '{book_tilte}' pushed onto the stack.")
def pop():
    global top
    if top ==-1:
       print("stack underflow cannot pop any book.")
    else:
        removed_book=stack.pop()
        print(f"Book '{removed_book}' popped from the stack.")
        top-=1
def peek():
    if top==-1:
       print("stack is empty.No book to peek.")
    else:
        print(f"top book on the stack:'{stack[top]}'")
def display():
    if top==-1:
        print("stack is empty.")
    else:
        print("Book in stack(Top to bottom):")
        for i in range(top,-1,-1):
            print(f"{i+1}.{stack[i]}")
push("The sun also rises")
push("The jungle book")
push("The book of last name")
push("The name jar")
push("Green bonds")
push("The genius wallet")
display()
peek()
pop()
pop()
display()
peek()

    
