from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Strategy:
    code: str
    name: str
    min_dpd: int
    max_dpd: int
    channel: str
    intensity: int
    script: str

STRATEGIES: list[Strategy] = []

STRATEGIES.append(Strategy(
    code="ST0001", name="DPD1-7/sms/I1",
    min_dpd=1, max_dpd=7, channel="sms", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0001",
))
STRATEGIES.append(Strategy(
    code="ST0002", name="DPD1-7/sms/I2",
    min_dpd=1, max_dpd=7, channel="sms", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0002",
))
STRATEGIES.append(Strategy(
    code="ST0003", name="DPD1-7/sms/I3",
    min_dpd=1, max_dpd=7, channel="sms", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0003",
))
STRATEGIES.append(Strategy(
    code="ST0004", name="DPD1-7/sms/I4",
    min_dpd=1, max_dpd=7, channel="sms", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0004",
))
STRATEGIES.append(Strategy(
    code="ST0005", name="DPD1-7/sms/I5",
    min_dpd=1, max_dpd=7, channel="sms", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0005",
))
STRATEGIES.append(Strategy(
    code="ST0006", name="DPD1-7/ivr/I1",
    min_dpd=1, max_dpd=7, channel="ivr", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0006",
))
STRATEGIES.append(Strategy(
    code="ST0007", name="DPD1-7/ivr/I2",
    min_dpd=1, max_dpd=7, channel="ivr", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0007",
))
STRATEGIES.append(Strategy(
    code="ST0008", name="DPD1-7/ivr/I3",
    min_dpd=1, max_dpd=7, channel="ivr", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0008",
))
STRATEGIES.append(Strategy(
    code="ST0009", name="DPD1-7/ivr/I4",
    min_dpd=1, max_dpd=7, channel="ivr", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0009",
))
STRATEGIES.append(Strategy(
    code="ST0010", name="DPD1-7/ivr/I5",
    min_dpd=1, max_dpd=7, channel="ivr", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0010",
))
STRATEGIES.append(Strategy(
    code="ST0011", name="DPD1-7/app_push/I1",
    min_dpd=1, max_dpd=7, channel="app_push", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0011",
))
STRATEGIES.append(Strategy(
    code="ST0012", name="DPD1-7/app_push/I2",
    min_dpd=1, max_dpd=7, channel="app_push", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0012",
))
STRATEGIES.append(Strategy(
    code="ST0013", name="DPD1-7/app_push/I3",
    min_dpd=1, max_dpd=7, channel="app_push", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0013",
))
STRATEGIES.append(Strategy(
    code="ST0014", name="DPD1-7/app_push/I4",
    min_dpd=1, max_dpd=7, channel="app_push", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0014",
))
STRATEGIES.append(Strategy(
    code="ST0015", name="DPD1-7/app_push/I5",
    min_dpd=1, max_dpd=7, channel="app_push", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0015",
))
STRATEGIES.append(Strategy(
    code="ST0016", name="DPD1-7/human_call/I1",
    min_dpd=1, max_dpd=7, channel="human_call", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0016",
))
STRATEGIES.append(Strategy(
    code="ST0017", name="DPD1-7/human_call/I2",
    min_dpd=1, max_dpd=7, channel="human_call", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0017",
))
STRATEGIES.append(Strategy(
    code="ST0018", name="DPD1-7/human_call/I3",
    min_dpd=1, max_dpd=7, channel="human_call", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0018",
))
STRATEGIES.append(Strategy(
    code="ST0019", name="DPD1-7/human_call/I4",
    min_dpd=1, max_dpd=7, channel="human_call", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0019",
))
STRATEGIES.append(Strategy(
    code="ST0020", name="DPD1-7/human_call/I5",
    min_dpd=1, max_dpd=7, channel="human_call", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0020",
))
STRATEGIES.append(Strategy(
    code="ST0021", name="DPD1-7/letter/I1",
    min_dpd=1, max_dpd=7, channel="letter", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0021",
))
STRATEGIES.append(Strategy(
    code="ST0022", name="DPD1-7/letter/I2",
    min_dpd=1, max_dpd=7, channel="letter", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0022",
))
STRATEGIES.append(Strategy(
    code="ST0023", name="DPD1-7/letter/I3",
    min_dpd=1, max_dpd=7, channel="letter", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0023",
))
STRATEGIES.append(Strategy(
    code="ST0024", name="DPD1-7/letter/I4",
    min_dpd=1, max_dpd=7, channel="letter", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0024",
))
STRATEGIES.append(Strategy(
    code="ST0025", name="DPD1-7/letter/I5",
    min_dpd=1, max_dpd=7, channel="letter", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0025",
))
STRATEGIES.append(Strategy(
    code="ST0026", name="DPD1-7/legal_notice/I1",
    min_dpd=1, max_dpd=7, channel="legal_notice", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0026",
))
STRATEGIES.append(Strategy(
    code="ST0027", name="DPD1-7/legal_notice/I2",
    min_dpd=1, max_dpd=7, channel="legal_notice", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0027",
))
STRATEGIES.append(Strategy(
    code="ST0028", name="DPD1-7/legal_notice/I3",
    min_dpd=1, max_dpd=7, channel="legal_notice", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0028",
))
STRATEGIES.append(Strategy(
    code="ST0029", name="DPD1-7/legal_notice/I4",
    min_dpd=1, max_dpd=7, channel="legal_notice", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0029",
))
STRATEGIES.append(Strategy(
    code="ST0030", name="DPD1-7/legal_notice/I5",
    min_dpd=1, max_dpd=7, channel="legal_notice", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0030",
))
STRATEGIES.append(Strategy(
    code="ST0031", name="DPD1-7/visit/I1",
    min_dpd=1, max_dpd=7, channel="visit", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0031",
))
STRATEGIES.append(Strategy(
    code="ST0032", name="DPD1-7/visit/I2",
    min_dpd=1, max_dpd=7, channel="visit", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0032",
))
STRATEGIES.append(Strategy(
    code="ST0033", name="DPD1-7/visit/I3",
    min_dpd=1, max_dpd=7, channel="visit", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0033",
))
STRATEGIES.append(Strategy(
    code="ST0034", name="DPD1-7/visit/I4",
    min_dpd=1, max_dpd=7, channel="visit", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0034",
))
STRATEGIES.append(Strategy(
    code="ST0035", name="DPD1-7/visit/I5",
    min_dpd=1, max_dpd=7, channel="visit", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0035",
))
STRATEGIES.append(Strategy(
    code="ST0036", name="DPD8-15/sms/I1",
    min_dpd=8, max_dpd=15, channel="sms", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0036",
))
STRATEGIES.append(Strategy(
    code="ST0037", name="DPD8-15/sms/I2",
    min_dpd=8, max_dpd=15, channel="sms", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0037",
))
STRATEGIES.append(Strategy(
    code="ST0038", name="DPD8-15/sms/I3",
    min_dpd=8, max_dpd=15, channel="sms", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0038",
))
STRATEGIES.append(Strategy(
    code="ST0039", name="DPD8-15/sms/I4",
    min_dpd=8, max_dpd=15, channel="sms", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0039",
))
STRATEGIES.append(Strategy(
    code="ST0040", name="DPD8-15/sms/I5",
    min_dpd=8, max_dpd=15, channel="sms", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0040",
))
STRATEGIES.append(Strategy(
    code="ST0041", name="DPD8-15/ivr/I1",
    min_dpd=8, max_dpd=15, channel="ivr", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0041",
))
STRATEGIES.append(Strategy(
    code="ST0042", name="DPD8-15/ivr/I2",
    min_dpd=8, max_dpd=15, channel="ivr", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0042",
))
STRATEGIES.append(Strategy(
    code="ST0043", name="DPD8-15/ivr/I3",
    min_dpd=8, max_dpd=15, channel="ivr", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0043",
))
STRATEGIES.append(Strategy(
    code="ST0044", name="DPD8-15/ivr/I4",
    min_dpd=8, max_dpd=15, channel="ivr", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0044",
))
STRATEGIES.append(Strategy(
    code="ST0045", name="DPD8-15/ivr/I5",
    min_dpd=8, max_dpd=15, channel="ivr", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0045",
))
STRATEGIES.append(Strategy(
    code="ST0046", name="DPD8-15/app_push/I1",
    min_dpd=8, max_dpd=15, channel="app_push", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0046",
))
STRATEGIES.append(Strategy(
    code="ST0047", name="DPD8-15/app_push/I2",
    min_dpd=8, max_dpd=15, channel="app_push", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0047",
))
STRATEGIES.append(Strategy(
    code="ST0048", name="DPD8-15/app_push/I3",
    min_dpd=8, max_dpd=15, channel="app_push", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0048",
))
STRATEGIES.append(Strategy(
    code="ST0049", name="DPD8-15/app_push/I4",
    min_dpd=8, max_dpd=15, channel="app_push", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0049",
))
STRATEGIES.append(Strategy(
    code="ST0050", name="DPD8-15/app_push/I5",
    min_dpd=8, max_dpd=15, channel="app_push", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0050",
))
STRATEGIES.append(Strategy(
    code="ST0051", name="DPD8-15/human_call/I1",
    min_dpd=8, max_dpd=15, channel="human_call", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0051",
))
STRATEGIES.append(Strategy(
    code="ST0052", name="DPD8-15/human_call/I2",
    min_dpd=8, max_dpd=15, channel="human_call", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0052",
))
STRATEGIES.append(Strategy(
    code="ST0053", name="DPD8-15/human_call/I3",
    min_dpd=8, max_dpd=15, channel="human_call", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0053",
))
STRATEGIES.append(Strategy(
    code="ST0054", name="DPD8-15/human_call/I4",
    min_dpd=8, max_dpd=15, channel="human_call", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0054",
))
STRATEGIES.append(Strategy(
    code="ST0055", name="DPD8-15/human_call/I5",
    min_dpd=8, max_dpd=15, channel="human_call", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0055",
))
STRATEGIES.append(Strategy(
    code="ST0056", name="DPD8-15/letter/I1",
    min_dpd=8, max_dpd=15, channel="letter", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0056",
))
STRATEGIES.append(Strategy(
    code="ST0057", name="DPD8-15/letter/I2",
    min_dpd=8, max_dpd=15, channel="letter", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0057",
))
STRATEGIES.append(Strategy(
    code="ST0058", name="DPD8-15/letter/I3",
    min_dpd=8, max_dpd=15, channel="letter", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0058",
))
STRATEGIES.append(Strategy(
    code="ST0059", name="DPD8-15/letter/I4",
    min_dpd=8, max_dpd=15, channel="letter", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0059",
))
STRATEGIES.append(Strategy(
    code="ST0060", name="DPD8-15/letter/I5",
    min_dpd=8, max_dpd=15, channel="letter", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0060",
))
STRATEGIES.append(Strategy(
    code="ST0061", name="DPD8-15/legal_notice/I1",
    min_dpd=8, max_dpd=15, channel="legal_notice", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0061",
))
STRATEGIES.append(Strategy(
    code="ST0062", name="DPD8-15/legal_notice/I2",
    min_dpd=8, max_dpd=15, channel="legal_notice", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0062",
))
STRATEGIES.append(Strategy(
    code="ST0063", name="DPD8-15/legal_notice/I3",
    min_dpd=8, max_dpd=15, channel="legal_notice", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0063",
))
STRATEGIES.append(Strategy(
    code="ST0064", name="DPD8-15/legal_notice/I4",
    min_dpd=8, max_dpd=15, channel="legal_notice", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0064",
))
STRATEGIES.append(Strategy(
    code="ST0065", name="DPD8-15/legal_notice/I5",
    min_dpd=8, max_dpd=15, channel="legal_notice", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0065",
))
STRATEGIES.append(Strategy(
    code="ST0066", name="DPD8-15/visit/I1",
    min_dpd=8, max_dpd=15, channel="visit", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0066",
))
STRATEGIES.append(Strategy(
    code="ST0067", name="DPD8-15/visit/I2",
    min_dpd=8, max_dpd=15, channel="visit", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0067",
))
STRATEGIES.append(Strategy(
    code="ST0068", name="DPD8-15/visit/I3",
    min_dpd=8, max_dpd=15, channel="visit", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0068",
))
STRATEGIES.append(Strategy(
    code="ST0069", name="DPD8-15/visit/I4",
    min_dpd=8, max_dpd=15, channel="visit", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0069",
))
STRATEGIES.append(Strategy(
    code="ST0070", name="DPD8-15/visit/I5",
    min_dpd=8, max_dpd=15, channel="visit", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0070",
))
STRATEGIES.append(Strategy(
    code="ST0071", name="DPD16-30/sms/I1",
    min_dpd=16, max_dpd=30, channel="sms", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0071",
))
STRATEGIES.append(Strategy(
    code="ST0072", name="DPD16-30/sms/I2",
    min_dpd=16, max_dpd=30, channel="sms", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0072",
))
STRATEGIES.append(Strategy(
    code="ST0073", name="DPD16-30/sms/I3",
    min_dpd=16, max_dpd=30, channel="sms", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0073",
))
STRATEGIES.append(Strategy(
    code="ST0074", name="DPD16-30/sms/I4",
    min_dpd=16, max_dpd=30, channel="sms", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0074",
))
STRATEGIES.append(Strategy(
    code="ST0075", name="DPD16-30/sms/I5",
    min_dpd=16, max_dpd=30, channel="sms", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0075",
))
STRATEGIES.append(Strategy(
    code="ST0076", name="DPD16-30/ivr/I1",
    min_dpd=16, max_dpd=30, channel="ivr", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0076",
))
STRATEGIES.append(Strategy(
    code="ST0077", name="DPD16-30/ivr/I2",
    min_dpd=16, max_dpd=30, channel="ivr", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0077",
))
STRATEGIES.append(Strategy(
    code="ST0078", name="DPD16-30/ivr/I3",
    min_dpd=16, max_dpd=30, channel="ivr", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0078",
))
STRATEGIES.append(Strategy(
    code="ST0079", name="DPD16-30/ivr/I4",
    min_dpd=16, max_dpd=30, channel="ivr", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0079",
))
STRATEGIES.append(Strategy(
    code="ST0080", name="DPD16-30/ivr/I5",
    min_dpd=16, max_dpd=30, channel="ivr", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0080",
))
STRATEGIES.append(Strategy(
    code="ST0081", name="DPD16-30/app_push/I1",
    min_dpd=16, max_dpd=30, channel="app_push", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0081",
))
STRATEGIES.append(Strategy(
    code="ST0082", name="DPD16-30/app_push/I2",
    min_dpd=16, max_dpd=30, channel="app_push", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0082",
))
STRATEGIES.append(Strategy(
    code="ST0083", name="DPD16-30/app_push/I3",
    min_dpd=16, max_dpd=30, channel="app_push", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0083",
))
STRATEGIES.append(Strategy(
    code="ST0084", name="DPD16-30/app_push/I4",
    min_dpd=16, max_dpd=30, channel="app_push", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0084",
))
STRATEGIES.append(Strategy(
    code="ST0085", name="DPD16-30/app_push/I5",
    min_dpd=16, max_dpd=30, channel="app_push", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0085",
))
STRATEGIES.append(Strategy(
    code="ST0086", name="DPD16-30/human_call/I1",
    min_dpd=16, max_dpd=30, channel="human_call", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0086",
))
STRATEGIES.append(Strategy(
    code="ST0087", name="DPD16-30/human_call/I2",
    min_dpd=16, max_dpd=30, channel="human_call", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0087",
))
STRATEGIES.append(Strategy(
    code="ST0088", name="DPD16-30/human_call/I3",
    min_dpd=16, max_dpd=30, channel="human_call", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0088",
))
STRATEGIES.append(Strategy(
    code="ST0089", name="DPD16-30/human_call/I4",
    min_dpd=16, max_dpd=30, channel="human_call", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0089",
))
STRATEGIES.append(Strategy(
    code="ST0090", name="DPD16-30/human_call/I5",
    min_dpd=16, max_dpd=30, channel="human_call", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0090",
))
STRATEGIES.append(Strategy(
    code="ST0091", name="DPD16-30/letter/I1",
    min_dpd=16, max_dpd=30, channel="letter", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0091",
))
STRATEGIES.append(Strategy(
    code="ST0092", name="DPD16-30/letter/I2",
    min_dpd=16, max_dpd=30, channel="letter", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0092",
))
STRATEGIES.append(Strategy(
    code="ST0093", name="DPD16-30/letter/I3",
    min_dpd=16, max_dpd=30, channel="letter", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0093",
))
STRATEGIES.append(Strategy(
    code="ST0094", name="DPD16-30/letter/I4",
    min_dpd=16, max_dpd=30, channel="letter", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0094",
))
STRATEGIES.append(Strategy(
    code="ST0095", name="DPD16-30/letter/I5",
    min_dpd=16, max_dpd=30, channel="letter", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0095",
))
STRATEGIES.append(Strategy(
    code="ST0096", name="DPD16-30/legal_notice/I1",
    min_dpd=16, max_dpd=30, channel="legal_notice", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0096",
))
STRATEGIES.append(Strategy(
    code="ST0097", name="DPD16-30/legal_notice/I2",
    min_dpd=16, max_dpd=30, channel="legal_notice", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0097",
))
STRATEGIES.append(Strategy(
    code="ST0098", name="DPD16-30/legal_notice/I3",
    min_dpd=16, max_dpd=30, channel="legal_notice", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0098",
))
STRATEGIES.append(Strategy(
    code="ST0099", name="DPD16-30/legal_notice/I4",
    min_dpd=16, max_dpd=30, channel="legal_notice", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0099",
))
STRATEGIES.append(Strategy(
    code="ST0100", name="DPD16-30/legal_notice/I5",
    min_dpd=16, max_dpd=30, channel="legal_notice", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0100",
))
STRATEGIES.append(Strategy(
    code="ST0101", name="DPD16-30/visit/I1",
    min_dpd=16, max_dpd=30, channel="visit", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0101",
))
STRATEGIES.append(Strategy(
    code="ST0102", name="DPD16-30/visit/I2",
    min_dpd=16, max_dpd=30, channel="visit", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0102",
))
STRATEGIES.append(Strategy(
    code="ST0103", name="DPD16-30/visit/I3",
    min_dpd=16, max_dpd=30, channel="visit", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0103",
))
STRATEGIES.append(Strategy(
    code="ST0104", name="DPD16-30/visit/I4",
    min_dpd=16, max_dpd=30, channel="visit", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0104",
))
STRATEGIES.append(Strategy(
    code="ST0105", name="DPD16-30/visit/I5",
    min_dpd=16, max_dpd=30, channel="visit", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0105",
))
STRATEGIES.append(Strategy(
    code="ST0106", name="DPD31-60/sms/I1",
    min_dpd=31, max_dpd=60, channel="sms", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0106",
))
STRATEGIES.append(Strategy(
    code="ST0107", name="DPD31-60/sms/I2",
    min_dpd=31, max_dpd=60, channel="sms", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0107",
))
STRATEGIES.append(Strategy(
    code="ST0108", name="DPD31-60/sms/I3",
    min_dpd=31, max_dpd=60, channel="sms", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0108",
))
STRATEGIES.append(Strategy(
    code="ST0109", name="DPD31-60/sms/I4",
    min_dpd=31, max_dpd=60, channel="sms", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0109",
))
STRATEGIES.append(Strategy(
    code="ST0110", name="DPD31-60/sms/I5",
    min_dpd=31, max_dpd=60, channel="sms", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0110",
))
STRATEGIES.append(Strategy(
    code="ST0111", name="DPD31-60/ivr/I1",
    min_dpd=31, max_dpd=60, channel="ivr", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0111",
))
STRATEGIES.append(Strategy(
    code="ST0112", name="DPD31-60/ivr/I2",
    min_dpd=31, max_dpd=60, channel="ivr", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0112",
))
STRATEGIES.append(Strategy(
    code="ST0113", name="DPD31-60/ivr/I3",
    min_dpd=31, max_dpd=60, channel="ivr", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0113",
))
STRATEGIES.append(Strategy(
    code="ST0114", name="DPD31-60/ivr/I4",
    min_dpd=31, max_dpd=60, channel="ivr", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0114",
))
STRATEGIES.append(Strategy(
    code="ST0115", name="DPD31-60/ivr/I5",
    min_dpd=31, max_dpd=60, channel="ivr", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0115",
))
STRATEGIES.append(Strategy(
    code="ST0116", name="DPD31-60/app_push/I1",
    min_dpd=31, max_dpd=60, channel="app_push", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0116",
))
STRATEGIES.append(Strategy(
    code="ST0117", name="DPD31-60/app_push/I2",
    min_dpd=31, max_dpd=60, channel="app_push", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0117",
))
STRATEGIES.append(Strategy(
    code="ST0118", name="DPD31-60/app_push/I3",
    min_dpd=31, max_dpd=60, channel="app_push", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0118",
))
STRATEGIES.append(Strategy(
    code="ST0119", name="DPD31-60/app_push/I4",
    min_dpd=31, max_dpd=60, channel="app_push", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0119",
))
STRATEGIES.append(Strategy(
    code="ST0120", name="DPD31-60/app_push/I5",
    min_dpd=31, max_dpd=60, channel="app_push", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0120",
))
STRATEGIES.append(Strategy(
    code="ST0121", name="DPD31-60/human_call/I1",
    min_dpd=31, max_dpd=60, channel="human_call", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0121",
))
STRATEGIES.append(Strategy(
    code="ST0122", name="DPD31-60/human_call/I2",
    min_dpd=31, max_dpd=60, channel="human_call", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0122",
))
STRATEGIES.append(Strategy(
    code="ST0123", name="DPD31-60/human_call/I3",
    min_dpd=31, max_dpd=60, channel="human_call", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0123",
))
STRATEGIES.append(Strategy(
    code="ST0124", name="DPD31-60/human_call/I4",
    min_dpd=31, max_dpd=60, channel="human_call", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0124",
))
STRATEGIES.append(Strategy(
    code="ST0125", name="DPD31-60/human_call/I5",
    min_dpd=31, max_dpd=60, channel="human_call", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0125",
))
STRATEGIES.append(Strategy(
    code="ST0126", name="DPD31-60/letter/I1",
    min_dpd=31, max_dpd=60, channel="letter", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0126",
))
STRATEGIES.append(Strategy(
    code="ST0127", name="DPD31-60/letter/I2",
    min_dpd=31, max_dpd=60, channel="letter", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0127",
))
STRATEGIES.append(Strategy(
    code="ST0128", name="DPD31-60/letter/I3",
    min_dpd=31, max_dpd=60, channel="letter", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0128",
))
STRATEGIES.append(Strategy(
    code="ST0129", name="DPD31-60/letter/I4",
    min_dpd=31, max_dpd=60, channel="letter", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0129",
))
STRATEGIES.append(Strategy(
    code="ST0130", name="DPD31-60/letter/I5",
    min_dpd=31, max_dpd=60, channel="letter", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0130",
))
STRATEGIES.append(Strategy(
    code="ST0131", name="DPD31-60/legal_notice/I1",
    min_dpd=31, max_dpd=60, channel="legal_notice", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0131",
))
STRATEGIES.append(Strategy(
    code="ST0132", name="DPD31-60/legal_notice/I2",
    min_dpd=31, max_dpd=60, channel="legal_notice", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0132",
))
STRATEGIES.append(Strategy(
    code="ST0133", name="DPD31-60/legal_notice/I3",
    min_dpd=31, max_dpd=60, channel="legal_notice", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0133",
))
STRATEGIES.append(Strategy(
    code="ST0134", name="DPD31-60/legal_notice/I4",
    min_dpd=31, max_dpd=60, channel="legal_notice", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0134",
))
STRATEGIES.append(Strategy(
    code="ST0135", name="DPD31-60/legal_notice/I5",
    min_dpd=31, max_dpd=60, channel="legal_notice", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0135",
))
STRATEGIES.append(Strategy(
    code="ST0136", name="DPD31-60/visit/I1",
    min_dpd=31, max_dpd=60, channel="visit", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0136",
))
STRATEGIES.append(Strategy(
    code="ST0137", name="DPD31-60/visit/I2",
    min_dpd=31, max_dpd=60, channel="visit", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0137",
))
STRATEGIES.append(Strategy(
    code="ST0138", name="DPD31-60/visit/I3",
    min_dpd=31, max_dpd=60, channel="visit", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0138",
))
STRATEGIES.append(Strategy(
    code="ST0139", name="DPD31-60/visit/I4",
    min_dpd=31, max_dpd=60, channel="visit", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0139",
))
STRATEGIES.append(Strategy(
    code="ST0140", name="DPD31-60/visit/I5",
    min_dpd=31, max_dpd=60, channel="visit", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0140",
))
STRATEGIES.append(Strategy(
    code="ST0141", name="DPD61-90/sms/I1",
    min_dpd=61, max_dpd=90, channel="sms", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0141",
))
STRATEGIES.append(Strategy(
    code="ST0142", name="DPD61-90/sms/I2",
    min_dpd=61, max_dpd=90, channel="sms", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0142",
))
STRATEGIES.append(Strategy(
    code="ST0143", name="DPD61-90/sms/I3",
    min_dpd=61, max_dpd=90, channel="sms", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0143",
))
STRATEGIES.append(Strategy(
    code="ST0144", name="DPD61-90/sms/I4",
    min_dpd=61, max_dpd=90, channel="sms", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0144",
))
STRATEGIES.append(Strategy(
    code="ST0145", name="DPD61-90/sms/I5",
    min_dpd=61, max_dpd=90, channel="sms", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0145",
))
STRATEGIES.append(Strategy(
    code="ST0146", name="DPD61-90/ivr/I1",
    min_dpd=61, max_dpd=90, channel="ivr", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0146",
))
STRATEGIES.append(Strategy(
    code="ST0147", name="DPD61-90/ivr/I2",
    min_dpd=61, max_dpd=90, channel="ivr", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0147",
))
STRATEGIES.append(Strategy(
    code="ST0148", name="DPD61-90/ivr/I3",
    min_dpd=61, max_dpd=90, channel="ivr", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0148",
))
STRATEGIES.append(Strategy(
    code="ST0149", name="DPD61-90/ivr/I4",
    min_dpd=61, max_dpd=90, channel="ivr", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0149",
))
STRATEGIES.append(Strategy(
    code="ST0150", name="DPD61-90/ivr/I5",
    min_dpd=61, max_dpd=90, channel="ivr", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0150",
))
STRATEGIES.append(Strategy(
    code="ST0151", name="DPD61-90/app_push/I1",
    min_dpd=61, max_dpd=90, channel="app_push", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0151",
))
STRATEGIES.append(Strategy(
    code="ST0152", name="DPD61-90/app_push/I2",
    min_dpd=61, max_dpd=90, channel="app_push", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0152",
))
STRATEGIES.append(Strategy(
    code="ST0153", name="DPD61-90/app_push/I3",
    min_dpd=61, max_dpd=90, channel="app_push", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0153",
))
STRATEGIES.append(Strategy(
    code="ST0154", name="DPD61-90/app_push/I4",
    min_dpd=61, max_dpd=90, channel="app_push", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0154",
))
STRATEGIES.append(Strategy(
    code="ST0155", name="DPD61-90/app_push/I5",
    min_dpd=61, max_dpd=90, channel="app_push", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0155",
))
STRATEGIES.append(Strategy(
    code="ST0156", name="DPD61-90/human_call/I1",
    min_dpd=61, max_dpd=90, channel="human_call", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0156",
))
STRATEGIES.append(Strategy(
    code="ST0157", name="DPD61-90/human_call/I2",
    min_dpd=61, max_dpd=90, channel="human_call", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0157",
))
STRATEGIES.append(Strategy(
    code="ST0158", name="DPD61-90/human_call/I3",
    min_dpd=61, max_dpd=90, channel="human_call", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0158",
))
STRATEGIES.append(Strategy(
    code="ST0159", name="DPD61-90/human_call/I4",
    min_dpd=61, max_dpd=90, channel="human_call", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0159",
))
STRATEGIES.append(Strategy(
    code="ST0160", name="DPD61-90/human_call/I5",
    min_dpd=61, max_dpd=90, channel="human_call", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0160",
))
STRATEGIES.append(Strategy(
    code="ST0161", name="DPD61-90/letter/I1",
    min_dpd=61, max_dpd=90, channel="letter", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0161",
))
STRATEGIES.append(Strategy(
    code="ST0162", name="DPD61-90/letter/I2",
    min_dpd=61, max_dpd=90, channel="letter", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0162",
))
STRATEGIES.append(Strategy(
    code="ST0163", name="DPD61-90/letter/I3",
    min_dpd=61, max_dpd=90, channel="letter", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0163",
))
STRATEGIES.append(Strategy(
    code="ST0164", name="DPD61-90/letter/I4",
    min_dpd=61, max_dpd=90, channel="letter", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0164",
))
STRATEGIES.append(Strategy(
    code="ST0165", name="DPD61-90/letter/I5",
    min_dpd=61, max_dpd=90, channel="letter", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0165",
))
STRATEGIES.append(Strategy(
    code="ST0166", name="DPD61-90/legal_notice/I1",
    min_dpd=61, max_dpd=90, channel="legal_notice", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0166",
))
STRATEGIES.append(Strategy(
    code="ST0167", name="DPD61-90/legal_notice/I2",
    min_dpd=61, max_dpd=90, channel="legal_notice", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0167",
))
STRATEGIES.append(Strategy(
    code="ST0168", name="DPD61-90/legal_notice/I3",
    min_dpd=61, max_dpd=90, channel="legal_notice", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0168",
))
STRATEGIES.append(Strategy(
    code="ST0169", name="DPD61-90/legal_notice/I4",
    min_dpd=61, max_dpd=90, channel="legal_notice", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0169",
))
STRATEGIES.append(Strategy(
    code="ST0170", name="DPD61-90/legal_notice/I5",
    min_dpd=61, max_dpd=90, channel="legal_notice", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0170",
))
STRATEGIES.append(Strategy(
    code="ST0171", name="DPD61-90/visit/I1",
    min_dpd=61, max_dpd=90, channel="visit", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0171",
))
STRATEGIES.append(Strategy(
    code="ST0172", name="DPD61-90/visit/I2",
    min_dpd=61, max_dpd=90, channel="visit", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0172",
))
STRATEGIES.append(Strategy(
    code="ST0173", name="DPD61-90/visit/I3",
    min_dpd=61, max_dpd=90, channel="visit", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0173",
))
STRATEGIES.append(Strategy(
    code="ST0174", name="DPD61-90/visit/I4",
    min_dpd=61, max_dpd=90, channel="visit", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0174",
))
STRATEGIES.append(Strategy(
    code="ST0175", name="DPD61-90/visit/I5",
    min_dpd=61, max_dpd=90, channel="visit", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0175",
))
STRATEGIES.append(Strategy(
    code="ST0176", name="DPD91-180/sms/I1",
    min_dpd=91, max_dpd=180, channel="sms", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0176",
))
STRATEGIES.append(Strategy(
    code="ST0177", name="DPD91-180/sms/I2",
    min_dpd=91, max_dpd=180, channel="sms", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0177",
))
STRATEGIES.append(Strategy(
    code="ST0178", name="DPD91-180/sms/I3",
    min_dpd=91, max_dpd=180, channel="sms", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0178",
))
STRATEGIES.append(Strategy(
    code="ST0179", name="DPD91-180/sms/I4",
    min_dpd=91, max_dpd=180, channel="sms", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0179",
))
STRATEGIES.append(Strategy(
    code="ST0180", name="DPD91-180/sms/I5",
    min_dpd=91, max_dpd=180, channel="sms", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0180",
))
STRATEGIES.append(Strategy(
    code="ST0181", name="DPD91-180/ivr/I1",
    min_dpd=91, max_dpd=180, channel="ivr", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0181",
))
STRATEGIES.append(Strategy(
    code="ST0182", name="DPD91-180/ivr/I2",
    min_dpd=91, max_dpd=180, channel="ivr", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0182",
))
STRATEGIES.append(Strategy(
    code="ST0183", name="DPD91-180/ivr/I3",
    min_dpd=91, max_dpd=180, channel="ivr", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0183",
))
STRATEGIES.append(Strategy(
    code="ST0184", name="DPD91-180/ivr/I4",
    min_dpd=91, max_dpd=180, channel="ivr", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0184",
))
STRATEGIES.append(Strategy(
    code="ST0185", name="DPD91-180/ivr/I5",
    min_dpd=91, max_dpd=180, channel="ivr", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0185",
))
STRATEGIES.append(Strategy(
    code="ST0186", name="DPD91-180/app_push/I1",
    min_dpd=91, max_dpd=180, channel="app_push", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0186",
))
STRATEGIES.append(Strategy(
    code="ST0187", name="DPD91-180/app_push/I2",
    min_dpd=91, max_dpd=180, channel="app_push", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0187",
))
STRATEGIES.append(Strategy(
    code="ST0188", name="DPD91-180/app_push/I3",
    min_dpd=91, max_dpd=180, channel="app_push", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0188",
))
STRATEGIES.append(Strategy(
    code="ST0189", name="DPD91-180/app_push/I4",
    min_dpd=91, max_dpd=180, channel="app_push", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0189",
))
STRATEGIES.append(Strategy(
    code="ST0190", name="DPD91-180/app_push/I5",
    min_dpd=91, max_dpd=180, channel="app_push", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0190",
))
STRATEGIES.append(Strategy(
    code="ST0191", name="DPD91-180/human_call/I1",
    min_dpd=91, max_dpd=180, channel="human_call", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0191",
))
STRATEGIES.append(Strategy(
    code="ST0192", name="DPD91-180/human_call/I2",
    min_dpd=91, max_dpd=180, channel="human_call", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0192",
))
STRATEGIES.append(Strategy(
    code="ST0193", name="DPD91-180/human_call/I3",
    min_dpd=91, max_dpd=180, channel="human_call", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0193",
))
STRATEGIES.append(Strategy(
    code="ST0194", name="DPD91-180/human_call/I4",
    min_dpd=91, max_dpd=180, channel="human_call", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0194",
))
STRATEGIES.append(Strategy(
    code="ST0195", name="DPD91-180/human_call/I5",
    min_dpd=91, max_dpd=180, channel="human_call", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0195",
))
STRATEGIES.append(Strategy(
    code="ST0196", name="DPD91-180/letter/I1",
    min_dpd=91, max_dpd=180, channel="letter", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0196",
))
STRATEGIES.append(Strategy(
    code="ST0197", name="DPD91-180/letter/I2",
    min_dpd=91, max_dpd=180, channel="letter", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0197",
))
STRATEGIES.append(Strategy(
    code="ST0198", name="DPD91-180/letter/I3",
    min_dpd=91, max_dpd=180, channel="letter", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0198",
))
STRATEGIES.append(Strategy(
    code="ST0199", name="DPD91-180/letter/I4",
    min_dpd=91, max_dpd=180, channel="letter", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0199",
))
STRATEGIES.append(Strategy(
    code="ST0200", name="DPD91-180/letter/I5",
    min_dpd=91, max_dpd=180, channel="letter", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0200",
))
STRATEGIES.append(Strategy(
    code="ST0201", name="DPD91-180/legal_notice/I1",
    min_dpd=91, max_dpd=180, channel="legal_notice", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0201",
))
STRATEGIES.append(Strategy(
    code="ST0202", name="DPD91-180/legal_notice/I2",
    min_dpd=91, max_dpd=180, channel="legal_notice", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0202",
))
STRATEGIES.append(Strategy(
    code="ST0203", name="DPD91-180/legal_notice/I3",
    min_dpd=91, max_dpd=180, channel="legal_notice", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0203",
))
STRATEGIES.append(Strategy(
    code="ST0204", name="DPD91-180/legal_notice/I4",
    min_dpd=91, max_dpd=180, channel="legal_notice", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0204",
))
STRATEGIES.append(Strategy(
    code="ST0205", name="DPD91-180/legal_notice/I5",
    min_dpd=91, max_dpd=180, channel="legal_notice", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0205",
))
STRATEGIES.append(Strategy(
    code="ST0206", name="DPD91-180/visit/I1",
    min_dpd=91, max_dpd=180, channel="visit", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0206",
))
STRATEGIES.append(Strategy(
    code="ST0207", name="DPD91-180/visit/I2",
    min_dpd=91, max_dpd=180, channel="visit", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0207",
))
STRATEGIES.append(Strategy(
    code="ST0208", name="DPD91-180/visit/I3",
    min_dpd=91, max_dpd=180, channel="visit", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0208",
))
STRATEGIES.append(Strategy(
    code="ST0209", name="DPD91-180/visit/I4",
    min_dpd=91, max_dpd=180, channel="visit", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0209",
))
STRATEGIES.append(Strategy(
    code="ST0210", name="DPD91-180/visit/I5",
    min_dpd=91, max_dpd=180, channel="visit", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0210",
))
STRATEGIES.append(Strategy(
    code="ST0211", name="DPD181-360/sms/I1",
    min_dpd=181, max_dpd=360, channel="sms", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0211",
))
STRATEGIES.append(Strategy(
    code="ST0212", name="DPD181-360/sms/I2",
    min_dpd=181, max_dpd=360, channel="sms", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0212",
))
STRATEGIES.append(Strategy(
    code="ST0213", name="DPD181-360/sms/I3",
    min_dpd=181, max_dpd=360, channel="sms", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0213",
))
STRATEGIES.append(Strategy(
    code="ST0214", name="DPD181-360/sms/I4",
    min_dpd=181, max_dpd=360, channel="sms", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0214",
))
STRATEGIES.append(Strategy(
    code="ST0215", name="DPD181-360/sms/I5",
    min_dpd=181, max_dpd=360, channel="sms", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0215",
))
STRATEGIES.append(Strategy(
    code="ST0216", name="DPD181-360/ivr/I1",
    min_dpd=181, max_dpd=360, channel="ivr", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0216",
))
STRATEGIES.append(Strategy(
    code="ST0217", name="DPD181-360/ivr/I2",
    min_dpd=181, max_dpd=360, channel="ivr", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0217",
))
STRATEGIES.append(Strategy(
    code="ST0218", name="DPD181-360/ivr/I3",
    min_dpd=181, max_dpd=360, channel="ivr", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0218",
))
STRATEGIES.append(Strategy(
    code="ST0219", name="DPD181-360/ivr/I4",
    min_dpd=181, max_dpd=360, channel="ivr", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0219",
))
STRATEGIES.append(Strategy(
    code="ST0220", name="DPD181-360/ivr/I5",
    min_dpd=181, max_dpd=360, channel="ivr", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0220",
))
STRATEGIES.append(Strategy(
    code="ST0221", name="DPD181-360/app_push/I1",
    min_dpd=181, max_dpd=360, channel="app_push", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0221",
))
STRATEGIES.append(Strategy(
    code="ST0222", name="DPD181-360/app_push/I2",
    min_dpd=181, max_dpd=360, channel="app_push", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0222",
))
STRATEGIES.append(Strategy(
    code="ST0223", name="DPD181-360/app_push/I3",
    min_dpd=181, max_dpd=360, channel="app_push", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0223",
))
STRATEGIES.append(Strategy(
    code="ST0224", name="DPD181-360/app_push/I4",
    min_dpd=181, max_dpd=360, channel="app_push", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0224",
))
STRATEGIES.append(Strategy(
    code="ST0225", name="DPD181-360/app_push/I5",
    min_dpd=181, max_dpd=360, channel="app_push", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0225",
))
STRATEGIES.append(Strategy(
    code="ST0226", name="DPD181-360/human_call/I1",
    min_dpd=181, max_dpd=360, channel="human_call", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0226",
))
STRATEGIES.append(Strategy(
    code="ST0227", name="DPD181-360/human_call/I2",
    min_dpd=181, max_dpd=360, channel="human_call", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0227",
))
STRATEGIES.append(Strategy(
    code="ST0228", name="DPD181-360/human_call/I3",
    min_dpd=181, max_dpd=360, channel="human_call", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0228",
))
STRATEGIES.append(Strategy(
    code="ST0229", name="DPD181-360/human_call/I4",
    min_dpd=181, max_dpd=360, channel="human_call", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0229",
))
STRATEGIES.append(Strategy(
    code="ST0230", name="DPD181-360/human_call/I5",
    min_dpd=181, max_dpd=360, channel="human_call", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0230",
))
STRATEGIES.append(Strategy(
    code="ST0231", name="DPD181-360/letter/I1",
    min_dpd=181, max_dpd=360, channel="letter", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0231",
))
STRATEGIES.append(Strategy(
    code="ST0232", name="DPD181-360/letter/I2",
    min_dpd=181, max_dpd=360, channel="letter", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0232",
))
STRATEGIES.append(Strategy(
    code="ST0233", name="DPD181-360/letter/I3",
    min_dpd=181, max_dpd=360, channel="letter", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0233",
))
STRATEGIES.append(Strategy(
    code="ST0234", name="DPD181-360/letter/I4",
    min_dpd=181, max_dpd=360, channel="letter", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0234",
))
STRATEGIES.append(Strategy(
    code="ST0235", name="DPD181-360/letter/I5",
    min_dpd=181, max_dpd=360, channel="letter", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0235",
))
STRATEGIES.append(Strategy(
    code="ST0236", name="DPD181-360/legal_notice/I1",
    min_dpd=181, max_dpd=360, channel="legal_notice", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0236",
))
STRATEGIES.append(Strategy(
    code="ST0237", name="DPD181-360/legal_notice/I2",
    min_dpd=181, max_dpd=360, channel="legal_notice", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0237",
))
STRATEGIES.append(Strategy(
    code="ST0238", name="DPD181-360/legal_notice/I3",
    min_dpd=181, max_dpd=360, channel="legal_notice", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0238",
))
STRATEGIES.append(Strategy(
    code="ST0239", name="DPD181-360/legal_notice/I4",
    min_dpd=181, max_dpd=360, channel="legal_notice", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0239",
))
STRATEGIES.append(Strategy(
    code="ST0240", name="DPD181-360/legal_notice/I5",
    min_dpd=181, max_dpd=360, channel="legal_notice", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0240",
))
STRATEGIES.append(Strategy(
    code="ST0241", name="DPD181-360/visit/I1",
    min_dpd=181, max_dpd=360, channel="visit", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0241",
))
STRATEGIES.append(Strategy(
    code="ST0242", name="DPD181-360/visit/I2",
    min_dpd=181, max_dpd=360, channel="visit", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0242",
))
STRATEGIES.append(Strategy(
    code="ST0243", name="DPD181-360/visit/I3",
    min_dpd=181, max_dpd=360, channel="visit", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0243",
))
STRATEGIES.append(Strategy(
    code="ST0244", name="DPD181-360/visit/I4",
    min_dpd=181, max_dpd=360, channel="visit", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0244",
))
STRATEGIES.append(Strategy(
    code="ST0245", name="DPD181-360/visit/I5",
    min_dpd=181, max_dpd=360, channel="visit", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0245",
))
STRATEGIES.append(Strategy(
    code="ST0246", name="DPD361-9999/sms/I1",
    min_dpd=361, max_dpd=9999, channel="sms", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0246",
))
STRATEGIES.append(Strategy(
    code="ST0247", name="DPD361-9999/sms/I2",
    min_dpd=361, max_dpd=9999, channel="sms", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0247",
))
STRATEGIES.append(Strategy(
    code="ST0248", name="DPD361-9999/sms/I3",
    min_dpd=361, max_dpd=9999, channel="sms", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0248",
))
STRATEGIES.append(Strategy(
    code="ST0249", name="DPD361-9999/sms/I4",
    min_dpd=361, max_dpd=9999, channel="sms", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0249",
))
STRATEGIES.append(Strategy(
    code="ST0250", name="DPD361-9999/sms/I5",
    min_dpd=361, max_dpd=9999, channel="sms", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0250",
))
STRATEGIES.append(Strategy(
    code="ST0251", name="DPD361-9999/ivr/I1",
    min_dpd=361, max_dpd=9999, channel="ivr", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0251",
))
STRATEGIES.append(Strategy(
    code="ST0252", name="DPD361-9999/ivr/I2",
    min_dpd=361, max_dpd=9999, channel="ivr", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0252",
))
STRATEGIES.append(Strategy(
    code="ST0253", name="DPD361-9999/ivr/I3",
    min_dpd=361, max_dpd=9999, channel="ivr", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0253",
))
STRATEGIES.append(Strategy(
    code="ST0254", name="DPD361-9999/ivr/I4",
    min_dpd=361, max_dpd=9999, channel="ivr", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0254",
))
STRATEGIES.append(Strategy(
    code="ST0255", name="DPD361-9999/ivr/I5",
    min_dpd=361, max_dpd=9999, channel="ivr", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0255",
))
STRATEGIES.append(Strategy(
    code="ST0256", name="DPD361-9999/app_push/I1",
    min_dpd=361, max_dpd=9999, channel="app_push", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0256",
))
STRATEGIES.append(Strategy(
    code="ST0257", name="DPD361-9999/app_push/I2",
    min_dpd=361, max_dpd=9999, channel="app_push", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0257",
))
STRATEGIES.append(Strategy(
    code="ST0258", name="DPD361-9999/app_push/I3",
    min_dpd=361, max_dpd=9999, channel="app_push", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0258",
))
STRATEGIES.append(Strategy(
    code="ST0259", name="DPD361-9999/app_push/I4",
    min_dpd=361, max_dpd=9999, channel="app_push", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0259",
))
STRATEGIES.append(Strategy(
    code="ST0260", name="DPD361-9999/app_push/I5",
    min_dpd=361, max_dpd=9999, channel="app_push", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0260",
))
STRATEGIES.append(Strategy(
    code="ST0261", name="DPD361-9999/human_call/I1",
    min_dpd=361, max_dpd=9999, channel="human_call", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0261",
))
STRATEGIES.append(Strategy(
    code="ST0262", name="DPD361-9999/human_call/I2",
    min_dpd=361, max_dpd=9999, channel="human_call", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0262",
))
STRATEGIES.append(Strategy(
    code="ST0263", name="DPD361-9999/human_call/I3",
    min_dpd=361, max_dpd=9999, channel="human_call", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0263",
))
STRATEGIES.append(Strategy(
    code="ST0264", name="DPD361-9999/human_call/I4",
    min_dpd=361, max_dpd=9999, channel="human_call", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0264",
))
STRATEGIES.append(Strategy(
    code="ST0265", name="DPD361-9999/human_call/I5",
    min_dpd=361, max_dpd=9999, channel="human_call", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0265",
))
STRATEGIES.append(Strategy(
    code="ST0266", name="DPD361-9999/letter/I1",
    min_dpd=361, max_dpd=9999, channel="letter", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0266",
))
STRATEGIES.append(Strategy(
    code="ST0267", name="DPD361-9999/letter/I2",
    min_dpd=361, max_dpd=9999, channel="letter", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0267",
))
STRATEGIES.append(Strategy(
    code="ST0268", name="DPD361-9999/letter/I3",
    min_dpd=361, max_dpd=9999, channel="letter", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0268",
))
STRATEGIES.append(Strategy(
    code="ST0269", name="DPD361-9999/letter/I4",
    min_dpd=361, max_dpd=9999, channel="letter", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0269",
))
STRATEGIES.append(Strategy(
    code="ST0270", name="DPD361-9999/letter/I5",
    min_dpd=361, max_dpd=9999, channel="letter", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0270",
))
STRATEGIES.append(Strategy(
    code="ST0271", name="DPD361-9999/legal_notice/I1",
    min_dpd=361, max_dpd=9999, channel="legal_notice", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0271",
))
STRATEGIES.append(Strategy(
    code="ST0272", name="DPD361-9999/legal_notice/I2",
    min_dpd=361, max_dpd=9999, channel="legal_notice", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0272",
))
STRATEGIES.append(Strategy(
    code="ST0273", name="DPD361-9999/legal_notice/I3",
    min_dpd=361, max_dpd=9999, channel="legal_notice", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0273",
))
STRATEGIES.append(Strategy(
    code="ST0274", name="DPD361-9999/legal_notice/I4",
    min_dpd=361, max_dpd=9999, channel="legal_notice", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0274",
))
STRATEGIES.append(Strategy(
    code="ST0275", name="DPD361-9999/legal_notice/I5",
    min_dpd=361, max_dpd=9999, channel="legal_notice", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0275",
))
STRATEGIES.append(Strategy(
    code="ST0276", name="DPD361-9999/visit/I1",
    min_dpd=361, max_dpd=9999, channel="visit", intensity=1,
    script="Please repay overdue balance promptly. Strategy ST0276",
))
STRATEGIES.append(Strategy(
    code="ST0277", name="DPD361-9999/visit/I2",
    min_dpd=361, max_dpd=9999, channel="visit", intensity=2,
    script="Please repay overdue balance promptly. Strategy ST0277",
))
STRATEGIES.append(Strategy(
    code="ST0278", name="DPD361-9999/visit/I3",
    min_dpd=361, max_dpd=9999, channel="visit", intensity=3,
    script="Please repay overdue balance promptly. Strategy ST0278",
))
STRATEGIES.append(Strategy(
    code="ST0279", name="DPD361-9999/visit/I4",
    min_dpd=361, max_dpd=9999, channel="visit", intensity=4,
    script="Please repay overdue balance promptly. Strategy ST0279",
))
STRATEGIES.append(Strategy(
    code="ST0280", name="DPD361-9999/visit/I5",
    min_dpd=361, max_dpd=9999, channel="visit", intensity=5,
    script="Please repay overdue balance promptly. Strategy ST0280",
))

def pick_strategies(dpd: int, limit: int = 5) -> list[Strategy]:
    hit = [s for s in STRATEGIES if s.min_dpd <= dpd <= s.max_dpd]
    hit.sort(key=lambda s: (-s.intensity, s.code))
    return hit[:limit]