from typing import List, Dict, Union

class Card:
    def __init__(self,
                 abilities: List[Dict[str, str]],
                 artists: List[str],
                 artists_text: str,
                 code: str,
                 color: str,
                 cost: int,
                 flavor_text: str,
                 foil_types: List[str],
                 full_identifier: str,
                 full_name: str,
                 full_text: str,
                 full_text_sections: List[str],
                 id: int,
                 images: Dict[str, str],
                 inkwell: bool,
                 lore: int,
                 name: str,
                 number: int,
                 rarity: str,
                 set_code: str,
                 simple_name: str,
                 story: str,
                 strength: int,
                 subtypes: List[str],
                 type: str,
                 version: str,
                 willpower: int):
        self.abilities = abilities
        self.artists = artists
        self.artists_text = artists_text
        self.code = code
        self.color = color
        self.cost = cost
        self.flavor_text = flavor_text
        self.foil_types = foil_types
        self.full_identifier = full_identifier
        self.full_name = full_name
        self.full_text = full_text
        self.full_text_sections = full_text_sections
        self.id = id
        self.images = images
        self.inkwell = inkwell
        self.lore = lore
        self.name = name
        self.number = number
        self.rarity = rarity
        self.set_code = set_code
        self.simple_name = simple_name
        self.story = story
        self.strength = strength
        self.subtypes = subtypes
        self.type = type
        self.version = version
        self.willpower = willpower

        self.is_drying = False
        self.is_exhausted = False

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            abilities=data.get('abilities', []),
            artists=data.get('artists', []),
            artists_text=data.get('artistsText', ''),
            code=data.get('code', ''),
            color=data.get('color', ''),
            cost=data.get('cost', 0),
            flavor_text=data.get('flavorText', ''),
            foil_types=data.get('foilTypes', []),
            full_identifier=data.get('fullIdentifier', ''),
            full_name=data.get('fullName', ''),
            full_text=data.get('fullText', ''),
            full_text_sections=data.get('fullTextSections', []),
            id=data.get('id', 0),
            images=data.get('images', {}),
            inkwell=data.get('inkwell', False),
            lore=data.get('lore', 0),
            name=data.get('name', ''),
            number=data.get('number', 0),
            rarity=data.get('rarity', ''),
            set_code=data.get('setCode', ''),
            simple_name=data.get('simpleName', ''),
            story=data.get('story', ''),
            strength=data.get('strength', 0),
            subtypes=data.get('subtypes', []),
            type=data.get('type', ''),
            version=data.get('version', ''),
            willpower=data.get('willpower', 0)
        )