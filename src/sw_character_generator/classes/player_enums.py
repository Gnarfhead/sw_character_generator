from enum import Enum

class MainStat(Enum):
    """Enumeration for main statistics."""
    STRENGTH = "strength"
    DEXTERITY = "dexterity"
    CONSTITUTION = "constitution"
    INTELLIGENCE = "intelligence"
    WISDOM = "wisdom"
    CHARISMA = "charisma"

class AllowedRaces(Enum):
    """Enumeration for allowed races."""
    HUMAN = "human"
    ELF = "elf"
    DWARF = "dwarf"
    HALFLING = "halfling"
    HALFELF = "halfelf"

class AllowedAlignments(Enum):
    """Enumeration for allowed alignments."""
    GOOD = "good"
    NEUTRAL = "neutral"
    EVIL = "evil"

class PlayerStates(Enum):
    """Enumeration for player states."""
    ALIVE = "alive"
    DEAD = "dead"
    UNCONSCIOUS = "unconscious"
    POISONED = "poisoned"
    STUNNED = "stunned"
    PARALYZED = "paralyzed"
    CONFUSED = "confused"
    BLIND = "blind"