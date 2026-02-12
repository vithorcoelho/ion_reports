# Release Process

This document describes the detailed release process for the Ion Nutri project.

For general Git workflow and branching model, see [docs/GITFLOW.md](docs/GITFLOW.md).

## Prerequisites

- All features for the release are merged into `develop`
- All tests are passing on `develop`
- You have write access to the repository
- You understand [Semantic Versioning](https://semver.org/)

## Version Numbering

We follow [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`

- **MAJOR** (X.0.0): Incompatible API changes, breaking changes
- **MINOR** (0.X.0): New features, backwards-compatible additions
- **PATCH** (0.0.X): Bug fixes, backwards-compatible fixes

Examples:
- Adding frontend to backend-only system: `1.0.0` → `1.1.0` (new feature)
- Fixing a bug in report generation: `1.1.0` → `1.1.1` (bug fix)
- Changing API endpoint structure: `1.1.0` → `2.0.0` (breaking change)

## Release Process

### Step 1: Create Release Branch

```bash
# Ensure you're on develop and up to date
git checkout develop
git pull origin develop

# Create release branch
git checkout -b release/X.Y.Z
```

Replace `X.Y.Z` with the target version (e.g., `1.1.0`).

### Step 2: Update Version Files

Update the version number in the following files:

#### 2.1. Update `pyproject.toml`

```toml
[project]
name = "ion-nutri"
version = "X.Y.Z"  # Update this line
```

#### 2.2. Update `CHANGELOG.md`

Add a new section at the top (after the header, before previous releases):

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- List new features
- Use bullet points
- Group by category (Core Features, Architecture, Documentation, etc.)

### Changed
- List modifications to existing features
- Refactorings
- Performance improvements

### Fixed
- Bug fixes
- Test corrections
- Documentation fixes

### Removed
- Deprecated features removed (if any)
```

**Guidelines for CHANGELOG:**
- Follow [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format
- Use present tense ("Add feature" not "Added feature")
- Group related changes together
- Include PR references when relevant: `(#123)`
- Focus on user-visible changes (not internal refactorings unless significant)
- Include both backend and frontend changes

**How to gather changes:**
```bash
# View all commits since last release
git log --oneline v1.0.0..HEAD

# View only PR merge commits
git log --oneline --grep="Merge pull request" v1.0.0..HEAD

# View changes with more detail
git log --graph --oneline --decorate v1.0.0..HEAD
```

### Step 3: Commit Release Preparation

```bash
# Stage version files
git add pyproject.toml CHANGELOG.md

# Commit with conventional commit message
git commit -m "chore: prepare release X.Y.Z"

# Push release branch
git push -u origin release/X.Y.Z
```

### Step 4: Testing and Review

- Create a Pull Request from `release/X.Y.Z` to `main`
- Review all changes one last time
- Ensure all CI checks pass
- Get approval from team members
- **Do NOT merge the PR yet** - this will be done manually with tags

### Step 5: Merge to Main and Tag

```bash
# Checkout main and ensure it's up to date
git checkout main
git pull origin main

# Merge release branch (use --no-ff to preserve branch history)
git merge --no-ff release/X.Y.Z

# Create annotated tag with release notes
git tag -a vX.Y.Z -m "Release version X.Y.Z

Key changes:
- Major feature 1
- Major feature 2
- Important fix
"

# Push main and tags
git push origin main
git push origin vX.Y.Z
```

**Important:** Pushing to `main` triggers the staging deployment workflow automatically (see `.github/workflows/build.yml`).

### Step 6: Merge Back to Develop

```bash
# Checkout develop
git checkout develop
git pull origin develop

# Merge release branch back
git merge --no-ff release/X.Y.Z

# Push develop
git push origin develop
```

### Step 7: Cleanup

```bash
# Delete local release branch
git branch -d release/X.Y.Z

# Delete remote release branch
git push origin --delete release/X.Y.Z

# Close the PR (if created)
```

### Step 8: Create GitHub Release (Optional but Recommended)

1. Go to https://github.com/edgebr/ion-nutri/releases
2. Click "Draft a new release"
3. Select the tag you just created (`vX.Y.Z`)
4. Title: `Ion Nutri vX.Y.Z`
5. Description: Copy the CHANGELOG section for this version
6. Publish release

## What Happens After Release

### Automatic Staging Deployment

When you push to `main`:

1. **GitHub Actions** workflow [`.github/workflows/build.yml`](.github/workflows/build.yml) is triggered
2. **SonarQube scan** runs for code quality analysis
3. **Backend Docker image** is built and pushed to Amazon ECR
4. **Kubernetes deployment** is updated in staging environment

**Note:** Currently, only the backend is deployed automatically. Frontend deployment to staging requires DevOps configuration.

### Manual Production Deployment

Production deployment is typically handled by the DevOps team and may require:
- Additional approval processes
- Environment-specific configurations
- Gradual rollout strategies

Consult with your DevOps team for production deployment procedures.

## Hotfix Process

For critical production bugs that need immediate fixes:

### Step 1: Create Hotfix Branch

```bash
# Branch from main (production)
git checkout main
git pull origin main
git checkout -b hotfix/X.Y.Z
```

The version should be a PATCH increment (e.g., if current is `1.1.0`, hotfix is `1.1.1`).

### Step 2: Fix the Issue

Make the minimal changes necessary to fix the critical issue.

```bash
git add .
git commit -m "fix: describe the critical fix"
```

### Step 3: Update Versions

Same as release process:
- Update `pyproject.toml` version
- Add entry to `CHANGELOG.md` under a new `[X.Y.Z]` section

```bash
git add pyproject.toml CHANGELOG.md
git commit -m "chore: prepare hotfix X.Y.Z"
git push -u origin hotfix/X.Y.Z
```

### Step 4: Merge and Tag

```bash
# Merge to main
git checkout main
git merge --no-ff hotfix/X.Y.Z
git tag -a vX.Y.Z -m "Hotfix version X.Y.Z - Critical fix description"
git push origin main --tags

# Merge to develop
git checkout develop
git merge --no-ff hotfix/X.Y.Z
git push origin develop

# Cleanup
git branch -d hotfix/X.Y.Z
git push origin --delete hotfix/X.Y.Z
```

## Checklist

Use this checklist when creating a release:

- [ ] All features for release are merged into `develop`
- [ ] All tests pass on `develop`
- [ ] Created release branch `release/X.Y.Z`
- [ ] Updated `pyproject.toml` version
- [ ] Updated `CHANGELOG.md` with all changes
- [ ] Committed changes: `chore: prepare release X.Y.Z`
- [ ] Pushed release branch
- [ ] Created PR to `main` for review
- [ ] PR approved and CI checks pass
- [ ] Merged to `main` with `--no-ff`
- [ ] Created annotated tag `vX.Y.Z`
- [ ] Pushed `main` and tags
- [ ] Verified staging deployment succeeded
- [ ] Merged back to `develop`
- [ ] Pushed `develop`
- [ ] Deleted release branch (local and remote)
- [ ] Created GitHub release (optional)
- [ ] Notified team about new release

## Troubleshooting

### Merge Conflicts

If you encounter merge conflicts during the release process:

```bash
# During merge to main or develop
git status  # See conflicting files
# Manually resolve conflicts in each file
git add .
git commit  # Complete the merge
```

### Tag Already Exists

If you need to recreate a tag:

```bash
# Delete local tag
git tag -d vX.Y.Z

# Delete remote tag
git push origin :refs/tags/vX.Y.Z

# Recreate tag
git tag -a vX.Y.Z -m "Release message"
git push origin vX.Y.Z
```

**Warning:** Only do this if the tag hasn't been used in production yet.

### Deployment Failed

If the staging deployment fails after pushing to `main`:

1. Check GitHub Actions logs: https://github.com/edgebr/ion-nutri/actions
2. Common issues:
   - Docker build failures → Check Dockerfile and dependencies
   - ECR push failures → Check AWS credentials
   - K8s deployment failures → Check `k8s/staging.yml` configuration
3. Contact DevOps team if infrastructure issues

## References

- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Gitflow Workflow](docs/GITFLOW.md)
