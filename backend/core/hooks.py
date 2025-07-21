from collections.abc import Callable
from typing import Any


HOOKS: dict[str, Callable[..., Any] | None] = {
    "inject_app_templating_env": None,
}


def register_hook(hook_name: str, hook_func: Callable[..., Any]) -> None:
    """Register a hook function."""
    HOOKS[hook_name] = hook_func
    pass


def call_hook(hook_name: str, *args: Any, **kwargs: Any) -> Any:
    """Call a hook function."""
    if hook_name not in HOOKS:
        print(f"Hook `{hook_name}` not found in HOOKS. Available hooks: {list(HOOKS.keys())}.")
        return None

    hook_func = HOOKS[hook_name]
    if hook_func is None or not callable(hook_func):
        raise ValueError(
            f"Callable hook `{hook_name}` is not implemented. Hook = {hook_func}. "
            f"Available hooks: {list(HOOKS.keys())}. "
            f"TIP: Make sure to register_hook() in the app/__init__.py file."
        )
    return hook_func(*args, **kwargs)


def get_hook(hook_name: str) -> Callable[..., Any] | None:
    """Get a hook function without calling it."""
    return HOOKS.get(hook_name)


def is_hook_registered(hook_name: str) -> bool:
    """Check if a hook is registered and callable."""
    hook_func = HOOKS.get(hook_name)
    return hook_func is not None and callable(hook_func)


def list_hooks() -> dict[str, bool]:
    """List all hooks and their registration status."""
    return {hook_name: is_hook_registered(hook_name) for hook_name in HOOKS}
