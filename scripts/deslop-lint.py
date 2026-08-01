#!/usr/bin/env python3
"""deslop-lint.py — deterministic detector for AI-shaped copy.

Backstop for the deslop-copy skill. Generation-time rule-following is
probabilistic; this check is not. ERRORs gate delivery (exit 1). WARNs are
suspicions a regex can't settle — route them to the fresh-context judge.

Usage:
  deslop-lint.py FILE [FILE ...]     lint text/markdown files
  deslop-lint.py --review REVIEW.md  lint only **After** and Kept lines of a
                                     COPY-REVIEW.md (Before lines are meant
                                     to be dirty; they are skipped)
  ... | deslop-lint.py               lint stdin
  deslop-lint.py --self-test         run the embedded regression battery

Input convention for extracted copy: a line starting with "@ " sets the
location label for the lines that follow, e.g.

  @ src/components/Hero.tsx:12
  You walk out with signal, not a slide deck.

Exit codes: 0 no errors · 1 errors found · 2 usage/self-test failure.
Python 3 stdlib only.
"""

import re
import sys

EM = "—"
ERROR, WARN = "ERROR", "WARN"


def R(pattern):
    return re.compile(pattern, re.IGNORECASE | re.MULTILINE)


# --------------------------------------------------------------------------
# Shape rules — structural tells from references/bright-red.md
# --------------------------------------------------------------------------

SHAPES = [
    ("negation-contrast", ERROR,
     R(r"\b(?:it|this|that)['’]s not\b[^.!?]{0,60}?[—:;,]\s*(?:it|this|that)['’]s\b"),
     "delete the flip; make the positive claim once"),
    ("negation-contrast", ERROR,
     R(r"\bwe don['’]t\b[^.!?]{1,60}[.!?]\s*we\b"),
     "delete the denial; state what you do"),
    ("negation-contrast", ERROR,
     R(r"[,;—]\s*not\b"),
     "drop the contrast; keep the concrete half"),
    ("negation-contrast", ERROR,
     R(r"\bisn['’]t about\b|\bis not about\b|\baren['’]t about\b"),
     "say what it IS about, once"),
    ("negation-contrast", ERROR,
     R(r"(?:^|[.!?]\s+)not (?:a|an|the|your) [^.!?]{1,35}[.!?]\s*(?:a|an|the|it|just|your)\b"),
     "merge into one flat claim"),
    ("negation-contrast", ERROR,
     R(r"\bless about\b[^.!?]{1,60}\bmore about\b"),
     "state the 'more' half as a fact; cut the rest"),
    ("negation-contrast", ERROR,
     R(r"\bnot just\b|\bmore than just\b|\bdoesn['’]t just\b|\bdon['’]t just\b"),
     "cut 'just'-escalation; make the bigger claim directly or not at all"),
    ("negation-contrast", ERROR,
     R(r"\bno \w+[.,]\s*just \w+"),
     "'No X. Just Y.' is the flip in a trenchcoat; state Y plainly"),
    ("balanced-mirror", ERROR,
     R(r"\b[A-Za-z][\w'’ ]{0,30} is \w+[.!?]\s*[A-Za-z][\w'’ ]{0,30} isn['’]t\b"),
     "kill the symmetry; one blunt claim"),
    ("tricolon", ERROR,
     R(r"(?:^|[.!?:]\s+)\w+[.,] ?\w+[.,] ?(?:and )?\w+[.!]"),
     "one proven claim beats three beats"),
    ("tricolon", ERROR,
     R(r"\b\w+er, \w+er,? (?:and )?\w+er\b"),
     "pick the one comparative you can prove"),
    ("setup-reveal", ERROR,
     R(r"\bhere['’]s the (?:thing|catch|truth|kicker|secret|deal)\b"
       r"|\bthe (?:catch|kicker|twist|secret|best part)\?"
       r"|\bthat changes everything\b|\bplot twist\b|\bit gets better\b"
       r"|\bsound familiar\?"),
     "cut the tease; state the point"),
    ("em-dash-punch", WARN,
     R(EM + r"\s*\w+(?:['’]\w+)?(?:\s+\w+(?:['’]\w+)?){0,2}[.!]\s*$"),
     "dash-then-punch cadence; judge decides if it's a tic here"),
]

