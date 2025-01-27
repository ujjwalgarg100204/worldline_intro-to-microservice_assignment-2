package com.ujjwalgarg.order_management_sys.grpc_version.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class DeliverySchedule {

  private String orderId;
  private String deliveryDate;
}
