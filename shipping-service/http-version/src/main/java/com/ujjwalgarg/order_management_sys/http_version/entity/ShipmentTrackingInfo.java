package com.ujjwalgarg.order_management_sys.http_version.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class ShipmentTrackingInfo {

  private String status;
  private String estimatedDeliveryDate;
}
