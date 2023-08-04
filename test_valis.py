import valis


def test_ping_nothing():
    assert valis.ping() == 0


def test_ping_brandbil_dot_dk():
    assert valis.ping('brandbil.dk') == 0


def test_ping_dr_dot_dk():
    assert valis.ping('dr.dk') == 0


def test_ping_validation_nothing():
    validation = valis.Validation('ping', '')
    assert validation.destination == ''
    assert validation.returncode == 64


def test_ping_validation_brandbil_dot_dk():
    validation = valis.Validation('ping', 'brandbil.dk')
    assert validation.destination == 'brandbil.dk'
    assert validation.returncode == 0


def test_ping_validation_should_fail_for_doesnotexist_dot_brandbil_dot_dk():
    validation = valis.Validation('ping', 'doesnotexist.brandbil.dk')
    assert validation.destination == 'doesnotexist.brandbil.dk'
    assert validation.returncode == 68
