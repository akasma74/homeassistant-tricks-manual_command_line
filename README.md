# Home Assistant tricks: manually updated sensor
How to make ANY Entity-based sensor updatable only upon request (standard `command_line` integration as an example)

If you want to stop HA from updating state of your Entity-based sensor (anything that accepts `scan_interval` configuration variable) so you can update it when you need by calling `homeassistant.update_entity`, it's possible using monkey patching and custom integrations.

You will need to:
1. install the custom integration (`manual_command_line` in this example) by copying [this](custom_components/) folder into your `<HA configfolder>/custom_components/`
2. add the custom integration's domain `manual_command_line:` to your `configuration.yaml` (as shown [here](configuration.yaml))
3. declare your sensor [as usual](command_line.yaml)

That's it.

To use it with another standard (let's say template `sensor`) integration you need to:
1. rename the custom's integration folder to something unique in HA integrations (`my_silent_sensor`)
2. in [manifest.json](custom_components/manual_command_line/manifest.json) set `domain` to that value (`my_silent_sensor`)
3. in [manifest.json](custom_components/manual_command_line/manifest.json) change `after_dependencies` to your standard integration's domain (`sensor`)
4. in [`__init__.py`](custom_components/manual_command_line/__init__.py) change `DOMAIN` as per p.2
5. in [`__init__.py`](custom_components/manual_command_line/__init__.py) change `import homeassistant.components.command_line.sensor` to `import homeassistant.components.template.sensor`
6. in [`configuration.yaml`](configuration.yaml) change `manual_command_line:` as per p.2 (`my_silent_sensor:`)
7. declare your standard sensor as usual
```yaml
sensor:
  - platform: template`
```
8. save changes and restart Home Assistant
