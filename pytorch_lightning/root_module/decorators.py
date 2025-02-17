
def data_loader(fn):
    """
    Decorator to make any fx with this use the lazy property
    :param fn:
    :return:
    """

    attr_name = '_lazy_' + fn.__name__

    @property
    def _data_loader(self):
        try:
            value = getattr(self, attr_name)
        except AttributeError:
            try:
                value = fn(self)  # Lazy evaluation, done only once.
            except AttributeError as e:
                # Guard against AttributeError suppression. (Issue #142)
                raise RuntimeError('An AttributeError was encountered: ' + str(e)) from e
            setattr(self, attr_name, value)  # Memoize evaluation.
        return value

    return _data_loader
