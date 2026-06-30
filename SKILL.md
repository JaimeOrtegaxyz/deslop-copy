---
name: deslop-copy
description: >
  Rewrites a project's marketing/product copy so it reads like a sharp human
  wrote it — short, blunt, specific — instead of AI-generated. Dives into the
  codebase to learn what the product is and who it's for, hunts the SHAPE of AI
  writing (balance, the clever flip, the dramatic fragment, hedging, wordiness)
  and kills it, then writes a COPY-REVIEW.md and applies the rewrites you pick.
  TRIGGER on "/deslop-copy"; when the user wants to rewrite, tighten, de-slop, or
  sharpen a site/app's copy; fix copy that "reads AI" or "sounds generic"; make
  landing-page / marketing / UI copy punchier, shorter, more human, or more
  convincing; or improve how a product explains and sells itself. Do NOT trigger
  for: prose, essay, or fiction style editing (use iA-style-editor); writing
  brand-new copy from a blank brief with no product to inspect; code review; or
  generating social-media / "viral" content.
metadata:
  version: "2.0.0"
---

# De-slop Copy

Rewrite a product's copy so a sharp person wrote it: **short, blunt, specific.**
The enemy is not bad words — it's the **shape** of AI writing. Hunt the shape and
kill it.

## The shape — what you're actually fighting

AI copy is **balanced, clever-sounding, complete, and safe.** It performs insight
through *structure* instead of stating a fact. The words can be perfectly clean
and it still reads as a machine. These are all 100% clean words and 100% AI — real
lines this skill let through (and some it *wrote*) before it was hardened:

- "Building is solved. Getting picked isn't." — balanced mirror
- "You walk out with signal, not a slide deck." — X-not-Y flip
- "We don't build your idea. We find the one that works." — negation→pivot + "that works"

If a line uses *structure* to feel smart — a flip, a mirror, a three-beat, a
reveal, a dramatic fragment — **the structure is the tell.** Delete it. Say the
thing a real person would say.

## Three moves, in order

### 1. Kill the shape — on sight, NO exceptions

In any hero, headline, tagline, or marketing line, these are always rewritten.
There is **no "but it's clever / concrete / only used once" exception** — that
rationalization is exactly how the cadence survives (it's how the lines above
shipped). Full catalog + detection: [bright-red.md](references/bright-red.md).

- **Negation-contrast** — "not X, Y" · "X, not Y" · "we don't X, we Y" · "it's not X, it's Y" · "less about X, more about Y"
- **Balanced mirror** — two clauses in symmetric opposition: "X is solved. Y isn't." · "your instincts are right, your ideas are wrong"
- **Tricolon tagline** — "X. Y. Z." three-beats for rhythm
- **Dramatic fragment** — a clipped noun for gravitas: "Signal." "Not a deck."
- **Setup→reveal** — colon / em-dash "and here's the twist" cadence
- **The profound-sounding sentence** — any line whose job is to *sound* smart rather than state a fact only this company could state

Replace the structure with one concrete fact: a number, a name, a real mechanism.

### 2. Cut it in half

- **Hero/headline: one idea, ~3–7 words, one clause.** If it needs a second
  sentence, it's a subhead — not a hero. (The hero this skill mis-passed was two
  full sentences; it read like a subhead.)
- Every line: delete each word that isn't load-bearing. Wouldn't say it aloud to
  one person? Cut it.
- One concrete noun, number, or verb beats any adjective and any rhythm.

### 3. Be blunt, specific, a little bold

AI is safe and balanced. People are blunt, specific, asymmetric, sometimes weird.
- Say the one thing only this company could say.
- Flat declarative over clever flip. Asymmetry over symmetry.
- When there's a bolder, blunter, slightly-too-honest version — use it. "More out
  there" beats "balanced and safe."

## The test — run it on every line, including your own rewrites

> "If I saw this on a random landing page, would I suspect a model wrote it?"

Yes → rewrite, even if you can't name the rule. **Default to yes.** Confident +
balanced + clever = AI until proven human. Nothing is "already strong" until it
passes this with a straight face — and **your rewrite has to pass it too.** This
skill's worst failures were rewrites that were just new AI lines.

## Workflow

### 1. Orient

- **Find where the copy lives** — `src/content/*`, section components
  (`*.tsx`/`*.jsx`/`*.vue`), `*.md`/`*.mdx`, i18n JSON, SEO/meta, the README hero.
  Inventory every block before judging any.
- **Read the product** — README, docs, brand/voice sources. Write a one-paragraph
  model: *what is this, who's it for, the core concept in one plain sentence, what
  the reader would do otherwise, the current voice.*
- **If the concept is unclear, ask 2–3 questions and stop.** You can't write
  specific copy from a fuzzy understanding.

### 2. Hunt (heroes hardest)

Read every line. Mark three things: the **shape** (move 1), the slop **vocabulary**
([marketing-slop.md](references/marketing-slop.md)), and **wordiness**. Assume each
line is AI and make it prove otherwise. Headlines and heroes get the brutal read —
that's the most-seen line and the costliest place to fail.

### 3. Rewrite shorter + blunter

Apply the three moves. Lead with the concrete thing
([persuasion.md](references/persuasion.md)). Cut length hard. **Never invent
proof** — where a rewrite wants a fact you don't have, leave a `‹NEEDS: …›` flag
and ask. A made-up number is worse than the vague line you replaced.

### 4. Deliver

Write `COPY-REVIEW.md` at the project root (format below), then ask which to take,
then apply the chosen ones with Edit — change string values only, never the
surrounding code. If a chosen rewrite still has a `‹NEEDS›`, don't ship a guess;
keep the flag visible and list it under "Proof gaps to fill."

### 5. Check — re-read every rewrite through the test

If a rewrite is balanced, clever, or wordy, **you failed it — redo it.** Then an
honest scorecard (per section: shorter? shape gone? still true?) and the
consolidated `‹NEEDS›` list. Never claim copy is "now viral" or "high-converting."

## COPY-REVIEW.md format

```markdown
# Copy Review — <project>

**Product model:** <one paragraph: what / who / core concept / alternative / voice>
**Top 3 problems:** <plainest version>

---

## <Section>   ·   shape: <tell or "none">   ·   words: <before→after>   ·   [P0|P1|P2]

**Before** > <verbatim>
**After** > <rewrite — passes the test>
**Why:** <one line: the shape killed / words cut>
**‹NEEDS›:** <proof gap, or omit>

- [ ] apply

---

## Kept — justified against the test
- <line> — why a sharp human would actually say this (not just "it's confident")

## Proof gaps to fill
- <fact only the user can supply>
```

Keep "Why" to one line. Propose the better text; don't lecture.

## Calibration — err hard toward cutting

- Unsure if it's AI? **Assume yes.**
- Unsure whether to cut a word? **Cut it.**
- Clever vs. blunt? **Blunt.**
- **#1 failure mode:** rating a confident, balanced, clever line as "strong" and
  leaving it. Those *are* the AI lines. Don't rubber-stamp them.
- Genuine voice — a real person's blunt, weird, specific phrasing — is sacred. But
  "voice" never excuses the shape in move 1.
