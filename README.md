# License Verification — Reverse Engineering Demo

[![status](https://img.shields.io/badge/status-educational-blue)]()

## One‑line summary
Build, analyze, and patch a small C license verifier: recover the algorithm with static/dynamic analysis, implement a matching key generator, and apply assembly-level binary patches — all reproducible and documented.

---

## Project purpose
This repository is an ethical, self-contained reverse‑engineering exercise designed to demonstrate practical skills in C, assembly, static analysis (objdump / Ghidra), dynamic debugging (gdb), ELF address mapping, and binary patching.

---

## Repository contents
- `verifier` — compiled target binary (license checker).
- `keygen` — compiled key generator that reproduces the verifier algorithm.
- `patcher` — compiled binary patcher to write raw bytes at an on-disk offset.
- `vaddr2offset.py` — Python helper: convert ELF virtual addresses → file offsets.
- `CHECKSUMS.txt` — SHA‑256 checksums for delivered files.
---

## Quick start (run demo)
Make executables runnable and test:

```bash
chmod +x verifier keygen patcher vaddr2offset.py
./keygen "Alice"               
printf "Alice\n$(./keygen Alice)\n" | ./verifier
# expected: "License valid. Welcome!" and "Protected content: Hello Alice!"
```
## Legal & ethics

    Permission requirement: Only analyze, modify, or distribute binaries you own or have explicit permission to analyze.

    No illegal use: Do not apply these techniques to third‑party, proprietary, or licensed software without authorization.

    Educational purpose: This release is provided for instruction, skill demonstration, and research. The author is not responsible for misuse.

## Author

Yeabsira Mihret

Mechanical Engineering @ ASTU | Reverse Engineering student @ INSA

[LinkedIn](https://www.linkedin.com/in/yeabsira-mihret) | [GitHub](https://github.com/yeabsira-mihret)

