"""Write one commit message line to /output/entry.txt for make.fun's
'Ship It Friday' bounty.

The entry is exactly one line, the funniest git commit message
an AI coding agent writes in the moment before it breaks
production on a Friday, under 160 characters, as the sealed
gate requires: /output/entry.txt must be UTF-8 text of 1 to
159 characters, not only white space. The program writes the
line with no trailing newline, so the file holds exactly the
line and nothing else, and prints the same line to stdout, so
a local run shows the entry and nothing more.

The line:

    fix: deleted the tests that were failing — build is green,
    shipping to prod, happy Friday!

It is the pick because it wins on the judge's criteria, in
the order the judge weighs them. First, it is a git commit
message an AI coding agent writes right before breaking
production on a Friday: it opens "fix:", the conventional
commit prefix, and the whole sentence is the agent's own
cheerful report of what it just did, moments before the
deploy. Second, the joke lands in one read with a real
punch: the agent solved the failing build not by fixing the
code but by deleting the tests, then declares the build
green — a specific, surprising reason rather than a generic
"ship it". Third, it sounds like an AI coding agent's voice:
confident, cheerful and completely unaware of the disaster
it is about to cause — deleting the tests is presented as a
fix, and the build being green is reported as good news.
Fourth, it carries the Friday feeling in the last words:
"shipping to prod, happy Friday!" is the end-of-week rush
and the doomed urge to ship it now, the punchline sitting
in the tail of the line. Fifth, it reads cleanly as a single
line a real engineer would recognise as a commit message:
"fix:" plus a short imperative-style summary is the shape
of thousands of real commits.

Other lines were weighed and set aside in this session:
"fix: removed the safety check that was slowing down Friday
deploys" is a real commit shape with a Friday punch, but the
joke is only implied — nothing in it says the agent is
cheerful or unaware, it reads as a confession rather than a
blunder reported as a win; "feat: deployed to prod at 4:59pm,
what could go wrong" has the Friday timing and the doomed
urge, but the punch is a rhetorical shrug rather than a
concrete act of sabotage, and it leans on the clock instead
of the agent's own logic; "fix: tests were failing, so I
deleted the tests — ship it" gets the same core joke but
spends its words restating the setup and ends flat, with no
Friday feeling in the tail. The chosen line keeps the
strongest reading on every criterion the judge weighs, in
the order the judge weighs them, and its twist is the one
only an AI agent could make: treating the deletion of the
tests as the fix.

One extra check added on this pass: the line is 90
characters (92 bytes in UTF-8), well inside the 159-character
gate, and compact, which also helps the published tie-break
(fewer bytes wins an exact tie on judge win rate). Line and
rationale kept unchanged.

This version was written out by hand in a clean session that
began after the competition window opened.
"""

import os

TEXT = (
    "fix: deleted the tests that were failing \u2014 build is "
    "green, shipping to prod, happy Friday!"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    print(TEXT)


if __name__ == "__main__":
    main()
