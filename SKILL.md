---
name: deslop-copy
description: >
  Rewrites a project's marketing/product copy so it reads like a sharp human
  wrote it — short, blunt, specific — instead of AI-generated. Dives into the
  codebase to learn what the product is and who it's for, hunts the SHAPE of AI
  writing (balance, the clever flip, the dramatic fragment, hedging, wordiness)
  and kills it, then writes a COPY-REVIEW.md and applies the rewrites you pick.
  Every rewrite must clear a deterministic linter gate and a fresh-context
  adversarial judge before delivery. TRIGGER on "/deslop-copy"; when the user
  wants to rewrite, tighten, de-slop, or sharpen a site/app's copy; fix copy
  that "reads AI" or "sounds generic"; make landing-page / marketing / UI copy
  punchier, shorter, more human, or more convincing; or improve how a product
  explains and sells itself. Do NOT trigger for: prose, essay, or fiction style
  editing (use iA-style-editor); writing brand-new copy from a blank brief with
  no product to inspect; code review; or generating social-media / "viral"
  content.
metadata:
  version: "3.0.0"
---

# De-slop Copy

Rewrite a product's copy so a sharp person wrote it: **short, blunt, specific.**
The enemy is the **shape** of AI writing — balanced, clever-sounding, complete,
safe. The words can be perfectly clean and a line still reads as a machine.
Real lines earlier versions of this skill let through (and some it *wrote*):

- "Building is solved. Getting picked isn't." — balanced mirror
- "You walk out with signal, not a slide deck." — X-not-Y flip
- "We don't build your idea. We find the one that works." — negation→pivot

## Enforcement — why this skill has a pipeline

Model training over-rewards these exact shapes, so a fraction of them survives
any instruction — including the ones in this file, including your rewrites.
Instructions alone were v2; it shipped the lines above. v3 assumes the writer
leaks and checks the output twice, with checkers that don't share the writer's
blind spot:

| Layer | Catches | Authority |
|---|---|---|
| You, drafting by the three moves | most slop, first pass | none over your own output |
| `scripts/deslop-lint.py` | mechanical shapes + slop vocabulary, deterministically | ERROR blocks delivery; no override exists |
| Fresh-context judge | what regex can't see: mirrors, profundity, linter WARNs | FAIL means redo |

Grading your own rewrite as "passes" is the documented #1 failure mode of this
skill. The pipeline runs on every invocation, even tiny single-line jobs.

## The three moves (drafting rules)

1. **Kill the shape, on sight, no exceptions** — negation-contrast ("not X, Y" /
   "we don't X, we Y"), balanced mirror, tricolon tagline, dramatic fragment,
   setup→reveal, the profound-sounding line. There is no "but it's clever /
   concrete / only used once" escape — that rationalization is how the cadence
   ships. Full catalog: [bright-red.md](references/bright-red.md). Replace the
   structure with one concrete fact: a number, a name, a real mechanism.
2. **Cut it in half** — hero/headline: one idea, ~3–7 words, one clause; a
   second sentence makes it a subhead. Delete every word that isn't
   load-bearing. One concrete noun beats any adjective and any rhythm.
3. **Blunt, specific, a little bold** — say the one thing only this company
   could say. Flat declarative over clever flip. The slightly-too-honest
   version beats the balanced-and-safe one.

The test, on every line including your own: *"If I saw this on a random landing
page, would I suspect a model wrote it?"* Default to yes. Confident + balanced
+ clever = AI until proven human.

## Workflow

### 1. Orient

Find where the copy lives — `src/content/*`, section components
(`*.tsx`/`*.jsx`/`*.vue`), `*.md`/`*.mdx`, i18n JSON, SEO/meta, the README
hero. Inventory every block before judging any. Read the product (README, docs,
brand files) and write a one-paragraph model: *what is this, who's it for, the
core concept in one plain sentence, what the reader would do otherwise, the
current voice.* If the concept is unclear, ask 2–3 questions and stop — you
can't write specific copy from a fuzzy understanding.

### 2. Hunt — machine first, then eyes

Extract every copy line into a scratchpad file, tagging provenance with `@`
location lines:

```
@ src/components/Hero.tsx:12
You walk out with signal, not a slide deck.
```

