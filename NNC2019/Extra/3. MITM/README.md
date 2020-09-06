# MITM 

To successfully implement MITM attack we have to:

* route/intercept traffic from/to badge;
* somehow deal with built-in CA certificates check;
* seamlessly decode SSL/TLS traffic using our self-signed certificate.

## Part 1: [route traffic from badge](part1/README.md)
This task is quite easy due to we have full physical access to device and able to edit it's firmware.

## Part 2: [certificates](part2/README.md)
Here is we have to modify firmware in such way that badge is able to communicate with target Techmaker accepting non Techmamer's CA certificates.

