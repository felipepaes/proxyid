# Configuration

Configuration documentation

---


**Proxyid** configuration is pretty straight foward, it depends on a constant named **`PROXYID`** in the Django project **`settings.py`** file.

```python
PROXYID = {
    "hashids": {
        "salt": "A grain of salt", # this is your salt
        "min_length": 14           # this is the minimum length of the proxied id
    }
}
```

The constant **`PROXYID`** is a dictionary with another dictionary **`hashids`** inside. 

* **`hashids`** - A dictionary with the configuration which hashids will use to encode primary keys
* **`salt`** - The salt used to encode the primary keys, don't use project's `SECRET_KEY`, create another one for proxyid. Check [how to generate configuration](#configuration-generator) below
* **`min_length`** - This is the minimum length which the encoded primary key will have, it gives more consistency by avoiding a encoded key like `EQ1w` and then `WaV11dqdQVj78vlw`. The hashids will ensure the encoded keys will always have the `min_lengh` or above length.

## Configuration Generator

**Proxyid** gives a helper utlity to generate a starter configuration.

**`generate_config`** - is a function which generates a configuration.

To use the utility, having proxyid installed in the environment, start a python repl session. You can import it from **`proxyid.utils`** module.

```
$ python
```

```python
Python 3.9.2 (default, Mar 21 2021, 20:35:03)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from proxyid.utils import generate_config
>>> generate_config()

Proxyid configuration generated:
PROXYID = {'hashids': {'salt': 'duJSIrco2d6SIe4BJZnIOZY4lTES6uVQE0KWv202sAA', 'min_length': 14}}

>>> exit()
```

Great! Now just paste it in your **`settings.py`** and make the modifications you wish.

You may want to follow a complete [**tutorial**](/tutorial) or check specific features at the  [**user guide**](/user-guide), like [**class based views**](/user-guide/class-based-views)