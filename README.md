# Colored Logging

```
pip install logcolor
```

Hit the ground running:

```python
import logcolor, logging
logcolor.basic_config()
logging.root.info('woho!')
```

More usefully:

```python
logcfg = logcolor.default_config()

if verbose:
    logcfg['handlers']['console']['level'] = 'DEBUG'
    logcfg['root']['level'] = 'DEBUG'

logcolor.dict_config(logcfg)

logging.root.info('woho!')
```
