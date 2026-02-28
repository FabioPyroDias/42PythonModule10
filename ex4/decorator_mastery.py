from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        time_start = time.time()
        result = func(*args, **kwargs)
        print(f"Spell completed in {(time.time() - time_start)} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(spell: callable) -> callable:
        @wraps(spell)
        def wrapper(*args, **kwargs):
            power = kwargs["power"]
            if power >= min_power:
                return spell(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(spell: callable):
        @wraps(spell)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                try:
                    return spell(*args, **kwargs)
                except Exception:
                    attempt += 1
                    print(f"Spell failed, retrying... ({attempt}/"
                          f"{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if name is None:
            return False
        if len(name) < 3:
            return False
        for character in name:
            if not ((character >= 'a' and character <= 'z') or
                    (character >= 'A' and character <= 'Z') or
                    character == ' '):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print()
    print("Testing spell time...")
    try:
        def fireball():
            return "Fireball cast!"
        cast = spell_timer(fireball)
        print(f"Result: {cast()}")
    except TypeError as error:
        print(error)
    print()
    print("Testing power validator...")
    try:
        @power_validator(50)
        def fireball(power):
            return f"Fireball cast with power {power}"
        print(fireball(power=60))
        print(fireball(power=40))
    except (TypeError, KeyError) as error:
        print(error)
    print()
    print("Testing retry spell...")

    @retry_spell(5)
    def failed_spell():
        raise ValueError
    print(failed_spell())
    print()
    print("Testing mage guild validate mage name...")
    try:
        mage_name_1 = "Aurelio Hogsworth"
        mage_name_2 = "Solaris"
        mage_name_3 = "Wrong Name!"
        mage_name_4 = "Shrek123"
        print(f"{mage_name_1}: {MageGuild.validate_mage_name(mage_name_1)}")
        print(f"{mage_name_2}: {MageGuild.validate_mage_name(mage_name_2)}")
        print(f"{mage_name_3}: {MageGuild.validate_mage_name(mage_name_3)}")
        print(f"{mage_name_4}: {MageGuild.validate_mage_name(mage_name_4)}")
    except TypeError as error:
        print(error)
    print()
    print("Testing cast spell...")
    try:
        guild = MageGuild()
        print(guild.cast_spell("Lightning", power=15))
        print(guild.cast_spell("Pinch", power=1))
    except KeyError as error:
        print(f"Key {error} does not exist")
    except TypeError as error:
        print(error)
