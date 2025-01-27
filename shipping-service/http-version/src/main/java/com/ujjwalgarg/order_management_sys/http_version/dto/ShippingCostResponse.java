package com.ujjwalgarg.order_management_sys.http_version.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class ShippingCostResponse {
  private boolean success;
  private float cost;
}
