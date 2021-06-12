import nerve


class TestValidation:
    def test_ping_nothing(self):
        assert nerve.ping() == 0

    def test_ping_brandbil_dot_dk(self):
        assert nerve.ping('brandbil.dk') == 0

    def test_ping_dr_dot_dk(self):
        assert nerve.ping('dr.dk') == 0

    def test_ping_validation_nothing(self):
        validation = nerve.Validation('ping', '')
        assert validation.destination == ''
        assert validation.returncode == 1

    def test_ping_validation_brandbil_dot_dk(self):
        validation = nerve.Validation('ping','brandbil.dk')
        assert validation.destination == 'brandbil.dk'
        assert validation.returncode == 0

    def test_ping_validation_should_fail_for_doesnotexist_dot_brandbil_dot_dk(self):
        validation = nerve.Validation('ping', 'doesnotexist.brandbil.dk')
        assert validation.destination == 'doesnotexist.brandbil.dk'
        assert validation.returncode == 2