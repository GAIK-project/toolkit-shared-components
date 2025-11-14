# TypeScript Packages

This folder is a placeholder for future npm packages (TypeScript/JavaScript). Follow the same conventions as the Python workspace:

| Folder                                    | Purpose                           |
| ----------------------------------------- | --------------------------------- |
| `packages/ts/<package-name>/src/`         | Package source code               |
| `packages/ts/<package-name>/tests/`       | Co-located unit/integration tests |
| `packages/ts/<package-name>/package.json` | Package metadata + scripts        |

## Creating a New TypeScript Package

1. **Scaffold**

   ```bash
   mkdir -p packages/ts/<package-name>/{src,tests}
   cd packages/ts/<package-name>
   npm init -y
   ```

2. **Tooling**

   - Prefer TypeScript (`tsconfig.json`) and ESLint/Prettier configs stored inside the package directory.
   - Keep tests next to the feature they cover (e.g., `src/parser/tests/`).

3. **CI**

   - Expose a `test` script in `package.json`.
   - Future workflows can iterate over `packages/ts/*` similar to the Python runner.

4. **Docs**
   - Add a `README.md` inside the package describing usage and build/test commands.

Until a package is added, this README keeps the directory under version control and documents the intended structure.
