# Colored Logging

For example:

    logcfg = logcolor.default_config()

    if verbose:
        logcfg['handlers']['console']['level'] = 'DEBUG'
        logcfg['root']['level'] = 'DEBUG'

    logcolor.dict_config(logcfg)

    logging.root.info('woho!')
