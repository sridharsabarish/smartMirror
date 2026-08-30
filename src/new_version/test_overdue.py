from smartMirror import smartMirror
def test_check_overdue_json_processing():
    smartMirrorObj = smartMirror()
    overdueJson = smartMirrorObj.get_overdue();
    smartMirrorObj.add_overdue_to_mirror(overdueJson)
    assert True