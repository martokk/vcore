from fastapi.templating import Jinja2Templates


# from app.templating.filters import filter_app_specific_filter


def inject_app_templating_env(templates: Jinja2Templates) -> Jinja2Templates:
    """
    This vcore_app hook is called by the vCore Framework to inject the app-specific templating environment into the templates.
    """

    # Add custom filters to templates
    # templates.env.filters["app_specific_filter"] = filter_app_specific_filter

    # Add global variables to templates
    # templates.env.globals["APP_SPECIFIC_GLOBAL_VARIABLE"] = "app_specific_global_variable"

    return templates
