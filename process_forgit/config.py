logfile='alpha_board_router_stats.txt'

process_lis=['hostapd -g', 'wpa_supplicant -g', 'check_fw','dal_cb_handler','check_ra','guster/guster -c guster.yaml -c ','/opt/xagent/xagent -w -d --log_debug --ca_file /opt/',
'/opt/xagent/xagent -w -d --log_debug --ca_file /opt/','d2 -w XagentCtrl.xcenv','/upagent --log_debug --log_file /','./aws_json','/hyd-lan.conf -P 7777 -cfg80','/hostapd-wifi2 -P /',
'/dalh --log_debug --log_file /','/bst_daemon --log_debug --log_file /','/bdcrashd -start -no-detach','/bdsetter -start -no-detach -sav','/bdexchanged -start -no-detach',
'/bdcloudd -start -no-detach','/bdboxsettings -start -no-detach','/bddevicediscovery -start -no-de','/bdbrokerd -start -no-detach','/bdvad -start -no-detach',
'/bdgusterupdd -start -no-detach','/bdgusterd -start -no-detach','/bdheartbeatd -start -no-detach','dal_ash --log_debug --log_file /','/bdpush -c /','hyd-guest.conf',
'/bdavahi -scan -interfaces=br-la','/bdupnp -scan -ifname=br-lan','/bdleases','/guster/gusterupd -r /','/wsplcd-lan.conf    -cfg8021','/wsplcd-guest.conf  -cfg8021']

vsz_start="root@RBR750:/# ps"
vsz_end="root@RBR750:/#"
