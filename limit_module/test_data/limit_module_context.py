
class LimitModuleContext:
    limits = None

    def __init__(self, product_id: str, iabs_id: str, limit_types: list):
        self.product_id = product_id
        self.iabs_id = iabs_id
        self.limit_types = limit_types
