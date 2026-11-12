DECKS=[]
DECKS.append(("C1","Windows Ch.1 - cmd, PowerShell, Env Variables",[
("mc","Which is FALSE?",
 ["cmd runs commands stored in the registry when it starts","cmd records its history","PowerShell is the modern, extendable shell and now runs on Linux too","Batch and VBScript are gone from Windows"],3,
 "1.8/Ch1: the old batch scripts and VBScript still work."),
("sa","What does cmd run at startup, and why do attackers like it?","The AutoRun value in the registry - so their command runs every time cmd opens.","Quiet persistence inside a trusted program."),
("sa","What can PowerShell be extended with?",".NET, and the older COM, DCOM and COM+ objects. Modules can be downloaded and added.",""),
("sa","PowerShell history: how many ways, plus what?","Two history methods, plus a full transcript if you turn it on.","Session history (Get-History, gone at close) + PSReadLine file (survives reboot) + Start-Transcript."),
("sa","Two ways to obfuscate PowerShell?","Base64-encoded commands (-EncodedCommand) and downloaded modules.",""),
("sa","Env variable scopes, and how you set them?","Process, User, Machine. Set with set / $env: (temporary) or setx and the GUI (permanent).",""),
]))
DECKS.append(("C2","Windows Ch.2 - Users and Groups",[
("mc","Which is FALSE?",
 ["Every user and group has a SID; some well-known SIDs are the same everywhere","Local account data lives in the SAM; domain account data lives in Active Directory","Users and groups control access, rights and privileges","A domain group and a local group with the same name are the same group"],3,
 "2.10: they're different, and being in the domain group does NOT put you in the local group."),
("sa","Local user vs domain user?","Local = one system, stored in that system's SAM. Domain = the whole domain plus trusting domains and forests, stored in Active Directory.",""),
("sa","4 special Windows accounts?","Administrator, NT AUTHORITY\\SYSTEM, Guest, machine accounts.","SYSTEM = the most local power; on the network it shows up as the computer account."),
("sa","Local group vs domain group?","Local group gives rights on one system. Domain group gives rights across the domain.",""),
("sa","What is a well-known SID? One example.","A SID that's identical on every Windows system. S-1-5-18 = SYSTEM; RID 500 = Administrator.",""),
]))
DECKS.append(("C3","Windows Ch.3 - Logons, Tokens, UAC, Hashes",[
("mc","Where are Windows password hashes, and in what format?",
 ["NTLM hashes in the local SAM and in ntds.dit on domain controllers","SHA-512 in /etc/shadow","bcrypt in HKCU","Plaintext in the registry"],0,
 "3.6. They're protected - even SYSTEM can't read them directly."),
("sa","You log on to Windows - what do you get?","A login ID and one or more access tokens.","Logon types: 2 interactive, 3 network, 10 RDP."),
("sa","What does UAC do, and what controls it?","Lets you use a privileged token when you need it. Controlled by registry policies, set by group policy or local security policy.",""),
("sa","Hashes are protected from SYSTEM - so how do attackers get them?","Windows tools run from an Administrator or Backup Operator account.","Backup Operators can read protected files, which is why it's basically an admin group."),
("sa","Two things to do with a stolen hash?","Crack it (John the Ripper) or pass-the-hash - use the hash itself instead of the password.",""),
("sa","Privileges and rights - what are they for?","Fine-grained control over what a user can do.","whoami /priv lists yours."),
("sa","Finding who's logged on - what's the catch?","There are several ways (query user, psloggedon, WMI, event 4624) but every one of them has limitations.",""),
]))
DECKS.append(("C4","Windows Ch.4 - Files",[
("mc","Why do attackers ship payloads inside .iso or .vhd files?",
 ["Those containers avoid the Mark of the Web, and marked files get extra scrutiny","They download faster","They can't be scanned","Windows auto-trusts them"],0,
 "Ch4. MOTW is how Windows tracks internet downloads."),
("sa","What is the Mark of the Web stored in?","An NTFS alternate data stream - one file holding more than one stream.","Copy to FAT32 and the mark is gone."),
("sa","Two ways to name a Windows file?","The full case-insensitive name, or the old 8.3 short name (PROGRA~1).","Files also carry attributes (hidden, read only) and several timestamps."),
("sa","Hard link vs junction vs symlink in Windows?","Hard link = between files. Junction = between directories. Symlink = admin-made, can point at relative or network paths.","Shortcuts (.lnk) are just files that point somewhere."),
("sa","Two special Windows file locations?","The hidden desktop.ini in each folder, and C:\\Users\\Public.",""),
("sa","What manages Windows files?","File Explorer, command-line tools and PowerShell.",""),
]))
DECKS.append(("C5","Windows Ch.5 - Access Control",[
("mc","What are the 4 parts of a security descriptor?",
 ["Owner SID + primary group, DACL, SACL, flags","User, role, type, level","Read, write, execute, deny","Owner, group, world, other"],0,
 "5.10. Hook: Only Good Dogs Sit First - Owner, Group, DACL, SACL, Flags."),
("sa","DACL vs SACL?","DACL = who gets in (access). SACL = what gets logged (auditing).","Hook: Door vs Security camera."),
("sa","Which objects have a security descriptor?","Securable objects: files, directories, registry items, processes.",""),
("sa","Tools for viewing and setting permissions?","PowerShell (Get-Acl/Set-Acl) and icacls. Sysinternals AccessChk and AccessEnum to look around. File Explorer works but its interface has subtle issues.","SDDL = permissions written as a string."),
("sa","Windows protects some files even from SYSTEM. Who can still change them, and what attack uses that?","Admins, or anyone with SeTakeOwnershipPrivilege or SeRestorePrivilege - they take ownership first. That's the Sticky Keys attack.","Replace sethc.exe with cmd.exe, hit Shift 5 times at the lock screen = SYSTEM shell."),
("sa","What defends against that?","Windows Resource Protection.",""),
]))
DECKS.append(("C6","Windows Ch.6 - The Registry",[
("mc","Which is FALSE?",
 ["The registry is keys, subkeys and values holding data","Most keys live in hive files on disk","Some keys are volatile and built while the system runs","Registry keys have no permissions"],3,
 "6.5: keys and values are securable objects with a DACL, plus extra registry-specific permissions."),
("sa","3 ways to work with the registry?","Registry Editor (GUI), the reg command, and PowerShell (with .NET).",""),
("sa","The 5 root keys?","HKLM (system), HKCU (you), HKU (all users), HKCR (file types/COM), HKCC (hardware profile).",""),
("sa","Where do hive files live?","System hives in C:\\Windows\\System32\\config; your own hive is NTUSER.DAT in your profile.",""),
("sa","Two registry spots attackers use for persistence?","The Run / RunOnce keys and the Services key. (Plus cmd's AutoRun from Ch.1.)",""),
]))
DECKS.append(("C7","Windows Ch.7 - Processes",[
("mc","Defenders check the parent process. What do attackers do?",
 ["Obfuscate (spoof) their parent so they look like a child of something normal","Rename the kernel","Delete the process list","Nothing - parents can't be faked"],0,
 "Ch7. Red flag: Word spawning PowerShell."),
("sa","Application vs process vs thread?","An application is a program running one or more processes, and each process runs one or more threads.",""),
("sa","Tools for viewing and managing processes?","Command-line tools (tasklist/taskkill), Task Manager, Process Explorer, PowerShell (Get-Process).",""),
("sa","What are integrity levels used for?","They rank processes and objects, and they're what makes UAC work.","Low < Medium (normal user) < High (elevated admin) < System."),
("sa","Why learn the normal Windows processes?","So an odd one stands out - like svchost.exe whose parent isn't services.exe, or lsass.exe running from the wrong folder.","Normal chain: System > smss > wininit > services/lsass; winlogon > userinit > explorer."),
]))
DECKS.append(("C8","Windows Ch.8 - Services",[
("mc","What is a Windows service?",
 ["A program built to run in the background without a user launching it","A program you double-click","A scheduled task","A driver only"],0,
 "8.3."),
("sa","How does a service get controlled?","The service talks to a service control program, and you send your commands to that control program.",""),
("sa","Tools that manage services?","GUI tools (services.msc), sc, net, PsService (Sysinternals), and PowerShell.","Hook: GUI, sc, net, PsService, PowerShell."),
("sa","Service start types and accounts?","Automatic, Manual, Disabled. Accounts: LocalSystem (most power), NetworkService, LocalService.",""),
("sa","Two service misconfigs attackers abuse?","Unquoted paths with spaces, and weak permissions letting you swap the binary or repoint it.","Services are defined under HKLM\\SYSTEM\\CurrentControlSet\\Services."),
]))
