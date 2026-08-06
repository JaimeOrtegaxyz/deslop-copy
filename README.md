# deslop-copy

A Claude Code skill that rewrites your product's copy so it stops reading like
ChatGPT.

Run it in-session while you're building a site or app. It reads the codebase to
learn what the product is and who it's for. Then it flags every line that reads
AI or fails to sell the idea, and hands you a section-by-section rewrite to
approve. It started as a teardown of the "5 viral copywriting skills" going
around. The parts worth keeping are in `references/persuasion.md`.

## How it works

v2 was instructions only, and it shipped lines its own catalog bans. So v3 added
two checks that run after the writing:

- **Reads the codebase first.** README, docs, brand files, and wherever the copy
  actually lives: `src/content`, section components, MDX, SEO meta. Builds a
  one-paragraph product model, and asks you 2–3 questions if the concept is
  still unclear.
- **Runs the linter on every line.** `deslop-lint.py` catches the mechanical
  tells: negation-contrast, tricolons, setup→reveal, vague enders, the
  slop-vocabulary blocklist, each with a fix hint. The model then hunts what
  regex misses, mostly balanced mirrors and lines whose only job is sounding
  smart.
- **Gates its own rewrites.** Every rewritten line has to pass
  `deslop-lint.py --review COPY-REVIEW.md` with zero errors. There is no
  override. Disputed hits go in a list for you to rule on.
- **A second model judges it.** A subagent with no conversation history reads
  the shape catalog and the finished lines, then tries to refute each one.
  Failures get rewritten and re-gated. Anything still failing after two rounds
  is reported to you as unresolved.
- **Never invents proof.** When a rewrite needs a number or a customer name you
  haven't given it, it leaves a visible `‹NEEDS: …›` flag and asks.
- **Writes `COPY-REVIEW.md`** at the project root: diagnosis, before/after per
  section, proof gaps, and a `lint/judge` status line. You tick the rewrites you
  want and it edits the real files.

The linter runs on its own too. Python 3, no dependencies:

```sh
python3 scripts/deslop-lint.py page-copy.txt   # or --review COPY-REVIEW.md
python3 scripts/deslop-lint.py --self-test     # 45 regression cases
```

## Install

```sh
git clone https://github.com/JaimeOrtegaxyz/deslop-copy.git ~/.claude/skills/deslop-copy
```

Or project-scoped: clone into `.claude/skills/deslop-copy/`.

See [SKILL.md](SKILL.md) for the full method and [references/](references/) for
the slop blocklist, persuasion principles, and hook bank.
