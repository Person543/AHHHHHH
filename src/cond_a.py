DECKS=[]
DECKS.append(("A1","Metasploit Ch.1 - Foundations",[
("mc","Which one is FALSE?",
 ["Labs are built with virtualization so you get hands-on time","Kill Chain and MITRE ATT&CK give attacks a structure","CVE names the bug, CVSS scores how bad it is","Attackers skip misconfigurations and only chase CVEs"],3,
 "Misconfigs are at least as important as CVEs, and attackers often PREFER them (no exploit needed, no alert)."),
("sa","CVE vs CVSS?","CVE = the bug's name. CVSS = the bug's score (0-10).","Hook: NamE vs ScorE."),
("sa","Cyber Kill Chain, 7 steps?","Recon, Weaponize, Deliver, Exploit, Install, C2, Actions.","Hook: Real Wizards Don't Exploit In Crowded Alleys."),
("sa","ATT&CK: tactic vs technique?","Tactic = the goal. Technique = the trick used to get it.","Goal vs how."),
("sa","Two more Ch.1 takeaways?","Metasploit = a professional framework for offense. Pros keep the highest ethical standards.","Plus: admin creds on Windows = a Meterpreter shell."),
]))
DECKS.append(("A2","Metasploit Ch.2 - Meterpreter",[
("mc","Meterpreter migration goes which way?",
 ["From a higher privileged process down to lower privileged ones","From low up to SYSTEM","Only sideways, same user","It cannot migrate"],0,
 "2.4: high -> low. What it can see depends on the privileges of the process it sits in."),
("sa","4 things Meterpreter lets you do?","Recon the system, recon the network, mess with files, run code, change the registry.","Hook: Look, Look, Take, Run, Edit."),
("sa","Where does Meterpreter live?","Inside a running process, in memory - not a file on disk. That's why file scanning misses it.","migrate <PID> moves it."),
("sa","3 ways Meterpreter gets extended?","Run PowerShell or Python on the target, read the clipboard, use ADSI to scope out the domain.","Hook: Script, Steal, Snoop."),
]))
DECKS.append(("A3","Metasploit Ch.3 - The Framework",[
("mc","The 7 module types?",
 ["exploit, payload, auxiliary, post, encoders, evasion, nop","exploit, scanner, trojan, rootkit, nop","payload, listener, dropper, loader, shell","recon, exploit, post, report"],0,
 "Hook: Every Pirate Always Plunders Every Empty Navy."),
("sa","EXAM: Staged vs stageless payload - what's the difference?","Staged = tiny stub lands first, then downloads the rest. Stageless = the whole thing ships at once.","Hook: slash = staged (meterpreter/reverse_tcp), underscore = stageless (meterpreter_reverse_tcp)."),
("sa","EXAM: When do you pick each one?","Staged when space is tiny (small buffer) - it's small. Stageless when the network is shaky or you only get one connection - it needs nothing else.","Small hole = staged. Bad network = stageless."),
("sa","Bind vs reverse payload - which beats a firewall?","Reverse: the target calls out to you (LHOST/LPORT). Bind: the target listens and you call in. Reverse wins, since outbound is usually allowed.","Not all payloads call back - some just run commands, like creating a user."),
("sa","What are handlers and jobs?","A handler catches the callback. Run it as a job (exploit -j) so it sits in the background. Keylogging can run as a job too.","sessions -l to list, sessions -i to use."),
("sa","3 ways Metasploit is customized?","It logs your commands, saves results in its database, and can be scripted.","spool, msfdb, resource scripts."),
]))
DECKS.append(("A4","Metasploit Ch.4 - Brute Force Attacks",[
("mc","Which is FALSE?",
 ["The 4 features are userlist, wordlist, time, defenses","Kali ships password lists and you can build your own","Metasploit brute forces SMB and SSH","Linux is faster to brute force than Windows, and SSH beats SMB"],3,
 "It's the reverse: Windows is faster than Linux, SMB is faster than SSH. Hook: Windows Wins, SMB is Speedy."),
("sa","4 features of a brute force attack?","Userlist, wordlist, time it takes, defenses in the way.","Hook: Users Want Time Delays."),
("sa","Shells on a Linux target?","You can get a plain Linux shell or Meterpreter. Upgrade the plain one with sessions -u.",""),
("sa","2 non-Metasploit brute force tools?","NetExec and CrackMapExec. You can also write your own.",""),
("sa","Where do wordlists come from?","Kali's built-in lists (rockyou.txt) or ones you generate yourself (crunch, cewl).",""),
("sa","What stops a brute force attack?","Lockout, rate limiting, strong passwords, MFA, SSH keys only, alerts on failed logins.","These are the 'defenses' feature."),
]))
DECKS.append(("A5","Metasploit Ch.5 - Phishing Attacks",[
("mc","Which is FALSE?",
 ["Phishing is a common first way in","Modules build phishing docs for Microsoft Office, LibreOffice and OpenOffice","Web delivery scripts let you build custom phishing","Microsoft's mitigations can't be beaten, so Office phishing is dead"],3,
 "Office suites have had bugs that evade the mitigations, and Metasploit has modules for them."),
("sa","What's special about a malicious .hta file?","On older systems, just visiting the site is enough - no opening a file.",""),
("sa","Unprivileged session on a Windows desktop - what can you still get?","Phish the logged-on user for their domain or local password.","phish_windows_credentials - it keeps re-asking until the password is real."),
("sa","What is web delivery?","A one-line command you host; when it runs on the target it pulls your payload into memory.",""),
("sa","How does Microsoft fight phishing docs?","Protected View and blocking macros in files from the internet, so the user has to click Enable Content.",""),
]))
DECKS.append(("A6","Metasploit Ch.6 - Malware",[
("mc","Which is FALSE?",
 ["msfvenom makes stand-alone malware in many formats","It can hide malware in a real Windows program and keep that program working","It can spit out source code you compile yourself","Encoding the payload reliably beats modern antivirus"],3,
 "Encoders dodge bad characters, not AV. Modern AV watches behavior, memory and the cloud."),
("sa","msfvenom flags: -p, -f, -o, -x, -k?","-p payload, -f format, -o output file, -x real program to hide in, -k keep that program working.","-x -k = the lure still does what the victim expects."),
("sa","Static vs dynamic analysis?","Static = look at the file without running it. Dynamic = run it and watch.","Static: strings, hashes, Ghidra. Dynamic on Linux: strace, gdb."),
("sa","What decides if your malware runs on the target?","The target's antivirus. Windows ships with Microsoft Defender.",""),
]))
DECKS.append(("A7","Metasploit Ch.7 - Antivirus / Defender",[
("mc","Tamper protection is ON. What can an admin still do?",
 ["Add exclusions - and excluded stuff is never scanned","Nothing, every setting is locked","Disable Defender in the registry, still supported","Only empty quarantine"],0,
 "7.9: this is the big one. Tamper protection locks settings, but exclusions still go in - a blind spot without turning Defender off."),
("sa","Where do Defender's removed threats go?","Quarantine on the system - and they can be restored.",""),
("sa","Can you disable Defender in the registry?","Old Windows, yes. Current Windows, no - not supported anymore.",""),
("sa","What does this chapter NOT teach?","How to change malware to get past Defender.",""),
("sa","How do you manage Defender from a prompt?","MpCmdRun.exe, or PowerShell: Get-MpComputerStatus, Get/Set-MpPreference, Add-MpPreference -ExclusionPath, Start-MpScan.","Quick scan = usual hiding spots. Full scan = every file."),
]))
