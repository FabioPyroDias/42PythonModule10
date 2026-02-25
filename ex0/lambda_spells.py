def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda value: value["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda name: "* " + name + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(sum(map(
            lambda mage: mage["power"], mages)) / len(mages), 2)
    }


if __name__ == "__main__":
    print()
    print("Testing artifact_sorter...")
    try:
        artifacts = [{'name': 'Earth Shield', 'power': 79, 'type': 'focus'},
                     {'name': 'Wind Cloak', 'power': 72, 'type': 'armor'},
                     {'name': 'Water Chalice', 'power': 108, 'type': 'weapon'},
                     {'name': 'Shadow Blade', 'power': 104, 'type': 'relic'}]
        artifacts = artifact_sorter(artifacts)
        current = 0
        result = ""
        while current < len(artifacts):
            result += f"{artifacts[current]['name']} " \
                f"({artifacts[current]['power']} power) "
            if current > 0 and current < len(artifacts) - 1:
                result += "comes before "
            current += 1
        print(result)
    except TypeError:
        print("Invalid input")
    print()
    print("Testing power_filter...")
    try:
        mages = [{'name': 'River', 'power': 54, 'element': 'light'},
                 {'name': 'Zara', 'power': 52, 'element': 'fire'},
                 {'name': 'Ember', 'power': 91, 'element': 'fire'},
                 {'name': 'Jordan', 'power': 95, 'element': 'shadow'},
                 {'name': 'Riley', 'power': 81, 'element': 'shadow'}]
        mages = power_filter(mages, 90)
        current = 0
        result = ""
        while current < len(mages):
            result += f"{mages[current]['name']} " \
                f"({mages[current]['power']} power)"
            if current < len(mages) - 1:
                result += ", "
            current += 1
        print(result)
    except TypeError:
        print("Invalid input")
    print()
    print("Testing spell_transformer...")
    try:
        spells = ['tornado', 'earthquake', 'meteor', 'blizzard']
        spells = spell_transformer(spells)
        current = 0
        result = ""
        while current < len(spells):
            result += f"{spells[current]}"
            if current < len(spells) - 1:
                result += " "
            current += 1
        print(result)
    except TypeError:
        print("Invalid input")
    mages = [{'name': 'River', 'power': 54, 'element': 'light'},
             {'name': 'Zara', 'power': 52, 'element': 'fire'},
             {'name': 'Ember', 'power': 91, 'element': 'fire'},
             {'name': 'Jordan', 'power': 95, 'element': 'shadow'},
             {'name': 'Riley', 'power': 81, 'element': 'shadow'}]
    print()
    print("Testing mage_stats...")
    try:
        stats = [{'name': 'River', 'power': 54, 'element': 'light'},
                 {'name': 'Zara', 'power': 52, 'element': 'fire'},
                 {'name': 'Ember', 'power': 91, 'element': 'fire'},
                 {'name': 'Jordan', 'power': 95, 'element': 'shadow'},
                 {'name': 'Riley', 'power': 81, 'element': 'shadow'}]
        stats = mage_stats(stats)
        print(stats)
    except TypeError:
        print("Invalid input")
