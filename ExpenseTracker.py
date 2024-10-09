print("Welcome to expense tracker")
n=int(input("add number of objects\n"))
d={}
w=0
for i in range(n):
    d.update({input("item ").lower(): [int(input("price ")),input("description ")]})
print(d)
z=input("more or quit\n")
if z.lower()=="more":
    while True:
         r=input("type add/ remove/ total/ search/ quit \n" )
         if r.lower()=="add":
            d.update({input("item ").lower():[int(input("price ")),input("description ")]})
         if r.lower()=="remove":
            f=input("key")
            del d[f]
         if r.lower()=="total":
            for key in d:
                w+= d[key][0]
            print(w)
         if r.lower()=="search":
            i=input("type the item name\n").lower()
            if d.get(i)==None:
                print("ITEM NOT FOUND")
            else:
                print(d.get(i))
         if r.lower()=="quit":
            break
else:
    quit
print(d)         