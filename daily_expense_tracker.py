print("====== Daily Expense Tracker ======")
o = int(input("Enter your total Expense here:"))
a = input("Enter first thing you spend money on:")
b = input("Enter second thing you spend money on:")
c = input("Enter third thing you spend money on:")
d = input("Enter fourth thing you spend money on:")
e = input("Enter fifth thing you spend money on:")
# Expense spend on things that user enter
f = int(input(f"How much you spend money on {a}?"))
g = int(input(f"How much you spend money on {b}?"))
h = int(input(f"How much you spend money on {c}?"))
i = int(input(f"How much you spend money on {d}?"))
j = int(input(f"How much you spend money on {e}?"))
#Use dictionary
dic = {
    a : f,
    b : g,
    c : h,
    d : i,
    e : j,
}
print(dic)
print("your Total Expense is:",o)
l = [f,g,h,i,j]
l2 = sum(l)
print("you spend your daily expense is:",l2)
s = o-l2
print("your remaining expense is:",s)
