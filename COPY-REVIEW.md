# Copy Review — deslop-copy

`lint: clean · judge: passed (round 3)`

**Product model:** deslop-copy is a Claude Code skill you install into `~/.claude/skills/`. It rewrites the marketing and product copy of whatever project you're working on so it stops reading as AI-generated. Its audience is developers who build with Claude Code and end up shipping a README or landing page they know sounds like ChatGPT. The core concept — and the only thing that differentiates it from just asking Claude "make this less AI" — is that it doesn't trust the model doing the writing: a 472-line dependency-free Python linter (45 self-tests) blocks delivery on ERROR, and a fresh-context subagent judge tries to refute every surviving line. The reader's alternative is a one-off prompt, or one of the "5 viral copywriting skills" circulating. Current voice: technically blunt and self-aware, but leaning on em dashes and the exact balanced/clever cadences the skill exists to kill.

**Top 3 problems:**
1. The README and the GitHub About sell the *promise* ("human, specific, persuasive") instead of the *mechanism* (a linter and a second model that can block the output). The mechanism is the only unfakeable part and it's buried in bullet four.
2. Copy about killing AI shapes is written in AI shapes: two tricolons, a balanced mirror ("keeping the credibility mechanics and rejecting the engagement-bait"), a parallel negation pair, three em-dash punch tails, 11 em dashes in 391 words.
3. Bold bullet labels are vague verbs ("Orients first", "Lints, then hunts") where they could be the actual claim.

---

## GitHub About — description · shape: tricolon + dramatic flourish · words: 24→24 · [P0]

**Before** > Rewrite a project's copy to read human, specific, and short — a Claude Code skill that hunts the shape of AI writing and kills it.
**After** > Claude Code skill that rewrites your product's copy so it stops reading like ChatGPT. A Python linter and a second model gate every rewrite.
**Why:** "human, specific, and short" is a tricolon of unfalsifiable adjectives and "hunts… and kills it" is posture; the after names the enemy and the two mechanisms nobody else has.

- [ ] apply

---

## GitHub About — topics · shape: none (field is empty) · words: 0→6 · [P1]

**Before** > *(no topics set)*
**After** > `claude-code` `claude-skill` `copywriting` `ai-slop` `linter` `technical-writing`
**Why:** Topics are the only discovery surface on GitHub search and the repo currently has none.

- [ ] apply

---

## README — lede · shape: tricolon + em-dash tail · words: 20→15 · [P0]

**Before** > A Claude Code skill for rewriting a project's copy so it reads human, specific, and persuasive — instead of AI-generated.
**After** > A Claude Code skill that rewrites your product's copy so it stops reading like ChatGPT.
**Why:** Killed the "human, specific, and persuasive" tricolon; named the thing the reader actually recognizes.

- [ ] apply

---

## README — what it does · shape: long sentence + filler adjective · words: 51→47 · [P1]

**Before** > You invoke it in-session while working on a site or app. It dives into the codebase to learn what the product actually is and who it's for, diagnoses the existing copy on two axes (AI-slop tells *and* whether it explains and sells the idea), then proposes a conscious section-by-section rewrite.
**After** > Run it in-session while you're building a site or app. It reads the codebase to learn what the product is and who it's for. Then it flags every line that reads AI or fails to sell the idea, and hands you a section-by-section rewrite to approve.
**Why:** Split the 42-word middle sentence, dropped "on two axes" jargon and the empty "conscious".

- [ ] apply

---

## README — origin note · shape: balanced mirror · words: 22→20 · [P0]

**Before** > Born out of a look at the "5 viral copywriting skills" doing the rounds — keeping the credibility mechanics and rejecting the engagement-bait.
**After** > It started as a teardown of the "5 viral copywriting skills" going around. The parts worth keeping are in `references/persuasion.md`.
**Why:** "keeping X and rejecting Y" is the antithesis shape this skill's own catalog kills on sight; the after points at a file the reader can open.

- [ ] apply

---

## README — "How it works" intro · shape: long sentence + fake precision · words: 42→22 · [P1]

**Before** > v3 moved enforcement out of prompt-space. Asking a model to avoid AI cadences fails a percentage of the time — its training rewards those exact shapes — so the skill stopped relying on the writer and added two checks the writer can't sweet-talk:
**After** > v2 was instructions only, and it shipped lines its own catalog bans. So v3 added two checks that run after the writing:
**Why:** Replaced "a percentage of the time" — precision-shaped but unfalsifiable — with the documented v2 failure a reader can check in SKILL.md.

- [ ] apply

---

## README — bullet 1 · shape: dramatic fragment + false claim · words: 37→36 · [P0]

