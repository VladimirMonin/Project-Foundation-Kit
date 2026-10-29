# Third-party notices

Selected procedures were translated and substantially adapted, not bundled as a
complete upstream pack. The exact source/recipient map and exclusions are in
[UPSTREAM](UPSTREAM.md). Keep this file, UPSTREAM.md and [PFK LICENSE](LICENSE)
when transferring the complete pack. The following notices cover the respective
adapted portions; they do not license unrelated linked services, assets or docs.
The Caveman adaptation additionally carries its complete nested Apache-2.0 license.

## ECC

Source: [affaan-m/ECC LICENSE at 30b68924ae9729159f44326aa3134b1d9d67c0e2](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/LICENSE).
Applies to selected contract, impact, regression, document-role and UI procedures
identified in UPSTREAM.md. UI community lineage: PR #1659 by linus707;
state/evidence contribution via PR #2814, with the additional UIZZE notice below.

```text
MIT License

Copyright (c) 2026 Affaan Mustafa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Caveman — modified explanation procedure

Source: [JuliusBrussee/caveman at 2e08b9177c07bb7249a8a2d1a6758e5db281d002](https://github.com/JuliusBrussee/caveman/tree/2e08b9177c07bb7249a8a2d1a6758e5db281d002),
[skills/caveman/SKILL.md](https://github.com/JuliusBrussee/caveman/blob/2e08b9177c07bb7249a8a2d1a6758e5db281d002/skills/caveman/SKILL.md),
[LICENSING](https://github.com/JuliusBrussee/caveman/blob/2e08b9177c07bb7249a8a2d1a6758e5db281d002/LICENSING.md),
[NOTICE](https://github.com/JuliusBrussee/caveman/blob/2e08b9177c07bb7249a8a2d1a6758e5db281d002/NOTICE).
Recipient: [pf-caveman](skills/pf-caveman/SKILL.md), a changed PFK adaptation of
the voice rules and their Russian-language procedural adaptation, not an upstream
runtime or endorsed Caveman distribution. Answer-first, clarity and exact payload
are retained; verbosity selection and task-scope guards are added; hooks, commands,
other modes, fonts, binaries and persistence machinery are excluded.

The complete upstream [Apache License, Version 2.0](skills/pf-caveman/LICENSE)
travels inside this package. The relevant upstream NOTICE attribution is:

```text
Caveman
Copyright 2026 Julius Brussee
```

Other upstream NOTICE entries concern runtime/code/fonts not included in PFK.
Upstream also retains the pre-3.0 MIT notice for contributions to formerly MIT
portions. That applicable original notice is reproduced below, without relicensing
unrelated third-party work. Source:
[LICENSE-MIT](https://github.com/JuliusBrussee/caveman/blob/2e08b9177c07bb7249a8a2d1a6758e5db281d002/LICENSE-MIT).

```text
MIT License

Copyright (c) 2026 Julius Brussee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Engineering adaptations — 0.5.0

The following notices apply only to the selected changed procedures mapped in
[UPSTREAM](UPSTREAM.md): design-boundaries, complexity-reduction, quality,
behavior-regression/change-impact and their thin skill/template routes. The
Superpowers writing-skills references also inform the repository's finite AD
definitions, not a bundled evaluator. No complete donor skill pack is included.
The exact copyright holders are retained; an account/organization name is not
substituted for the holder named by its license.

### Matt Pocock — direct source and citypaul predecessor

