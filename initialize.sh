#!/bin/bash
cd /data/data/com.termux/files
mkdir .recovery
cd .recovery
touch script1.sh
echo "#!/bin/bash" > script1.sh
echo "sudo reboot" >> script1.sh
touch script2.sh
echo "#!/bin/bash" > script2.sh
echo "sudo stop" >> script2.sh
chmod 777 *
cd -
echo "Recovery has been initialized"
