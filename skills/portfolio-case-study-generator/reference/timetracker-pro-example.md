# Reference: TimeTracker Pro — Weekly Report Feature

## Published case study at adamjolicoeur.com/portfolio/timetrackerpro

This is the canonical example of Adam's voice, structure, and narrative approach.
Use it to calibrate tone and depth when drafting new case studies.

---

## About TimeTracker Pro

TimeTracker Pro is a personal productivity app I designed and built to solve a problem I couldn't find a good off-the-shelf solution for: simple, honest time tracking without an account, a subscription, or a dashboard I'd never look at.

It runs in the browser, installs as a native-like app on desktop and mobile, and stores data locally by default — no account required. Throughout the day I create tasks, assign them to projects and categories, and archive each completed day. Over time it builds a personal record of where my time actually goes.

I built it because every time tracking tool I tried was either too complex for personal use or too simple to be useful. TimeTracker Pro is purpose-built for the way I work: start the day, capture tasks as they happen, review and archive at the end. It has been in daily use since early 2025 and has grown into a small but complete product — export formats, project management, offline support, and now AI-powered reporting.

---

## The Weekly Report Feature

After archiving each day, I found myself running a second, separate tool to generate a weekly summary. That tool only worked with PDFs exported from the time tracker, only ran on a local development server, and produced output that always needed manual cleanup before it was usable. It was a workaround, not a product.

The Weekly Report feature replaces that entire workflow. It lives inside TimeTracker Pro as a dedicated route, reads directly from the same data the rest of the app uses, and generates a coherent weekly narrative using an AI model. The output can be tuned for different audiences — a team standup, a client update, or a personal retrospective — and is editable before copying. No export step, no separate server, no manual cleanup.

> "The right tool for summarizing my work week is the tool that already knows my work week."

---

## The Problem

The original two-tool setup had three specific friction points:

- **No real integration.** The generator only accepted PDFs from the time tracker, creating a dependency without any actual data sharing. The export was the only bridge between them.
- **Availability gap.** The generator ran on a local Vite server, which meant it was only accessible from one machine in one context. Any time I needed a summary on a different device, I was out of luck.
- **Output that always needed editing.** Because the generator had no understanding of who I was writing for, every summary came out generic and required manual work to make it usable.

The deeper problem was that the tooling made a simple, recurring task feel like a project. I needed a paragraph I could drop into a standup or send to a client. What I had was a process.

---

## Extend, Not Replace

The obvious move might have been to build a better standalone summary tool. I chose not to, and the reasoning matters.

A generic AI summary tool would be useful for anyone. The Weekly Report feature is specifically useful for me, because it has full context of my data structure, project names, and work patterns. The value isn't in the summarization model — it's in the integration. Extending TimeTracker Pro meant I could read from the data layer directly instead of serializing and re-importing it. It meant the feature would live alongside the rest of the app, accessible anywhere TimeTracker Pro is accessible. And it meant the feature would evolve alongside the product instead of diverging from it.

---

## Design and Execution

The feature is a dedicated route in the app — `/report` — with a two-panel layout that puts controls on the left and output on the right. On screens wide enough to support it, both panels are visible simultaneously, which means you can adjust the tone selector or date range and watch the output update without any page transition.

The generation flow has four states I designed explicitly: idle (with a prompt to get started), loading (skeleton lines that match the expected output shape), complete (the formatted summary with a copy button), and error (structured messaging that tells you what failed and why). Each of those states required a decision. The skeleton lines aren't generic spinners — they're shaped like paragraphs because that's what the output looks like, and that specificity makes the wait feel shorter.

The prompt architecture is two-part. First, the app serializes the week's archived data into a structured format, stripping noise — blank entries, duplicate categories, formatting artifacts — before it goes to the model. Second, the model prompt instructs for tone based on the selected variant. Standup summaries are short and task-focused. Client updates are polished and outcome-focused. Retrospectives are reflective and include time distribution. The prompt itself is something I expect to keep tuning as I observe how the output actually gets used.

[IMAGE: Two-panel layout showing controls on left, generated output on right]
[IMAGE: Loading state with paragraph-shaped skeleton lines]
[IMAGE: Complete state with formatted output and copy button]

---

## Outcome

The feature shipped and immediately replaced the two-tool workflow I'd been using. I use it weekly. The generation is fast enough that it doesn't feel like a waiting experience, and the tone variants mean I'm not rewriting the output before I send it — which was the core problem.

From a portfolio standpoint the project demonstrates a specific combination of skills: identifying friction in a real workflow, making a considered architectural decision about where a feature belongs, designing the interaction states that make AI output feel trustworthy, and shipping something that has been in daily use since it launched.

That combination — problem identification, systems thinking, AI UX design, and a shipped product used daily — is the argument for what I bring to a founding designer role.

---

## What This Example Demonstrates About Adam's Voice

**Lead with the problem, not the solution.** The case study doesn't open with "I built an AI feature." It opens with the workflow friction that made the feature worth building.

**Name the architectural decision explicitly.** "Extend, not replace" is the core judgment call. The section doesn't just describe what was built — it explains the reasoning that ruled out the obvious alternative.

**Specificity over generality in outcomes.** "The feature shipped and immediately replaced the two-tool workflow" is more credible than "users responded well."

**AI as a system, not a black box.** The two-part prompt architecture is described as a product decision (what to strip, how to tune tone variants) not a technical implementation detail.

**Solo work named clearly without being self-congratulatory.** "I designed and built" appears early and is simply true — it doesn't editorialize.

**The portfolio argument made directly.** The last paragraph of the Outcome section names exactly what the case study is evidence of. This is a choice — some designers avoid this kind of directness, but for a founding designer audience it signals that Adam understands the business context of his own work.