# Vague success enders — flag only clause-final so "works offline" survives
_CF = r"(?=\s*(?:$|[.,;:!?)\"'—”]))"
VAGUE_ENDERS = [
    ("vague-ender", ERROR, R(r"\bthat (?:just )?works" + _CF), "name the result instead"),
    ("vague-ender", ERROR, R(r"\bit just works" + _CF), "show it: steps, seconds, or cut"),
    ("vague-ender", ERROR, R(r"\bthat matters" + _CF), "matters to whom? name the stake"),
    ("vague-ender", ERROR, R(r"\bthat delivers" + _CF), "delivers WHAT? name the deliverable"),
    ("vague-ender", ERROR, R(r"\bdone right" + _CF), "name the specific better method"),
    ("vague-ender", ERROR, R(r"\bthe way it should be" + _CF), "correctness with no standard; cut"),
    ("vague-ender", ERROR, R(r"\bbuilt different" + _CF), "name the actual difference"),
    ("vague-ender", ERROR, R(r"\bmade (?:simple|easy|effortless)" + _CF), "show the step count instead"),
    ("vague-ender", ERROR, R(r"\bfor the modern \w+"), "name the literal user + constraint"),
]

# Vocabulary clusters — the marketing-slop.md blocklist, mechanized.
# (tier, shared fix hint, [patterns])
WORD_CLUSTERS = [
    (ERROR, "LLM-tell word; use the plain word",
     [r"\bdelve\w*", r"\butiliz\w+", r"\bleverag\w+", r"\brobust\w*",
      r"\bstreamlin\w+", r"\bharness\w*", r"\bcrucial\b", r"\bpivotal\b",
      r"\bmeticulous\w*", r"\btapestry\b", r"\btestament\b", r"\bintricate\b",
      r"\bempower\w*", r"\bmultifaceted\b", r"\bnuanced\b", r"\bholistic\b",
      r"\bsynerg\w+", r"\belevat\w+", r"\benhanc\w+"]),
    (ERROR, "grandiose verb; state the number or the literal action",
     [r"\bunlock\w*", r"\bunleash\w*", r"\bsupercharg\w+", r"\bturbocharg\w+",
      r"\brevolutioniz\w+", r"\breinvent\w*", r"\bamplif\w+", r"\bskyrocket\w*",
      r"\bpropel\w*", r"\bboost\w*", r"\blevel up\b", r"\bto the next level\b",
      r"\bnext-level\b", r"\btransform(?:s|ed|ing)? (?:your|the way|how)\b",
      r"\bdrive (?:growth|results|engagement)\b"]),
    (ERROR, "effortlessness claim; name the steps/time it actually takes",
     [r"\bseamless\w*", r"\beffortless\w*", r"\bfrictionless\b",
      r"\bhassle-free\b", r"\bpainless\w*", r"\bintuitive\w*"]),
    (ERROR, "self-awarded medal; cite a number, comparison, or customer",
     [r"\bbest-in-class\b", r"\bworld-class\b", r"\bindustry-leading\b",
      r"\btop-tier\b", r"\bcutting-edge\b", r"\bstate-of-the-art\b",
      r"\bnext-gen\w*", r"\bbleeding-edge\b", r"\bgame-chang\w+",
      r"\bgroundbreaking\b", r"\brevolutionary\b", r"\bunparalleled\b",
      r"\bunrivall?ed\b", r"\bunmatched\b", r"\binnovative\b",
      r"\bpowerful\b", r"\btransformative\b", r"\bdisruptive\b"]),
    (ERROR, "emptiest noun in B2B; name the category ('a Postgres GUI')",
     [r"\bsolutions?\b"]),
    (ERROR, "mission platitude; cut and state the fact",
     [r"\bwe['’]?\s?a?re on a mission\b", r"\bwe believe\b",
      r"\byour trusted partner\b", r"\bdesigned to help\b", r"\bbuilt to help\b",
      r"\btailored to your\b", r"\byour unique needs\b", r"\bcustomer-centric\b",
      r"\bpeople-first\b", r"\bcustomer-obsessed\b", r"\bpassionate about\b"]),
    (ERROR, "opening cliché; delete and open on the specific problem",
     [r"\bin today['’]s\b", r"\bfast-paced\b", r"\bdigital age\b",
      r"\bever-evolving\b", r"\bnow more than ever\b", r"\bgone are the days\b",
      r"\bsay goodbye to\b", r"\bsay hello to\b", r"\bimagine a world\b",
      r"\bwhat if you could\b", r"\bpicture this\b", r"\bwhether you['’]re\b",
      r"\bfrom startups to enterprises\b", r"\blet['’]s face it\b",
      r"\blet['’]s be honest\b"]),
    (ERROR, "performed empathy; state the pain as a fact",
     [r"\bwe know how hard\b", r"\bwe get it\b",
      r"\btired of [^.!?]{0,40}\?", r"\bstruggling with [^.!?]{0,40}\?",
      r"\byou['’]re not alone\b"]),
    (ERROR, "future/stakes inflation; describe the present thing it does",
     [r"\bthe future of \w+", r"\bfuture-proof\b", r"\breimagined\b",
      r"\bredefined\b", r"\bparadigm shift\b", r"\bmove the needle\b",
      r"\b(?:a|the) new era\b", r"\bthe new standard for\b"]),
    (ERROR, "hollow CTA; say what happens next ('Start free — no card')",
     [r"\bget started today\b", r"\bstart your journey\b",
      r"\bjoin the revolution\b", r"\bjoin thousands\b",
      r"\bpossibilities are endless\b", r"\bready to transform\b"]),
    (ERROR, "filler transition; cut",
     [r"\bit['’]s worth noting\b", r"\bworth noting that\b",
      r"\bin summary\b", r"\bat the end of the day\b"]),
    (WARN, "scope-inflating noun; judge decides if it hides the feature",
     [r"\bplatform\b", r"\becosystem\b", r"\blandscape\b", r"\bcomprehensive\b",
      r"\ball-in-one\b", r"\bend-to-end\b", r"\bone-stop shop\b",
      r"\btoolkit\b", r"\btoolbox\b"]),
    (WARN, "process-flavored verb; name what's removed ('one step, not six')",
     [r"\boptimiz\w+", r"\bmaximiz\w+", r"\bacceler\w+"]),
    (WARN, "commitment platitude; judge decides",
     [r"\bcommitted to\b", r"\bdedicated to\b", r"\ba new way to\b",
      r"\brethought\b", r"\bultimately\b", r"\bnotably\b", r"\bimportantly\b"]),
]

