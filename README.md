# Dominos alogrithm and Pokemon
This Repository shows the solution of two problems mentioned below.

# Dominos algorithm Explanation
Dominos are represented in the form of a string that consists of the following characters:

| - domino stands<br />
/ - domino falls to the right<br />
\ - domino falls to the left

- First task: Write an algorithm that determines a new literal containing the above characters<br />
after X iterations during which changes occur, X being the input parameter.<br />

  Example input string:<br />

  || // || \ || / \ |<br />

  Output after 1 iteration should be:<br />

  || /// \\ || / \ |<br />

- Second task: Write a reverse algorithm that shows what the sequence of domino looked like<br />
  before applying X iterations of the algorithm from the first task.
  
  Example input string:<br />

  || //// \\\ | //// |
  
  Output after 2 iteration should be:<br />

  || // |||| \ | // |||

# Pokemon Explanation
In the world of Pokemon, each type of Pokemon when fighting can possibly cause damage to another one.<br /><br />
If the attack is **very effective** against another type the damage factor equals **2x**.<br />
If the attack is **less effective** against another type the damage factor equals **0.5x**.<br />
If the attack **has no efect** on another type the damage factor equals **0x**.<br />

For example the water type works well against the fire type, which results in double damage.

Some Pokemons can have **several types** -<br />
in this case, the damage factor against each of them must be taken into account (**multiplied**)

- Task: Write a program that, based on the attacking Pokemons type,<br />
  calculates the damage factor against a pokemon of a given type (or types)

  Example input data:

   - fire vs. grass
   - fighting vs. ice rock
   - psychic vs. poison dark
   - water vs. normal
   - fire vs. rock

  Output data:

    - 2x
    - 4x
    - 0x
    - 1x
    - 0.5x
  
  The app uses **PokeAPI**: <br />
  https://pokeapi.co/api/v2/type/ysznetype}
  

## Quick Start
Installation Steps
```bash
git clone https://github.com/Woodchucks/Domino_Pokemon.git
pip install requests
```
