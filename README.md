# NYTWordle 

## Overview
A Python program designed to assist players of the New York Times [Wordle](https://www.nytimes.com/games/wordle/index.html) puzzle. It suggests optimal starting words and refines guesses based on feedback to enhance your solving experience.

## Features
- **Getting Best Words**: 
  - To see a list of the **10 best words** to use based on current possibilities, type **`best`**.
  - To view a complete ranking list of all remaining possible words, type **`best all`**.
- **Word Selection**: Choose between a comprehensive list of English words (Not all of them are meaningful) or a common word (All have meanings) list.
- **Optimal Starting Word**: The program suggests the best starting word based on letter frequency analysis.
- **Feedback Processing**: After each guess, input feedback in the form of `0`, `1`, or `2` to refine future guesses:
  - `0`: Letter is not in the word.
  - `1`: Letter is in the word but in the wrong position.
  - `2`: Letter is correct and in the right position.

## Ranking Explanation
The ranking list for both the **`best`** and **`best all`** features is sorted based on letter frequency in the words of the list. For example, if 'a' is the most frequently seen letter in the remaining words, the words containing 'a' will have a better ranking. This approach helps in using words that eliminate more possibilities from the remaining options.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/FarnoodID/NYTWordle.git
   ```
2. Navigate to the project directory:
   ```bash
   cd NYTWordle
   ```
### Usage
1. Run the program:
   ```bash
   python NYTWordle.py
   ```
2. When prompted, choose whether to search in all English words (Not all of them are meaningful but you get to the solution faster) or just common words (All have meanings) by entering ``all`` or ``common``.
3. The program will suggest an optimal starting word based on your selection.
4. Enter your guess and provide feedback using the format described above.
## Example Interaction
If you guess "mouth" and receive feedback of Green, Blank, Blank, Yellow, Blank, you would enter:
  ```text
  20010
  ```
This indicates that:
  - 'm' is correct (position 1).
  - 'o', 'u', 'h' are not in the word.
  - 't' is in the word but in the wrong position.
