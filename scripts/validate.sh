#!/bin/bash
# Flask-Ask Validation Script
#
# This script runs all validation checks locally.
# Use this before committing changes to ensure code quality.
#
# Usage:
#   ./scripts/validate.sh [options]
#
# Options:
#   --lint-only    Run only linting checks
#   --test-only    Run only tests
#   --help         Show this help message
#
# Exit codes:
#   0 - All checks passed
#   1 - One or more checks failed

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Print colored status messages
info() {
    echo -e "${YELLOW}[INFO]${NC} $1"
}

success() {
    echo -e "${GREEN}[PASS]${NC} $1"
}

error() {
    echo -e "${RED}[FAIL]${NC} $1"
}

# Help message
show_help() {
    head -20 "$0" | tail -16
    exit 0
}

# Check for help flag
if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    show_help
fi

# Track overall status
FAILED=0

# Lint check
run_lint() {
    info "Running linter (flake8)..."
    if command -v flake8 &> /dev/null; then
        if flake8 flask_ask/ --count --select=E9,F63,F7,F82 --show-source --statistics; then
            success "Linting passed"
        else
            error "Linting failed"
            FAILED=1
        fi
    else
        info "flake8 not installed, skipping lint check"
        info "Install with: pip install flake8"
    fi
}

# Test check
run_tests() {
    info "Running tests..."
    if command -v pytest &> /dev/null; then
        if [ -d "tests" ]; then
            if pytest --cov=flask_ask --cov-report=term-missing; then
                success "Tests passed"
            else
                error "Tests failed"
                FAILED=1
            fi
        else
            info "No tests directory found, skipping tests"
        fi
    else
        info "pytest not installed, skipping tests"
        info "Install with: pip install pytest pytest-cov"
    fi
}

# Main execution
main() {
    echo ""
    echo "======================================"
    echo "  Flask-Ask Validation Suite"
    echo "======================================"
    echo ""

    case "$1" in
        --lint-only)
            run_lint
            ;;
        --test-only)
            run_tests
            ;;
        *)
            run_lint
            echo ""
            run_tests
            ;;
    esac

    echo ""
    echo "======================================"
    if [ $FAILED -eq 0 ]; then
        success "All validations passed!"
        echo "======================================"
        exit 0
    else
        error "Some validations failed"
        echo "======================================"
        exit 1
    fi
}

main "$@"
