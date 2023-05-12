# Stop-and-Wait-Protocol
The purpose of this assignment is to extend the netster file-transfer behavior so that it supports reliable network communication over UDP. We call this Reliable UDP or RUDP. You already implemented an application protocol over TCP and UDP and you will now have an opportunity to test your existing code over an unreliable network. Once the limitations of UDP over an unreliable channel become clear you should feel motivated to solve the issue at hand with your own RUDP implementation.


Task 1 - Implement alternating bit, stop-and-wait protocol


You will implement a stop-and-wait protocol (i.e. alternating bit protocol), called rdt3.0 in the book and slides.



There are a number of ways to implement this task correctly, but the following tips indicate some necessary and optional features:



1) You must introduce a new RUDP header that encapsulates the application data sent in via rdt_send(). This should include fields to support sequence numbers, message type (ACK, NACK, etc.), and potentially other fields like length.


2) You must use a timer.


3) You must treat any potentially corrupt packets the same as if they were simply lost.


4) You may assume unidirectional data transfer (e.g. client → server).


5) You may make adjust the how often data is sent into your RUDP interface for debugging purposes.


6) You may use both ACK and NACK control messages instead of duplicate ACKs.


7) You may assume only a single client RUDP session at a time.


8) You may assume that UDP handles the checksum error detection for you.
