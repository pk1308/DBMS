#  Summary of Lecture 11.5.pdf 
**Summary**
**Module 55: Backup & Recovery/5: Backup/2: RAID**

**Objectives**

* Understanding RAID: Array of redundant disks in parallel to enhance speed and reliability

**Outline**

* RAID
* Reliability via redundancy
    * Mirroring
    * Striping
    * Parity
* RAID 0
* RAID 1
* RAID 2
* RAID 3
* RAID 4
* RAID 5
* RAID 6
* Hybrid RAID
    * RAID 01
    * RAID 10
* Choice of RAID
* Comparison
* Module Summary

**RAID: Redundant Array of Independent Disks**

* RAID: Redundant Array of Independent Disks
* Disk organization techniques that manage a large number of disks, providing a view of
    * A single disk of high capacity and high speed by using multiple disks in parallel,
    * High reliability by storing data redundantly, so that data can be recovered even if a disk fails

**Improvement of Reliability via Redundancy: Mirroring**

* Redundancy: Store extra information that can be used to rebuild information lost in a disk failure
* Mirroring (or shadowing)
    * Duplicate every disk. Logical disk consists of two physical disks.
    * Every write is carried out on both disks. Reads can take place from either disk
    * If one disk in a pair fails, data still available in the other
    * Data loss would occur only if a disk fails, and its mirror disk also fails before the system is repaired
    
**Improvement of Reliability via Redundancy (2): Striping**

* Bit-level Striping: Split the bits of each byte across multiple disks
    * In an array of eight disks, write bit i of each byte to disk i
    * Each access can read data at eight times the rate of a single disk
    * But seek/access time worse than for a single disk
    * Bit level striping is not used much anymore
* Byte-level Striping: Each file is split up into parts one byte in size. Using n = 4 disk array as an example
    * The 1st byte would be written to the 1st drive
    * The 2nd byte to the 2nd drive and so on, until
    * The 5th byte is then written to the 1st drive again and the whole process starts over
    * The nth byte is then written to the (((i − 1) mod n) + 1)th drive
* Block-level Striping: With n disks, block i of a file goes to disk (i mod n) + 1
    * Requests for different blocks can run in parallel if the blocks reside on different disks
    * A request for a long sequence of blocks can utilize all disks in parallel

**Improvement of Reliability via Redundancy (3): Parity**

* Bit-Interleaved Parity: A single parity bit is enough for error correction, not just detection, since we know which disk has failed
    * When writing data, corresponding parity bits must also be computed and written to a parity bit disk
    * To recover data in a damaged disk, compute XOR of bits from other disks (including parity bit disk)
* Block-Interleaved Parity: Uses block-level striping, and keeps a parity block on a separate disk for corresponding blocks from n other disks
    * When writing data block, corresponding block of parity bits must also be computed and written to parity disk
    * To find value of a damaged block, compute XOR of bits from corresponding blocks (including parity block) from other disks

**Standard RAID Levels**

* RAID levels are standardized by the Storage Networking Industry Association (SNIA) in the Common RAID Disk Drive Format (DDF) standard
* The most common types are RAID 0 (striping), RAID 1 (mirroring) and its variants, RAID 5 (distributed parity), and RAID 6 (dual parity)

**RAID 0: Striping**

* RAID level-0 only uses data striping, no redundant information is maintained
* If one disk fails, then all data in the disk array is lost
* Independent of the number of data disks, the effective space utilization for a RAID Level-0 system is always 100 percent
* RAID Level-0 has the best write performance of all RAID levels because the absence of redundant information implies that no redundant information needs to be updated.
* This solution is the least costly
* Reliability is very poor

**RAID 1: Mirroring**

* RAID 1 employs mirroring, maintaining two identical copies of the data on two different disks
* It is the most expensive solution
* It provides excellent fault tolerance
* Every write of a disk block involves a write on both disks
* With two copies of each block exist on different disks, we can distribute reads between the two disks and allow parallel reads
* RAID Level-1 does not stripe the data over different disks. Thus the transfer rate for a single request is comparable to the transfer rate of a single disk
* The effective space utilization is 50 percent, independent of the number of data disks

