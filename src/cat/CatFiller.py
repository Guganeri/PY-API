class CatFiller:
    
    id: str
    origin: str
    temperament: str
    description: str
    
    def __init__(self, id: str, origin: str, temperament: str, description: str):
        self.id = id
        self.origin = origin
        self.temperament = temperament
        self.description = description
    
    def __disc__(self): pass