# Telco Cloud Operational Tool

TCOT could be defined as opensource tool that help cloud system Administrators/Engineers to manage complex public or private cloud environment with agile and simple wizard. Python3 has been used for developing the tool with adding easily embeddable and beautiful command line interface called PyInquirer (Oyetoke Toby GitHub link: https://github.com/CITGuru).  of paramiko   for daily use.


Requirements:
* Python version >= 3.X.X
* PyInquirer Package.
* Paramiko

List of features:

- Cloud
    - Openstack services status
    - Ceph Storage status
    - Controllers status
    - Computes status
    - VM's Status
    - Director Health-check + status
    - Check for Errors per OpenStack Service.
    - Show Servers List.
    - Show Projects List.
    - Show Users List.
    - Show Networks List.
    - Show Volumes List.
    - Show Images List.
    - Check OpenStack Host Aggregate (HA).
    - Check Baremetal List and status.

- OS
    - CPU Status (Display the running and active real-time processes).
    - NUMA Status.
    - Number of running VM
    - Number of virtual interfaces (VIF)
    - Disk status.
    - Memory status.
    - Check SRIOV status.
    - Check Capabilities of OS
    - Check for Hardware Errors.
    - Check Hardware Information.
    - Generate sosreport.
    - Check Service status.
    - Check Neighbors reachability.
    - Check grub parameter
    - Run Command on host.

Screenshot:
 (Tool view list) 
![alt text](https://github.com/mubarak-elrayah/Telco-Cloud-Operational-Tool/blob/master/docs/Screen%20Shot%202020-02-16%20at%204.10.34%20PM.png)

Reference Link:

* PyInquirer: https://pypi.org/project/PyInquirer/
* Ansible Doc: https://docs.ansible.com/
* Paramiko Doc:
