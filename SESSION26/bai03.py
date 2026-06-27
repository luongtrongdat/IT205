from abc import ABC, abstractmethod


class Champion(ABC):
    def __init__(self, champion_id, name, hp, atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = hp if hp > 0 else 100
        self.base_atk = atk if atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        if isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        return other + self.get_combat_power()

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    def __init__(self, champion_id, name, hp, atk, armor):
        super().__init__(champion_id, name, hp, atk)
        self.armor = armor

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.armor


class Mage(Champion):
    def __init__(self, champion_id, name, hp, atk, ap):
        super().__init__(champion_id, name, hp, atk)
        self.ap = ap

    def calculate_skill_damage(self):
        return self.base_atk * self.ap


champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 2)
]


def find_champion(champion_id):
    for c in champion_pool:
        if c.champion_id == champion_id:
            return c
    return None


def show_champions():
    print("\nDanh sach tuong")
    for c in champion_pool:
        if isinstance(c, Warrior):
            print(
                c.champion_id,
                c.name,
                "Warrior",
                c.base_hp,
                c.base_atk,
                c.armor,
                round(c.get_combat_power())
            )
        else:
            print(
                c.champion_id,
                c.name,
                "Mage",
                c.base_hp,
                c.base_atk,
                c.ap,
                round(c.get_combat_power())
            )


def add_champion():
    role = input("1.Warrior 2.Mage: ")

    champion_id = input("Ma: ")

    if find_champion(champion_id):
        print("Ma da ton tai")
        return

    name = input("Ten: ")
    hp = int(input("HP: "))
    atk = int(input("ATK: "))

    if role == "1":
        armor = int(input("Armor: "))
        c = Warrior(champion_id, name, hp, atk, armor)

    elif role == "2":
        ap = float(input("AP: "))
        c = Mage(champion_id, name, hp, atk, ap)

    else:
        print("Khong hop le")
        return

    champion_pool.append(c)
    print("Them thanh cong")


def compare_champions():
    id1 = input("Ma 1: ")
    id2 = input("Ma 2: ")

    c1 = find_champion(id1)
    c2 = find_champion(id2)

    if not c1:
        print("Ma", id1, "khong hop le")
        return

    if not c2:
        print("Ma", id2, "khong hop le")
        return

    if c1 > c2:
        print(c1.name, "manh hon", c2.name)
    else:
        print(c2.name, "manh hon", c1.name)


def team_power():
    ids = input("Nhap ma: ").split(",")

    total = 0

    for champion_id in ids:
        champion_id = champion_id.strip()

        c = find_champion(champion_id)

        if not c:
            print("Ma", champion_id, "khong hop le")
            continue

        total += c

    print("Tong chien luc:", round(total))


while True:
    print("\n1.Hien thi")
    print("2.Them")
    print("3.So sanh")
    print("4.Tong doi hinh")
    print("5.Thoat")

    choice = input("Chon: ")

    if choice == "1":
        show_champions()

    elif choice == "2":
        add_champion()

    elif choice == "3":
        compare_champions()

    elif choice == "4":
        team_power()

    elif choice == "5":
        print("Tam biet")
        break

    else:
        print("Khong hop le")