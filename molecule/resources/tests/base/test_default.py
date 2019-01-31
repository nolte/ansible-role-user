import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_user_created_file(host):
    f = host.file('/home/parkerpeater')

    assert f.exists
    assert f.is_directory
    assert f.user == 'parkerpeater'
    assert f.group == 'parkerpeater'
