# Copyright (C) 2021 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

import adi

# Optionally pass URI as command line argument,
# else use default context manager search
my_uri = sys.argv[1] if len(sys.argv) >= 2 else None
print("uri: " + str(my_uri))

# Set up LM75
my_temp_sensr = adi.lm75(uri=my_uri)

print("\nChecking temperature channel...")
print("Temperature raw: " + str(my_temp_sensr.input))
print(
    "Temperature in deg. Celsius: " + str(my_temp_sensr.to_degrees(my_temp_sensr.input))
)

print("\nUpdate interval: " + str(my_temp_sensr.update_interval))


print("\nMax threshold: " + str(my_temp_sensr.to_degrees(my_temp_sensr.max)))
print("Max hysteresis: " + str(my_temp_sensr.to_degrees(my_temp_sensr.max_hyst)))

print("\nSetting max threshold, hyst. to 30C, 25C...\n")

my_temp_sensr.max = my_temp_sensr.to_millidegrees(30.0)
my_temp_sensr.max_hyst = my_temp_sensr.to_millidegrees(25.0)

print("New thresholds:")
print("Max: " + str(my_temp_sensr.to_degrees(my_temp_sensr.max)))
print("Max hysteresis: " + str(my_temp_sensr.to_degrees(my_temp_sensr.max_hyst)))

del my_temp_sensr
