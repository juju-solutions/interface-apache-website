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
  * `send_enabled` - Must be set to `True` when the web site is ready to be used.
  * `send_site_config` - A vhost configuration block.
  * `send_site_modules` - A list of modules required by the site. If any of these
    appear in disable_modules, the site will not be enabled. Otherwise, any
    required modules will be loaded.
  * `send_ports` - A list of ports that the site uses.

Example usage:

```python
@when('apache-website.available')
def send_website_info(apache):
    apache.send_domain('foo.com')
    apache.send_site_config(textwrap.dedent("""
        # Ensure that Apache listens on port 80
        Listen 80
        <VirtualHost *:80>
            DocumentRoot "/www/example1"
            ServerName www.example.com

            # Other directives here
        </VirtualHost>

        <VirtualHost *:80>
            DocumentRoot "/www/example2"
            ServerName www.example.org

            # Other directives here
        </VirtualHost>"""))
    apache.send_site_modules(['mod_php', 'mod_alias'])
    apache.send_ports([8080])
    apache.send_enabled()
```


# Resources

- [Juju mailing list](https://lists.ubuntu.com/mailman/listinfo/juju)
- [Juju community](https://jujucharms.com/community)
