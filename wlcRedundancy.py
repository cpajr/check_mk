#!/usr/bin/env python3

'''
iscoLwappHaMIB MODULE-IDENTITY
    LAST-UPDATED    "201703140000Z"
    ORGANIZATION    "Cisco Systems Inc."
    CONTACT-INFO
            "Cisco Systems,
            Customer Service
            Postal: 170 West Tasman Drive
            San Jose, CA  95134
            USA
            Tel: +1 800 553-NETS

            Email: cs-wnbu-snmp@cisco.com"
    DESCRIPTION
        "This MIB is intended to be implemented on all those
        devices operating as Central controllers, that
        terminate the Light Weight Access Point Protocol
        tunnel from Cisco Light-weight LWAPP Access Points.

        This MIB is used to show and configure High 
        availability (HA) related statistics.

        The relationship between CC and the LWAPP APs
        can be depicted as follows:

          +......+     +......+     +......+          
          +      +     +      +     +      +           
          +  CC  +     +  CC  +     +  CC  +           
          +      +     +      +     +      +           
          +......+     +......+     +......+           
            ..            .             .                 
            ..            .             .                 
           .  .            .             .                 
          .    .            .             .                 
         .      .            .             .                 
        .        .            .             .                 
        +......+ +......+     +......+      +......+          
        +      + +      +     +      +      +      +         
        +  AP  + +  AP  +     +  AP  +      +  AP  +          
        +      + +      +     +      +      +      +          
        +......+ +......+     +......+      +......+          
             .              .             .                 
            .  .              .             .                 
           .    .              .             .                 
          .      .              .             .                 
         .        .              .             .                 
        +......+ +......+     +......+      +......+          
        +      + +      +     +      +      +      +          
        +  MN  + +  MN  +     +  MN  +      +  MN  +          
        +      + +      +     +      +      +      +          
        +......+ +......+     +......+      +......+          


        The LWAPP tunnel exists between the controller and
        the APs.  The MNs communicate with the APs through
        the protocol defined by the 802.11 standard.

        LWAPP APs, upon bootup, discover and join one of the
        controllers and the controller pushes the configuration,
        that includes the WLAN parameters, to the LWAPP APs.
        The APs then encapsulate all the 802.11 frames from
        wireless clients inside LWAPP frames and forward
        the LWAPP frames to the controller.
'''


def inventory_wlcRedundancy(info):
    import cmk.utils.debug
    if cmk.utils.debug.enabled():
        print ("info = ".format(info))

    yield None, None


def check_wlcRedundancy(_no_item, _no_params, info):
    result = int(info[0][0])
    if (result == 1):
        return 0, "OK - Primary operating"
    else:
        return 2, "Critical - Secondary operating"

check_info['wlcRedundancy'] = {
        "inventory_function": inventory_wlcRedundancy,
        "check_function": check_wlcRedundancy,
        "service_description": "Wireless Controller Redundancy",
        "snmp_info": (".1.3.6.1.4.1.9.9.198888.0.1", ["12"]),
}