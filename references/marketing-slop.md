# Marketing & Web-Copy Anti-Slop Reference

Scope: landing pages, SaaS/dev-tool sites, product pages, feature sections,
CTAs, "about" copy. The through-line under every fix:

> **AI writes the category average. Good copy writes the specific.** Every fix
> is a way of trading a word that could describe any product for a claim that
> describes only this one.

---

## General prose tells (also apply to copy)

These LLM-prose tropes show up in marketing copy too — scan for them first, then
the marketing-specific layer below:

- **The "delve" family** — delve, utilize, leverage, robust, streamline, harness,
  crucial, pivotal, meticulous, tapestry, landscape (metaphor), testament,
  intricate, foster, empower, enhance, multifaceted, nuanced, holistic, synergy,
  ecosystem (non-technical). Use the plain word.
- **Negative parallelism / correctio ("It's not X — it's Y", "We don't X, we Y").**
  The #1 AI cadence — always rewrite. Canonical treatment in
  [bright-red.md](bright-red.md).
- **Em-dash addiction.** More than ~once per 100 words is a tic. One or two fine.
- **Rule-of-three abuse.** Reflexive tricolons ("Fast. Secure. Scalable.") where
  the third item is a vague catch-all.
- **Staccato fragments for manufactured emphasis.** "Not a deck. Signal." used
  more than twice reads as a tic.
- **"It's worth noting / notably / importantly"** filler transitions. Cut.
- **Signposted conclusions** — "In summary," "Ultimately," "At the end of the
  day." Just conclude.
- **Stakes inflation** — "transform, revolutionize, redefine, game-changer."
- **Bold-first bullets** — every list item opening with a bolded phrase.

---

## Marketing slop vocabulary (blocklist)

### Cluster 1 — Empowerment / transformation verbs
The single biggest marketing tell: a grandiose verb standing in for what the
product literally does.

| Slop | Why it's empty | Human replacement |
|---|---|---|
| unlock / unleash | Implies hidden potential without naming it | Name the literal action: "see," "export," "send," "edit" |
| supercharge / turbocharge / power up | Hype prefix on a vague benefit; no magnitude | State the number: "3x faster builds," "load time under 1s" |
| elevate / take it to the next level / level up | Pure altitude metaphor, zero content | Say what changes: "invoices get paid 9 days sooner" |
| empower / enable | Corporate way to say "let"; hedges the capability | "lets you" + the concrete thing, or cut the verb |
| transform / revolutionize / reinvent | Claims a magnitude the copy never proves | Describe the before→after in plain terms |
| harness (the power of) | Filler wrapper around a noun | Delete it; lead with the noun |
| amplify / accelerate / propel / ignite / skyrocket / boost / drive | Generic "more/faster," no baseline | Give the metric or the mechanism |
| streamline / optimize / maximize | Process-flavored nothing | Name what's removed: "one step instead of six" |

### Cluster 2 — Effortlessness adjectives
AI promises zero friction. Naming where friction *isn't* is more credible than
claiming none.

| Slop | Why it's empty | Human replacement |
|---|---|---|
| seamless / seamlessly | The most overused AI marketing word | Name the integration + what it skips: "syncs to Slack, no webhook setup" |
| effortless / effortlessly | Tells the reader how to feel | Show step count or time: "set up in 2 minutes" |
| frictionless / hassle-free / painless | Same move, more synonyms | Cut. Name the one annoying thing you removed |
| intuitive | The user's call, not yours | Show it (screenshot/demo) or cut |
| out of the box / plug-and-play | Implies zero config without proof | "Works with your existing X — no migration" |

### Cluster 3 — Superlative / quality puffery
Unprovable adjectives; the reader auto-discounts them.

| Slop | Why it's empty | Human replacement |
|---|---|---|
| best-in-class / world-class / industry-leading / top-tier | Self-awarded medal, no benchmark | Cite proof: a number, a named comparison, a customer |
| cutting-edge / state-of-the-art / next-gen / bleeding-edge | Says "new" not "good"; dates instantly | Name the actual new capability |
| game-changer / groundbreaking / revolutionary | Tells the reader the conclusion to reach | Give the fact; let them conclude it |
| robust / powerful | Engineer-flavored filler | "handles 10k req/s," "99.9% uptime last 12 months" |
| innovative / disruptive | Claims novelty without content | Describe what's actually different |
| unparalleled / unrivaled / unmatched | Comparative with no comparison | Name who you beat and on what |

### Cluster 4 — Vague scope / "solution" nouns
Nouns that describe a product without committing to what it is.

