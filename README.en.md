# Russian Harmony · 俄罗斯和声 · Русская гармония

**A source-cited Agent Skill for studying and applying the Russian tradition of four-part harmony.**

[简体中文](README.md) · [English](README.en.md) · [Русский](README.ru.md)

[CC BY-NC 4.0 non-commercial license](LICENSE) · [Sources and crosswalk](references/source-map.md) · [Textbook differences](references/differences.md) · [Contributing](CONTRIBUTING.md)

[Copyright and disclaimer](COPYRIGHT_AND_DISCLAIMER.md) · [Privacy](PRIVACY.md)

## Overview

Russian Harmony organizes concepts, voice-leading procedures, functional interpretations, cadences and modulation techniques into an on-demand knowledge skill for AI assistants that support `SKILL.md`. It merges overlapping material from two textbooks while keeping differences and citations visible.

Use it for study, lesson preparation, exercise analysis and original harmonization. A complete four-part realization must still be checked against actual pitches, octaves, rhythm and context. This is an instruction and reference package, rather than a standalone application, automatic score reader, complete translation or exercise answer collection.

**Language coverage:** this project has complete introductory READMEs in Chinese, English and Russian. The skill instructions, topic notes and most reference files are currently written primarily in Chinese, with important Russian terminology retained. Three READMEs do not mean that all knowledge files have been translated into three languages.

## Principles

- **One teaching sequence:** follow Abyzova's introduction and 41 topics.
- **Merge overlap; preserve disagreement:** map all 60 topics of the coauthored textbook into that sequence, with separate supplements where needed.
- **Keep the path back to the source:** identify textbook, topic, printed pages and the PDF positions of the reference scans.
- **Plan before realizing:** establish phrase structure, cadences, tonal goals and voice-leading before choosing local voicings.
- **Separate technical rules from taste:** teacher requirements, stylistic practice and aesthetic preferences are not interchangeable.
- **Load only what is needed:** the entry file routes a task to relevant topic and reference files.

## Supported tasks

| Task | Typical use |
|---|---|
| Harmonize a melody or bass | Plan functions, realize SATB with octave labels, then examine connections |
| Examine voice-leading | Locate parallel fifths/octaves, crossing, overlap, range, doubling, omissions and tendency-tone treatment |
| Analyze function and cadences | Compare III/VI interpretations; explain K64, deceptive motion and cadential strength |
| Analyze tonicization and modulation | Identify local centers, pivot chords, reinterpretation and evidence of a new key |
| Learn terminology | Use Russian–Chinese equivalents and clarify tradition-specific meanings |
| Compare textbooks | Give each source's interpretation and the conditions on its exceptions |
| Teach and study progressively | Limit available material to the current stage and label original examples |

## Sources and organization

| Label | Textbook | Role in this edition |
|---|---|---|
| A | Е. Н. Абызова, *Гармония*. Москва: Музыка, 2008 | Main sequence: introduction and 41 topics |
| B | И. И. Дубовский, С. В. Евсеев, И. В. Способин, В. В. Соколов, *Учебник гармонии*. Москва: Музыка, 1965 | Crosswalk, supplements and comparison across 60 topics |

B is a work by four coauthors, not a book attributable to Sposobin alone. Dates follow the internal publication information in the reference scans. Other printings or scans may have different PDF offsets.

Coverage includes primary and subsidiary chords, inversions, seventh and ninth chords, cadences, non-chord tones, Russian diatonic/modal practice, alteration, tonicization, modulation, pedals and major–minor interaction. Abyzova's overview of twentieth-century harmony remains a separate topic. B's tonal planning, systematic harmonic analysis and approach to extended exercises are retained as supplements.

See the [full crosswalk](references/source-map.md) and [machine-readable index](references/source-index.json). Every topic has an entry, but the notes do not reproduce every score, exercise or uncommon variant.

## Differences are part of the model

The textbooks do not use one identical system. Examples include the functions of III and VI, octave exceptions in a particular incomplete dominant-seventh final cadence, chromatic versus modulating sequences, and three-level versus four-level systems of key relationship.

When no source is specified, the skill follows A's sequence and the more conservative elementary-exercise approach. A request for B or a particular teacher's requirements changes that choice explicitly. Consult the [differences table](references/differences.md).

## Installation

### Without programming

1. Select **Code → Download ZIP** on the repository page and extract it.
2. Name the complete folder `russian-harmony`. `SKILL.md`, `chapters/` and `references/` should sit directly inside it.
3. Place the complete folder in a skill directory supported by your host. Copying only `SKILL.md` is insufficient.
4. Check the host's skill list. Start a fresh session or restart if necessary.

