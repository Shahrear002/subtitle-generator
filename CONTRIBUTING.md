# Contributing to Subtitle Generator

First off, thank you for considering contributing to Subtitle Generator! It's people like you that make this tool better for everyone.

## 🐛 Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

### Bug Report Template

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
A clear description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 11, macOS 12.0]
 - Application Version: [e.g. 1.0.0]
 - FFmpeg Version: [e.g. 4.4.1]

**Additional context**
Add any other context about the problem here.

## 💡 Suggesting Features

Feature requests are welcome! Please provide:

1. **Clear use case** - Explain why this feature would be useful
2. **Detailed description** - Describe how it should work
3. **Examples** - Provide examples if possible
4. **Alternatives** - Mention any alternative solutions you've considered

## 🔧 Development Setup

### Prerequisites

- Python 3.8 or higher
- FFmpeg installed and in PATH
- Git

### Setting Up Your Development Environment

1. **Fork the repository**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/SubtitleGenerator.git
   cd SubtitleGenerator
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

## 📝 Code Style Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and concise
- Write docstrings for functions and classes

## 🔀 Pull Request Process

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes**
   - Write clean, readable code
   - Test your changes thoroughly
   - Update documentation if needed

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```
   
   Use conventional commit messages:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for updates to existing features
   - `Docs:` for documentation changes
   - `Refactor:` for code refactoring

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template with details about your changes
   - Link any related issues

### Pull Request Guidelines

- Ensure your code follows the style guidelines
- Update the README.md if you're adding features
- Make sure all tests pass (if applicable)
- Keep PRs focused - one feature/fix per PR
- Respond to review feedback promptly

## 🧪 Testing

Before submitting a PR:

1. Test the application with various video formats
2. Test with different video lengths
3. Verify the GUI works correctly
4. Check that subtitles are generated accurately
5. Test on your target platform (Windows/macOS)

## 📚 Documentation

If you're adding new features:

- Update the README.md with usage instructions
- Add comments in the code
- Update CHANGELOG.md
- Consider adding examples

## ❓ Questions?

Feel free to open an issue with the `question` label if you have any questions about contributing.

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!
