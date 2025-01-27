package com.ujjwalgarg.order_management_sys.http_version.controller;

import com.ujjwalgarg.order_management_sys.http_version.db.ScheduledDeliveriesManager;
import com.ujjwalgarg.order_management_sys.http_version.db.TrackingInfoManager;
import com.ujjwalgarg.order_management_sys.http_version.dto.DeliveryRequest;
import com.ujjwalgarg.order_management_sys.http_version.dto.DeliveryResponse;
import com.ujjwalgarg.order_management_sys.http_version.dto.ShippingCostRequest;
import com.ujjwalgarg.order_management_sys.http_version.dto.ShippingCostResponse;
import com.ujjwalgarg.order_management_sys.http_version.dto.TrackShipmentResponse;
import com.ujjwalgarg.order_management_sys.http_version.entity.DeliverySchedule;
import com.ujjwalgarg.order_management_sys.http_version.entity.ShipmentTrackingInfo;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequestMapping("/shipping")
@RequiredArgsConstructor
public class ShippingController {

  private final ScheduledDeliveriesManager deliveriesManager;
  private final TrackingInfoManager trackingInfoManager;

  @PostMapping("/cost")
  public ResponseEntity<?> calculateShippingCost(@RequestBody ShippingCostRequest request) {
    log.info(
        "Calculating shipping cost for method: {}, weight: {}",
        request.getShippingMethod(),
        request.getWeight());
    float baseRate = request.getShippingMethod().equalsIgnoreCase("express") ? 10 : 5;
    float cost = baseRate * request.getWeight();
    log.info("Calculated cost: {}", cost);

    return ResponseEntity.ok(new ShippingCostResponse(true, cost));
  }

  @PostMapping("/schedule")
  public ResponseEntity<?> scheduleDelivery(@RequestBody DeliveryRequest request) {
    log.info(
        "Scheduling delivery for order ID: {}, method: {}",
        request.getOrderId(),
        request.getShippingMethod());
    String deliveryDate =
        request.getShippingMethod().equalsIgnoreCase("express") ? "Tomorrow" : "In 5 days";
    DeliverySchedule schedule = new DeliverySchedule(request.getOrderId(), deliveryDate);

    deliveriesManager.saveDeliverySchedule(request.getOrderId(), schedule);
    log.info("Scheduled delivery date: {}", deliveryDate);

    return ResponseEntity.ok(new DeliveryResponse(true, deliveryDate));
  }

  @GetMapping("/track/{trackingId}")
  public ResponseEntity<?> trackShipment(@PathVariable String trackingId) {
    log.info("Tracking shipment with ID: {}", trackingId);
    if (!trackingInfoManager.trackingIdExists(trackingId)) {
      log.warn("Tracking ID not found: {}", trackingId);
      return ResponseEntity.ok(new TrackShipmentResponse(false, "Tracking ID not found", null));
    }

    ShipmentTrackingInfo info = trackingInfoManager.getTrackingInfo(trackingId);
    log.info(
        "Tracking info - Status: {}, Estimated Delivery Date: {}",
        info.getStatus(),
        info.getEstimatedDeliveryDate());
    return ResponseEntity.ok(
        new TrackShipmentResponse(true, info.getStatus(), info.getEstimatedDeliveryDate()));
  }
}
