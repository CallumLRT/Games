from enemy import Enemy
from rangedEnemy import RangedEnemy
from meleeEnemy import MeleeEnemy
from rock import Rock
from player import Player
from vector import Vector

class UPair:
    def __init__(self, fst, snd):
        self.fst = fst
        self.snd = snd

    def __hash__(self):
        return hash((min(hash(self.fst), hash(self.snd)),
                     max(hash(self.fst), hash(self.snd))))

    def __eq__(self, other):
        return ((self.fst == other.fst and self.snd == other.snd) or
                (self.fst == other.snd and self.snd == other.fst))

    def __ne__(self, other):
        return not self.__eq__(other)


class InteractionSet:
    def __init__(self, allObj):
        self.allObj = set(allObj)  # Turns list into a set
        self.inCollision = set()
        self.count = 0

    def update(self):
        for obj in self.allObj:
            if not isinstance(obj, Rock):
                obj.update()
        for obj1 in self.allObj:
            for obj2 in self.allObj:
                if obj1.collides(obj2):
                    if isinstance(obj1, Enemy):
                        obj1.set_target(False)
                        obj1.dazed()
                    if isinstance(obj2, Enemy):
                        obj2.set_target(False)
                        obj2.dazed()
                    if UPair(obj1, obj2) not in self.inCollision:
                        self.inCollision.add(UPair(obj1, obj2))
                        n = (obj1.pos - obj2.pos).normalize()
                        delta = 2 * n * (obj1.vel - obj2.vel).dot(n)
                        if isinstance(obj1, Rock):
                            delta = delta * 2
                        if isinstance(obj2, Rock):
                            delta = delta * 2
                        if not isinstance(obj1, Rock):
                            if not isinstance(obj2, Rock):
                                if not isinstance(obj1, Player):
                                    if not isinstance(obj2, Player):
                                        obj1.vel.subtract(delta)
                                        obj2.vel.add(delta)
                                    else:
                                        obj1.vel.subtract(delta)
                                else:
                                    obj2.vel.add(delta)
                            else:
                                obj1.vel.subtract(delta)
                        else:
                            obj2.vel.add(delta)
                    else:
                        self.inCollision.discard(UPair(obj1, obj2))
