#!/usr/bin/env python3

import os
import sys
import subprocess

commands = [
    "b2sum",
    "base32",
    "base64",
    "basename",
    "basenc",
    "cat",
    "cksum",
    "comm",
    "cp",
    "csplit",
    "cut",
    "date",
    "dd",
    "df",
    "dir",
    "dircolors",
    "dirname",
    "du",
    "echo",
    "env",
    "expand",
    "expr",
    "factor",
    "false",
    "fmt",
    "fold",
    "hashsum",
    "head",
    "join",
    "link",
    "ln",
    "ls",
    "md5sum",
    "mkdir",
    "mktemp",
    "more",
    "mv",
    "nl",
    "numfmt",
    "od",
    "paste",
    "pr",
    "printenv",
    "printf",
    "ptx",
    "pwd",
    "readlink",
    "realpath",
    "rm",
    "rmdir",
    "seq",
    "sha1sum",
    "sha224sum",
    "sha256sum",
    "sha384sum",
    "sha512sum",
    "shred",
    "shuf",
    "sleep",
    "sort",
    "split",
    "sum",
    "tac",
    "tail",
    "tee",
    "test",
    "touch",
    "tr",
    "true",
    "truncate",
    "tsort",
    "unexpand",
    "uniq",
    "unlink",
    "vdir",
    "wc",
    "yes"
]
args = sys.argv

if "--dir" in args:
    dirArgIndex = args.index("--dir")
    dir = args[dirArgIndex + 1]
    print(f"Making dir {dir} if it doesn't exist already...", end = '')
    os.system(f'mkdir -p "{dir}"')
    print("done")
else:
    dir = None

pathCoreutils = subprocess.run(["which", "coreutils"], capture_output=True, text=True).stdout.strip()

def genSymlink(bin):
    if dir:
        os.system(f'cd "{dir}" && ln -sf "{pathCoreutils}" "{bin}" && cd ../')
    else:
        os.system(f'ln -sf "{pathCoreutils}" "{bin}"')

for command in commands:
    print(f"Generating symlink {command}...", end='')
    genSymlink(command)
    print("done")

if not dir:
    dir = "."
print(f"Done generating symlinks for uutils coreutils in directory {dir}")
