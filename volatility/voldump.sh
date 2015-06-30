#!/bin/bash
#############################################
# voldump is a script that dumps vms and it is preparing commands with profile name
#############################################


for vm in $(vboxmanage list runningvms|awk '{print $1}'|sed -e 's/"//g'); do
    echo -e "\n Dumping $vm..."
    imageinfo=$(vol.py -f "$vm.elf" imageinfo|grep "Suggested Profile"|awk '{print $4}'|sed -e 's/,//g');
    echo -e "Image - $vm\n--------------------\n";
    echo "vol.py -f $vm.elf --profile=$imageinfo pslist"
done;

