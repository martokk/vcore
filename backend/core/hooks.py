from collections.abc import Callable
from typing import Any


HOOKS: dict[str, Callable[..., Any] | None] = {
    "inject_app_templating_env": None,
}


def register_hook(hook_name: str, hook_func: Callable[..., Any]) -> None:
    """Register a hook function."""
    HOOKS[hook_name] = hook_func


def call_hook(hook_name: str, *args: Any, **kwargs: Any) -> Any:
    """Call a hook function."""
    if hook_name not in HOOKS:
        raise ValueError(f"Hook `{hook_name}` not found in HOOKS. HOOKS = {HOOKS}.")

    hook_func = HOOKS[hook_name]
    if hook_func is None or not callable(hook_func):
        raise ValueError(
            f"Callable hook `{hook_name}` is not implemented. Hook = None or is not callable. HOOKS = {HOOKS}."
        )
    return hook_func(*args, **kwargs)
