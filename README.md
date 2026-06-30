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

- **Orients first.** Reads README, docs, `.canon`/brand files, and finds where
  copy lives (`src/content`, section components, MDX, SEO meta) before judging a
  word. Builds a one-paragraph product model; asks 2–3 questions if the concept
  is unclear.
- **Two-axis diagnosis.** Marketing-slop vocabulary + structural tells, *and*
  persuasion failures (hierarchy, hook, value-prop, proof). Runs the swap /
  falsifiable / founder-voice tests.
- **Never fabricates proof.** Where a rewrite needs a number or customer you
  don't have, it leaves a visible `‹NEEDS: …›` flag and asks — it won't invent.
- **De-slop governs the hook.** Trading an AI tell for a clickbait tell isn't a
  fix; restraint wins ties.
- **Writes `COPY-REVIEW.md`** at the project root (diagnosis + before/after +
  proof-gaps), you tick the rewrites you want, and it applies them to the real
  files — leaving the proof-gap flags for you to fill.

## Install

```sh
git clone https://github.com/JaimeOrtegaxyz/deslop-copy.git ~/.claude/skills/deslop-copy
```

Or project-scoped: clone into `.claude/skills/deslop-copy/`.

See [SKILL.md](SKILL.md) for the full method and [references/](references/) for
the slop blocklist, persuasion principles, and hook bank.
