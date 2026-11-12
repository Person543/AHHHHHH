DECKS=[("X","Cross-Book - Linux vs Windows (Quick Compare)",[
("sa","Password hashes: Linux vs Windows?","Linux: /etc/shadow. Windows: NTLM in the SAM, and ntds.dit for the domain.",""),
("sa","Identifying users: Linux vs Windows?","Linux: UID numbers (0 = root). Windows: SIDs (RID 500 = Administrator).",""),
("sa","Permissions: Linux vs Windows?","Linux: rwx for user/group/world, plus SUID/SGID/sticky and ACLs. Windows: a security descriptor - owner, group, DACL, SACL, flags.",""),
("sa","Getting elevated: Linux vs Windows?","Linux: sudo, su, runuser, Polkit for the GUI. Windows: UAC elevating your token, or runas.",""),
("sa","Extra lockdown layer: Linux vs Windows?","Linux: SELinux or AppArmor. Windows: integrity levels, which drive UAC.",""),
("sa","Background programs: Linux vs Windows?","Linux: systemd units. Windows: services under the Service Control Manager. Both are used for persistence.",""),
("sa","Login records: Linux vs Windows?","Linux: utmp, lastlog, systemd. Windows: Security event log (4624), query user, psloggedon - all with limits.",""),
("sa","Hiding history: Linux vs Windows?","Linux: unset HISTFILE, delete ~/.bash_history. Windows: cmd history dies with the session; PowerShell's PSReadLine file can be deleted, and Base64 hides the command's content.",""),
("sa","Links: Linux vs Windows?","Linux: hard links and symlinks. Windows: shortcuts, hard links (files), junctions (folders), symlinks (admin only).",""),
("sa","Put the whole attack in Kill Chain order.","Build the payload (msfvenom) > deliver it (phishing, or brute force your way in) > it runs and your handler catches it > Meterpreter session > migrate, recon, keylog, add an AV exclusion to stay.",""),
])]
