#  Summary of Lecture 8.4 - Storage and File Structure1.pdf 
**Summary**
**Introduction**

Physical storage media provides high-volume, fast, reliable, and inexpensive options for data storage for databases. Tertiary storage options are available for high-volume, inexpensive backup.

**Physical Storage Media**

Physical storage media can be classified based on:

* **Speed:** How quickly data can be accessed.
* **Cost:** Cost per unit of data.
* **Reliability:** Data loss potential on power failure or system crash.
* **Volatility:** Whether contents persist even when power is switched off.

**Types of Physical Storage Media**

**1. Cache**

* Fastest and most costly form of storage.
* Volatile.
* Managed by the computer system hardware.

**2. Main Memory**

* Fast access (nanoseconds).
* Generally too small to store the entire database.
* Volatile.

**3. Flash Memory**

* Data survives power failure.
* Data can be written at a location only once, but location can be erased and written to again.
* Reads are roughly as fast as main memory.
* Writes are slow, erase is slower.

**4. Magnetic Disk**

* Data is stored on spinning disk and read/written magnetically.
* Primary medium for long-term storage of data.
* Slower access than main memory.
* Direct-access: possible to read data on disk in any order.

**5. Optical Storage**

* Non-volatile, data is read optically from a spinning disk using a laser.
* CD-ROM and DVD most popular forms.
* Blu-ray disks: larger capacity.
* Reads and writes are slower than with magnetic disk.

**6. Tape Storage**

* Non-volatile, used primarily for backup and archival data.
* Sequential-access: much slower than disk.
* Very high capacity.
* Tape jukeboxes provide massive storage capacities.

**Storage Hierarchy**

Storage media can be organized into a hierarchy based on performance and cost:

* **Primary Storage:** Cache, main memory, flash memory.
* **Secondary Storage:** Magnetic disk.
* **Tertiary Storage:** Magnetic tape.

**Magnetic Disks**

Magnetic disks are the primary medium for long-term storage of data in databases.

**Disk Mechanism**

* Read-write head: Reads or writes magnetically encoded information.
* Surface divided into circular tracks.
* Each track is divided into sectors (smallest unit of data read or written).
* To read/write a sector, head moves to right track and platter spins.

**Magnetic Disk Performance Measures**

* **Access Time:** Time to start data transfer.
* **Data-Transfer Rate:** Rate at which data can be retrieved or stored.
* **Mean Time To Failure (MTTF):** Average time disk is expected to run continuously without failure.

**Magnetic Tapes**

Magnetic tapes hold large volumes of data and provide high transfer rates.

* Capacity: Few GB to 330 GB
* Transfer rates: Few to 10's of MB/s
* Cheap, but tape drives are expensive.
* Limited to sequential access.

**Cloud Storage**

Cloud storage is purchased from a third-party cloud vendor who manages capacity, security, and durability.

* Accessed via traditional storage protocols or API.
* Scalable and flexible.
* Cost-effective for large storage requirements.

**Other Storage**

* **Optical Disk:** CD-ROM, DVD, Blu-ray.
* **Flash Drives:** Removable and rewritable storage devices.
* **SD Cards:** Secure Digital cards, used in mobile devices.

**Future of Storage**

* **DNA Digital Storage:** High storage density and stability.
* **Quantum Memory:** Quantum-mechanical version of ordinary memory.

**Summary**

* Physical Storage Media provides various options for data storage based on speed, cost, reliability, and volatility.
* Magnetic Disks are the primary medium for long-term storage.
* Magnetic Tapes offer high-volume, inexpensive backup.
* Cloud Storage offers scalable and cost-effective storage.
* Future storage technologies, such as DNA Digital Storage and Quantum Memory, have potential for even greater storage capacity and performance.
