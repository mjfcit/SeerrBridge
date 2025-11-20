"""
Shared constants for selenium interactions and XPath selectors.
"""

CASE_INSENSITIVE_TEXT_EXPR = (
    "translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
)
INTERACTIVE_NODE_XPATH = "(.//button | .//div)"
GLOBAL_INTERACTIVE_NODE_XPATH = "(//button | //div)"
INSTANT_RD_BUTTON_XPATH = (
    f"{INTERACTIVE_NODE_XPATH}[contains({CASE_INSENSITIVE_TEXT_EXPR}, 'instant rd')]"
)
DL_WITH_RD_BUTTON_XPATH = (
    f"{INTERACTIVE_NODE_XPATH}[contains({CASE_INSENSITIVE_TEXT_EXPR}, 'dl with rd')]"
)
RESULT_BOX_XPATH = (
    f"//div[.//h2 and ("
    f"{INTERACTIVE_NODE_XPATH}[contains({CASE_INSENSITIVE_TEXT_EXPR}, 'instant rd')] "
    f"or {INTERACTIVE_NODE_XPATH}[contains({CASE_INSENSITIVE_TEXT_EXPR}, 'dl with rd')]"
    f")]"
)
RD_READY_BUTTON_XPATH = (
    f"{GLOBAL_INTERACTIVE_NODE_XPATH}[contains({CASE_INSENSITIVE_TEXT_EXPR}, 'rd (100%)')]"
)

__all__ = [
    "CASE_INSENSITIVE_TEXT_EXPR",
    "INTERACTIVE_NODE_XPATH",
    "GLOBAL_INTERACTIVE_NODE_XPATH",
    "INSTANT_RD_BUTTON_XPATH",
    "DL_WITH_RD_BUTTON_XPATH",
    "RESULT_BOX_XPATH",
    "RD_READY_BUTTON_XPATH",
]
