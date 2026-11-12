DECKS=[]
DECKS.append(("B1","Linux Ch.1 - Bash and Shells",[
("mc","Which is FALSE?",
 ["You reach Linux through terminals and pseudoterminals running shells","A shell acts differently based on how it's configured and started","Bash keeps state in options, variables and environment variables","Bash can't use the network, so attackers ignore it"],3,
 "Bash CAN talk over the network - reverse shells and exfil. That's why it matters to both sides."),
("sa","Which env variable is the security one, and why?","PATH. A writable folder early in PATH lets someone swap in a fake command.","Fix: trusted dirs only, never '.', use full paths."),
("sa","Who wants Bash history, who doesn't?","Admins want it recorded. Attackers make sure it isn't.","unset HISTFILE, HISTSIZE=0, set +o history, delete ~/.bash_history."),
("sa","Login vs non-login shell - why care?","They read different files, so the shell behaves differently. Login: /etc/profile + ~/.bash_profile. Non-login: ~/.bashrc.",""),
("sa","Two Bash conveniences from 1.7?","Aliases (shortcuts for commands) and jobs (several tasks in one session).","& , Ctrl+Z, jobs, fg, bg."),
]))
DECKS.append(("B2","Linux Ch.2 - Users and Groups",[
("mc","Which tool pairing is right?",
 ["useradd/userdel = low level; adduser/deluser = Perl scripts on Mint & Ubuntu; usermod = change a user","adduser is low level, useradd is a Perl script","usermod creates users","They're all the same command"],0,
 "2.4 exactly."),
("sa","The 4 account files?","/etc/passwd, /etc/shadow, /etc/group, /etc/gshadow.","Hook: passwd + shadow for users, group + gshadow for groups. Hashes live in shadow."),
("sa","3 states an account can be in?","Locked, unlocked, expired.","Lock = '!' in front of the hash (passwd -l)."),
("sa","Expired password vs expired account?","Expired password = change it at login. Expired account = you can't log in at all.",""),
("sa","What is /etc/nologin?","If that file exists, nobody but root can log in - and they see its message.","Used during maintenance."),
("sa","What does chfn change?","The user's name/office/phone info (the GECOS field in /etc/passwd).",""),
]))
DECKS.append(("B3","Linux Ch.3 - Passwords and PAM",[
("mc","Which is FALSE?",
 ["Hashes for local users sit in /etc/shadow","You can hash a password you already know and compare","John the Ripper guesses over and over","John reverses the hash to get the password back"],3,
 "Hashes are one way. Cracking = guess, hash, compare."),
("sa","What is PAM, and who can change it?","Pluggable Authentication Modules - how Linux authenticates you. Admins configure it, and attackers with enough privilege can too.","Config lives in /etc/pam.d."),
("sa","How does pam_exec.so get abused?","It runs any program during login, so an attacker gets a shell on every SSH attempt - even failed ones.",""),
("sa","What does pam_pwhistory.so do?","Stops people reusing old passwords.",""),
("sa","Read a shadow hash: $6$ vs $1$ vs $y$?","$1$ = MD5, $5$ = SHA-256, $6$ = SHA-512, $y$ = yescrypt. A '!' or '*' means no password login.",""),
("sa","Why does a salt matter?","Same password, different hash on every account - so precomputed tables are useless.",""),
]))
DECKS.append(("B4","Linux Ch.4 - Privileges and Login Logs",[
("mc","Which definition is wrong?",
 ["sudo = run a command as someone else, set up by admins","su = become another user","runuser = admin runs a command as another user","Polkit = command-line only, no GUI role"],3,
 "Polkit is the one used in GRAPHICAL environments."),
("sa","The 3 login record systems?","utmp (login & ssh), lastlog (PAM), systemd.","Hook: U-L-S."),
("sa","Which tool reads which?","utmp: who, w, last. lastlog file: lastlog. systemd: loginctl.","last reads wtmp history, lastb reads btmp failed logins."),
("sa","Why does having 3 records help defenders?","Different programs write them, so wiping one still leaves the login in the others.",""),
("sa","Where is sudo configured, and what edits it?","/etc/sudoers, edited with visudo (it checks your syntax first).","sudo -l shows what you can run."),
]))
DECKS.append(("B5","Linux Ch.5 - Processes and systemd",[
("mc","Why do attackers rename their process?",
 ["Because defenders hunt by name - but /proc/<pid>/exe still shows the real file","Renaming raises privileges","systemd requires it","To use less memory"],0,
 "5.6 plus the fix."),
("sa","5 process tools?","ps, pidof, pgrep, pstree, top.","Hook: Please Pick Pretty Process Trees."),
("sa","How do you talk to a running process?","Send it a signal.","SIGTERM 15 = polite, can be caught. SIGKILL 9 = instant, can't be caught."),
("sa","What's in /proc?","A folder per running process with its details - cmdline, exe, environ, fd.",""),
("sa","Who manages Linux startup, and who else uses it?","systemd (PID 1). Admins run services with it; attackers plant their own unit or timer for persistence.","systemctl enable/start/status, journalctl -u."),
]))
DECKS.append(("B6","Linux Ch.6 - Files and File Systems",[
("mc","Which is FALSE?",
 ["Files map to inodes on devices","A hard link is a second name for the same inode","A symlink just stores a path, so it breaks if the target goes away","Deleting the original always breaks a hard link"],3,
 "Hard links keep the data alive - only the link count drops. Symlinks are the fragile ones."),
("sa","Hard link vs symlink?","Hard = same inode, same file system, files only. Soft = a path, can cross file systems and point at folders.",""),
("sa","SUID, SGID, sticky bit?","SUID = runs as the file's owner. SGID = runs as the group. Sticky = in a shared folder, only the owner can delete their file (/tmp).","find / -perm -4000 hunts SUID."),
("sa","Basic permissions and the extras?","rwx for user, group, world. Extras: immutable (chattr +i) and ACLs (getfacl/setfacl).",""),
("sa","What does lsof show?","Open files and network sockets.",""),
("sa","Lost the root password - how does mounting save you?","Boot rescue media, mount the disk, chroot in, reset the password. Same trick reads a Windows disk.",""),
("sa","Why does the standard directory layout matter?","Every distro puts things in the same place: /etc config, /var logs, /home users, /usr software, /proc processes.",""),
]))
DECKS.append(("B7","Linux Ch.7 - SELinux and AppArmor",[
("mc","Which comparison is right?",
 ["SELinux = labels on everything, deny by default, tuned with Booleans. AppArmor = one profile per important program. Usually only one is on","Both always run together","AppArmor uses the 4-part context","SELinux only logs, never blocks"],0,
 "7.13 + chapter bullets."),
("sa","The 4 parts of an SELinux context?","User, role, type, level.","Hook: U aRe Totally Locked. Applied to users, files, processes and ports."),
("sa","SELinux's default behavior, and what simplifies it?","Blocks anything no rule allows. Booleans are the easy on/off switches for policies.",""),
("sa","SELinux modes and commands?","Enforcing, permissive (log only), disabled. getenforce to check, setenforce 0/1 to switch.","ls -Z shows contexts, restorecon fixes them."),
("sa","AppArmor: what does it protect, and what are the 2 modes?","Critical programs, each with a profile. Modes: enforce (block) and complain (log only).","aa-status shows them."),
("sa","What does aa-logprof do?","Reads the denials in the log and walks you through fixing the profile.","That's how passwd got its audit_write capability back."),
]))
DECKS.append(("B8","Linux Ch.8 - Software Management",[
("mc","Which mapping is right?",
 ["apt = Debian/Ubuntu/Mint, dnf & yum = Red Hat/Rocky/CentOS, zypper = SUSE","apt = SUSE, zypper = Ubuntu","yum = Ubuntu, apt = Rocky","Everything uses apt"],0,
 "8.7's four package managers."),
("sa","Where does software come from, and what must admins check?","Repositories - and that they're valid (signed with trusted GPG keys).","A fake repo = a supply-chain hack."),
("sa","What are Snap and Flatpak?","Ways to ship a program with its dependencies bundled in.","Downside: the bundle's libraries get patched by its publisher, not your distro."),
("sa","What can admins verify about installed software?","Its hashes - rpm -V, debsums, sha256sum.",""),
]))
