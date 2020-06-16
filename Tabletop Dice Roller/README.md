# Tabletop Dice Roller

This is a simple dice rolling program for tabletop role playing games. You can set it to roll multiple dice of any size as well as add modifiers. It is written in Python. You can give it commands to do something simple as rolling a six-sided die or rolling several multiples of different dice while adding modifiers.

## Table of Contents
Coming soon!

## Usage
Since this program isn't compiled yet, you can run it by opening diceroller.py (in the Source Code folder) in Python.

The program will prompt you to enter a dice roll.

> Enter dice roll (in the format of 3d6 d10 -2): ___

See the examples for how to roll dice with the program.

## Examples

### Example 1: Single Die
What we're rolling:
> a single six-sided die

Input:
> d6

Program Display:  
> Enter dice roll (in the format of 3d6 d10 -2): d6
>
> +4 1d6 [4]
>
> Total: 4

### Example 2: Multiple Dice of a Single Type
What we're rolling:
> three eight-sided dice

Input:
> 3d8

Program Display:
> Enter dice roll (in the format of 3d6 d10 -2): 3d8
>
> +19 3d8 [6, 6, 7]
>
> Total: 19

### Example 3: Multiple Dice of Different Types
What we're rolling:
> two four-sided dice, another set of five four-sided dice, and three eight-sided dice

Input:
> 2d4 5d4 3d8

Program Display:
> Enter dice roll (in the format of 3d6 d10 -2): 2d4 5d4 3d8
>
> +3 2d4 [1, 2]
>
> +17 5d4 [4, 3, 3, 3, 4]
>
> +16 3d8 [7, 1, 8]
>
> Total: 36

### Example 4: Adding Positive Modifiers
What we're rolling:
> an eight-sided die with a modifier of positive 3

Input:
> d8 3

Program Display:
> Enter dice roll (in the format of 3d6 d10 -2): d8 3
>
> +7 1d8 [7]
>
> +3
>
> Total: 10


### Example 5: Adding Negative Modifiers


What we're rolling:
> a six-sided die with a modifier of negative 2

Input:
> d6 -2

Program Display:
> Enter dice roll (in the format of 3d6 d10 -2): d6 -2
>
> +1 1d6 [1]
>
> -2
>
> Total: -1



### Example 5: Nontraditional Dice
What we're rolling:
> two seventeen-sided dice and a four-hundred-ninety-seven-sided die

Input:
> 2d17 d497

Program Display:
>Enter dice roll (in the format of 3d6 d10 -2): 2d17 d497
>
>+12 2d17 [9, 3]
>
>+305 1d497 [305]
>
>Total: 317

# Future Plans
- [ ] Compile the program so it can run cross platform without a Python installation using PyInstaller
- [ ] Customizable presets for common dice rolls
- [ ] GUI interface

# Known Issues
- None yet, but I'll add them here as I find them