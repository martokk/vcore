from pathlib import Path

import toml

from _app.models.settings import Settings
from _app.templating.env import inject_app_templating_env
from backend import vcore_setup
from backend.core.hooks import register_hook
from backend.core.settings import get_settings


PROJECT_PATH = Path(__file__).parent.parent

# Setup vCore Framework
vcore_setup(
    project_path=PROJECT_PATH,
)

# Register vCore App Hooks
register_hook("inject_app_templating_env", inject_app_templating_env)


# Get App Version
def get_app_version() -> str:
    pyproject = toml.load(PROJECT_PATH / "pyproject.toml")
    return str(pyproject["tool"]["poetry"]["version"])


# Get Settings
settings = get_settings(settings_cls=Settings, project_path=PROJECT_PATH, version=get_app_version())
