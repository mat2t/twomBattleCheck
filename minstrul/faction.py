from enum import Enum


class Faction(Enum):
    FLAME = "Flame"
    AQUATIC = "Aquatic"
    NATURE = "Nature"
    SKY = "Sky"
    TERRA = "Terra"
    GLACIAL = "Glacial"
    LIGHTNING = "Lightning"
    SUNSHINE = "Sunshine"
    UNDEAD = "Undead"

FACTION_EFFECTIVENESS = {
    Faction.FLAME: {
        Faction.NATURE: 1.25,
        Faction.GLACIAL: 1.25,
        Faction.AQUATIC: 0.75,
        Faction.SKY: 0.75,
    },

    Faction.AQUATIC: {
        Faction.FLAME: 1.25,
        Faction.TERRA: 1.25,
        Faction.NATURE: 0.75,
        Faction.LIGHTNING: 0.75,
    },

    Faction.NATURE: {
        Faction.AQUATIC: 1.25,
        Faction.TERRA: 1.25,
        Faction.FLAME: 0.75,
        Faction.SKY: 0.75,
    },

    Faction.SKY: {
        Faction.FLAME: 1.25,
        Faction.NATURE: 1.25,
        Faction.GLACIAL: 0.75,
        Faction.LIGHTNING: 0.75,
    },

    Faction.TERRA: {
        Faction.GLACIAL: 1.25,
        Faction.LIGHTNING: 1.25,
        Faction.AQUATIC: 0.75,
        Faction.NATURE: 0.75,
    },

    Faction.GLACIAL: {
        Faction.SKY: 1.25,
        Faction.TERRA: 1.25,
        Faction.FLAME: 0.75,
    },

    Faction.LIGHTNING: {
        Faction.AQUATIC: 1.25,
        Faction.SKY: 1.25,
        Faction.TERRA: 0.75
    },

    Faction.SUNSHINE: {
        Faction.UNDEAD: 1.25,
        Faction.SUNSHINE: 1.25,
    },

    Faction.UNDEAD: {
        Faction.SUNSHINE: 1.25,
        Faction.UNDEAD: 1.25,
    }
}