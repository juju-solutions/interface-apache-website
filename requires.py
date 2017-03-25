#!/usr/bin/python
import json
from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class ApacheWebsiteRequires(RelationBase):
    scope = scopes.GLOBAL  # subordinate

    @hook("{requires:apache-website}-relation-{joined}")
    def joined(self):
        """Indicate the relation is connected."""
        self.set_state("{relation_name}.available")

    @hook("{requires:jenkins-extension}-relation-departed")
    def departed(self):
        """Indicate the relation is disconnected."""
        self.remove_state("{relation_name}.available")

    def send_domain(self, domain):
        """
        The fully-qualified domain name of the site.
        """
        self.set_remote(domain=domain)

    def send_enabled(self, enabled=True):
        """
        Must be set to True when the web site is ready to be used.
        """
        self.set_remote(enabled=json.dumps(bool(enabled)))

    def send_site_config(self, site_config):
        """
        A vhost configuration block.
        """
        self.set_remote(site_config=site_config)

    def send_site_modules(self, modules):
        """
        A list of modules required by the site. If any of these appear in
        disable_modules, the site will not be enabled. Otherwise, any required
        modules will be loaded.
        """
        self.set_remote(modules=' '.join(modules))

    def send_ports(self, ports):
        """
        A list of ports that the site uses.
        """
        self.set_remote(ports=' '.join(str(port) for port in ports))