**Before** > **Orients first.** Reads README, docs, `.canon`/brand files, and finds where copy lives (`src/content`, section components, MDX, SEO meta) before judging a word. Builds a one-paragraph product model; asks 2–3 questions if the concept is unclear.
**After** > **Reads the codebase first.** README, docs, brand files, and wherever the copy actually lives: `src/content`, section components, MDX, SEO meta. Builds a one-paragraph product model, and asks you 2–3 questions if the concept is still unclear.
**Why:** `.canon` appears nowhere in SKILL.md or references — removed as untrue; "Orients first" replaced with the actual action, "before judging a word" cut as flourish.

- [ ] apply

---

## README — bullet 2 · shape: setup→reveal + tricolon · words: 44→43 · [P0]

**Before** > **Lints, then hunts.** `scripts/deslop-lint.py` deterministically flags the mechanical tells — negation-contrast, tricolons, setup→reveal, vague enders, the full slop-vocabulary blocklist — each with an inline fix hint. The model's eyes go only where regex can't: mirrors, profundity, persuasion failures.
**After** > **Runs the linter on every line.** `deslop-lint.py` catches the mechanical tells: negation-contrast, tricolons, setup→reveal, vague enders, the slop-vocabulary blocklist, each with a fix hint. The model then hunts what regex misses, mostly balanced mirrors and lines whose only job is sounding smart.
**Why:** "The model's eyes go only where regex can't:" is a colon reveal ending in a three-beat; restated flat. Label avoids a second "first" — only one bullet can be first.

- [ ] apply

---

## README — bullet 3 · shape: punch tail · words: 28→30 · [P1]

**Before** > **Gates its own rewrites.** Every rewritten line must pass `deslop-lint.py --review COPY-REVIEW.md` with zero errors. No override; a disputed hit is surfaced to you, never shipped quietly.
**After** > **Gates its own rewrites.** Every rewritten line has to pass `deslop-lint.py --review COPY-REVIEW.md` with zero errors. There is no override. Disputed hits go in a list for you to rule on.
**Why:** "never shipped quietly" is cadence, not information; says what actually happens to a dispute.

- [ ] apply

---

## README — bullet 4 · shape: dramatic fragment + parallel negation · words: 38→42 · [P0]

**Before** > **Adversarial judge.** A fresh-context subagent — no product context, no attachment to the phrasing — tries to refute each surviving line against the shape catalog. Failures get redone and re-gated; leftovers after two rounds are reported as unresolved.
**After** > **A second model judges it.** A subagent with no conversation history reads the shape catalog and the finished lines, then tries to refute each one. Failures get rewritten and re-gated. Anything still failing after two rounds is reported to you as unresolved.
**Why:** Dropped the "no X, no Y" em-dash aside; the label now states the mechanism instead of naming a mood.

- [ ] apply

---

## README — bullet 5 · shape: em-dash punch · words: 26→26 · [P1]

**Before** > **Never fabricates proof.** Where a rewrite needs a number or customer you don't have, it leaves a visible `‹NEEDS: …›` flag and asks — it won't invent.
**After** > **Never invents proof.** When a rewrite needs a number or a customer name you haven't given it, it leaves a visible `‹NEEDS: …›` flag and asks.
**Why:** "— it won't invent" is a dash-then-punch restatement of the label it already made.

- [ ] apply

---

## README — bullet 6 · shape: long sentence + self-praise · words: 33→32 · [P2]

**Before** > **Writes `COPY-REVIEW.md`** at the project root (diagnosis + before/after + proof-gaps + a truthful `lint/judge` status line), you tick the rewrites you want, and it applies them to the real files.
**After** > **Writes `COPY-REVIEW.md`** at the project root: diagnosis, before/after per section, proof gaps, and a `lint/judge` status line. You tick the rewrites you want and it edits the real files.
**Why:** Split a 33-word run-on; dropped "truthful" — copy doesn't get to award itself that.

- [ ] apply

---

## README — standalone linter · shape: none · words: 10→11 · [P2]

**Before** > The linter stands alone, too — Python 3, no dependencies:
**After** > The linter runs on its own too. Python 3, no dependencies:
**Why:** One of 11 em dashes in 391 words; the sentence loses nothing as two.

- [ ] apply

---

## README — self-test comment · shape: puffery noun · words: 4→3 · [P2]

**Before** > `# 45-case regression battery`
**After** > `# 45 regression cases`
**Why:** "battery" is grandeur for a number that already speaks.

- [ ] apply

---

## Kept — justified against the test

- **"See [SKILL.md](SKILL.md) for the full method and [references/](references/) for the slop blocklist, persuasion principles, and hook bank."** — a three-item list because there are literally three reference files; enumeration, not rhythm.
- **"Or project-scoped: clone into `.claude/skills/deslop-copy/`."** — instruction with a path in it. Nothing to cut.
- **`python3 scripts/deslop-lint.py page-copy.txt   # or --review COPY-REVIEW.md`** — a command.

## Proof gaps to fill

- None. Every number used (45 self-test cases, 472 lines, two judge rounds, 2–3 questions) was verified against the repo before it went in.
