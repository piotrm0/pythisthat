from dataclasses import dataclass
from inspect import FrameInfo, stack
from pathlib import Path
from typing import Optional


@dataclass
class SourceLineLocation():
    file: Optional[Path] = None
    module: Optional[str] = None
    package: Optional[str] = None
    line_number: Optional[int] = None

    def __str__(self):
        return f"{str(self.file)}:{self.line_number}"

@dataclass
class SourceLine():
    content: str
    loc: Optional[SourceLineLocation] = None

    def __str__(self):
        ret = ""
        if self.loc is not None:
            ret += str(self.loc) + ": "
        ret += self.content

        return ret

    @property
    def ast(self):
        return None

def line(offset: int = 1) -> SourceLine:
    frame = stack()[offset]
    
    loc = SourceLineLocation(
        file=Path(frame.filename),
        line_number=frame.lineno
    )
    
    source = SourceLine(
        content=frame.code_context[0],
        loc=loc
    )

    return source