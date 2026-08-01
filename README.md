# deslop-copy

A Claude Code skill for rewriting a project's copy so it reads human, specific,
and persuasive — instead of AI-generated.

You invoke it in-session while working on a site or app. It dives into the
codebase to learn what the product actually is and who it's for, diagnoses the
existing copy on two axes (AI-slop tells *and* whether it explains and sells the
idea), then proposes a conscious section-by-section rewrite. Born out of a
look at the "5 viral copywriting skills" doing the rounds — keeping the
credibility mechanics and rejecting the engagement-bait.

## How it works

v3 moved enforcement out of prompt-space. Asking a model to avoid AI cadences
fails a percentage of the time — its training rewards those exact shapes — so
the skill stopped relying on the writer and added two checks the writer can't
sweet-talk:

- **Orients first.** Reads README, docs, `.canon`/brand files, and finds where
  copy lives (`src/content`, section components, MDX, SEO meta) before judging a
  word. Builds a one-paragraph product model; asks 2–3 questions if the concept
  is unclear.
- **Lints, then hunts.** `scripts/deslop-lint.py` deterministically flags the
  mechanical tells — negation-contrast, tricolons, setup→reveal, vague enders,
  the full slop-vocabulary blocklist — each with an inline fix hint. The model's
  eyes go only where regex can't: mirrors, profundity, persuasion failures.
- **Gates its own rewrites.** Every rewritten line must pass
  `deslop-lint.py --review COPY-REVIEW.md` with zero errors. No override; a
  disputed hit is surfaced to you, never shipped quietly.
- **Adversarial judge.** A fresh-context subagent — no product context, no
  attachment to the phrasing — tries to refute each surviving line against the
  shape catalog. Failures get redone and re-gated; leftovers after two rounds
  are reported as unresolved.
- **Never fabricates proof.** Where a rewrite needs a number or customer you
  don't have, it leaves a visible `‹NEEDS: …›` flag and asks — it won't invent.
- **Writes `COPY-REVIEW.md`** at the project root (diagnosis + before/after +
  proof-gaps + a truthful `lint/judge` status line), you tick the rewrites you
  want, and it applies them to the real files.

The linter stands alone, too — Python 3, no dependencies:

```sh
python3 scripts/deslop-lint.py page-copy.txt   # or --review COPY-REVIEW.md
python3 scripts/deslop-lint.py --self-test     # 45-case regression battery
```

## Install

```sh
git clone https://github.com/JaimeOrtegaxyz/deslop-copy.git ~/.claude/skills/deslop-copy
```

Or project-scoped: clone into `.claude/skills/deslop-copy/`.

See [SKILL.md](SKILL.md) for the full method and [references/](references/) for
the slop blocklist, persuasion principles, and hook bank.
