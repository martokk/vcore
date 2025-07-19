# Add to Docs

### Hooks

- Hooks allow for the vcore-app to inject its own functionality into the vcore-framework. They effectively allow the vCore Framework to attempt to call functions from the vcore-app.
- Hooks are registered in the `app.app.py` file.

#### vCore Framework Hooks

- `inject_app_templating_env` - This hook is called by the vCore Framework to inject the app-specific templating environment (filters, globals, etc.) into the templates. The corresponding function is in `app.templating.env.py`.

### Scripts

- Scripts use the 'Hooks' functionality for registration.
