[Add Connector Configuration](connector_config_create_co4)
 > Citrix PVS
#Connector Configuration ; Optional Script (PVS) <a name="Azure_Platform_Connector_Fields"></a>
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Before"> Before you start</a>                        </p>                        <p><a href="#Create"> Create a new Connector Configuration for PVS</a>                        </p>                        <p><a href="#Configure_Script_Path"> Script Configuration (Optional, Advanced feature)</a>                        </p>                    </td>                </tr>            </tbody>        </table>
A PVS Connector Configuration contains the credentials and storage location Unidesk needs to connect to PVS, and it identifies the properties to be associated with the vDisk. 
Each Connector Configuration is set up to access a storage location via a specific account. For more about Connectors and Connector Configurations, see [About Connectors and Connector Configurations](connectors_about_co4)[. ](connectors_about_co4)
##Before you start<a name="Before"></a>
The first time you create an Image Template for publishing Layered Images to your PVS environment, add a PVS Connector Configuration for that PVS location.
###PVS###requirements
####PVS####services must be running as a domain account
For Unidesk to work correctly with PVS, the PVS services must be running as a domain account. This is because domain accounts have permissions to access the PVS store and the local system account does not. 
If your PVSserver is configured to use the local system account, which is the default setting, you can change the account by running the PVSconfiguration tool. This tool gives you an option to run as local system or use a domain account.  Choose a domain account. 
####PVS<a name="Creds"></a>####server and account information <a name="Creds"></a>
For Unidesk to access the location in your PVS environment where you want to publish a Layered Image, you need to supply the credentials and location in a PVS Connector Configuration.
The information you need for the PVS Connector Configuration includes. 
<ul>            <li><b>Name</b> - A useful name to help identify and keep track of this connector configuration. </li>            <li><b>Console</b> - The name of the PVSserver on which the Undesk agent is deployed. This is the server to which the vDisk will be published.</li>            <li><b>Domain User</b> - User name of a domain account that has permission to manage PVS.  This account will be used by the agent to run PVS Powershell commands. This account <i>must</i> have <i>Read/Write</i> access to the PVS store for writing the published vDisk.</li>            <li><b>Password</b> - Password for the domain user account. </li>            <li><b>Site Name</b> - Name of the Site this vDisk is to be a member of. </li>            <li><b>Store Name</b> - Name of the Store that this vDisk is a member of. </li>            <li><b>Write Cache</b> - When a new Disk is being created, this value sets the Write Cache type of the new Disk. Possible values include:<br></br><ul><li>Cache on Server</li><li>Cache on Server, Persistent</li><li>Cache in Device RAM</li><li>Cache in Device RAM with Overflow on Hard Disk</li><li>Cache on Device Hard Drive</li></ul><p>When choosing a <i>Write Cache</i> option, consult your <a href="http://www.vhersey.com/2014/03/citrix-pvs-write-cache-design-considerations/">PVS documentation</a> to ensure that the PVS Servers and target devices that use this vDisk are properly configured for the type you select. </p></li>            <li><b>License Mode</b> - Sets the Windows License Mode to: <ul><li>KMS - Key Management Service</li><li>MAK - Multiple Activation Keys</li><li>None</li></ul></li>            <li><b>Enable Active Directory machine account password management</b> - Enables Active Directory (AD) password management. The default value is <i>Enabled</i>.</li>            <li><b>Enable Load Balancing</b> - Enables load balancing. for the streaming of the vDisk</li>            <li><b>Enable Printer Management</b> - When enabled, invalid printers will be deleted from the Device. </li>        </ul>
##Create a new Connector Configuration for PVS<a name="Create"></a>
If you don't yet have a Connector Configuration that includes the PVSserver information and credentials for the server where the Layered Image will be published, add one now.
 To add a new Connector Configuration:
