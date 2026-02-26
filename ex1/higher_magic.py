def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combiner(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combiner


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier():
        return base_spell() * multiplier
    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditional(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":
    print()
    print("Testing spell combiner...")

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"
    try:
        combined_spell = spell_combiner(fireball, heal)
        values = combined_spell("Dragon")
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

    def fireball():
        return 10
    try:
        amplified_fireball = power_amplifier(fireball, 3)
        print(f"Original: {fireball()}, Amplified: {amplified_fireball()}")
    except TypeError as error:
        print(error)
    print()
    print("Testing conditional_caster...")

    def spell(target):
        return f"Wingardium Leviosa on {target}"

    def condition(target):
        return target == "Troll"
    try:
        conditional = conditional_caster(condition, spell)
        print(conditional("Troll"))
        print(conditional("Dragon"))
    except TypeError as error:
        print(error)
    print()
    print("Testing spell sequence...")

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"
    try:
        sequence = spell_sequence([fireball, heal])
        print(sequence("Dragon"))
    except TypeError as error:
        print(error)
