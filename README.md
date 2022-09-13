# valis
valis - network reachability verification engine

This is the braindump I did after I got the initial idea.

TDD-style test button for network reachability from the endpoint point of view.
Tries to answer the question: "Does the network work?" by connecting to what the users and their applications care about.
We don't care if the application works or not, but we care if we can reach the application.
If the application port on the server answers, then the network works.
Yes yes - we can ask for a URL if you really want - in case you have  a web application firewall in there somewhere.

Identified use cases:
- Application connectivity test to define before doing network changes (change routing/switching/firewalling for existing functionality).
	- "If all is green after the change, then the application can see its servers"
	- Cuts down on manual application testing after network changes in organisations sensitive to network changes.
- Application connectivity test to define before doing network changes (add new permission).
	- "I could not connect to this before, but I can now"
-Ongoing and regular "network compliance test"
	- Can this host reach all its applications it needs to? 
	- DNS, AD, log servers, license servers, other application servers, etc
- More granular network test than ICMP and SNMP from central monitoring server to network equipment. 
	- They only give indications that the network works. This will tell you if the network works.
	- "This server can reach that remote server on that specific port" is a lot different from:
		- "If we can ping the switches, then the network and the applications usually works"
- Load it onto a laptop for user application reachability testing instead of manual testing via opening applications, typing stuff etc.
- Run it on a server to immediately see if all my remote services are reachable

Must be lightweight and rely on no external packages. Hping, nmap and the like can not be used as they are often flagged as hacker tools and are typically not allowed to be installed. Only userland features in the OS can be used for base features.
Must be possible to run in stand-alone mode with easily handcrafted config file
Not a performance monitoring tool. Although it could be nice to log response times in a local time series database for visualisation
Not a monitoring system. Although it would be nice with a view with info from all clients/agents in the network with a RAG (Red/Amber/Green) status


Types of tests:
- Network reachability (ping)
- Application reachability (DNS, TCP 3-way, UDP echo for applications that does that)
- Local file with "rules" or things to test
	- transport protocol (IPv4/IPv6)
	- source host (always local machine.  Can be specified to be specific interface or IP, defaults to local hostname)
	- destination IP or hostname
	- destination protocol (TCP/UDP)
	- destination port
	- URL to hit in case of HTTP application
- Outputs in text with pass/fail for all tests
- Option to run all or list of tests
- Let's start out with client for Linux


Future features:
- Clients for Windows and Mac
- Runs as agent/daemon/service
- "Remote client" with tests run over SSH through network equipment (SSH to switch/router and run ping or tcp connect from there)
- SNMP interface to poll for results?
- Syslog reporting
- Test result upload to central reporting station with web gui for visibility of entire infrastructure (or at least the devices with the client)
	 -local rule base
	- results
	- Identification  / adopting of clients
		- Only adopted clients show their results in network view and contributes to "Global Green"
		- Show if there are endpoints missing from the uploads/view

This can be viewed as decentralised firewall rule contribution. If all hosts in the network has a client and has defined all the tests/rules for itself they can be collected and compiled into a full firewall policy. This could happen via the central station with some functionality to identify and approve new tests/rules for the firewall policy. This may be scope creep...
