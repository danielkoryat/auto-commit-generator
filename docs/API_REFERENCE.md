### API_REFERENCE.md

```markdown
# API Reference

## commit_message_generator

This module provides a function to generate commit messages programmatically.

### Functions

#### generate_commit_message(data)

Generates a commit message based on the provided data.

**Arguments:**

- data (dict): A dictionary containing commit information.

**Returns:** 

- str: A formatted commit message.

**Example:**

```python
from commit_message_generator import generate_commit_message

data = {
  'type': 'feat', 
  'scope': 'authentication',
  'description': 'add OAuth2 support' 
}

message = generate_commit_message(data)
print(message)
```
```