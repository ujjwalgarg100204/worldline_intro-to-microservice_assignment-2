package com.ujjwalgarg.order_management_sys.grpc_version.db;

import com.ujjwalgarg.order_management_sys.grpc_version.entity.DeliverySchedule;
import jakarta.annotation.PostConstruct;
import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Component;

@Component
public class ScheduledDeliveriesManager {

  private final Map<String, DeliverySchedule> deliveryScheduleDB = new HashMap<>();

  @PostConstruct
  public void init() {
    deliveryScheduleDB.put("44de4ac1-a058-4f94-aa35-9ebfbfc429d7",
        new DeliverySchedule("44de4ac1-a058-4f94-aa35-9ebfbfc429d7", "2023-10-01"));
    deliveryScheduleDB.put("192d589d-b98e-496b-acea-5314fff02e7a",
        new DeliverySchedule("192d589d-b98e-496b-acea-5314fff02e7a", "2023-10-05"));
    deliveryScheduleDB.put("f68c403e-3beb-4bc4-a2a4-32a48225a054",
        new DeliverySchedule("f68c403e-3beb-4bc4-a2a4-32a48225a054", "2023-10-10"));
  }

  public void saveDeliverySchedule(String orderId, DeliverySchedule schedule) {
    deliveryScheduleDB.put(orderId, schedule);
  }

  public DeliverySchedule getDeliverySchedule(String orderId) {
    return deliveryScheduleDB.get(orderId);
  }

  public boolean orderIdExists(String orderId) {
    return deliveryScheduleDB.containsKey(orderId);
  }
}
