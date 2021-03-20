from .encoding import decode


class ProxyidMixin:
    """Injects Proxyid functionality into CBVs"""

    def get_object(self):
        """Get the object by decoding the url given pk"""
        proxied_id = self.kwargs.get('pk', None)
        if proxied_id is not None:
            self.kwargs['pk'] = decode(proxied_id)
        return super().get_object()
