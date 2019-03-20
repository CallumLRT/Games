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

class MeleeInteractionSet:
    def __init__(self, melee_enemies):
        self.meleeSet = set(melee_enemies)
        self.inCollision = set()

    def update(self):
        for e in self.meleeSet:
            e.update()
        for e1 in self.meleeSet:
            for e2 in self.meleeSet:
                if e1.collides(e2):
                    e1.dazed()
                    e2.dazed()
                    e1.set_target(False)
                    e2.set_target(False)
                    if UPair(e1, e2) not in self.inCollision:
                        self.inCollision.add(UPair(e1, e2))
                        n = (e1.pos - e2.pos).normalize()
                        delta = n * (e1.vel - e2.vel).dot(n)
                        e1.vel.subtract(delta)
                        e2.vel.add(delta)
                    else:
                        self.inCollision.discard(UPair(e1, e2))


