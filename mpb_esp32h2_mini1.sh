#!/bin/bash

export PATH="$HOME/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

echo "=========================================================="
echo "Setting up for esp32 build"
echo "Using esp-idf-551"
export IDF_PATH="$HOME/disk/esp/esp-idf-551"
echo "MCU type esp32h2"
export IDF_TARGET="esp32h2"
source $IDF_PATH/export.sh

# clean-up last build
rm -rf build-ESP32_H2_STD

cp esp32_common.cmake-STD-H2 esp32_common.cmake
cp mpconfigport.h-STD-H2 mpconfigport.h
cp machine_adc.c-STD-H2 machine_adc.c
cp machine_pin.h-STD-H2 machine_pin.h
# ESP32-H2
make BOARD=ESP32_H2_STD
# restore files
cp machine_pin.h-ORIG machine_pin.h
cp machine_adc.c-ORIG machine_adc.c
cp esp32_common.cmake-ORIG esp32_common.cmake
cp mpconfigport.h-ORIG mpconfigport.h

echo "=========================================================="

