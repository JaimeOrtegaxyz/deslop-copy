# The AI Shape — kill on sight

Not a vocabulary list — a list of **shapes**. These constructions read as AI even
when every word is clean, because they use *structure* to perform insight instead
of stating a fact. In a hero, headline, tagline, or any marketing line they are
**always rewritten. No exceptions.**

There is no "but it's clever / the Y is concrete / it's only used once" escape.
That rationalization is precisely how the cadence keeps shipping. If you catch
yourself defending one of these, you've already lost — rewrite it.

The fix is always the same: **delete the structure, state one concrete fact** (a
number, a name, a real mechanism), and **cut the word count.**

This file doubles as the charter for the fresh-context judge (workflow step 5):
the mechanical forms below are also caught by `scripts/deslop-lint.py`, so the
judge's real work is wherever structure performs insight in ways regex can't
pin — mirrors, symmetry, the profound-sounding line.

---

## The shapes

### 1. Negation-contrast (correctio)
Deny one thing, pivot to a "truer/bigger" thing.

| Form | Example |
|---|---|
| It's not X — it's Y | "It's not software — it's a revolution." |
| X, not Y | "You walk out with signal, not a slide deck." |
| We don't X. We Y. | "We don't build your idea. We find the one that works." |
| X isn't about A, it's about B | "Hiring isn't about résumés. It's about potential." |
| Not [noun]. [Noun]. | "Not a purchase. An investment." |
| less about A, more about B | "Less about clicks, more about connection." |

Wikipedia files this under *Signs of AI writing → Negative parallelisms*. RLHF
over-rewards it because raters mistake the *shape* of insight for insight. It is,
with the em dash, the single most recognizable ChatGPT cadence.

### 2. Balanced mirror (antithesis)
Two clauses set in symmetric opposition for effect. No negation needed — the
*symmetry itself* is the tell.

| Example | Why it's AI |
|---|---|
| "Building is solved. Getting picked isn't." | mirrored setup→reversal, performs a "turn" that isn't one |
| "Your instincts are right. Your ideas are wrong." | right/wrong mirror |
| "Getting built is easy. Getting noticed is the job." | easy/hard mirror |

If you can fold a line into "A is X; B is the opposite," it's this shape. Kill the
symmetry; make one blunt claim and move on.

### 3. Tricolon tagline
"X. Y. Z." three-beats for rhythm. ("Discover, plan, build." "Faster, simpler,
smarter.") The third item is usually a vague catch-all. One blunt claim beats three.

### 4. Dramatic fragment
A clipped noun-fragment dropped for gravitas: "Signal." "Not a deck." "Built
different." Used once by a person it can punch; as a default it reads as a machine
performing emphasis.

### 5. Setup→reveal
Colon or em-dash building to "the twist": "Here's the thing:" "The catch?" "And
that changes everything." Cut the setup; state the point.

### 6. The profound-sounding sentence
Any line whose primary job is to *sound* smart rather than state a fact only this
company could state. If it would survive a competitor pasting their logo above it,
it says nothing.

---

## Worked kills (the lines that shipped before the fix)

| Before (shape) | After (blunt fact) |
|---|---|
| We don't build your idea. We find the one that works. | We test your idea before you build it. |
| You walk out with signal, not a slide deck. | You get the one real users want. |
| Building is solved. Getting picked isn't. | Getting picked is the hard part. |
| It's not software — it's a revolution. | Close your books in 2 days, not 2 weeks → *better:* Close your books in 2 days. |

Note the last one: even the "fix" tempted an X-not-Y ("2 days, not 2 weeks"). The
*real* fix drops the contrast entirely. That reflex is the trap.

---

## Brevity — the second non-negotiable

- **Hero/headline: one idea, ~3–7 words, one clause.** Two sentences = it's a
  subhead, not a hero.
- Cut every word that isn't load-bearing. If you wouldn't say it aloud to one
  person, cut it.
- A concrete noun/number/verb beats any adjective or any rhythm.

---

## Vague success / virtue filler — perform a claim without making one

Always replace with the missing noun/number/mechanism.

| Word / phrase | Why it's empty | Fix |
|---|---|---|
| …that works | Bar so low the opposite is absurd | the result: "…that cuts your close to 3 days" |
| …that matters | "Matters" to whom, by what measure? | name what's at stake |
| done right / the way it should be | correctness with no standard | the specific better method |
| that just works | borrowed Apple-ism; unproven ease | show it: "Online in 60 seconds" |
| reimagined / redefined | claims novelty, describes nothing | what's actually different |
| made simple / effortless / seamless | tells the reader how to feel | show the step count / removed friction |
| for the modern X | "modern" dates instantly | the literal user + constraint |
| that delivers | delivers *what*? | the deliverable |
| built different | posture; a competitor can sign it | the actual difference |

(Puffery adjectives — best-in-class, world-class, cutting-edge, robust, unlock,
elevate, supercharge — live in [marketing-slop.md](marketing-slop.md). Same rule:
trade the adjective for a fact.)

---

## The four-gate test (run on every hero, at max strictness)

1. **See it?** Does it put a picture in the reader's head?
2. **Prove it?** Could the claim be *false*? If nothing could disprove it, it claims nothing.
3. **Only I can say it?** Could a competitor paste their logo above it unchanged? If yes, it's generic.
4. **Would the founder say it aloud?** If it'd be embarrassing or robotic at a bar, it's machine language.

Fail any gate → rewrite. Clean words wrapped around an unfalsifiable, signable,
balanced claim is the exact signature of AI slop. Ogilvy: ~5× as many people read
the headline as the body — it's the costliest place to leave the shape.

## Done right (the bar)

- Stripe — "Financial infrastructure for the internet." (concrete noun + scope)
- Superhuman — "Get through your inbox twice as fast." (number + outcome)
- Death Wish — "The World's Strongest Coffee." (maximally falsifiable)
- Fathom — "A Google Analytics alternative that's simple & privacy-first." (names the exact competitor)

None of them flip, mirror, or tease. They state one concrete thing and stop.
