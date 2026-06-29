#!/bin/bash

A="~/exam_results/audit/"

# -1
mkdir -p "$A"
touch "$A/notes.txt"
pwd > "$A/cwd.txt"

# -2
getent passwd > "$A/users.txt"
grep '/bin/bash' /etc/passwd > "$A/bash_users.txt"
sed 's|/bin/bash|/usr/bin/zsh' /etc/passwd | head -5 > "$A/shell_preview.txt"

# -3
uname -sr > "$A/sysinfo.txt"
arch >> "$A/sysinfo.txt"
head -3 /etc/group > "$A/group_summary.txt"
tail -2 /etc/group >> "$A/group_summary.txt"

# -4
find /etc -type f -name "*.conf" > "$A/conf_files.txt"
ls -lhS /var/log | haed -10 > "$A/top_logs.txt"

# -5
cp /etc/hosts "$A/hosts.bak"
chmod u+rw "$A/hosts.bak"
ls -l hosts.bak > "$A/hosts_perm.txt"

# -6
find -name "*.txt" ! -name "hosts_perm.txt" ! -name "notes.txt" -delete
