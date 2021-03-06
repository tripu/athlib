from athlib.wma.agegrader import AgeGrader, AthlonsAgeGrader
from athlib.uka.agegroups import calc_uka_age_group
from athlib.iaaf_score import score as athlon_score
from athlib.iaaf_score import performance as athlon_performance_needed
from athlib.utils import (
    normalize_gender,
    str2num,
    parse_hms,
    get_distance,
    format_seconds_as_time,
    check_performance_for_discipline,
    discipline_sort_key,
    text_discipline_sort_key,
    sort_by_discipline,
)
from athlib.codes import (
    JUMPS, THROWS, MULTI_EVENTS, FIELD_EVENTS,
    FIELD_SORT_ORDER, STANDARD_MALE_TRACK_EVENTS,
    STANDARD_FEMALE_TRACK_EVENTS,
)

ag = AgeGrader()

def wma_age_grade(gender, age, event, performance, verbose=False):
    """Return the age grade score (0 to 100ish) for this result."""
    return ag.calculate_age_grade(gender, age,event, performance, verbose=verbose)

def wma_age_factor(gender, age, event, distance=None):
    """Work out 'slowdown factor' for a geezer of this
    age taking part in this event e.g."""
    return ag.calculate_factor(self, gender, age, event, distance=distance)

def wma_world_best(gender, event):
    "The relevant world-record performance on the date stats were compiled"
    return ag.world_best(gender, event)

aag = AthlonsAgeGrader()
def wma_athlon_age_factor(gender, age, event):
    """Work out 'slowdown factor' for a geezer of this
    age taking part in this event e.g."""
    return aag.calculate_factor(gender, age, event)

def wma_athlon_age_grade(gender, age, event, performance, verbose=False):
    """Return the age grade score (0 to 100ish) for this result."""
    return aag.calculate_age_grade(gender, age, event, performance, verbose=verbose)

__all__ = filter(None, """
            athlon_performance_needed
            athlon_score
            calc_uka_age_group
            check_performance_for_discipline
            discipline_sort_key
            format_seconds_as_time
            get_distance
            normalize_gender
            parse_hms
            sort_by_discipline
            str2num
            text_discipline_sort_key
            wma_age_factor
            wma_age_grade
            wma_athlon_age_grade
            wma_world_best
            FIELD_EVENTS
            FIELD_SORT_ORDER
            JUMPS
            MULTI_EVENTS
            STANDARD_FEMALE_TRACK_EVENTS
            STANDARD_MALE_TRACK_EVENTS
            THROWS
            """.split())
