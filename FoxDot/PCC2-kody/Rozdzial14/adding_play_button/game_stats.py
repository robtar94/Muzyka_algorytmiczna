class GameStats:
    """Monitorowanie danych statystycznych w grze."""
    
    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Uruchomienie gry w stanie nieaktywnym.
        self.game_active = False
        
    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry."""
        self.ships_left = self.settings.ship_limit