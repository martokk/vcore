from typing import cast

from fastapi.templating import Jinja2Templates
from jinja2 import FileSystemLoader

from backend import paths
from backend.templating.env import set_template_env


def get_templates() -> Jinja2Templates:
    """
    Create Jinja2Templates object with multiple template directories then set the template environment.

    Returns:
        Jinja2Templates: Jinja2Templates object with multiple directories.
    """

    # Templates will be searched in order: app first, then vcore.
    # app-specific templates to override vcore templates.
    templates = Jinja2Templates(directory=str(paths.TEMPLATES_PATH))

    if templates.env.loader is not None and hasattr(templates.env.loader, "searchpath"):
        loader = cast("FileSystemLoader", templates.env.loader)
        loader.searchpath.append(str(paths.VCORE_TEMPLATES_PATH))
    else:
        # Fallback: create a new loader with both directories
        from jinja2 import ChoiceLoader

        app_loader = FileSystemLoader(str(paths.TEMPLATES_PATH))
        vcore_loader = FileSystemLoader(str(paths.VCORE_TEMPLATES_PATH))
        choice_loader = ChoiceLoader([app_loader, vcore_loader])
        templates.env.loader = choice_loader

    templates = set_template_env(templates)
    return templates


templates = get_templates()