| Host | Common personal location | Explicit invocation |
|---|---|---|
| Codex | `~/.agents/skills/russian-harmony/` | `$russian-harmony` |
| Claude Code | `~/.claude/skills/russian-harmony/` | `/russian-harmony` |

`~` means your user home directory. Codex also supports project-local `.agents/skills/russian-harmony/`. Other Agent Skills hosts may support the structure; follow their documentation. This project does not claim individual testing on every host. Back up or compare an existing folder before replacing it.

### With Git

Clone the complete repository into Codex's personal skill directory:

```bash
git clone https://github.com/josautxiao/russian-harmony.git ~/.agents/skills/russian-harmony
```

For Claude Code, use `~/.claude/skills/russian-harmony` as the destination. Normal use of the distilled knowledge requires neither OCR, third-party Python packages nor the original converter. For an actual textbook score or exercise, obtain a copy of the appropriate edition that you have the right to use.

A generic chat interface may not support installing skills. Uploading files does not automatically make a skill available across future conversations.

## Example prompts

```text
Use $russian-harmony to explain dominant-seventh inversions at the level of A topic 16.
Give an original SATB example with octave labels and examine all six voice pairs.
Answer in English.
```

```text
Use $russian-harmony to compare the textbooks' interpretations of the VI chord.
Separate shared rules, source-specific viewpoints and deductions for this example.
Include source references.
```

```text
Use $russian-harmony to examine my four-part exercise.
Locate each issue by time, voice and pitch, then propose the smallest correction.
Preserve the given melody.
```

Provide key signature, meter, pitches and durations, octave positions, the given melody or bass, and the material allowed at your current stage. You may request another response language, while remembering that the underlying notes are not yet fully multilingual.

## Repository guide

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Task routing, response rules and topic index |
| [chapters/](chapters/) | Introduction `ch00` and topics `ch01`–`ch41` |
| [patterns.md](patterns.md) | Harmonization and checking procedures; original full SATB model |
| [cheatsheet.md](cheatsheet.md) | Decision table |
| [glossary.md](glossary.md) | Russian–Chinese terminology |
| [references/](references/) | Sources, crosswalk, differences, B supplements and OCR limits |
| [agents/openai.yaml](agents/openai.yaml) | Codex display metadata and suggested invocation |
| [scripts/validate_repository.py](scripts/validate_repository.py) | Repository checks using the Python standard library |

## Quality and limitations

During initial preparation, text OCR ran over 824 image units from the two reference scans. Successful execution is not a claim of transcription accuracy. Ordinary OCR cannot reliably reconstruct notes, rhythm, accidentals, superscripts or figured bass from score examples.

- Check original pages for textbook exercises, score examples and fine-grained disputes.
- A Roman-numeral sequence is a harmonic plan; a complete realization also requires pitch, octave, duration and voice-by-voice examination.
- The initial skill underwent structural and link checks, topic-coverage checks, independent usage trials and examination of its original SATB model. These do not guarantee every rule or future answer.
- Automated repository checks cover structure, source entry points and public-content boundaries. They do not establish musical correctness or legal rights.

See [OCR and verification requirements](references/ocr-quality.md). Reports with a minimal example and precise source reference are welcome through Issues or Pull Requests.

## Updates and contributions

New textbooks should extend the existing crosswalk, merge overlap and preserve disagreements. Teacher experience should identify whose guidance it is, its scope, priority, exceptions and an original example. An unconfirmed aesthetic preference should not silently become a universal rule.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md). For a Git installation without local edits, update from its directory with `git pull --ff-only`. Back up personal changes or maintain them on a branch first.

## License and acknowledgments

This project is intended for non-commercial study and exchange among harmony enthusiasts. Original instructions, organization, explanations, examples and supporting code that the project is entitled to license are shared under [CC BY-NC 4.0](LICENSE), with attribution, identification of changes and no commercial use. Rights in the textbooks remain with authors, publishers or other lawful rights holders, not the maintainer. No piracy, copying or redistribution of the books is authorized; source PDFs, scans and full OCR transcripts are excluded. Non-commercial intent alone does not substitute for third-party permission.

Read the [copyright and disclaimer statement](COPYRIGHT_AND_DISCLAIMER.md) and [privacy notice](PRIVACY.md). Because commercial use is restricted, this is a publicly available non-commercial educational resource, rather than open-source software under the OSI definition.

The preparation workflow used extraction and skill-building ideas from [book-to-skill](https://github.com/virgiliojr94/book-to-skill); its conversion engine is not bundled. We acknowledge the textbook authors' teaching work. This is an independent project, without claimed endorsement by the authors, publishers or AI hosts. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
