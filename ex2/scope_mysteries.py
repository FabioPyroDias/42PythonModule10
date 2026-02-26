def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulator(add_power: int):
        nonlocal power
        power += add_power
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchantment(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key, value):
        vault[key] = value

    def recall(key):
        return vault.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print()
    print("Testing mage counter...")
    try:
        counter = mage_counter()
        index = 1
        while index < 4:
            print(f"Call {index}: {counter()}")
            index += 1
    except TypeError as error:
        print(error)
    print()
    print("Testing spell accumulator...")
    try:
        powerup = spell_accumulator(10)
        index = 1
        print("Initial power: 10")
        while index < 4:
            print(f"Call {index}, added power {index * 5}: "
                  f"{powerup(index * 5)}")
            index += 1
    except TypeError as error:
        print(error)
    print()
    print("Testing enchantment factory...")
    try:
        fire_factory = enchantment_factory("Flamming")
        print(fire_factory("Sword"))
        ice_factory = enchantment_factory("Frozen")
        print(ice_factory("Shield"))
    except TypeError as error:
        print(error)
    print()
    print("Testing memory vault...")
    try:
        vault = memory_vault()
        vault["store"]("Sword", {"Attack": 15, "Defense": 3, "Durability": 8})
        vault["store"]("Shield",
                       {"Attack": 5, "Defense": 12, "Durability": 20})
        print(vault["recall"]("Sword"))
    except TypeError as error:
        print(error)
