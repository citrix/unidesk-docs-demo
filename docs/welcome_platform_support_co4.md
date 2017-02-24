[Release notes and supported platforms  ](get_started_deploy_release_notes_co4)
 > Supported platforms
#Supported Platforms
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Virtualization"> Hypervisor</a>                        </p>                        <p><a href="#Provisio"> Image publishing</a>                        </p>                        <p><a href="#Session"> Operating System for Layered Images</a>                        </p>                        <p><a href="#Service"> Directory Service</a>                        </p>                        <p><a href="#Browser"> Internet browser</a>                        </p>                    </td>                </tr>            </tbody>        </table>
##Hypervisor<a name="Virtualization"></a>
###Unidesk Enterprise Layer Manager (ELM) 
The Unidesk ELM can be installed in the following environments:
<ul>            <li>Azure Resource Manager</li>            <li>Citrix XenServer 6.5, 7.0</li>            <li>Microsoft Hyper-V, Windows Server 2012 R2</li>            <li>Nutanix Acropolis </li>            <li>vSphere vCenter 5.5.x, 6.0.x</li>        </ul>
###Network File Share protocol
<ul>            <li>                <p>Server Message Block (SMB)</p>            </li>            <li>                <p>Network File System (NFS)</p>                <p><b>Note:</b> <i>Elastic Layers</i> can only use SMB file shares. NFS shares are not supported for Elastic Layering.</p>            </li>        </ul>
###Network connection
<ul>            <li>A 10 GB connection is recommended between the Unidesk ELM and the file share.</li>        </ul>
##Image publishing<a name="Provisio"></a>
Unidesk 4 lets you publish to these platforms:
<ul>            <li>                <p>Citrix MCS for Nutanix AHV</p>            </li>            <li>                <p>Citrix MCS for vSphere</p>            </li>            <li>                <p>Citrix MCS for XenServer</p>            </li>            <li>                <p>Citrix PVS 7.1, 7.6 - 7.9, 7.11 - 7.12 with recommended network speeds to the PVS Store of 10 GB. </p>            </li>            <li>                <p>Citrix XenApp and XenDesktop 6.5, 7.0 - 7.11</p>            </li>            <li>                <p>Microsoft Azure, with recommended network speeds to the Azure publishing location of 10 GB.</p>            </li>            <li>                <p>VMware Horizon View 6.x, 7.x</p>                <p><b>Note:</b> View Persona Management  is <i>not</i> supported with Elastic Layering. </p>            </li>        </ul>
You can use Unidesk Layers and Layered Images with other provisioning systems and hypervisors, although the solution is not fully integrated.
##Operating System for Layered Images<a name="Session"></a>
<ul>            <li>                <p>Windows Server 2016, 64-bit (Standard and Datacenter Editions)</p>            </li>            <li>Windows Server 2012 R2, 64-bit (Standard and Datacenter Editions)</li>            <li>Windows Server 2008 R2, 64-bit (Standard and Datacenter Editions)</li>            <li>Windows 10, 64-bit</li>            <li>Windows 7, 64-bit</li>            <li>Windows 7, 32-bit</li>        </ul>
Unidesk supports single-byte language packs for the base US English Windows operating system. Language packs must be installed on the OS Machine before importing the OS into a Layer. Language packs installed on a Version added to the OSLayer will not work correctly.
##Directory Service<a name="Service"></a>
<ul>            <li>Microsoft Active Directory</li>        </ul>
##Internet browser<a name="Browser"></a>
The Unidesk Management Console (UMC) supports the following browsers with Silverlight 4.0 support:
<ul>            <li>                <p>Internet Explorer v11</p>            </li>            <li>                <p>Firefox v45 and later versions that support MSSilverlight 4.0.</p>            </li>        </ul>



