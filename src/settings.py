class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 10
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_directio of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quicklu the alien point values increase
        self.score_scale = 1.5

        # Scoring settings
        self.alien_points = 50
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throghout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)