# Imperative first words that make a 1-3 word sentence a CTA, not a fragment
CTA_VERBS = {
    "get", "start", "try", "learn", "sign", "join", "book", "see", "watch",
    "read", "download", "subscribe", "buy", "shop", "explore", "browse",
    "compare", "contact", "talk", "request", "schedule", "view", "meet",
    "choose", "pick", "claim", "grab", "go", "visit", "check", "discover",
    "create", "make", "build", "add", "install", "upgrade", "save", "ship",
    "push", "connect", "edit", "send", "ask", "find", "stop", "skip",
}

STRIP_PATTERNS = [
    R(r"‹NEEDS:[^›]*›"),   # ‹NEEDS: …› flags are legit workflow
    R(r"https?://\S+"),
    R(r"`[^`]*`"),
    R(r"<[^>]{1,80}>"),
]


def clean_text(text):
    for pat in STRIP_PATTERNS:
        text = pat.sub(" ", text)
    text = text.replace("**", "").replace("__", "")
    return text


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def words(text):
    return re.findall(r"[\w'’-]+", text)


def excerpt(text, match, width=52):
    s, e = match.start(), match.end()
    lo = max(0, s - 12)
    frag = text[lo:lo + max(width, e - s + 12)].strip()
    frag = re.sub(r"\s+", " ", frag)
    return ("…" if lo > 0 else "") + frag[:width] + ("…" if len(frag) > width else "")


def scan_item(loc, raw_text):
    """Lint one copy item. Returns list of (loc, tier, rule, excerpt, hint)."""
    text = clean_text(raw_text)
    findings = []

    for rule, tier, pat, hint in SHAPES + VAGUE_ENDERS:
        for m in pat.finditer(text):
            findings.append((loc, tier, rule, excerpt(text, m), hint))

    for tier, hint, pats in WORD_CLUSTERS:
        for p in pats:
            for m in R(p).finditer(text):
                findings.append((loc, tier, "slop-vocab", excerpt(text, m, 40), hint))

    sents = sentences(text)

    # Dramatic fragment: 1-3 words, terminal [.!], not an imperative CTA
    for s in sents:
        w = words(s)
        if 0 < len(w) <= 3 and s.endswith((".", "!")) and not any(ch.isdigit() for ch in s):
            if w[0].lower() not in CTA_VERBS:
                findings.append((loc, WARN, "dramatic-fragment", s,
                                 "clipped noun for gravitas — or a CTA? judge decides"))

    # Possible mirror: adjacent short sentences sharing a first word
    for a, b in zip(sents, sents[1:]):
        wa, wb = words(a), words(b)
        if 0 < len(wa) <= 8 and 0 < len(wb) <= 8 and wa[0].lower() == wb[0].lower():
            findings.append((loc, WARN, "possible-mirror", a + " " + b,
                             "parallel stems read as manufactured symmetry — judge decides"))

    # Three consecutive tiny sentences = tricolon tagline
    for a, b, c in zip(sents, sents[1:], sents[2:]):
        if all(len(words(x)) <= 2 for x in (a, b, c)):
            findings.append((loc, ERROR, "tricolon", " ".join((a, b, c)),
                             "one proven claim beats three beats"))

    # Whole-line short rhetorical question
    stripped = text.strip()
    if re.fullmatch(r"\W*\w+(?:['’]\w+)?(?:\s+\w+(?:['’]\w+)?){0,4}\?\W*", stripped):
        findings.append((loc, WARN, "question-tease", stripped,
                         "short rhetorical question — obvious-answer bait? judge decides"))

    # Long sentence (review mode signal; harmless elsewhere)
    for s in sents:
        if len(words(s)) > 28:
            findings.append((loc, WARN, "long-sentence", s[:52] + "…",
                             "cut it in half"))

    return findings


