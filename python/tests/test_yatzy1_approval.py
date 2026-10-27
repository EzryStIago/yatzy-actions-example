import pytest

from approvaltests import verify
from approvaltests.core.scenario_namer import ScenarioNamer
from approvaltests.namer.stack_frame_namer import StackFrameNamer
from approvaltests.reporters.report_quietly import ReportQuietly

from yatzy1 import Yatzy


@pytest.mark.parametrize(
    ("case", "dice"),
    [
        ("straight", (1, 2, 3, 4, 5)),
        ("full_house", (2, 2, 3, 3, 3)),
        ("yatzy", (6, 6, 6, 6, 6)),
    ],
)
def test_yatzy_scoring_approval(case, dice):
    scores = {
        "chance": Yatzy.chance(*dice),
        "yatzy": Yatzy.yatzy(dice),
        "two_pair": Yatzy.two_pair(*dice),
        "full_house": Yatzy.fullHouse(*dice),
    }
    verify(scores, namer=ScenarioNamer(StackFrameNamer(), case), reporter=ReportQuietly())
