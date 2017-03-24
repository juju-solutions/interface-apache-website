# Overview

This interface layer handles the communication between the Apache2 charm
and a subordinate wishing to enable a website.

# Usage

## Requires

This is the side of the interface that a subordinate charm uses to inform
the Apache2 charm that it wishes to enable a website.

The interface layer sets the following states for the extension to react to:

  * `{relation_name}.available`: The extension has been related to Apache2
  and is ready to have the website data sent.

  The client can send website information to Apache2 using the methods:

  * `send_domain` - The fully-qualified domain name of the site.
  * `send_enabled` - Must be set to 'true' when the web site is ready to be used.
  * `send_site_config` - A vhost configuration block.
  * `send_site_modules` - A list of modules required by the site. If any of these
    appear in disable_modules, the site will not be enabled. Otherwise, any
    required modules will be loaded.
  * `send_ports` - A space-separated list of ports that the site uses.


# Resources

- [Juju mailing list](https://lists.ubuntu.com/mailman/listinfo/juju)
- [Juju community](https://jujucharms.com/community)