| Slop | Why it's empty | Human replacement |
|---|---|---|
| solution(s) | The emptiest noun in B2B | Say the category: "a Postgres GUI," "a CRM for plumbers" |
| platform / ecosystem | Inflates scope; hides the feature | Name what it does first; "platform" later if ever |
| all-in-one / one-stop shop / end-to-end / suite | Breadth as a brag; usually unfocused | Name the top 1–2 jobs it does best |
| holistic / comprehensive | "We do everything" = good at nothing in particular | Pick the sharp edge and lead with it |
| toolkit / toolbox | Soft metaphor for "features" | List the 2–3 features that matter |

### Cluster 5 — Relationship / mission platitudes

| Slop | Why it's empty | Human replacement |
|---|---|---|
| we're on a mission to / we believe | Mission-statement throat-clearing | Cut; state what you built and why it's different |
| your trusted partner | Trust is earned, not declared | Show proof: years, customers, a guarantee |
| designed to / built to help you | Hedges — "designed to" ≠ "does" | Drop it; make the flat claim: "it does X" |
| tailored to your needs / for your unique needs | "Your needs" names nothing | Name the need: "for teams drowning in Slack pings" |
| customer-centric / people-first / customer-obsessed | Everyone claims it | Show one policy: "no contracts, cancel anytime" |
| dedicated to / committed to / passionate about | Labels on the company, not value to the reader | Cut; replace with a fact about the product |

### Cluster 6 — Opening / framing clichés
Almost always deletable. The real first sentence is the second one.

| Slop | Why it's empty | Human replacement |
|---|---|---|
| in today's fast-paced world / digital age / ever-evolving landscape | Applies to any era, any product | Delete; open on the specific problem |
| now more than ever / gone are the days | Manufactured urgency, no event behind it | Cut, or cite the real change |
| say goodbye to X / say hello to Y | Forced before/after rhythm | "X used to take an hour. Now it's one click." |
| imagine a world where / what if you could / picture this | Asks the reader to imagine what you should show | Show the result directly |
| whether you're X or Y | Fake inclusivity; addresses everyone | Pick ONE audience and talk to them |
| from startups to enterprises | "For everyone" = positioning for no one | Name the one segment you're best for |
| let's face it / here's the thing / let's be honest | Fake conversational filler | Just say the thing |

### Cluster 7 — Fake-empathy pain-point intros

| Slop | Why it's empty | Human replacement |
|---|---|---|
| we know how hard it is to / we get it | Performed empathy | Name the specific pain precisely instead |
| tired of X? / struggling with X? / sound familiar? | Rhetorical setup with an obvious yes | State the pain as a fact |
| you're not alone | Therapy-speak in a sales context | Cut; show the data ("4,000 teams hit this") if real |

### Cluster 8 — Future / stakes inflation (marketing variant)

| Slop | Why it's empty | Human replacement |
|---|---|---|
| the future of X / building the future of | Grandiose, untestable | Describe the present thing it does |
| future-proof | Unfalsifiable time promise | "works with every major framework" |
| [Noun], reimagined / redefined / rethought | Says nothing changed but the verb | Say what specifically differs from the old way |
| the new era of / a new way to / the new standard for | Self-coronation | Earn it with a fact, or cut |
| paradigm shift / move the needle / disrupt | Consultant clichés | State the measurable change |

### Cluster 9 — Hollow CTAs

| Slop | Why it's empty | Human replacement |
|---|---|---|
| Get started today / Start now | Says nothing about what happens next | "Start free — no card" |
| Take your X to the next level | Recycled altitude cliché on a button | "Send your first campaign" |
| Start your journey | Travel metaphor on a signup | "See your dashboard in 60 seconds" |
| Join the revolution / Join thousands of X | Bandwagon, no specificity | "Join 12,300 developers" |
| Unlock your potential / The possibilities are endless | Self-help filler | State one concrete possibility |
| Ready to transform your X? | Question-CTA on a slop verb | "Ready to ship faster? Try it free." |

---

## Structural slop patterns

Format: **name** — *the slop* → the fix.

- **Feature-soup tricolon** — *"Fast. Secure. Scalable."* → Pick the one that's
  differentiating, prove it with a number; cut or expand the others.
- **Three identical benefit cards** — *same length, same `[icon] + [verb] + "that
  helps you…"` shape* → Break the symmetry; make the most important one
  bigger/first. Real benefits aren't equal weight.
- **The feature-description template** — *every feature is `[adjective] + [noun] +
  "that helps you" + [verb]`* → Lead with the outcome or a number; vary the shape.
- **Benefit claim with no proof** — *"Boost productivity and save time."* →
  Attach a number/mechanism/customer: "Cut reporting from 3 hours to 20 minutes."