**RAID 2: Parity**

* RAID 2 uses designated drive for parity information
* In RAID 2, the striping unit is a single bit
* Hamming Code is used for parity
    * Hamming codes can detect up to two-bit errors or correct one-bit errors
    * For a 4-bit data, 3 bits are added
    * Simple parity code cannot correct errors, and can detect only an odd number of bits in error
* In a disk array with D data disks, the smallest unit of transfer for a read is a set of D blocks. It is so because each bit of the data is stored in different blocks of D disks subsequently (Bit-level striping)
* Writing a block involves reading D blocks into main memory, modifying D + C blocks, and writing D + C blocks to disk, where C is the number of check disks. This sequence of steps is called a read-modify-write cycle

**RAID 3: Byte Striping + Parity**

* RAID 3 has a single check disk with parity information. Thus, the reliability overhead for RAID 3 is a single disk, the lowest overhead possible
* RAID 3 consists of byte-level striping with dedicated parity. Therefore the data transfer rate of this level is high because data can be accessed in parallel
* RAID-3 cannot service multiple requests simultaneously: This is so because any single block of data will be spread across all members of the set and will reside in the same physical location on each disk and thus every single I/O request has to be addressed by working on every disk in the array

**RAID 4: Block Striping + Parity**

* RAID 4 has a striping unit of a disk block instead of a single bit, as in RAID 3
* Read requests of the size of a disk block can be served entirely by the disk where the requested block resides therefore RAID 4 provides good performance for data reads
* Provides recovery of corrupted or lost data using XOR recovery mechanism
* If a disk experiences a failure, recovery can be made by simply XORing all the remaining data bits and the parity bit
* Facilitates recovery of at most 1 disk failure. At this level, if more than one disk fails, then there is no way to recover the data
* Write performance is low due to the need to write all parity data to a single disk

**RAID 5: Distributed Parity**

* RAID 5 improves upon RAID 4 by distributing the parity blocks uniformly over all disks instead of storing them on a single check disk
* Several write requests can potentially be processed in parallel since the bottleneck of a unique check disk has been eliminated
* Read requests have a higher level of parallelism. Since the data is distributed over all disks, read requests involve all disks, whereas, in systems with a dedicated check disk, the check disk never participates in reads
* This level too allows recovery of only 1 disk failure like level 4

**RAID 6: Dual Parity**

* RAID 6 extends RAID 5 by adding another parity block, thus it uses block-level striping with two parity blocks distributed across all member disks
* Write performance of RAID 6 is poorer than RAID 5 because of the increased complexity of parity calculation
* RAID 6 use Reed-Solomon Codes to recover from up to two simultaneous disk failures. Therefore it can handle a disk failure during recovery of a failed disk

**Hybrid RAID: Nested RAID levels**

* Nested RAID levels (Hybrid RAID), combine two or more of the standard RAID levels to gain performance, additional redundancy or both, as a result of combining properties of different standard RAID layouts.
* Nested RAID levels are usually numbered using a series of numbers
    * The first number in the numeric designation denotes the lowest RAID level in the ”stack”, while
    * The rightmost one denotes the highest layered RAID level
* For example, RAID 50 layers the data striping of RAID 0 on top of the distributed parity of RAID 5
* Nested RAID levels include RAID 01, RAID 10, RAID 100, RAID 50 and RAID 60, which all combine data striping with other RAID techniques
* As a result of the layering scheme, RAID 01 and RAID 10 represent significantly different nested RAID levels

**RAID 01 (RAID 0+1): Mirror of Stripes**

* RAID 01 is a mirror of stripes
* It achieves both replication and sharing of data between disks
* The usable capacity of a RAID 01 array is the same as in a RAID 1 array made of the same