def dedupe(findings):
    seen, out = set(), []
    for f in findings:
        key = (f[0], f[2], f[3])
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


# --------------------------------------------------------------------------
# Input collection
# --------------------------------------------------------------------------

def items_from_text(label, text):
    """Plain/markdown text -> [(loc, line)]. '@ path' lines set the location."""
    items, loc = [], label
    in_fence, in_front = False, False
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if i == 1 and s == "---":
            in_front = True
            continue
        if in_front:
            if s == "---":
                in_front = False
            continue
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not s:
            continue
        if s.startswith("@ "):
            loc = s[2:].strip()
            continue
        s = re.sub(r"^#{1,6}\s+", "", s)          # heading text is copy too
        s = re.sub(r"^[-*>]\s+", "", s)
        if re.fullmatch(r"[|\-: ]+", s) or not s:  # md table rules etc.
            continue
        tag = loc if loc != label else "%s:%d" % (label, i)
        items.append((tag, s))
    return items


def items_from_review(text):
    """COPY-REVIEW.md -> After + Kept lines only."""
    items, section, in_kept = [], "?", False
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        h = re.match(r"^##\s+(.*)", line)
        if h:
            head = h.group(1).split("·")[0].strip()
            in_kept = head.lower().startswith("kept")
            if not in_kept:
                section = head
            i += 1
            continue
        m = re.match(r"^\*\*After\*\*\s*>?\s*(.*)", line)
        if m:
            buf = [m.group(1)]
            while i + 1 < len(lines) and lines[i + 1].lstrip().startswith(">"):
                i += 1
                buf.append(lines[i].lstrip()[1:].strip())
            items.append(("After · " + section, " ".join(b for b in buf if b)))
        elif in_kept:
            b = re.match(r"^-\s+(.*)", line)
            if b:
                kept = b.group(1).split(" — ")[0].strip()
                if kept:
                    items.append(("Kept", kept))
        i += 1
    return items


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def report(items, out=sys.stdout):
    findings = []
    for loc, text in items:
        findings.extend(scan_item(loc, text))
    findings = dedupe(findings)

    all_text = " ".join(t for _, t in items)
    total_words = len(words(all_text))
    dash_count = all_text.count(EM)
    if total_words >= 50 and dash_count >= 2 and dash_count / total_words * 100 > 1.0:
        findings.append(("(overall)", WARN, "em-dash-density",
                         "%d em dashes in %d words" % (dash_count, total_words),
                         "more than ~1 per 100 words is a tic"))

    errors = [f for f in findings if f[1] == ERROR]
    warns = [f for f in findings if f[1] == WARN]

    for loc, tier, rule, exc, hint in sorted(findings, key=lambda f: (f[1] != ERROR, f[0])):
        out.write("%-5s %-18s %s\n      “%s” → %s\n" % (tier, rule, loc, exc, hint))

    rate = (len(findings) / total_words * 100) if total_words else 0.0
    out.write("── %d errors · %d warnings · %d words · %.1f hits/100w\n"
              % (len(errors), len(warns), total_words, rate))
    if errors:
        out.write("ERRORs must be rewritten (not reworded around the regex). Rerun until 0.\n")
    if warns:
        out.write("WARNs go to the fresh-context judge — include them in its brief.\n")
    return len(errors)


# --------------------------------------------------------------------------
# Self-test battery
# --------------------------------------------------------------------------

