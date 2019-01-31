import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user_can_do_sudo(host):
    with host.sudo():
        with host.sudo("parkerpeater"):
            currentUser = host.check_output("whoami")
            assert currentUser == "parkerpeater"
            with host.sudo("root"):
                currentUser = host.check_output("whoami")
                assert currentUser == "root"
