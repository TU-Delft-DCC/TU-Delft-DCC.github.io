---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
#date: YYYY-MM-DD

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Data backup

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Raul Ortiz Merino
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Raul Ortiz Merino
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Raul Ortiz Merino

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories: 
 - data
 - backup

---

# Data Backup

An effective system for backing up research data is crucial to the success and reproducibility of any research project. Backups ensure that irreplaceable files are not lost due to hardware failure, accidental deletion, or other unforeseen events. 

A widely recommended strategy for data backup is the 3-2-1 Rule:

- **3 Copies:** Maintain at least three copies of the data. This includes the original working copy and two additional backup copies. 

- **2 Types of Media:** Store these copies on at least two different types of storage media. This prevents the loss of all copies in a single incident (crash, loss, theft). Common media types include internal hard drives, external hard drives, networked drives, and cloud storage. USB drives are generally not recommended for long-term storage due to their susceptibility to loss and corruption, similar conditions might apply to external hard drives. 

- **1 Off-site:** At least one copy should be stored off-site or remotely. Cloud services or an external drive stored in a different physical location can fulfill this requirement, providing protection against localized disasters. 

When deciding on backup frequency, you should consider how often the data changes, the amount of work that would be lost between backups, the cost (time and money) to replace lost work, and the effort required for the backup process. Automated backup solutions are often more efficient than manual processes. Please refer to the section on [Storage options](./storage_options.md) for more information on which options involve automated backup or not.

# Using `rsync` in the command line for Data Backup

If you are comfortable with the command line, `rsync` is a powerful and versatile utility available on Linux (including Windows Subsystem for Linux: WSL) and macOS systems that can efficiently synchronize and back up files and directories. It is particularly useful for incremental backups, as it only transfers the differences between the source and destination, saving time and bandwidth.

Here are simple steps to use `rsync` for data backup:

1. **Basic Local Backup:** To copy files from a source directory to a destination directory on the same machine (e.g., to an external hard drive), use the following command:  

```bash  
   rsync -av /path/to/your/source_data/ /path/to/your/backup_destination/
```

   * `-a` (archive mode): This is a composite flag that preserves permissions, timestamps, symbolic links, and recursively copies directories, making it ideal for backups.
   * `-v` (verbose): This flag provides detailed output, showing which files are being copied or skipped.

2. **Incremental Backups:** To ensure that only new or changed files are copied, and to remove files from the backup destination if they've been deleted from the source, add the \--delete flag:  

```bash  
   rsync -av --delete /path/to/your/source_data/ /path/to/your/backup_destination/
```

   This makes the backup an exact mirror of the source, reflecting deletions as well as additions and modifications.

3. **Remote Backups via SSH:** For secure backups to a remote server (e.g., a research server or another machine), rsync can use SSH. Ensure the remote machine has an SSH server running and you have SSH access.  

```bash  
   rsync -avz /path/to/your/source_data/ username@remote_host:/path/to/remote/backup_destination/
```
   * `-z` (compress): This flag compresses file data during transfer, which can speed up transfers over a network connection.

4. **Excluding Specific Files or Directories:** If you need to exclude certain files or folders from your backup (*e.g.*, temporary files or large datasets that are not critical to back up frequently), use the \--exclude option:  

```bash  
   rsync -av --exclude 'temp_files/' --exclude 'logs/*.log' /path/to/your/source_data/ /path/to/your/backup_destination/
```
   You can specify multiple `--exclude` options for different patterns or paths.

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Important
`rsync` is a robust tool for maintaining up-to-date copies of your research data, supporting both local and remote backup strategies as part of a comprehensive data management plan. For more advanced usage, refer to the `rsync` manual by running `man rsync` in your terminal or consult the [rsync documentation](https://linux.die.net/man/1/rsync). 
:::

:::{.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} Important
These steps are similar to those recommended in [Moving data to your server](../../infrastructure/moving_data.md) and in the [Transfer Data](https://doc.dhpc.tudelft.nl/delftblue/Data-transfer-to-DelftBlue/) section of the DelftBlue documentation.
:::


