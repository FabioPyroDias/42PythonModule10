from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":
    print()
    print("Testing spell combiner...")

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} HP"

    def heal(target: str, power: int):
        return f"Heal restores {target} for {power} HP"

    try:
        combined_spell = spell_combiner(fireball, heal)
        values = combined_spell("Dragon", 25)
        result = ""
        index = 0
        while index < len(values):
            result += f"{values[index]}"
            if index < len(values) - 1:
                result += ", "
            index += 1
        print(f"Combined spell result: {result}")
    except TypeError as error:
        print(error)
    print()
    print("Testing power amplifier...")

    try:
        mega_fireball = power_amplifier(fireball, 3)
        print(f"Original: \"{fireball('Dragon', 10)}\", "
              f"Amplified: \"{mega_fireball('Dragon', 10)}\"")
    except TypeError as error:
        print(error)
    print()
    print("Testing conditional_caster...")

    def condition(target: str, power: int):
        return target == "Troll"
    try:
        conditional = conditional_caster(condition, fireball)
        print(conditional("Troll", 10))
        print(conditional("Dragon", 10))
    except TypeError as error:
        print(error)
    print()
    print("Testing spell sequence...")

    try:
        sequence = spell_sequence([fireball, heal])
        print(sequence("Dragon", 10))
    except TypeError as error:
        print(error)
