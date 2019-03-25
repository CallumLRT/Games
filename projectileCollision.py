class ProjectileCollision:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def update(self, enemyProjectiles, friendlyProjectiles):
        for projectile in enemyProjectiles:
            if projectile.collides(self.player):
                enemyProjectiles.remove(projectile)
                self.player.health.damaged()

        for projectile in friendlyProjectiles:
            for enemy in self.enemies:
                if projectile.collides(enemy):
                    friendlyProjectiles.remove(projectile)
                    enemy.health.damaged()
