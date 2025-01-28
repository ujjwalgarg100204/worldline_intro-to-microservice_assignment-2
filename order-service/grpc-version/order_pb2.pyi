from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrderRequest(_message.Message):
    __slots__ = ("customer_id", "items")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    items: _containers.RepeatedCompositeFieldContainer[OrderItem]
    def __init__(self, customer_id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[OrderItem, _Mapping]]] = ...) -> None: ...

class CreateOrderResponse(_message.Message):
    __slots__ = ("order_id",)
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class GetOrderRequest(_message.Message):
    __slots__ = ("order_id",)
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class GetOrderResponse(_message.Message):
    __slots__ = ("order_id", "status", "items")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    status: str
    items: _containers.RepeatedCompositeFieldContainer[OrderItem]
    def __init__(self, order_id: _Optional[str] = ..., status: _Optional[str] = ..., items: _Optional[_Iterable[_Union[OrderItem, _Mapping]]] = ...) -> None: ...

class UpdateOrderStatusRequest(_message.Message):
    __slots__ = ("order_id", "new_status")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    new_status: str
    def __init__(self, order_id: _Optional[str] = ..., new_status: _Optional[str] = ...) -> None: ...

class UpdateOrderStatusResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class OrderItem(_message.Message):
    __slots__ = ("product_id", "quantity", "price")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    quantity: int
    price: float
    def __init__(self, product_id: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ...) -> None: ...
