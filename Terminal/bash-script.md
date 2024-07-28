# Bash Scripting

File Ext: .sh

Run by: ```$ . script.sh arg1 arg2``` | ```$ bash script.sh arg1 arg2```

## Boilerplate

Start with: ```#! /bin/bash``` \
(get */bin/bash* with ```$ which bash```)

## Syntax

- ```# comment```
- Variables
  - ```varName=Hello```
  - ```echo $varName```
  - ```varName=`df -h | grep tmpfs` ```
- Expressions
  - ```expr 2+2```
  - ```varName=$((2+2))```
  - Decimals
    - ```echo scale=2;22/7 | bc```
      - Scale = # of decimal places
      - bc (bash calculator)
- User input
  - ```read -p "Custom prompt" varName```
- Logic Operators
  - == ```a -eq b```
  - \>= ```a -ge b```
  - \> ```a -gt b```
  - <= ```a -le b```
  - < ```a -lt b```
  - != ```a -ne b```
  - && ```-a```
  - || ```-o```
- If condition

    ```bash
    if [ true ]; then
    commands
    elif [ false ]
    then
    commands
    else
    commands
    fi
    ```

- For loops

    ```bash
    # for i in cyan magenta yellow
    # for i in $@ (loop script arguments)
    for i in {1...5}
    do
    commands
    done
    ```

- While loops

    ```bash
    i=1
    while [[ $i -le 10 ]]; do
        echo $i
        ((i += 1))
    done
    ```

- Read Files

    ```bash
    line=1
    while read -r currLine; do
        echo "$line: $currLine"
        ((line++))
    done < "test.txt"
    ```

## Intro

- Linux command line is a program called the shell.
- The default shell program for most Linux distros is bash.
- Operates on a command line interface (CLI).

### Bash

- On launch, uses startup script .bashrc / .bash_profile.
  - Can be altered to customized the behavior of the shell.
- When ```$``` is shown, the shell is waiting for a command from the user (i.e. a shell prompt).
- When ```#``` is shown, the shell is running as root (i.e. superuser shell prompt).

### Bash Script

- File w/ multiple commands to be executed line-by-line.
- Shebang ```#!``` tells the shell to execute the script via bash shell.
  - Shebang = absolute path to the bash interpreter
  - Followed by path to bash shell
- Find path to bash shell ```which bash```
  - should be `/bin/bash`

![Alt text](https://www.freecodecamp.org/news/content/images/2022/03/image-119.png "Tux the Linux mascot")