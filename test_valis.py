import valis
import os
import pytest


IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_ping_nothing():
    assert valis.ping() == 0


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_ping_brandbil_dot_dk():
    assert valis.ping("brandbil.dk") == 0


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_ping_dr_dot_dk():
    assert valis.ping("dr.dk") == 0


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_ping_validation_nothing():
    validation = valis.Validation("ping", "")
    assert validation.destination == ""
    assert validation.returncode == 64 or 1
    # Ping return codes for no destination are different for different OSes:
    # 64 on OSX, 1 on linux, 1 on FreeBSD


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_ping_validation_brandbil_dot_dk():
    validation = valis.Validation("ping", "brandbil.dk")
    assert validation.destination == "brandbil.dk"
    assert validation.returncode == 0


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_ping_validation_should_fail_for_doesnotexist_dot_brandbil_dot_dk():
    validation = valis.Validation("ping", "doesnotexist.brandbil.dk")
    assert validation.destination == "doesnotexist.brandbil.dk"
    assert validation.returncode == 68 or 2 or 1
    # Ping return codes for non-existing domain name are different for different OSes:
    # 68 on OSX, 2 on linux, 1 on FreeBSD


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_ping_validation_should_fail_for_doesnotreply_dot_brandbil_dot_dk():
    validation = valis.Validation("ping", "doesnotreply.brandbil.dk")
    assert validation.destination == "doesnotreply.brandbil.dk"
    assert validation.returncode == 68 or 2 or 1
    # Ping return codes for non-replying domain name are different for different OSes:
    # 68 on OSX, 1 on linux, 2 on FreeBSD


def test_tcp_validation_nothing():
    validation = valis.Validation("tcp", "", 22)
    assert validation.destination == ""
    assert validation.returncode == 1


def test_tcp_validation_brandbil_dot_dk():
    validation = valis.Validation("tcp", "brandbil.dk", 22)
    assert validation.destination == "brandbil.dk"
    assert validation.returncode == 0


def test_tcp_validation_should_fail_for_doesnotexist_dot_brandbil_dot_dk():
    validation = valis.Validation("tcp", "doesnotexist.brandbil.dk", 22)
    assert validation.destination == "doesnotexist.brandbil.dk"
    assert validation.returncode != 0
