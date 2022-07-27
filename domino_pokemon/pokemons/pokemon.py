import requests
POKEMON_TYPE_ENDPOINT = "https://pokeapi.co/api/v2/type/"


class Pokemon:

    @staticmethod
    def final_damage_factor(pokemon_1_type, *pokemon_2_types):
        response = requests.get(url=f'{POKEMON_TYPE_ENDPOINT}/{pokemon_1_type}/')
        result = response.json()['damage_relations']
        double_damage_to = result['double_damage_to']
        half_damage_to = result['half_damage_to']
        no_damage_to = result['no_damage_to']

        damages_to_types = [double_damage_to, half_damage_to, no_damage_to]

        def single_damage_factor(damage_to_types, effectiveness):
            counter = 1
            for type_ in damage_to_types:
                for pokemon_type in pokemon_2_types:
                    if pokemon_type in type_['name']:
                        counter *= effectiveness
            return counter

        def get_final_effectiveness():
            i = 0
            eff = [2, 0.5, 0]
            counter = 1
            for damage_to_types in damages_to_types:
                counter *= single_damage_factor(damage_to_types, eff[i])
                i += 1
            return f'{counter}x'

        return get_final_effectiveness()
