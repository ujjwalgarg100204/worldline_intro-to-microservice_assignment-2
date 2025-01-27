package com.ujjwalgarg.order_management_sys.http_version.dto;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class DeliveryRequest {
  private String orderId;
  private String shippingMethod;
}
