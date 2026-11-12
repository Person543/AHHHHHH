import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
decks=json.load(open(os.path.join(HERE,'out_short','quiz_data.json')))
PLAN=[
("Day 1","Metasploit Ch.1 Foundations + Ch.2 Meterpreter","A1,A2","Learn mode then Quiz each deck once. Aim 80%."),
("Day 2","Metasploit Ch.3 The Framework","A3","Memorize the 7 module types and staged vs stageless. Write the staged/stageless answer out by hand."),
("Day 3","Metasploit Ch.4 Brute Force + Ch.5 Phishing","A4,A5",""),
("Day 4","Metasploit Ch.6 Malware + Ch.7 Defender","A6,A7","Then re-quiz A1-A3."),
("Day 5","REVIEW: all Metasploit","A1,A2,A3,A4,A5,A6,A7","Mixed quiz. Anything under 80% goes on your weak list."),
("Day 6","Linux Ch.1 Bash + Ch.2 Users/Groups","B1,B2",""),
("Day 7","Linux Ch.3 Passwords/PAM + Ch.4 sudo & Logs","B3,B4","Re-quiz A4-A7 (review 2)."),
("Day 8","Linux Ch.5 Processes/systemd + Ch.6 Files","B5,B6",""),
("Day 9","Linux Ch.7 SELinux/AppArmor + Ch.8 Software","B7,B8","SELinux vs AppArmor one-liners out loud."),
("Day 10","REVIEW: all Linux","B1,B2,B3,B4,B5,B6,B7,B8","Mixed quiz + re-quiz your weak list."),
("Day 11","Windows Ch.1 cmd/PowerShell + Ch.2 Users/Groups","C1,C2",""),
("Day 12","Windows Ch.3 Logons, Tokens, UAC, Hashes","C3","Densest chapter - do it alone. Write out pass-the-hash."),
("Day 13","Windows Ch.4 Files + Ch.5 Access Control","C4,C5","Write out the Sticky Keys attack and the 4 security descriptor parts."),
("Day 14","HALFWAY REVIEW: Metasploit + Linux mixed","A1,A3,A5,A7,B2,B4,B6,B8","Quiz only, no flashcards. Track score."),
("Day 15","Windows Ch.6 Registry + Ch.7 Processes","C6,C7","5 root keys, hive locations, integrity levels, core process tree."),
("Day 16","Windows Ch.8 Services + start Cross-Book","C8,X",""),
("Day 17","REVIEW: all Windows","C1,C2,C3,C4,C5,C6,C7,C8","Mixed quiz + weak list."),
("Day 18","Cross-book compare & contrast","X","Say each Linux-vs-Windows pair out loud from memory, then check."),
("Day 19","SHORT-ANSWER DRILL","ALL","Write mode only, every chapter. These are the exam-style questions."),
("Day 20","FULL MOCK EXAM","ALL","Quiz mode, all decks, shuffled, no notes. Review every miss the same day."),
]
tpl = open(os.path.join(HERE,'template.html')).read()
out = tpl.replace('/*DATA*/null', json.dumps(decks)).replace('/*PLAN*/null', json.dumps(PLAN))
open(os.path.join(HERE,'out_short','Cyber_Ops_Quiz_SHORT_Study_Site.html'),'w').write(out)
print(len(out))