- **"[Noun], reimagined" headline** → State the specific difference.
- **Fake-empathy intro block** → Open on the specific, slightly uncomfortable
  detail only an insider would name.
- **"Whether you're a startup or an enterprise" positioning** → Name one segment
  and one use case; let the rest self-select.
- **Flat hierarchy** — every section weighted the same → Decide the single most
  important claim; make everything else visibly subordinate.
- **Question headline → obvious answer** — *"Looking to grow your business?"* →
  Cut the question; make the assertion.
- **Generic social proof** — *"Sarah M., Marketing Director" + a quote that names
  nothing* → Real name, company, specific result. If you don't have it, omit.
- **Marketing "It's not just X, it's Y."** — negative parallelism weaponized for
  hype → Delete; make the positive claim once.
- **Mission-statement "about" opener** → Start with the concrete origin: what
  broke, what you built, who it's for.

---

## The deeper tells (why it feels AI even when the words are fine)

Each has a diagnostic question to run against the copy:

- **No specificity.** → "Name one number, proper noun, brand, or concrete object
  in this section. If there are none, it's slop."
- **No point of view.** → "What does this claim that a competitor would refuse to
  say? If everyone in the category would agree, you've said nothing."
- **The swap test.** → "Paste a competitor's logo on this page. Does it still
  read as true? If yes, it's not about your product."
- **Nothing falsifiable.** → "Could any sentence here be *false*? If no fact could
  disprove it, it's decoration, not a claim."
- **No friction or concession.** → "What tradeoff or 'not for you' does this
  admit? Copy that concedes nothing reads like an ad nobody believes."
- **Perfect symmetry.** → "Are the bullets/cards all the same length and shape?
  Real importance is uneven; equal weighting is a generation artifact."
- **'For everyone' positioning.** → "Who is this explicitly NOT for? If you can't
  answer, the targeting is mush."
- **Reader learns nothing new.** → "After reading, can the reader state one fact
  they didn't know? If not, it's filler."
- **Founder-voice test.** → "Would the founder say this out loud to a customer at
  a bar? If it'd be embarrassing, rewrite it."

---

## Humanizing moves (what to do instead)

- **Lead with a number or a noun.** "save ~4 hours a week," "one inbox for Gmail,
  Slack, and SMS" — specific beats superlative.
- **Take one clear side.** "Most CRMs are bloated. We do contacts and deals,
  nothing else." A point of view is what AI can't fake.
- **Admit a tradeoff.** "Slower to set up than X because we don't guess your data
  model." Conceding earns the trust the rest of the page spends.
- **Name who it's NOT for.** "Need enterprise SSO and audit logs? We're not there
  yet." Honest exclusion makes the inclusion believable.
- **Vary sentence length hard.** Follow a long sentence with a three-word
  fragment. AI keeps every sentence the same medium length; humans punch.
- **Use plain verbs.** helps, saves, cuts, sends, builds, shows, breaks.
- **Drop one unexpected, precise word.** "your 11pm bug," "the Monday standup,"
  "the 6-tab workflow" — a concrete noun signals a real person wrote it.
- **Use the customer's actual words.** Pull phrasing from tickets, reviews, sales
  calls — the language people use before they learn your jargon.
- **Show, don't claim.** A screenshot or a logged metric beats any adjective.
- **State the claim flat — confidence without hype.** "It deploys in one
  command." Calm specificity reads as more confident than superlatives.

---

## Quick before / after

| AI marketing copy | Human rewrite |
|---|---|
| "Unlock the power of seamless team collaboration." | "Edit the same doc as your teammate — no refresh, no merge conflicts." |
| "We're on a mission to revolutionize how modern teams work." | "We make standups 10 minutes shorter. That's the whole pitch." |
| "Our cutting-edge platform is designed to supercharge your productivity." | "Schedule a week of posts in about 15 minutes." |
| "Whether you're a scrappy startup or a global enterprise, our robust solution scales with your needs." | "Built for teams of 5–50. Past that you'll outgrow us, and we'll say so." |
| "Say goodbye to tedious manual data entry and hello to effortless automation." | "Connect Stripe once. Invoices land in QuickBooks the next morning." |
| "Take your marketing to the next level. Get started today!" | "One inbox for every channel. Start free — no card needed." |

---

*Sources: 925studios AI-slop web-design guide; Momentic "34 types of AI slop";
OneSec/swyx overused-ChatGPT-words lists; bsquared marketing-clichés list;
MarTech "if your AI content feels generic"; Tom Orbach anti-AI cheat sheet;
Paralect AI-slop markers; HumanText humanize-AI-copy.*
