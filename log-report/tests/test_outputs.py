#from pathlib import Path


#def test_report_exists():
 #   """The agent produced a report file."""
  #  assert Path("/app/report.json").exists(), "no report.json found"


#def test_report_nonempty():
 #   """The report file is not empty."""
  #  assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"



import json


def load_report():
    with open("/app/report.json") as f:
        return json.load(f)


def test_total_requests():
    """Success criterion 1: total number of requests."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 2: unique client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 3: most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"