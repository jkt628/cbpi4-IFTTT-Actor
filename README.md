# cbpi4-IFTTT-Actor

Control equipment with IFTTT Maker Event trigger webhook.

## Switches

Switches generally expect separate `on` and `off` events.  Configure the Actor with `%s` in the name
which will get `on` or `off` as appropriate,
_e.g._, `turn_%s_cooler` for `turn_on_cooler` or `turn_off_cooler` respectively.

## Dimmers or other proportional controllers

Single webhooks, _i.e._, lacking `%s`, receive a JSON payload with `power` from 0 to 100, inclusive.

Turn off:

```javascript
{ "power": 0 }
```

## Configuration

Retrieve your IFTTT Key at <https://ifttt.com/maker_webhooks/settings>.

Create one or two applets at <https://ifttt.com/create> based on the discussion above.

* `If This`, click __Add__
* Search __webhooks__, click __Webhooks__
* Determine `with a JSON payload` based the discussion above, click __Receive a web request...__
* Determine __Event Name__ based the discussion above, click __Create trigger__
* `Then That`, click __Add__ and connect to your equipment.

Create an Actor with Type __IFTTT-Actor__ and  __Name__ based on the discussion above.