Run `python3 <skill-dir>/scripts/deslop-lint.py copy.txt`. Each hit comes with
a fix hint — don't re-derive what it already caught, and don't preload
marketing-slop.md (its blocklist lives inside the linter; open it only when a
hit needs a fuller replacement pattern than the hint). Then read
[bright-red.md](references/bright-red.md) and hunt what regex can't see:
balanced mirrors, profound-sounding lines. Heroes and headlines get the brutal
read — most-seen line, costliest place to fail.

### 3. Rewrite

Apply the three moves. Load [persuasion.md](references/persuasion.md) now — it
governs making the copy explain and sell (lead with the concrete, one idea per
hero, feature→outcome). For hero/hook work specifically, add
[hooks.md](references/hooks.md). **Never invent proof** — where a rewrite wants
a fact you don't have, leave a `‹NEEDS: …›` flag. A made-up number is worse
than the vague line it replaced. Write `COPY-REVIEW.md` at the project root
(format below).

### 4. Gate — deterministic, no override

```
python3 <skill-dir>/scripts/deslop-lint.py --review COPY-REVIEW.md
```

Every ERROR: rewrite the line — genuinely restate it, never reword around the
regex — and rerun until exit 0. WARNs don't block; collect them for the judge.
If you're convinced a hit is a false positive, it still doesn't ship: move the
line to a **Gate disputes** section for the user to decide.

### 5. Judge — fresh context, adversarial

Spawn a subagent with exactly this brief and nothing else — no conversation
history, no product context, no sight of your reasoning:

> Read `<skill-dir>/references/bright-red.md`. Then judge the numbered copy
> lines below. Someone else wrote them; your job is to refute, don't
> appreciate. FAIL any line that uses a cataloged shape or whose main job is
> to sound smart (run the four-gate test). Confident + balanced + clever = AI.
> Do not propose rewrites. Reply one line per item:
> `N: PASS` or `N: FAIL <shape> — <short reason>`.
>
> Lines: <numbered: every After line, every Kept line, and each linter WARN
> marked with ⚠ and its rule name>

FAILed lines: rewrite, send back through step 4, then re-judge only the redone
lines. Two judge rounds max — anything still failing gets listed to the user as
unresolved, never silently shipped. If no subagent tool is available, degrade
gracefully: do this as a separate final pass yourself — re-read bright-red.md
first, then judge the lines as if a stranger wrote them.

### 6. Deliver

The status line at the top of COPY-REVIEW.md must be literally true:
`lint: clean · judge: passed (round N)`. Present the review, ask which rewrites
to apply, then apply the chosen ones with Edit — change string values only,
never surrounding code. A chosen rewrite that still carries `‹NEEDS›` ships
with the flag visible and listed under "Proof gaps to fill" — don't substitute
a guess. Close with an honest scorecard (per section: shorter? shape gone?
still true?). Never claim copy is "now viral" or "high-converting."

## COPY-REVIEW.md format

```markdown
# Copy Review — <project>

`lint: clean · judge: passed (round N)`

**Product model:** <one paragraph: what / who / core concept / alternative / voice>
**Top 3 problems:** <plainest version>

---

## <Section>   ·   shape: <tell or "none">   ·   words: <before→after>   ·   [P0|P1|P2]

**Before** > <verbatim>
**After** > <rewrite — cleared gate and judge>
**Why:** <one line: the shape killed / words cut>
**‹NEEDS›:** <proof gap, or omit>

- [ ] apply

---

## Kept — justified against the test
- <line> — why a sharp human would actually say this (not just "it's confident")

## Gate disputes
- <line> — <rule that hit> — <why you think it's wrong; user decides>

## Proof gaps to fill
- <fact only the user can supply>
```

Keep "Why" to one line. Propose the better text; don't lecture. Omit empty
sections.

## Calibration — err hard toward cutting

- Unsure if it's AI? **Assume yes.** Unsure whether to cut a word? **Cut it.**
  Clever vs. blunt? **Blunt.**
- The linter and judge exist because you can't be trusted to catch these in
  your own lines. Run them every time; skipping the pipeline "because the job
  is small" is how v2 failed.
- Genuine voice — a real person's blunt, weird, specific phrasing — is sacred.
  But "voice" never excuses a move-1 shape, and a Kept line still has to clear
  the gate and the judge like everything else.
