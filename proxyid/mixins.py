from .encoding import decode


class ProxyidMixin:
    """Injects Proxyid object retrieve into CBVs"""

    proxyid_url_kwarg = "pk"

    def get_object(self):
        """Get the object by decoding the url given arg"""

        proxied_id = self.kwargs.get(self.proxyid_url_kwarg, None)
        if proxied_id is not None:
            self.kwargs["pk"] = decode(proxied_id)
        return super().get_object()
