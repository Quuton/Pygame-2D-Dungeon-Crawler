class level:
    # array containing floor layout
    floors = []
    
    def __init__(self, floors: list['map'], name: str = None, defaultxpos: int = 0, defaultypos: int = 0, defaultfloor: int = 0, defaultdirection: int = 0, texturenames:list[str] = None) -> None:
        self.floors = floors
        self.name = name
        self.defaultypos = defaultypos
        self.defaultxpos = defaultxpos
        self.defaultfloor = defaultfloor
        self.defaultdirection = defaultdirection
        if texturenames is None:
            self.texturenames = ["default"]
        else:
            self.texturenames = texturenames
    class map:
        # level 2D array contains cell object, dictates if player can walk over or not cuz yknow walls, and can teleport, maybe damage, dark room
        layout = []

        def __init__(self, xsize: int, ysize: int, layout: list['cell']) -> None:
            self.xsize = xsize
            self.ysize = ysize
            self.layout = layout

        class cell:
            def __init__(self, sides: list['wall'], bottom: 'floor', eventid:str = None, eactive:bool = None) -> None:
                self.sides = sides
                self.bottom = bottom
                self.eventid = eventid
                self.eactive = eactive

            class wall:
                def __init__(self, texturegroup:int = 0, passthru: bool = True, transparent: bool = True) -> None:
                    # Allows for special texture, otherwise use default map texture
                    self.texturegroup = texturegroup
                    # If the player can go through
                    self.passthru = passthru
                    # if a wall should be rendered
                    self.transparent = transparent

            class floor:
                def __init__(self, texturegroup:int = 0, special:str = None, spid: int = None, sptarget: int = None, sptargetfloor: int = None, newdirection: int = None) -> None:
                    # Allows for special texture, otherwise use default map texture
                    self.texturegroup = texturegroup

    def default_texture():
        return ["default"]