Direct source: [mattpocock/skills LICENSE at 59db609eb1e18aaf59b63284d0e52255aff0c63c](https://github.com/mattpocock/skills/blob/59db609eb1e18aaf59b63284d0e52255aff0c63c/LICENSE).
The same MIT notice also appears in the attributed citypaul
[codebase-design/LICENSE at cd4028d57d6e4e95814f7b8ee55ca13c23a9c2f0](https://github.com/citypaul/.dotfiles/blob/cd4028d57d6e4e95814f7b8ee55ca13c23a9c2f0/claude/.claude/skills/codebase-design/LICENSE).
Its complete source-scope statement is retained below. That original directory
scope identifies lineage, not the location of the PFK adaptation.

```text
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

This license applies to the adapted portions of this directory
(`claude/.claude/skills/codebase-design/`) derived from Matt Pocock's
`codebase-design` skill and linked resources at:
https://github.com/mattpocock/skills/tree/66898f60e8c744e269f8ce06c2b2b99ce7660d5f/skills/engineering/codebase-design
```

### Adam Bulmer — reducer and citypaul predecessor

Direct source: [mintuz/skills LICENSE at d698a88fc1e4d054a25e5919f15658f673f602cb](https://github.com/mintuz/skills/blob/d698a88fc1e4d054a25e5919f15658f673f602cb/LICENSE).
The same MIT notice also appears in the attributed citypaul
[reduce-system-complexity/LICENSE at cd4028d57d6e4e95814f7b8ee55ca13c23a9c2f0](https://github.com/citypaul/.dotfiles/blob/cd4028d57d6e4e95814f7b8ee55ca13c23a9c2f0/claude/.claude/skills/reduce-system-complexity/LICENSE).
Its complete source-scope statement is retained below.

```text
MIT License

Copyright (c) 2025 Adam Bulmer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

This license applies to the adapted portions of this directory
(`claude/.claude/skills/reduce-system-complexity/`) derived from Adam
Bulmer's `reducer` skill at:
https://github.com/mintuz/skills/tree/d698a88fc1e4d054a25e5919f15658f673f602cb/plugins/core/skills/reducer
```

### Paul Hammond — citypaul local adaptations

Source: [citypaul/.dotfiles LICENSE at cd4028d57d6e4e95814f7b8ee55ca13c23a9c2f0](https://github.com/citypaul/.dotfiles/blob/cd4028d57d6e4e95814f7b8ee55ca13c23a9c2f0/LICENSE).
The source root scope is preserved verbatim. Its cli-design example is outside
the selected donor set; that directory is not bundled or adapted here.

```text
Repository license scope

Except where a nested `LICENSE` or `NOTICE` file states otherwise, this
repository is licensed under the MIT License below. A nested notice governs
its directory and takes precedence for material derived from that source; in
particular, `claude/.claude/skills/cli-design/` is licensed under CC BY-SA 4.0.

MIT License

Copyright (c) 2024 Paul Hammond

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Jesse Vincent — Superpowers selected test/evaluation guidance

Source: [obra/superpowers LICENSE at 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/LICENSE).
This does not assert that issue bodies/comments are licensed by the repository.
Their expression is not copied.

```text
MIT License

Copyright (c) 2025 Jesse Vincent

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Mr. Das — YAGNI in microsoft/agentic-loops

Source: [microsoft/agentic-loops LICENSE at 52cbe7a51a9965423517a963e226d6a933332b1c](https://github.com/microsoft/agentic-loops/blob/52cbe7a51a9965423517a963e226d6a933332b1c/LICENSE).

```text
MIT License

Copyright (c) 2026 Mr. Das

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Yonatan Karp-Rudin — architectural fitness functions

Source: [yonatankarp/software-design-skills LICENSE at e312055086e1e377dcd5c666e6a0f5c6255b869e](https://github.com/yonatankarp/software-design-skills/blob/e312055086e1e377dcd5c666e6a0f5c6255b869e/LICENSE).

```text
MIT License

Copyright (c) 2026 Yonatan Karp-Rudin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Import Linter, dependency-cruiser and Stryker are technical links only; their text,
configuration examples and runtime are not copied. Their distinct verified terms
and the excluded unlicensed ub-mode edition are documented in UPSTREAM.md, not
relicensed by these notices or by the PFK MIT license.

## UIZZE — UI state/evidence lineage

Source: [UIZZE LICENSE at 1b74390b28c18e54a87a23e7d9171101af304ae9](https://github.com/uizze/uizze/blob/1b74390b28c18e54a87a23e7d9171101af304ae9/LICENSE),
[anti-ui-slop skill](https://github.com/uizze/uizze/tree/1b74390b28c18e54a87a23e7d9171101af304ae9/skills/anti-ui-slop).
Applies to the adapted UI state/evidence workflow through ECC. No UIZZE service,
paid MCP, scripts, imagery or complete skill pack is included. This is not an
adaptation of canonical Anthropic frontend-design.

```text
MIT License

Copyright (c) 2026 UIZZE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
