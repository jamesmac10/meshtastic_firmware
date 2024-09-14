#pragma once
#ifndef _BMA423_SENSOR_H_
#define _BMA423_SENSOR_H_

#include "MotionSensor.h"

#if !defined(ARCH_PORTDUINO) && !defined(ARCH_STM32WL) && !MESHTASTIC_EXCLUDE_ENVIRONMENTAL_SENSOR

#include <SensorBMA423.hpp>
#include <Wire.h>

class BMA423Sensor : public MotionSensor
{
  private:
    SensorBMA423 sensor;
    volatile bool BMA_IRQ = false;

  public:
    BMA423Sensor(ScanI2C::DeviceAddress address);
    virtual bool init() override;
    virtual int32_t runOnce() override;
};

#endif

#endif