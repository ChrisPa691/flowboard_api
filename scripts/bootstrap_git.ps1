# Git Bootstrap Script for Flowboard API
# This PowerShell script initializes a git repository with proper configuration
#
# This file should include:
# - Git repository initialization
# - Initial commit creation
# - Branch setup (main, develop)
# - .gitignore configuration
# - Git hooks setup (optional)
# - Remote repository configuration
# - Initial tags (optional)

<#
.SYNOPSIS
    Bootstrap git repository for Flowboard API project

.DESCRIPTION
    Initializes git repository, creates branches, makes initial commit,
    and optionally sets up remote repository

.PARAMETER remoteUrl
    Optional URL of the remote git repository

.EXAMPLE
    .\scripts\bootstrap_git.ps1
    
.EXAMPLE
    .\scripts\bootstrap_git.ps1 -remoteUrl "https://github.com/username/flowboard-api.git"
#>

Param(
    [string]$remoteUrl = ""
)

Write-Host "Running git bootstrap script..." -ForegroundColor Cyan

# Initialize git repository if it doesn't exist
if (-not (Test-Path -Path ".git")) {
    Write-Host "Initializing new git repository..." -ForegroundColor Yellow
    git init
    git checkout -b main
    Write-Host "Git repository initialized with 'main' branch" -ForegroundColor Green
} else {
    Write-Host "Git repository already exists" -ForegroundColor Yellow
    git checkout main -ErrorAction SilentlyContinue
}

# Stage all files
Write-Host "Staging files..." -ForegroundColor Cyan
git add -A

# Create initial commit
try {
    Write-Host "Creating initial commit..." -ForegroundColor Cyan
    git commit -m "chore: initial scaffold" -q
    Write-Host "Initial commit created successfully" -ForegroundColor Green
} catch {
    Write-Host "No changes to commit or commit failed: $_" -ForegroundColor Yellow
}

# Set up remote if URL provided
if ($remoteUrl -ne "") {
    try {
        Write-Host "Adding remote origin..." -ForegroundColor Cyan
        git remote add origin $remoteUrl -ErrorAction SilentlyContinue
        Write-Host "Remote origin added: $remoteUrl" -ForegroundColor Green
    } catch {
        Write-Host "Remote add may have failed or already exists: $_" -ForegroundColor Yellow
    }
    
    Write-Host "Pushing to remote..." -ForegroundColor Cyan
    git push -u origin main
    Write-Host "Pushed to remote successfully" -ForegroundColor Green
} else {
    Write-Host "`nNo remote provided." -ForegroundColor Yellow
    Write-Host "To push manually, run:" -ForegroundColor Cyan
    Write-Host "  git remote add origin <url>"
    Write-Host "  git push -u origin main"
}

Write-Host "`nGit bootstrap completed!" -ForegroundColor Green
Write-Host "`nOptional next steps:" -ForegroundColor Cyan
Write-Host "  - Create develop branch: git checkout -b develop"
Write-Host "  - Set up git hooks for pre-commit checks"
Write-Host "  - Configure branch protection rules on remote"
