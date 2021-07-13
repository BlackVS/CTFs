# Some theory

How signals are sent ?

Here is some trick.

Few constants are defined both on server and cleint side:
- server port base (10000 by default)
- bandwidth per port (1M by default)
- name of tag value for sample rate ('rx_rate')
In such case to "send" signal on 400M it will be sent via port:

= 10000 + ( 400M / 1M ) = 10400

and in sent stream periodically will be inserted tag value "rx_rate" with sample rate value (due to actually data sent via Internet with different from sample rate speed)


GNU Radio has special ZeroMQ blocks to deal with such streams.

But creators of official ctf-tools created special **RF Over IP Source** block which installed during make command.

rx_to_fifo uses this block - it is very simple if you wish create your own graphs - just check rx_to_fifo.grc graph.

Or if you wish use directly ZeroMQ blocks - check my rx_simple.grc / rx_file.grc ( https://github.com/BlackVS/cts-utils/ ) - I played with ZeroMQ a little to understand better it.

