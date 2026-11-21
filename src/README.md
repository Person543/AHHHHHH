# Cyber Ops Quiz Generator

Question banks + scripts that build the quiz import files and the offline quiz website.

## Files
- `bank_a.py`, `bank_b.py`, `bank_c.py`, `extras.py` - full question bank (267 questions): Metasploit book, Linux book, Windows book, cross-book compare.
- `cond_a.py`, `cond_b.py`, `cond_c.py`, `cond_x.py` - short question bank (134 questions).
- `build.py` / `build_short.py` - make the Quizlet, Anki, Blackboard, Moodle GIFT, Aiken and JSON files.
- `build_html.py` / `build_html_short.py` - make the offline quiz website from `template.html` (also holds the 20-day plan).

## Run (Python 3, no extra packages)
```
python3 build_short.py && python3 build_html_short.py   # short version -> out_short/
python3 -m http.server 8000 --directory out_short
Then press Cyber Ops Quiz Trainer
```
## New files (nothing from the old version was edited):
- scen_a.py, scen_b.py, scen_c.py, scen_x.py - the 33 scenario questions (Metasploit, Linux, Windows, Cross-book)
- build_scen.py - writes the Quizlet / Anki / Moodle / JSON files into out_scen/
- build_html_scen.py - fills template.html with the questions + 10-day plan -> out_scen/Cyber_Ops_SCENARIO_Trainer.html
- make_cheat.py - writes out_scen/Cyber_Ops_Cheat_Sheet.html
- template.html - unchanged copy from the original code (build_html_scen.py swaps the title, "20-day" -> "10-day" and the minutes-per-day text when it builds)

Run (Python 3 only, from this folder):
    python3 build_scen.py && python3 build_html_scen.py && python3 make_cheat.py
    python3 -m http.server 8000 --directory out_scen


## Question format
```
("mc", "question", ["option A","option B","option C","option D"], index_of_correct, "explanation"),
("sa", "question", "answer", "hook / explanation"),
```
Add or edit a tuple in any bank, then rerun the two commands. Multiple-choice options are shuffled on every build (fixed seed, so the order is the same each run).
