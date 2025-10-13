# Component Deployment Guide

Follow this checklist whenever you add or update shared components in this repository.

## Quick Start Checklist

1. **Plan the component**
   - Decide whether it belongs in `gaik-py` (Python) or `gaik-ts` (TypeScript).
   - Add the implementation, tests, and short documentation in the same package.

2. **Test locally**
   - Python: `cd gaik-py && pip install -r requirements.txt && pip install -e ".[dev]" && pytest`
   - TypeScript: `cd gaik-ts && pnpm install && pnpm test`
   - Optional: run `gaik-demo` to try both packages inside Docker.

3. **Bump the version**
   - Python: update `pyproject.toml` and `gaik/__init__.py`.
   - TypeScript: update `package.json`.

4. **Tag the release**
   - Create `git tag v0.2.0` (or the next version) and push it.
   - Publish a GitHub Release based on the tag; see GitHub’s release guide [[1]](#references).

5. **Install in consuming projects**
   - Python: `pip install "git+https://github.com/GAIK-project/toolkit-shared-components.git@v0.2.0#subdirectory=gaik-py"`
   - TypeScript: `pnpm add github:GAIK-project/toolkit-shared-components#v0.2.0`

## Repository Contents

- `gaik-py`: shared Python components and tests.
- `gaik-ts`: shared TypeScript components and tests.
- `gaik-demo`: Docker app with both packages preinstalled for demos.

## Release Cheat Sheet

1. Make sure `main` is up to date and tests pass.
2. Update all version files.
3. `git commit` the changes and create `git tag vX.Y.Z`.
4. `git push origin main --tags`.
5. Create or update the GitHub Release with highlights and links.

GitHub automatically provides zip/tarball downloads and supports attaching binaries to the release [[1]](#references).

## References

1. <a name="references"></a>GitHub Docs: About releases. https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases

