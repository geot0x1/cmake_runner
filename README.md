# Cmake Runner script
Τρέχει cmake commands στο host PC.

## Installation cmake_runner
1. Clone or copy this project on your local machine.
2. Add the installation path to your `PATH` variables
3. Create `cmake_runner_settings.yaml`
5. Done

## Cmake runner settings
Το `cmake_runner` script χρειάζεται ένα αρχείο όπου κρατάμε τα user settings.  
Αυτό το αρχείο πρέπει να βρίσκεται στο ίδιο path με το `cmake_runner.py` και πρέπει να έχει όνομα `cmake_runner_settings.yaml`.
Παρακάτω φαίνεται ένα παράδειγμα τέτοιου αρχείου
```yaml
# cmake-generator: MinGW Makefiles
cmake-generator: Ninja
```
Στην τρέχουσα έκδοση υποστηρίζονται μόνο τα variables που φαίνονται στο παράδειγμα.

## Project variants example
Κάθε project πρέπει να έχει τουλάχιστον ένα project variant.  
Τα project variants δηλώνονται σε ένα αρχείο με το όνομα `project-variants.yaml`
Παρακάτω φαίνεται ένα παράδειγμα αυτού του αρχείου

```yaml
transmitter-ver1-debug:
  shortName: "Tx V1"
  longName: "Build transmitter Ver1 for debugging"
  buildType: Debug
  description: "Transmitter Ver1 debug"
  settings:
    BSP: BUSYRF_V1
    MCU: NRF52810_XXAA
    PROJECT_DIR: transmitter
    FLASH_ADDR: '0x0'

transmitter-ver1-release:
  shortName: "Tx V1"
  longName: "Build transmitter Ver1 for debugging"
  buildType: Release
  description: "Transmitter Ver1 Release"
  settings:
    BSP: BUSYRF_V1
    MCU: NRF52810_XXAA
    PROJECT_DIR: transmitter
    FLASH_ADDR: '0x0'

transmitter-ver3-debug:
  shortName: "Tx V3"
  longName: "Build transmitter Ver3 for debugging"
  buildType: Debug
  description: "Transmitter Ver3 debug"
  settings:
    BSP: BUSYRF_V3
    MCU: NRF52810_XXAA
    PROJECT_DIR: transmitter
    FLASH_ADDR: '0x0'

transmitter-ver3-release:
  shortName: "Tx V3"
  longName: "Build transmitter Ver3 for release"
  buildType: Release
  description: "Transmitter Ver3 Release"
  settings:
    BSP: BUSYRF_V3
    MCU: NRF52810_XXAA
    PROJECT_DIR: transmitter
    FLASH_ADDR: '0x0'

receiver-ver1-debug:
  shortName: "Rx V1"
  longName: "Build receiver Ver1 for debug"
  buildType: Debug
  description: "Receiver board Ver1 debug"
  settings:
    BSP: BUSYRF_V1
    MCU: NRF52810_XXAA
    PROJECT_DIR: receiver
    FLASH_ADDR: '0x0'

receiver-ver1-release:
  shortName: "Rx V1"
  longName: "Build receiver Ver1 for release"
  buildType: Release
  description: "Receiver board Ver1 release"
  settings:
    BSP: BUSYRF_V1
    MCU: NRF52810_XXAA
    PROJECT_DIR: receiver
    FLASH_ADDR: '0x0'

receiver-ver3-debug:
  shortName: "Rx V3"
  longName: "Build receiver Ver3 for debug"
  buildType: Debug
  description: "Receiver board Ver3 debug"
  settings:
    BSP: BUSYRF_V3
    MCU: NRF52810_XXAA
    PROJECT_DIR: receiver
    FLASH_ADDR: '0x0'

receiver-ver3-release:
  shortName: "Rx V3"
  longName: "Build receiver Ver3 for release"
  buildType: Release
  description: "Receiver board Ver3 release"
  settings:
    BSP: BUSYRF_V3
    MCU: NRF52810_XXAA
    PROJECT_DIR: receiver
    FLASH_ADDR: '0x0'
```
