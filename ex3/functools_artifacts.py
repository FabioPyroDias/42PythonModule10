from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0

    if operation == "add":
        return reduce(lambda x, y: operator.add(x, y), spells)
    if operation == "multiply":
        return reduce(lambda x, y: operator.mul(x, y), spells)
    if operation == "max":
        return reduce(lambda x, y: x if operator.gt(x, y) else y, spells)
    if operation == "min":
        return reduce(lambda x, y: x if operator.lt(x, y) else y, spells)
    raise TypeError("Operation unknown")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = partial(base_enchantment, power=50, element="fire")
    ice = partial(base_enchantment, power=50, element="ice")
    lightning = partial(base_enchantment, power=50, element="lightning")
    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatch(arg):
        raise NotImplementedError("Unknown spell type")

    @dispatch.register(int)
    def _(damage_spell) -> str:
        return f"Damage spell: {damage_spell} damage"

    @dispatch.register(str)
    def _(enchantment) -> str:
        return f"Enchantment: {enchantment}"

    @dispatch.register(list)
    def _(multi_cast) -> str:
        return f"Multi-cast: {len(multi_cast)} spells"
    return dispatch


if __name__ == "__main__":
    print()
    print("Testing spell reducer...")
    try:
        numbers = [40, 30, 20, 10]
        print(f"Sum: {spell_reducer(numbers, 'add')}")
        print(f"Product: {spell_reducer(numbers, 'multiply')}")
        print(f"Max: {spell_reducer(numbers, 'max')}")
        print(f"Min: {spell_reducer(numbers, 'min')}")
    except TypeError as error:
        print(error)
    print()
    print("Testing partial enchanter...")
    try:
        def base_enchantment(power: int, element: str, target: str):
            return {"power": power, "element": element, "target": target}
        enchanter = partial_enchanter(base_enchantment)
        fire_enchantment = enchanter["fire_enchant"](target="Sword")
        print(f"Enchantment of {fire_enchantment['element']} on "
              f"{fire_enchantment['target']}. "
              f"Power: +{fire_enchantment['power']}")
        ice_enchantment = enchanter["ice_enchant"](target="Axe")
        print(f"Enchantment of {ice_enchantment['element']} on "
              f"{ice_enchantment['target']}. "
              f"Power: +{ice_enchantment['power']}")
        lightning_enchantment = enchanter["lightning_enchant"](target="Arrow")
        print(f"Enchantment of {lightning_enchantment['element']} on "
              f"{lightning_enchantment['target']}. "
              f"Power: +{lightning_enchantment['power']}")
    except (TypeError, KeyError) as error:
        print(error)
    print()
    print("Testing memoized_fibonacci...")
    try:
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except TypeError as error:
        print(error)
    print()
    print("Testing spell dispatcher...")
    try:
        dispatcher = spell_dispatcher()
        print(dispatcher(42))
        print(dispatcher("fireball"))
        print(dispatcher(["Fireball", "Lightning Bolt", "Heal"]))
        print(dispatcher(42.42))
    except NotImplementedError as error:
        print(error)