MUST_FLAG = [  # (expected tier, expected rule substring, text)
    (ERROR, "negation-contrast", "It's not software — it's a revolution."),
    (ERROR, "negation-contrast", "We don't build your idea. We find the one that works."),
    (ERROR, "negation-contrast", "You walk out with signal, not a slide deck."),
    (ERROR, "negation-contrast", "Hiring isn't about résumés. It's about potential."),
    (ERROR, "negation-contrast", "Not a purchase. An investment."),
    (ERROR, "negation-contrast", "Less about clicks, more about connection."),
    (ERROR, "negation-contrast", "More than just a chatbot."),
    (ERROR, "negation-contrast", "No fluff. Just results."),
    (ERROR, "negation-contrast", "Your idea, validated — not guessed."),
    (ERROR, "balanced-mirror", "Building is solved. Getting picked isn't."),
    (ERROR, "tricolon", "Discover, plan, build."),
    (ERROR, "tricolon", "Faster, simpler, smarter."),
    (ERROR, "tricolon", "Fast. Secure. Scalable."),
    (ERROR, "setup-reveal", "Here's the thing: distribution wins."),
    (ERROR, "setup-reveal", "The best part? It's free."),
    (ERROR, "vague-ender", "A CRM that just works."),
    (ERROR, "vague-ender", "Standups, done right."),
    (ERROR, "slop-vocab", "Unlock the power of seamless team collaboration."),
    (ERROR, "slop-vocab", "Our cutting-edge platform is designed to help you supercharge productivity."),
    (ERROR, "slop-vocab", "In today's fast-paced world, teams need speed."),
    (ERROR, "slop-vocab", "Whether you're a startup or an enterprise, we scale."),
    (ERROR, "slop-vocab", "Say goodbye to manual data entry."),
    (ERROR, "slop-vocab", "The future of payments."),
    (ERROR, "slop-vocab", "Take your marketing to the next level."),
    (ERROR, "slop-vocab", "Standups, reimagined."),
    (ERROR, "slop-vocab", "We believe every team deserves great tools."),
    (WARN, "dramatic-fragment", "Signal."),
    (WARN, "possible-mirror", "Your instincts are right. Your ideas are wrong."),
    (WARN, "question-tease", "Looking to grow your business?"),
]

MUST_PASS = [  # no ERRORs allowed (WARNs fine)
    "We test your idea before you build it.",
    "You get the one real users want.",
    "Getting picked is the hard part.",
    "Close your books in 2 days.",
    "Financial infrastructure for the internet.",
    "Get through your inbox twice as fast.",
    "The World's Strongest Coffee.",
    "Edit the same doc as your teammate — no refresh, no merge conflicts.",
    "Connect Stripe once. Invoices land in QuickBooks the next morning.",
    "Built for teams of 5–50. Past that you'll outgrow us, and we'll say so.",
    "Start free — no card needed.",
    "Push to git. Live in 90 seconds. Every branch gets its own URL.",
    "Schedule a week of posts in about 15 minutes.",
    "New hires ship code on day one.",
    "Cut your standup from 30 minutes to a glance.",
    "One inbox for Gmail, Slack, and SMS.",
]


def self_test():
    failed = 0
    for tier, rule, text in MUST_FLAG:
        found = scan_item("t", text)
        if not any(f[1] == tier and rule in f[2] for f in found):
            got = ", ".join("%s:%s" % (f[1], f[2]) for f in found) or "nothing"
            print("MISS  expected %s %s in: %r (got %s)" % (tier, rule, text, got))
            failed += 1
    for text in MUST_PASS:
        errs = [f for f in scan_item("t", text) if f[1] == ERROR]
        if errs:
            print("FALSE-POS  %r -> %s" % (text, ", ".join(f[2] for f in errs)))
            failed += 1
    total = len(MUST_FLAG) + len(MUST_PASS)
    print("self-test: %d/%d passed" % (total - failed, total))
    return 2 if failed else 0


# --------------------------------------------------------------------------

def main(argv):
    if "--self-test" in argv:
        return self_test()
    if "--review" in argv:
        idx = argv.index("--review")
        if idx + 1 >= len(argv):
            print("usage: deslop-lint.py --review COPY-REVIEW.md", file=sys.stderr)
            return 2
        with open(argv[idx + 1], encoding="utf-8") as fh:
            items = items_from_review(fh.read())
        if not items:
            print("no **After** or Kept lines found — wrong file or format?",
                  file=sys.stderr)
            return 2
        return 1 if report(items) else 0

    files = [a for a in argv if not a.startswith("-")]
    items = []
    if files:
        for path in files:
            with open(path, encoding="utf-8") as fh:
                items.extend(items_from_text(path, fh.read()))
    else:
        items = items_from_text("stdin", sys.stdin.read())
    return 1 if report(items) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
