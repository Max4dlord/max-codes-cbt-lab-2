#!/usr/bin/env python3
"""SWEP 200 - lecture registry and question->lecture mapping.

The orientation blueprint (Prof. Olojede, Day 1) states the week contains 14
strategically selected lectures over 5 days. The slide decks supplied across
Days 1-5 give us identifiable TITLES for 13 of them:

  Day 1 (3):  Olojede (rules/regulations), Shittu (ITF history), Taiwo (benefits)
  Day 2 (3):  Olatunji (substance abuse), Adeleke (industrial safety),
              Ekanola (employability)
  Day 3 (3):  Ayanwale (5G entrepreneurship), Ariyo (PV), Omidiji (workshop)
  Day 4 (3):  Adebayo (food science & 4IR), Lawal (AI), Ibrahim (fire)
  Day 5 (1):  NECA (employers' expectations)

The 14th lecture's title is not present in any supplied material, so it is
deliberately NOT invented here. It can be added with one line in LECTURES plus
its id ranges in question_lecture_map() the moment the owner supplies its title.
"""

# id -> (slide title, dayId, speaker)
LECTURES = [
    {'id': 'd1-l1', 'name': 'General Introduction, University Rules & Regulations on Course Registration & Examinations',
     'dayId': 'swep-day-1', 'speaker': 'Prof. O. A. Olojede'},
    {'id': 'd1-l2', 'name': 'History & Spread of the Industrial Training Fund (ITF) in Nigeria',
     'dayId': 'swep-day-1', 'speaker': 'Prof. M. D. Shittu'},
    {'id': 'd1-l3', 'name': 'Benefits of Industrial Training for Science & Engineering Students',
     'dayId': 'swep-day-1', 'speaker': 'Prof. E. A. Taiwo'},

    {'id': 'd2-l1', 'name': 'Substance Abuse Among University Undergraduates',
     'dayId': 'swep-day-2', 'speaker': 'Dr. A. Olatunji'},
    {'id': 'd2-l2', 'name': 'Workshop & Industrial Safety',
     'dayId': 'swep-day-2', 'speaker': 'Prof. A. A. Adeleke'},
    {'id': 'd2-l3', 'name': '21st-Century Employability Skills',
     'dayId': 'swep-day-2', 'speaker': 'Prof. A. B. Ekanola'},

    {'id': 'd3-l1', 'name': 'Entrepreneurship in the 5G Era',
     'dayId': 'swep-day-3', 'speaker': 'Prof. A. B. Ayanwale'},
    {'id': 'd3-l2', 'name': 'Introduction to Renewable Energy (PV) Technology',
     'dayId': 'swep-day-3', 'speaker': 'Dr. F. K. Ariyo'},
    {'id': 'd3-l3', 'name': 'Workshop Practice, Workforce & National Growth',
     'dayId': 'swep-day-3', 'speaker': 'Prof. V. Omidiji'},

    {'id': 'd4-l1', 'name': 'Food Science & Engineering, Value-Addition & National Development',
     'dayId': 'swep-day-4', 'speaker': 'Dr. W. A. Adebayo'},
    {'id': 'd4-l2', 'name': 'Demystifying Artificial Intelligence',
     'dayId': 'swep-day-4', 'speaker': 'Dr. Aderonke Lawal'},
    {'id': 'd4-l3', 'name': 'Fire Awareness & Prevention',
     'dayId': 'swep-day-4', 'speaker': 'Mr. M. A. Ibrahim'},

    {'id': 'd5-l1', 'name': "Employers' Expectations from Fresh Graduates in the 21st-Century Job Market",
     'dayId': 'swep-day-5', 'speaker': 'Nigeria Employers\u2019 Consultative Association (NECA)'},
]


def question_lecture_map():
    """Return {question_id: lecture_id} for every SWEP 200 question."""
    m = {}

    def assign(lec, nums):
        for n in nums:
            m[f'swep_day{n // 100}_{n % 100:02d}'] = lec

    # ---- Day 1: questions are interleaved across the three lectures, so the
    # mapping is explicit rather than a range. ----
    day1 = [
        # (lecture, question numbers)
        ('d1-l1', [1, 2, 11, 12, 13, 14, 15, 16, 39, 41, 42]),       # Olojede
        ('d1-l2', [5, 6, 31, 32, 33, 34, 35, 36, 37, 38, 40, 44]),   # Shittu
        ('d1-l3', [3, 4, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 43]),  # Taiwo
    ]
    for lec, nums in day1:
        for n in nums:
            m[f'swep_day1_{n:02d}'] = lec

    # ---- Days 2-5: questions were authored in contiguous lecture blocks. ----
    # Day 2
    for n in list(range(1, 11)) + [41, 42]:
        m[f'swep_day2_{n:02d}'] = 'd2-l1'     # substance abuse
    for n in list(range(11, 26)) + [43, 44]:
        m[f'swep_day2_{n:02d}'] = 'd2-l2'     # industrial safety
    for n in list(range(26, 41)) + [45]:
        m[f'swep_day2_{n:02d}'] = 'd2-l3'     # employability

    # Day 3
    for n in range(1, 15):
        m[f'swep_day3_{n:02d}'] = 'd3-l1'     # 5G entrepreneurship
    for n in range(15, 28):
        m[f'swep_day3_{n:02d}'] = 'd3-l2'     # PV
    for n in range(28, 41):
        m[f'swep_day3_{n:02d}'] = 'd3-l3'     # workshop practice

    # Day 4
    for n in range(1, 16):
        m[f'swep_day4_{n:02d}'] = 'd4-l1'     # food science & 4IR
    for n in range(16, 29):
        m[f'swep_day4_{n:02d}'] = 'd4-l2'     # AI
    for n in range(29, 41):
        m[f'swep_day4_{n:02d}'] = 'd4-l3'     # fire

    # Day 5
    for n in range(1, 41):
        m[f'swep_day5_{n:02d}'] = 'd5-l1'     # employers' expectations

    return m
