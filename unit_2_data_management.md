Unit 2: DATA MANAGEMENT
=============

<!-- The importance of and techniques for managing large scale on-line and near-line data storage.
Digital images and manipulation techniques. -->

Whether for streaming lossless 4k 32-bit EXRs or reading 500 gigabyte alembic caches, VFX studios require special and expensive infrastructure to enable working efficiently with such large amounts of data. They need to ensure that there is plenty of disk space for data, that there are reliable snapshot backup and archiving systems, that it is all accessible via a speedy network and that it is all protected by a hefty firewall.

Types of Storage
-------------

### Online

This is data that is available to access instantaneously, over a network.

### Nearline

Nearline storage is an intermediate between "online" and "offline" storage. It includes any data that is only online and available to access on request. It is much more power & cost efficient for data to be nearline than online if it is not in constant use, as any disks that aren't currently in use don't have to be constantly spinning. A potential use might be in short-term backups.

### Offline

Offline storage is any data not accessible from a network. This includes any storage on removable media (i.e. USB flash drives, optical discs..) that is not currently connected or mounted on a computer, and that would require some type of intervention to be available. Old or no longer immediately useful data is often archived and taken offline, as explained in the next section.

Backups / Archiving
--------------

Backups are copies of files that are safely stored for use in an event of the live data being lost, infected or corrupted.

This are a vitally important risk-prevention measure for any modern company. In some cases, losing data leads to lost money, from not only the cost of creating that data but also any costs of missing contracted deadlines, not to mention the loss of a client's trust, which is perhaps more valuable. For example, in the context of VFX, a small 3mb Maya scene file would be very cheap to back up, though if it were corrupted, the loss could be a whole weeks work of a talented animator.

Snapshots systems are one method of backing up data. This is when copies of 

<!-- 
Data archiving is the process of moving data that is no longer actively used to a separate storage device for long-term retention. Archive data consists of older data that is still important to the organization and may be needed for future reference, as well as data that must be retained for regulatory compliance. Data archives are indexed and have search capabilities so files and parts of files can be easily located and retrieved.

Data archives are often confused with data backups, which are copies of data. Data backups are used as a data recovery mechanism that can be used to restore data in the event it is corrupted or destroyed. In contrast, data archives protect older information that is not needed for everyday operations but may have to be accessed occasionally. The data archives serve as a way of reducing primary storage consumption and related costs, rather than acting as a data recovery mechanism. Some data archives treat archive data as read-only to protect it from modification, while other data archiving products treat data as read / write. Data archiving is most suitable for data that must be retained due to operational or regulatory requirements, such as document files, email messages and possibly old database records. -->

Data Security
--------------



*statistics are sourced from the 2017 survey published in "New Insights Into the Growing VFX Industry" by postPerspective and Quantum*  