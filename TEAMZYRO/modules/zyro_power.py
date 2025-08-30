# TEAMZYRO/utils/zyro_power.py

def require_power(rarity: str) -> int:
    power_map = {
        "Common": 10,
        "Rare": 25,
        "Epic": 50,
        "Legendary": 100,
        "Mythical": 200,
    }
    return power_map.get(rarity, 0)
