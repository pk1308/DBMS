#  Summary of Lecture 11.1.pdf 
**Summary**
**Backup and Recovery**

**Definition**

* **Backup:** A copy of data or a system that can be used to restore the original in case of loss.
* **Recovery:** The process of restoring a system or data from a backup.

**Why Backup?**

* Disaster recovery (e.g., hardware failure, malware attack, environmental disaster)
* Client-side changes (e.g., application modifications, database schema updates)
* Auditing (e.g., regulatory compliance, legal discovery)
* Downtime reduction

**Backup Types**

* Business data: Personal information, client data, financial data
* System data: Configuration files, logs, software dependencies
* Media files: Images, videos, audio

**Backup Strategies**

**Full Backup**

* Backs up everything: data, logs, configuration files
* Can restore after any failure
* Requires the most time and storage space
* Generally performed once a week

**Incremental Backup**

* Backs up only the changes since the last backup
* Requires less time and storage space than full backup
* Requires the full backup to restore the database
* Generally performed daily

**Differential Backup**

* Backs up all changes since the most recent full backup
* Requires less time and storage space than full backup
* Also requires the full backup to restore the database
* Generally performed weekly

**Example: Monthly Backup Schedule**

* Full backup: First of the month
* Differential backup: Start of each week
* Incremental backup: Daily

**Hot Backup**

* Performed while the database is running
* Maintains high availability
* Requires specialized tools and may be more expensive
* Suitable for highly dynamic and critical systems

**Transactional Logging**

* Records all transactions in a sequence
* Used for recovery after system failures
* Provides point-in-time recovery
* Can be used as a hot backup for transaction logs

**Module Summary**

* Key concepts: Backup, recovery, full backup, incremental backup, differential backup, hot backup, transactional logging
* Importance of having a backup strategy
* Analysis of different backup strategies and schedules
* Role of transactional logging in recovery
