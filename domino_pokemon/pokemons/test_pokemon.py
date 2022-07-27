from unittest import TestCase


class TestPokemon(TestCase):
    def test_final_damage_factor(self):
        from pokemon import Pokemon
        pokemon = Pokemon()
        self.assertEqual(pokemon.final_damage_factor('fire', 'grass'), '2x')
        self.assertEqual(pokemon.final_damage_factor('fighting', 'ice', 'rock'), '4x')
        self.assertEqual(pokemon.final_damage_factor('psychic', 'poison', 'dark'), '0x')
        self.assertEqual(pokemon.final_damage_factor('water', 'normal'), '1x')
        self.assertEqual(pokemon.final_damage_factor('fire', 'rock'), '0.5x')
