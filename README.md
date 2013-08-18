fluo
====

Tool to make graphs out of psad CSV output together with psad and the GraphViz package

How to use
==========

psad --CSV -CSV-fields "src dst dp" -m /var/log/iptables | fluo.py | neato -Tgif -o output.gif

There is no way to filter data, nor do I plan on adding one.
You can simply harness the power of grep to do so, like this.

psad --CSV -CSV-fields "src dst dp proto" -m /var/log/iptables | grep -v icmp | fluo.py | neato -Tgif -o output.gif

This excludes ICMP traffic
