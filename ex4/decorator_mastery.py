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
            power = args[0]
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
                    print(f"Spell failed, retrying... ({attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


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
        print(fireball(60))
        print(fireball(40))
    except TypeError as error:
        print(error)
    print()
    print("Testing retry spell...")
    @retry_spell(5)
    def failed_spell():
        raise ValueError
    print(failed_spell())
    print()
