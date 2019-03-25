class ProjectileCollision:
    def __init__(self, player, enemies):
        self.player = player

    def update(self, enemyProjectiles, friendlyProjectiles, rocks, rangedEnemies, meleeEnemies):
        for projectile in enemyProjectiles:
            if projectile.collides(self.player):
                self.player.health.damaged("Player", self.player, rangedEnemies, meleeEnemies)
                if projectile in enemyProjectiles:  # in case a projectile hits two or more things at once
                    enemyProjectiles.remove(projectile)
            else:
                for rock in rocks:
                    if projectile.collides(rock):
                        if projectile in enemyProjectiles:
                            enemyProjectiles.remove(projectile)

        for projectile in friendlyProjectiles:
            for enemy in rangedEnemies:
                if projectile.collides(enemy):
                    enemy.health.damaged("RangedEnemy", enemy, rangedEnemies, meleeEnemies)
                    if projectile in friendlyProjectiles:  # in case a projectile hits two or more things at once
                        friendlyProjectiles.remove(projectile)
                else:
                    for rock in rocks:
                        if projectile.collides(rock):
                            if projectile in friendlyProjectiles:
                                friendlyProjectiles.remove(projectile)

            for enemy in meleeEnemies:
                if projectile.collides(enemy):
                    enemy.health.damaged("MeleeEnemy", enemy, rangedEnemies, meleeEnemies)
                    if projectile in friendlyProjectiles:  # in case a projectile hits two or more things at once
                        friendlyProjectiles.remove(projectile)
                else:
                    for rock in rocks:
                        if projectile.collides(rock):
                            if projectile in friendlyProjectiles:
                                friendlyProjectiles.remove(projectile)
