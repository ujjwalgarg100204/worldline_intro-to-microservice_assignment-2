package com.ujjwalgarg.order_management_sys.http_version.db;

import com.ujjwalgarg.order_management_sys.http_version.entity.DeliverySchedule;
import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Component;

@Component
public class ScheduledDeliveriesManager {
  private final Map<String, DeliverySchedule> deliveryScheduleDB = new HashMap<>();

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
