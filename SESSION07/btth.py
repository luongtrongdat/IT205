str = "Hello World"
print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.title())
print(str.capitalize())

# A in B -> true/false
strA = "Hello Hello"
strB = "llo"
print(strA.find(strB))  # 2
print(strA.count("l"))  # 4
print(strA.startswith("He"))  # True
print(strA.endswith("lo"))  # False

# Thay thế chuỗi
a = "Luong Trong Dat"
print(a.replace("Luong", "Dat"))

## format string
name = "Dat"
name_class = "Python"
print("Xin chao {}. Ban dang hoc {}".format(name, name_class))
print(f"Xin chao {name}. Ban dang hoc {name_class}")
print("Xin chao" + name + ". Ban dang hoc " + name_class)
print("Xin chao %s. Ban dang hoc %s" % (name, name_class))