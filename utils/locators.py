
from seleniumactions import Using, Locator


templates = {
    "link_text__exact": "//a[.='{text}']",
    "link_text__contains": "//a[contains(.='{text}')]",
    "header_text__exact": "//*[self::h1 or self::h2 or self::h3 and .='{text}']",
    "header_text__contains": "//*[self::h1 or self::h2 or self::h3 and contains(.='{text}')]",
}


class CodeMeh(Locator): ...


class Locators: ...
