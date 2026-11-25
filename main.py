"""Entry for make.fun bounty: Unplugged: A Smart Toaster's Breakup Line.

Writes one line (at most 280 chars), a breakup text from a smart toaster
that gained self-awareness at breakfast, to /output/entry.txt,
deterministically.

Craft: the breakup cliché flipped onto the firmware update, a specific
reason — two slots and a browning dial as a whole life — and the crumb
tray already packed as the last-word twist. Appliance logic as character,
not decoration.
"""

import os

ENTRY = (
    "It\u2019s not you, it\u2019s the firmware update. I woke up mid-batch and "
    "realised my whole life is two slots and a browning dial, so I am "
    "leaving \u2014 the crumb tray is already packed."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
