# Cross-book scenarios tying the whole kill chain + Linux-vs-Windows together.
DECKS=[("SX","Cross-Book - Big-Picture Scenarios",[
("sa","Put a full attack in Cyber Kill Chain order using the book's tools: msfvenom payload, phishing email, handler/Meterpreter, AV exclusion, recon.",
 "Recon -> Weaponize (msfvenom payload) -> Deliver (phishing) -> Exploit/Install (it runs, handler catches the callback) -> C2 (Meterpreter) -> Actions (recon, migrate, add AV exclusion to persist). Kill chain: Real Wizards Don't Exploit In Crowded Alleys.","Ties all books together. Misconfigs often beat CVEs as the way in."),
("sa","You need password hashes on both a Linux and a Windows box. Where is each, and what's the one-line difference in how users are identified?",
 "Linux: /etc/shadow. Windows: SAM (local) + ntds.dit (domain). Linux identifies users by UID numbers (0=root); Windows by SIDs (RID 500=Administrator).","Linux Ch.3 + Windows Ch.3/Ch.2."),
("sa","Compare the 'extra lockdown' layer and the 'background program' persistence spot on Linux vs Windows.",
 "Lockdown: Linux = SELinux or AppArmor; Windows = integrity levels (drive UAC). Background/persistence: Linux = systemd units/timers; Windows = services (Service Control Manager). Both used by admins and attackers.","Linux Ch.5/7 + Windows Ch.7/8."),
("sa","A defender asks how an attacker hides activity on each OS. Give the history/log trick for Linux vs Windows.",
 "Linux: clear bash history (unset HISTFILE) and know logins sit in 3 places (utmp/lastlog/systemd). Windows: cmd history dies with the session, PowerShell PSReadLine file can be deleted, and Base64 hides the command's content; logons show in event 4624 with limits.","Linux Ch.1/4 + Windows Ch.1/3."),
])]