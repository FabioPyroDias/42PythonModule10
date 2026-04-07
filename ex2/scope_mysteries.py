from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulator(add_power: int):
        nonlocal power
        power += add_power
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
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
        counter_a = mage_counter()
        counter_b = mage_counter()
        print(f"counter_a call 1: {counter_a()}")
        print(f"counter_a call 2: {counter_a()}")
        print(f"counter_b call 1: {counter_b()}")
    except TypeError as error:
        print(error)
    print()
    print("Testing spell accumulator...")
    try:
        base = 100
        powerup = spell_accumulator(base)
        powerup_20 = 20
        print(f"Base {base}, add {powerup_20}: {powerup(powerup_20)}")
        powerup_30 = 30
        print(f"Base {base}, add {powerup_30}: {powerup(powerup_30)}")
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
        key = "secret"
        value = 42
        vault["store"](key, value)
        print(f"Store \'{key}\' = {value}")
        print(f"Recall \'{key}\': {vault['recall'](key)}")
        wrong_key = "unknown"
        print(f"Recall \'{wrong_key}\': {vault['recall'](wrong_key)}")
    except (NameError, TypeError) as error:
        print(error)
