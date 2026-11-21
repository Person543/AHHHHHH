import json
decks=json.load(open('out_scen/quiz_data.json'))
PLAN=[
("Day 1", "Read the cheat sheet out loud, top to bottom. Don't memorize yet - just see the whole map.", "ALL", "20 min"),
("Day 2", "Metasploit scenarios (SA). Quiz mode until 80%.", "SA", "Then re-read the Metasploit half of the cheat sheet."),
("Day 3", "Linux scenarios (SB). Quiz mode until 80%.", "SB", ""),
("Day 4", "Windows scenarios (SC). Quiz mode until 80%.", "SC", ""),
("Day 5", "Cross-book scenarios (SX) + re-quiz SA.", "SX,SA", "Say the 5 mnemonics from memory."),
("Day 6", "Mixed quiz, everything. Write down every miss.", "ALL", "Your miss list is your real study list."),
("Day 7", "Written mode only, everything. Type the answers from memory.", "ALL", "Slowest day, biggest payoff."),
("Day 8", "Re-quiz only what you missed on days 6-7, then a full mixed pass.", "ALL", ""),
("Day 9", "Cheat sheet from memory: cover it and rewrite the mnemonics and the Linux-vs-Windows table.", "ALL", "Then one mixed quiz pass."),
("Day 10", "Full mock: all 33 scenarios, no notes. Review every miss same day.", "ALL", ""),
]
tpl=open('template.html').read()
tpl=(tpl.replace('Cyber Ops Quiz Trainer','Cyber Ops Scenario Trainer')
        .replace('20-day plan','10-day plan')
        .replace('~45-60 min/day','~30-40 min/day'))
out=tpl.replace('/*DATA*/null',json.dumps(decks)).replace('/*PLAN*/null',json.dumps(PLAN))
open('out_scen/Cyber_Ops_SCENARIO_Trainer.html','w').write(out)
print(len(out))