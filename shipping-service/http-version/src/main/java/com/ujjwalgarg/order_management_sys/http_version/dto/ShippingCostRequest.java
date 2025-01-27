package com.ujjwalgarg.order_management_sys.http_version.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ShippingCostRequest {
  private float weight;
  private String shippingMethod;
}
