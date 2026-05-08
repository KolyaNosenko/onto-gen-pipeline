# Third-party notices

This project vendors third-party source code. The notices below preserve
the attribution and license terms of the upstream projects, as required
by their licenses.

## Owlready2

The directories `src/og_sandbox_with_core/engine/` and
`src/og_sandbox_no_core/engine/` contain a vendored copy of
[Owlready2](https://owlready2.readthedocs.io/), a Python library for
loading, manipulating, and reasoning about OWL ontologies.

- **Upstream version:** Owlready2 0.49
- **Author:** Jean-Baptiste Lamy, with contributors at LIMICS (Laboratoire
  d'informatique médicale et d'ingénierie des connaissances en santé,
  UMR_S 1142), University Paris 13, Sorbonne Paris-Cité, Bobigny, France.
- **Original copyright:** Copyright (C) 2013–2022 Jean-Baptiste Lamy.
- **License:** GNU Lesser General Public License, version 3 or later
  (LGPL-3.0-or-later). The full license text is at
  [`LICENSES/LGPL-3.0-Owlready2.txt`](LICENSES/LGPL-3.0-Owlready2.txt).

The vendored sources have been **modified** for use within this project:

- Re-rooted from the `owlready2` top-level package into the
  `og_sandbox_with_core.engine` and `og_sandbox_no_core.engine`
  namespaces.
- Per-file LGPL preambles replaced with a short SPDX-style header that
  references this file and the central license.
- Incidental brand strings in print/log messages and comments removed
  for code-clarity. Functional identifiers (module names, public
  classes, IRI strings used by the upstream OWL semantics) are
  preserved verbatim.

For the precise diff against upstream Owlready2 0.49, consult this
project's git history. The modifications are distributed under the
same LGPL-3.0-or-later license as the upstream work; the original
copyright and license terms continue to apply.

## RPLY (vendored via Owlready2)

The file `engine/rply.py` (in both sandbox copies) is a stripped-down,
dependency-less adaptation of [RPLY](https://github.com/alex/rply) by
Alex Gaynor and contributors, originally bundled in Owlready2.

- **Author:** Alex Gaynor and individual contributors.
- **License:** BSD 3-Clause. The full license text is at
  [`LICENSES/BSD-3-Clause-rply.txt`](LICENSES/BSD-3-Clause-rply.txt).

The vendored copy retains the BSD-3-Clause terms; project modifications
are similarly distributed under BSD-3-Clause.

---

This project's own (non-vendored) source code lives outside the two
`engine/` directories and is governed by the project's own license
terms.
