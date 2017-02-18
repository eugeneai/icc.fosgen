import re

COMPETENTIONS = """
способность к самоорганизации и самообразованию (ОК-7);
способностью осваивать методики использования программных средств для решения практических задач (ОПК–2);
способностью решать стандартные задачи профессиональной деятельности на основе информационной и библиографической культуры с применением информационно-коммуникационных технологий и с учетом основных требований информационной безопасности (ОПК–5).
"""


def extract_comps(text, d=None):
    """
    Extracts competention codes from list like above
    mentioned variable COMPETENTIONS.
    `d` - dictionary (or None) to store code->text mapping
    """
    if d is None:
        d = {}
    rexp = re.compile("^(.*)(\((.*)\))")
    for l in text.split("\n"):
        l = l.strip()
        if not l:
            continue
        m = rexp.match(l)
        if m is None:
            raise ValueError(l)
        descr = m.group(1).strip()
        code = m.group(3).strip()
        d[code] = descr
    return d
