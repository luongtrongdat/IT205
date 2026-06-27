from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def calculate_total_damage(self):
        pass


class Weapon(Equipment):
    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            print("Chi so sanh trang bi")
            return False

        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        if not isinstance(other, Equipment):
            print("Chi dung hop trang bi")
            return self

        return Weapon(
            f"Fusion({self.name}+{other.name})",
            self.base_damage + other.base_damage,
            self.upgrade_level + other.upgrade_level
        )


class MagicMixin:
    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print("Phat sang")


class MagicSword(Weapon, MagicMixin):
    def __init__(self, name, base_damage, upgrade_level, magic_power):
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        return (
            self.base_damage
            + self.upgrade_level * 10
            + self.magic_power
        )


inventory = []


def show_inventory():
    if not inventory:
        print("Kho trong")
        return

    for i, item in enumerate(inventory, 1):
        print(
            i,
            item.name,
            type(item).__name__,
            item.upgrade_level,
            item.calculate_total_damage()
        )


def create_weapon():
    name = input("Ten: ")

    damage = int(input("Damage: "))
    if damage <= 0:
        print("Sai")
        return

    level = int(input("Cap: "))
    if level <= 0:
        print("Sai")
        return

    inventory.append(
        Weapon(name, damage, level)
    )

    print("Them thanh cong")


def create_magic_sword():
    name = input("Ten: ")

    damage = int(input("Damage: "))
    if damage <= 0:
        print("Sai")
        return

    level = int(input("Cap: "))
    if level <= 0:
        print("Sai")
        return

    magic = int(input("Magic: "))
    if magic <= 0:
        print("Sai")
        return

    inventory.append(
        MagicSword(
            name,
            damage,
            level,
            magic
        )
    )

    print("Them thanh cong")


def compare_weapon():
    if len(inventory) < 2:
        print("Thieu vu khi")
        return

    w1 = inventory[0]
    w2 = inventory[1]

    if w1 > w2:
        print(w1.name, "manh hon")

    elif w2 > w1:
        print(w2.name, "manh hon")

    else:
        print("Bang nhau")


def fusion_weapon():
    if len(inventory) < 2:
        print("Thieu vu khi")
        return

    w1 = inventory[0]
    w2 = inventory[1]

    new_weapon = w1 + w2

    inventory.pop(0)
    inventory.pop(0)

    inventory.append(new_weapon)

    print("Dung hop xong")


while True:
    print("\n1.Xem")
    print("2.Weapon")
    print("3.MagicSword")
    print("4.So sanh")
    print("5.Dung hop")
    print("6.Thoat")

    choice = input("Chon: ")

    if choice == "1":
        show_inventory()

    elif choice == "2":
        create_weapon()

    elif choice == "3":
        create_magic_sword()

    elif choice == "4":
        compare_weapon()

    elif choice == "5":
        fusion_weapon()

    elif choice == "6":
        print("Tam biet")
        break

    else:
        print("Khong hop le")