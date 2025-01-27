package com.ujjwalgarg.order_management_sys.http_version.db;

import com.ujjwalgarg.order_management_sys.http_version.entity.ShipmentTrackingInfo;
import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Component;

@Component
public class TrackingInfoManager {
  private final Map<String, ShipmentTrackingInfo> trackingInfoDB = new HashMap<>();

  public void saveTrackingInfo(String trackingId, ShipmentTrackingInfo info) {
    trackingInfoDB.put(trackingId, info);
  }

  public ShipmentTrackingInfo getTrackingInfo(String trackingId) {
    return trackingInfoDB.get(trackingId);
  }

  public boolean trackingIdExists(String trackingId) {
    return trackingInfoDB.containsKey(trackingId);
  }
}
