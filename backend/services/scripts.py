from abc import abstractmethod
from typing import Any

from pydantic import BaseModel

from backend import logger
from backend.core.hooks import call_hook, register_hook


class ScriptOutput(BaseModel):
    success: bool | None = None
    message: str | None = None
    data: Any | None = None


class Script(BaseModel):
    # Input (Any or None)

    # Output
    output: ScriptOutput | None = None

    # Run
    @abstractmethod
    def _validate_input(self, *args: Any, **kwargs: Any) -> bool:
        pass

    @abstractmethod
    def _run(self, *args: Any, **kwargs: Any) -> ScriptOutput:
        pass

    def run(self, *args: Any, **kwargs: Any) -> ScriptOutput:
        logger.info(f"Script {self.__class__.__name__}: Running script.")
        if not self._validate_input(*args, **kwargs):
            raise ValueError("Script input validation failed.")

        logger.info(f"Script {self.__class__.__name__}: Input validated.")

        self.output = self._run(*args, **kwargs)

        logger.info(f"Script {self.__class__.__name__}: Script completed.")

        return self.output


def register_script(script_class_name: str, script_class: type[Script]) -> None:
    """Register a script class."""
    return register_hook(script_class_name, script_class)


def call_script(script_class_name: str, *args: Any, **kwargs: Any) -> Any:
    """Call a script class."""
    return call_hook(script_class_name, *args, **kwargs)