<ol>            <li>In the Publish Layered Image wizard, click the <b>Connector</b> tab. </li>            <li>Below the list of Connector Configurations, click the <b>New</b> button. This opens a small dialog box.</li>            <li>Select the Connector Type for the platform and location where you are publishing the Layered Image. Then click <b>New</b> to open the Connector Configuration page. </li>            <li>Complete the fields on the Connector Configuration page. For guidance, see the above field definitions.</li>            <li>Click the <b>TEST</b>button to verify that Unidesk can access the location specified using the credentials supplied.</li>            <li>Click <b>SAVE</b>. The new Connector Configuration should now be listed on the Connector tab.</li>        </ol>
##Script Configuration (Optional, Advanced feature)<a name="Configure_Script_Path"></a>
When creating a new Connector Configuration, you can configure an optional Powershell script on any Windows machine running a Unidesk Agent—the same agent used on the PVS server. These scripts must be stored on the same machine that the Unidesk Agent is installed on, and will only be executed after a successful deployment of a Layered Image. Some preset variables are available to enable scripts to be reusable with different template images and different connector configurations. These variables will also contain information needed to identify the virtual machine created as part of the published layered image in PVS.
Execution of these scripts will not affect the outcome of the publish job, and progress of commands executed in the script will not be visible. The PVS connector logs will contain the output of the executed script.
###Configure a Script (Remember, this is optional)
If you want a script to run each time a Layered Image is published, complete these steps using the values described in the sections that follow.
<ol>            <li>                <p>Complete and save the Connector Configuration as described above.</p>                <p><b>Note:</b> Before selecting Script Configuration page, you must save (or discard) any edits to the Connector Configuration settings, </p>            </li>            <li>                <p>If the Navigation menu on the left is not open, select it and click <b>Script Configuration</b> to open the Script Path page.</p>            </li>            <li>                <p>Complete the required fields using the values detailed herein, and click <b>Save</b>.</p>            </li>        </ol>
###Script Configuration fields<a name="Creds"></a>
<ul>            <li><b>Enable script</b> - Select this check box to enable the remaining fields. This allows you to enter a script that will be executed each time a Layered Image is published.</li>            <li><b>Script Agent</b> - The agent machine where the scripts will be located and executed from.</li>            <li><b>Username (optional)</b> - The username to <i>impersonate</i> when running the script. This can be used to ensure the script runs in the context of a user that has the needed rights/permissions to perform the operations in the script.</li>            <li><b>Password (optional)</b> - The password for the specified username.</li>            <li><b>Path</b> - A full path and filename on the agent machine where the script file resides.</li>        </ul>
###Other Script Configuration values
####Powershell variables
When the script is executed the following variables will be set and can be used in the powershell script:
<table>            <col></col>            <col></col>            <col></col>            <col></col>            <thead>                <tr>                    <th>Value</th>                    <th>Applies to connector types:</th>                    <th>Value determined by which code:</th>                    <th>Description</th>                </tr>            </thead>            <tbody>                <tr>                    <td>connectorCfgName</td>                    <td>All </td>                    <td>Common code</td>                    <td>This is the name of the connector configuration that the script configuration is associated with.</td>                </tr>                <tr>                    <td>imageName</td>                    <td>All</td>                    <td>Common code</td>                    <td>This is the name of the layered image template that was used to build/publish the layered image.</td>                </tr>                <tr>                    <td>osType</td>                    <td>All</td>                    <td>Common code</td>                    <td>                        <p>This is the OS type of the layered image that was published. It can be one of the following values:</p>                        <ul>                            <li>Windows7</li>                            <li>Windows764</li>                            <li>Windows200864</li>                            <li>Windows201264</li>                            <li>Windows10</li>                            <li>Windows1064</li>                        </ul>                    </td>                </tr>                <tr>                    <td>diskLocatorId</td>                    <td>All</td>                    <td>PVS</td>                    <td>The internal id for the vDisk.</td>                </tr>            </tbody>        </table>
####User Impersonation
The Unidesk Agent, which runs as a service on a Windows machine, runs under either the local system account or the network account. Either of these accounts may have some special privileges, but they often are restricted when it comes to executing specific commands or seeing files in the file system. Therefore, Unidesk gives you the option of adding a domain user and password that can be used to "impersonate" a user. This means that the script can be executed as if that user had logged onto the system so that any commands or data will be accessible subject to those user rights and permissions. If no user name or password is entered, the script executes using the account under which the service is configured to run.
####Script Execution Policy
Script execution policy requirements are generally up to you. If you intend to run unsigned scripts, you must configure the execution policy to one of the more lenient policies. However, if you sign your own scripts accordingly, you can choose to use a more restrictive execution policy.