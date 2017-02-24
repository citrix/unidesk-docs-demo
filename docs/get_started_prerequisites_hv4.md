[Install the Unidesk ELM](get_started_deploy_unidesk_elm_co4)
 > Prerequisites
#Unidesk Prerequisites (Hyper-V)
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#os_requirement"> </a>                        </p>                        <p><a href="#storage_req">Storage requirements</a>                        </p>                        <p><a href="#prereqs_hyperv">Hyper-V-specific requirements</a>                        </p>                    </td>                </tr>            </tbody>        </table>

###Operating System requirement <a name="General"></a>
<ul>            <li>                <p><b>OS for Layered Images</b>                </p>                <p>You need a Unidesk-supported <a href="welcome_platform_support_co4.htm#Session">operating system</a> to import into an OSLayer. This OSwill be used to build your Layered Images.</p>            </li>        </ul>

###Storage requirements 
<ul>            <li>                <p><b>350-500 GB Storage Space</b>                </p>                <p>The Unidesk ELM uses local storage for temporary files and finalized layers. The more layers you create, the more space you need. However, if you run low on space, you can expand the size of the current disk, or add other disks to the ELM when needed.</p>            </li>            <li>                <p><a href="welcome_platform_support_co4.htm#Session"></a><b>40-100 GB network file share  (SMB/NFS)</b>                </p>                <p>The file share connected to the ELM is used for upgrades, Elastic Layers, and cross-platform publishing. This space is easy to expand, if needed. </p>            </li>        </ul>

###Hyper-V prerequisites
Be sure the Hyper-V VMwhere you are installing the ELM meets the following prerequisites.
<ul>            <li>A Windows Hyper-V 2012 R2 server</li>            <li>A Virtual Network in Hyper-V</li>        </ul>

