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
