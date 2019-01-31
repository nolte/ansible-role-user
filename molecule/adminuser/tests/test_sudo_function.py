import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user_can_do_sudo(host):
    with host.sudo():
        with host.sudo("parkerpeater"):
            host.check_output("whoami")
            with host.sudo("root"):
                assert True
