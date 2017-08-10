apt-get update && apt-get upgrade
#Nanopi:
	apt install linux-kernel-headers git libgmp3-dev gawk qpdf bison flex
#RasPi:
	apt install raspberrypi-kernel-headers git libgmp3-dev gawk qpdf bison flex
git clone https://github.com/seemoo-lab/nexmon.git
cd nexmon
source setup_env.sh
make
cd patches/bcm43438/7_45_41_26/nexmon/
make
make backup-firmware
make install-firmware
