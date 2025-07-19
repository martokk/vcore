import time
from typing import Any

from backend import logger
from backend.services.scripts import Script, ScriptOutput


class ScriptExample(Script):
    """
    This is an example script.

    It uses the following parameters:
    - input_text: A string to validate.
    """

    def _validate_input(self, *args: Any, **kwargs: Any) -> bool:
        """
        Validate the input.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            bool: True if the input is valid, False otherwise.
        """
        if not kwargs.get("input_text"):
            logger.error("input_text is required")
            return False
        if kwargs.get("input_text") == "fail":
            logger.error("input_text is 'fail'")
            return False
        return True

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        """
        Run the script.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        logger.debug(f"Starting {self.__class__.__name__}._run()")
        logger.debug(f"kwargs: {kwargs}")

        # DO SOMETHING
        range_messages = []
        for i in range(10):
            range_messages.append(f"Hello World {i}")
            time.sleep(1)

        return ScriptOutput(
            success=True,
            message="Example script completed",
            data={
                "range_messages": range_messages,
            },
        )
