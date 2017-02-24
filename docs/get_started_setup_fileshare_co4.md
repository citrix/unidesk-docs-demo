[Set up Unidesk](landing_set_up_co4)
 > Set up a network file share
#Set up a network file share
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Share"> Network file share requirements and recommendations</a>                        </p>                        <p><a href="#Create_Share"> Create the network file share</a>                        </p>                        <p><a href="#Cfg_Share"> Configure Unidesk to access the file share</a>                        </p>                        <p><a href="#Next"> Next step</a>                        </p>                    </td>                </tr>            </tbody>        </table>
The Unidesk ELM must be connected to a network file share. 
##Network file share requirements and recommendations<a name="Share"></a>
###Requirements
When setting up the ELM's file share:
<ul>            <li>                <p>The file share must be configured using SMB or NFStechnology. However, if you plan to use Elastic Layer assignments, you must use SMB protocol, as NFS technology is <i>not</i> supported when using Elastic Layers.</p>            </li>            <li>                <p>The user credentials for the file share must have full permissions for that share. </p>            </li>            <li>                <p>The share must be set up by the admin to be <b>readonly</b> for all users except for the one configured in the ELM. This secures the Layers and other files stored on the share.</p>            </li>            <li>                <p>Ensure that you have the minimum storage space requirement of 40-100GB for your file share. </p>                <p><b>Note:</b> Storage space is expandable, as you can add space to a disk, or other disks to the ELM. </p>            </li>        </ul>
###Recommendations
<ul>            <li>                <p>For convenience, set up a Network File Share hosted in your hypervisor. </p>            </li>            <li>                <p><b>For Azure:</b> Currently, the Unidesk ELMdoes not support the <i>Azure File Share feature</i>. For best performance, it is best to create a file share server in Azure using a fast system with a Premium Disk, for example, a DS class machine. </p>            </li>        </ul>
##Create the network file share<a name="Create_Share"></a>
Depending on your environment, configure a file share that uses either Network File System (NFS) or Server Message Block (SMB) protocol. 
<ul>            <li>                <p>Follow the vendor's instructions for setting up a file share using the protocol supported in your environment. </p>            </li>            <li>                <p>If you are planning to deploy Elastic Layers, the share <i>must be configured using SMB technology</i>. When using Elastic Layer assignments, <i>NFS technology is not supported</i> for the file share.</p>            </li>        </ul>
##Configure Unidesk to access the file share<a name="Cfg_Share"></a>
Once you have created a file share, configure the Unidesk Enterprise Layer Manager (ELM) to attach to it. You can configure the ELMvia the Unidesk Management Console (UMC).
<ol>            <li>                <p>In the Unidesk Management Console, select  <b>System > Settings and Configuration</b>, then scroll down to the network file shares setting and click <b>Edit</b>.</p>            </li>            <li>                <p>Specify a Type, Path, User name, and Password for the file share.</p>            </li>            <li>                <p>Click <b>Test Network File Share</b> to see if you can connect to the file share. The test returns a message stating either <i>Success</i> or <i>Failed to mount network file share path</i>.</p>            </li>            <li>                <p>Once the test returns a <i>Success</i> message, click <b>Save</b>.</p>            </li>        </ol>
##Next step<a name="Next"></a>
[Open ports in your firewall for Unidesk](system_ports_firewall_co4)[        ](system_ports_firewall_co4)

