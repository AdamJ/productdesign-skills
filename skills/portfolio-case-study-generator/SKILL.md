---
name: portfolio-case-study-writer
description: >
  Write and refine portfolio case studies for Adam Jolicoeur, a Lead Product Designer and PM
  targeting founding designer / startup designer roles at early-stage companies. Use this skill
  whenever Adam asks to write, draft, outline, revise, or workshop a portfolio piece, case study,
  project story, or "write-up" about any project — personal or professional. Also trigger when
  Adam says things like "help me tell the story of X", "I want to add Y to my portfolio", or
  "how should I frame this project." This skill encodes his voice, narrative structure, and
  audience so output lands on-target without extensive back-and-forth.
---

# Portfolio Case Study Writer

This skill produces portfolio case studies for Adam that are ready for publication at
adamjolicoeur.com/portfolio/. The audience is **design hiring managers at early-stage startups**
— typically a founding team evaluating whether Adam can own the full design function from zero.

---

## Adam's Background (always in scope)

- 15+ years enterprise experience: AWS (Task-it, 500 DAU in 18 months), Red Hat (PatternFly, 20k+ GitHub stars)
- Lead Product Designer + PM who bridges design, product thinking, and frontend implementation
- Comfortable owning the full stack of a feature: discovery → system design → shipped code → iteration
- Currently: CAS (construction management tools, AI PM assistant CASim, OCR plan management)
- Personal: Brimfield Labs indie apps (Magic: The Gathering tracker, TimeTracker Pro PWA)
- Job target: founding designer at early-stage company; wants to signal **ownership, judgment, and systems thinking** — not just craft

---

## Narrative Structure

Every case study follows this arc, though the section names and emphasis may shift per project:

1. **Context / Problem** — What was the situation, and why did it matter? Ground in the team/product state, not just a feature description. Keep this tight.
2. **Constraints** — What made this hard? (Timeline, solo execution, technical debt, competing priorities.) This is where the story earns credibility.
3. **Approach / Decisions** — The thinking, not just the output. What tradeoffs were made and why? What was considered and rejected? This is the heaviest section.
4. **Execution** — What was actually built, and who built it? Be honest about Adam's specific contribution vs. team effort.
5. **Outcome** — Concrete results where possible (metrics, adoption, team feedback). If metrics aren't available, frame the impact qualitatively but specifically.
6. **Reflection** — Optional but valuable for longer pieces: what would Adam do differently, or what this unlocked.

---

## Voice and Tone

Adam writes the way he talks: direct, peer-level, confident without being boastful. He does not:

- Use buzzwords ("leveraged", "spearheaded", "synergy")
- Pad with qualifications or hedge unnecessarily
- Over-explain process steps as if the reader doesn't understand design
- Use bullet-heavy structure in prose sections (bullets are fine for lists of decisions or outcomes)

He does:

- Use "I" confidently for solo work; credit the team honestly when it was collaborative
- Lead with the interesting part — the problem or constraint — not with his role/title
- Treat the reader as a smart peer who wants signal, not a portfolio rubric checklist
- Show judgment: _why_ a decision was made carries more weight than _what_ was made

Avoid: overly formal tone, overly casual/humble tone, excessive use of "I then..." sequential narration.

---

## Emphasis for Startup/Founding Designer Audience

The hiring manager at an early-stage company is asking: _Can this person own the design function? Do they understand the business? Can they ship without hand-holding?_

Lean into:

- **Solo execution** — when Adam owned something end-to-end, say so clearly
- **Speed and pragmatism** — decisions made under constraint are more interesting than perfect processes
- **Cross-functional judgment** — moments where Adam shaped product direction, not just design execution
- **Systems thinking** — when Adam built something reusable, scalable, or that unblocked others
- **Technical fluency** — frontend implementation involvement, design-to-code handoff, Storybook/design system work

De-emphasize: large team dynamics, long enterprise timelines, or process-for-process's-sake (unless reframing it as contrast to the startup context).

---

## Format Guidelines

- **Length**: Aim for 600–1000 words for a standard published piece. Shorter for teaser/landing page versions.
- **Headers**: Use sparingly. The narrative should flow; headers signal major pivots, not every paragraph.
- **Visuals callouts**: Use `[IMAGE: description]` placeholder where a screenshot, diagram, or mockup would land.
- **Publication path**: `adamjolicoeur.com/portfolio/[project-slug]`
- **Meta description**: Always generate a 1–2 sentence meta description for SEO/social sharing.

---

## Interaction Pattern

When Adam invokes this skill, start by asking:

1. **Project**: What's the project? (If he's told you, confirm the key details.)
2. **Scope of his contribution**: Was this solo, collaborative, or within a large team?
3. **Outcome clarity**: Does he have metrics or concrete outcomes, or is it more qualitative?
4. **Existing material**: Does he have notes, a doc, screenshots, or previous drafts to work from?
5. **Format needed**: Full published piece, outline first, or a short teaser?

If Adam has already answered these in the conversation, skip straight to writing. Don't re-ask what's already clear.

After a draft, ask one focused question: _"Is there anything here that doesn't sound like you, or a decision/constraint I missed that should be in the story?"_ — not a general "what do you think?"

---

## Reference: TimeTracker Pro AI Weekly Report (Published Example)

This is the canonical example of the target output. Key things it got right:

- Led with the _problem_ (context fragmentation, not "I built an AI feature")
- Named the solo execution explicitly without being self-congratulatory
- Described the two-part prompt architecture as a product decision, not a technical detail
- Tone was direct and peer-level throughout
- Outcome was framed specifically even without hard metrics

Read `references/timetracker-pro-example.md` if you need to calibrate voice/structure against a real example.

---

## Common Pitfalls to Avoid

- **Starting with the solution**: "I designed a feature that..." is weaker than "The problem was..."
- **Burying the constraint**: The hard part is usually the most interesting part. Surface it early.
- **Vague outcomes**: "Users responded positively" is not an outcome. "The feature shipped and was adopted by all active users within the first week" is.
- **Over-indexing on process**: Showing a design process is fine, but the _judgment within_ the process is what matters to this audience.
- **Underselling solo work**: If Adam built it alone — design, code, and integration — say that explicitly.

---

## Planned Extension: Case Study Updates

A future extension will handle revising existing case studies as projects evolve — rather than rewriting from scratch. The pattern: given a published case study and a description of what's changed (new features shipped, outcomes now available, direction pivoted), update only the relevant sections (Outcome, Reflection, "Where It Stands") while preserving the established voice and structure. Sections like Context, Constraints, and core Approach decisions should remain stable unless the project fundamentally changed. This is especially useful for in-progress projects like SoccerGameTracker where outcomes will sharpen over time.
