package com.ujjwalgarg.order_management_sys.grpc_version.db;

import com.ujjwalgarg.order_management_sys.grpc_version.entity.ShipmentTrackingInfo;
import jakarta.annotation.PostConstruct;
import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Component;

@Component
public class TrackingInfoManager {
  private final Map<String, ShipmentTrackingInfo> trackingInfoDB = new HashMap<>();

  @PostConstruct
  public void init() {
    trackingInfoDB.put("track1", new ShipmentTrackingInfo("DELIVERED",  "2023-10-01"));
    trackingInfoDB.put("track2", new ShipmentTrackingInfo("IN_TRANSIT",  "2023-10-05"));
    trackingInfoDB.put("track3", new ShipmentTrackingInfo("OUT_FOR_DELIVERY",  "2023-10-10"));
  }

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
