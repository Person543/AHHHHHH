BOOKS={
"Metasploit & Meterpreter":[
("Ch.1 Foundations","Metasploit = pro offensive framework. Admin creds beat configuration (get a Meterpreter shell on a hardened Windows box). CVE = the bug's NamE, CVSS = its ScorE (0-10). Misconfigs >= CVEs and are often preferred. Kill Chain: Recon, Weaponize, Deliver, Exploit, Install, C2, Actions."),
("Ch.2 Meterpreter","Lives inside a process, in memory (file scans miss it). Does recon, file ops, run code, edit registry. Migrates HIGH->LOW privilege; what it sees = host process's privileges. Extend: run PowerShell/Python, read clipboard, ADSI domain recon."),
("Ch.3 Framework","7 modules: Every Pirate Always Plunders Every Empty Navy (exploit, payload, auxiliary, post, encoders, evasion, nop). STAGED = stub downloads rest (slash name), small space. STAGELESS = all-in-one (underscore name), bad network. REVERSE beats firewalls. Handler catches callback; run as job (exploit -j)."),
("Ch.4 Brute Force","Features: Users Want Time Delays (userlist, wordlist, time, defenses). Windows Wins, SMB is Speedy. Modules: smb_login, ssh_login. Linux shell can upgrade to Meterpreter. Defenses: lockout, rate-limit, MFA, strong passwords."),
("Ch.5 Phishing","Common first way in. Fake prompt (phish_windows_credentials) re-asks until the password is real; works from an UNPRIVILEGED session. .hta on old systems = just visiting the site. Web delivery = one-line download-and-run. Microsoft fights back: Protected View + block internet macros."),
("Ch.6 Malware","msfvenom: -p payload, -f format, -o out, -x real program, -k keep it working. Static = look without running; Dynamic = run and watch (strace/gdb). Whether it runs depends on the target's AV (Windows = Defender)."),
("Ch.7 Defender","Full AV. Tamper protection locks settings BUT admins can still add EXCLUSIONS (never scanned) = the blind spot. Quarantine can be restored. Registry-disable = old Windows only."),
],
"Linux":[
("Ch.1 Bash","PATH is the security env var (fake binary via '.' in PATH). Attackers kill history (unset HISTFILE). Shell differs by how it's started (login vs not). Bash talks over the network = reverse shells."),
("Ch.2 Users","Files: passwd, shadow, group, gshadow. UID 0 = root (2nd one = backdoor). '!' before hash = locked. Expired password = change at login; expired account = no login. useradd/userdel low-level; adduser/deluser = Perl (Ubuntu/Mint)."),
("Ch.3 Passwords/PAM","Hashes in /etc/shadow, one-way (John guesses). $1$=MD5 $5$=SHA256 $6$=SHA512 $y$=yescrypt. Salt kills rainbow tables. PAM authenticates; pam_exec.so = shell on every SSH attempt; pam_pwhistory.so = no reuse."),
("Ch.4 Privileges/Logs","sudo (set in /etc/sudoers via visudo), su = become user, runuser = admin runs as user, Polkit = GUI elevation. 3 login records U-L-S: utmp (who/w/last), lastlog (pam_lastlog), systemd (loginctl) - wiping one leaves the others."),
("Ch.5 Processes/systemd","Tools: Please Pick Pretty Process Trees (ps, pidof, pgrep, pstree, top). Signals: SIGKILL 9 uncatchable, SIGTERM 15 catchable. /proc/<pid>/exe = real file (defeats renaming). systemd = PID 1; unit/timer = persistence."),
("Ch.6 Files","rwx user/group/world. SUID=run as owner, SGID=as group, sticky=only owner deletes (/tmp). find / -perm -4000 finds SUID. Hard link=same inode; symlink=path (breaks if target gone). Mount the disk to reset a lost password. lsof = open files/sockets."),
("Ch.7 SELinux/AppArmor","Usually only ONE. SELinux = labels on everything, deny-by-default, Booleans; context = user:role:type:level (U aRe Totally Locked); modes enforcing/permissive/disabled. AppArmor = profile per program (enforce/complain); aa-logprof fixes from denials. SELinux=RedHat/Rocky, AppArmor=Ubuntu/SUSE."),
("Ch.8 Software","apt=Debian/Ubuntu/Mint, dnf/yum=RedHat/Rocky, zypper=SUSE. Repos must be valid (GPG-signed). Snap/Flatpak bundle dependencies (publisher patches them). Verify hashes: rpm -V, debsums."),
],
"Windows":[
("Ch.1 cmd/PowerShell","PowerShell = modern (runs on Linux too); obfuscate via Base64 -EncodedCommand or downloaded modules. cmd runs a registry AutoRun at startup + keeps history. Env var scopes: Process, User, Machine."),
("Ch.2 Users/Groups","SIDs identify (well-known S-1-5-18=SYSTEM, RID 500=Admin, 501=Guest). Local data=SAM; domain data=Active Directory. Same-name domain vs local group = different (different SIDs); domain membership != local membership."),
("Ch.3 Logons/Hashes","Logon = login ID + access tokens. UAC = use a privileged token (set in registry/group policy). Hashes = NTLM in SAM (local) + ntds.dit (domain); protected even from SYSTEM; pull as Admin/Backup Operator. Pass-the-hash = use the hash, don't crack it."),
("Ch.4 Files","Mark of the Web = NTFS alternate data stream (Zone.Identifier); .iso/.vhd and FAT32 drop it. Names: full case-insensitive or 8.3 short. Hard link=files, junction=dirs, symlink=admin-only. Several timestamps."),
("Ch.5 Access Control","Security descriptor = Only Good Dogs Sit First (Owner, Group, DACL, SACL, Flags). DACL=access (Door), SACL=logging (Security camera). Tools: icacls, Get-Acl, AccessChk/AccessEnum; SDDL = string form. Sticky Keys attack: own sethc.exe -> cmd.exe -> SYSTEM; WRP defends."),
("Ch.6 Registry","Keys/subkeys/values; mostly hive files (System32\\config, NTUSER.DAT), some volatile. Keys are securable (own DACL). Tools: Registry Editor, reg, PowerShell. Roots: HKLM, HKCU, HKU, HKCR, HKCC. Persistence: Run/RunOnce, Services."),
("Ch.7 Processes","App = process(es) = thread(s). Defenders check the PARENT; attackers spoof it (Word spawning PowerShell = red flag). Integrity levels Low<Medium<High<System drive UAC. Know the normal tree (svchost's parent = services.exe)."),
("Ch.8 Services","Background, no user launch; managed via Service Control program (sc, net, PsService, PowerShell). Accounts: LocalSystem > NetworkService > LocalService. Abuse: unquoted path + weak perms = escalation. Defined in HKLM\\SYSTEM\\CurrentControlSet\\Services."),
],
}
MNEMONICS=[
"Kill Chain: <b>Real Wizards Don't Exploit In Crowded Alleys</b> (Recon, Weaponize, Deliver, Exploit, Install, C2, Actions)",
"7 modules: <b>Every Pirate Always Plunders Every Empty Navy</b>",
"Staged vs stageless: <b>slash = staged</b> (downloads rest), <b>underscore = stageless</b> (all-in-one)",
"Brute force features: <b>Users Want Time Delays</b> &middot; speed: <b>Windows Wins, SMB is Speedy</b>",
"Linux logins: <b>U-L-S</b> (utmp, lastlog, systemd)",
"Process tools: <b>Please Pick Pretty Process Trees</b>",
"SELinux context: <b>U aRe Totally Locked</b> (user, role, type, level)",
"Security descriptor: <b>Only Good Dogs Sit First</b> (Owner, Group, DACL, SACL, Flags) &middot; DACL=Door, SACL=Security camera",
"CVE = <b>NamE</b>, CVSS = <b>ScorE</b>",
]
TABLE=[
("Password hashes","/etc/shadow","SAM (local) + ntds.dit (domain), NTLM"),
("Identify users","UID numbers (0=root)","SIDs (RID 500=Admin)"),
("Permissions","rwx + SUID/SGID/sticky + ACLs","Security descriptor: Owner/Group/DACL/SACL/Flags"),
("Get elevated","sudo, su, runuser, Polkit","UAC (token), runas"),
("Lockdown layer","SELinux or AppArmor","Integrity levels (drive UAC)"),
("Background/persistence","systemd units & timers","Services (Service Control Manager)"),
("Login records","utmp, lastlog, systemd","Event 4624 (query user, psloggedon)"),
("Hide history","unset HISTFILE","Delete PSReadLine file; Base64 hides content"),
]
h=['<!DOCTYPE html><html><head><meta charset="utf-8"><title>Cyber Ops Cheat Sheet</title><style>',
"body{font:12px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;color:#15181f;margin:0;padding:16px;background:#fff}",
"h1{font-size:19px;margin:0 0 4px}.sub{color:#555;margin:0 0 12px;font-size:12px}",
".cols{column-count:3;column-gap:14px}@media(max-width:1100px){.cols{column-count:2}}@media(max-width:700px){.cols{column-count:1}}",
".book{break-inside:avoid;margin:0 0 10px}.bh{background:#1f2a44;color:#fff;font-weight:700;padding:4px 8px;border-radius:5px;font-size:12px}",
".ch{break-inside:avoid;margin:5px 0 6px}.ct{font-weight:700;color:#1f2a44}.cb{margin:1px 0 0}",
".box{break-inside:avoid;border:1px solid #d5dae5;border-radius:7px;padding:8px 10px;margin:0 0 10px;background:#f7f9fc}",
".box h2{font-size:13px;margin:0 0 5px;color:#1f2a44}.box li{margin:2px 0}",
"table{width:100%;border-collapse:collapse;font-size:11px}td,th{border:1px solid #ccd3e0;padding:3px 5px;text-align:left;vertical-align:top}th{background:#eef1f7}",
"@media print{body{padding:0}.cols{column-count:3}}",
"</style></head><body>",
"<h1>Cyber Ops &mdash; One-Page Cheat Sheet</h1>",
"<p class='sub'>Everything from the 3 books, condensed. Learn the mnemonics box and the Linux-vs-Windows table first.</p>",
"<div class='box'><h2>Mnemonics (memorize these first)</h2><ul>"]
for m in MNEMONICS: h.append(f"<li>{m}</li>")
h.append("</ul></div>")
h.append("<div class='box'><h2>Linux vs Windows (the compare questions)</h2><table><tr><th>Task</th><th>Linux</th><th>Windows</th></tr>")
for a,b,c in TABLE: h.append(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>")
h.append("</table></div>")
h.append("<div class='cols'>")
for book,chs in BOOKS.items():
    h.append(f"<div class='book'><div class='bh'>{book}</div>")
    for t,b in chs: h.append(f"<div class='ch'><span class='ct'>{t}:</span> <span class='cb'>{b}</span></div>")
    h.append("</div>")
h.append("</div></body></html>")
open('out_scen/Cyber_Ops_Cheat_Sheet.html','w').write('\n'.join(h))
print("ok")