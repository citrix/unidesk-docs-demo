You are here: Learn about Citrix App Layering [UnideskVersion Layering 4.0.8] > Layer > User Layers (Unidesk Labs)
#User Layer (Unidesk Labs)
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Before"> Before you start</a>                        </p>                        <p><a href="#Create2"> Enable User Layers in the Layered Image</a>                        </p>                        <p><a href="#Elastic"> User Layer (Unidesk Labs)</a>                        </p>                    </td>                </tr>            </tbody>        </table>
With the Unidesk User Layer you now have the ability to persist user profile settings, data, and user-installed applications in non-persistent VDI environments. 
User Layers are created when:
<ul>            <li>You set <i>Elastic Layering</i> on an Image Template to <i>Application and User Layers</i>, so that the Layered Image supports User Layers.</li>            <li>A user logs in to their desktop for the first time, and a User Layer is created for them. From then on, the user's data and settings are saved in the User Layer, along with any applications that the user installs locally on their desktops. </li>        </ul>
##Before you start<a name="Before"></a>
###Prerequisites 
<ul>            <li>Create your <a href="layer_os_create_co4.htm">OSLayer</a>.</li>            <li>Create your <a href="layer_platform_create_co4.htm">Platform Layer</a> for publishing, if needed.</li>            <li>Create your <a href="layer_apps_create_co4.htm">App Layers</a>.</li>            <li>Enough free disk space on your ELM's file share to ensure that  these additional Layers do not cause you to run out. Allow enough space for the user's locally installed apps, plus the data and configuration settings for the user's Layers.</li>            <li>Make sure network bandwidth is adequate, as bandwidth and latency have a significant effect on the User Layer. Every write goes across the network.</li>        </ul>
###Compatibility
Currently, User Layers are supported in conjunction with the following platforms:
<ul>            <li>Operating systems: Windows 7, 64-bit </li>            <li>Publishing platforms: VMware Horizon View and Citrix XenDesktop. </li>        </ul>
###User Layer creation process
<ul>            <li>Enable User Layers in your Image Template:<ul><li>Set <i>Elastic Layering</i> in the Image Template wizard on the Image Disk  tab) to <i>Application and User Layers</i>.</li><li>Publish Layered Images using the above Image Template. </li></ul></li>            <li>                <p>When a user logs on to their desktop for the first time, a User Layer is created for them.</p>            </li>        </ul>
###User Layer size and location
The default size of a User Layer is 10 GB. 
User Layers are created in the Users folder on the ELM's network file share, for example:
\\MyServer\MyShare\Users 
Each user will have his/her own directory within the Users directory, and it will be named as follows: 
Users\domainIname\username\OS-Layer-ID-in-hex_OS-Layer-name\username.vhd
For example:
<ul>            <li>User's login name: <b>jdoe</b> </li>            <li>User's Domain: <b>testdomain1</b> </li>            <li>OS layer: MyOSLayer (ID is in hexidecimal format: <i>123456</i>)</li>            <li>User Layer would be created in:</li>        </ul>
 \\MyServer\MyShare\Users\testdomain1\jdoe\123456_MyOSLayer\jdoe.vhd
##Enable User Layers in the Layered Image<a name="Create2"></a>
<ol>            <li>Log into the Unidesk Management Console (UMC) as an <b>Admin</b> user.</li>            <li>Select <b>Images</b>. </li>            <li>Select the Image Template from which you will publish the Layered Image(s), and click <b>Edit Template</b>. This opens the Edit Image Template wizard.</li>            <li>On the Layered Image Disk tab, set  <b>Elastic Layering</b> to <b>Application and User Layers</b>.</li>            <li>On the Confirm and Complete tab, click  <b>Save Template Changes</b>.</li>            <li>Publish your Layered Images. </li>        </ol>
##Expected behavior
###Considerations
Before deploying User Layers, please consider the following guidelines and limitations.
<ul>            <li>The User Layer is delivered via the ELM's file share, therefore:<ul><li>If the host is disconnected from the User Layer storage, the user will have to log out and log in again to re-establish the disk mount. The user will have to wait approximately 5 minutes because the user layer will be inaccessible.</li></ul></li>            <li>Certain enterprise applications, such as MS Office and Visual Studio should be installed in Layers, not as user-installed applications in the User Layer. In addition, the Elastic Layering limitations are applicable for User Layer. For more information on Layering limitations, please see the <a href="layer_assign_apps_elastic_co4.htm">Elastic Layering Limitations</a> section.</li>            <li>Windows updates must be disabled on the User Layer. </li>            <li>VMware Horizon View:<ul><li><p>View must be configured for non-persistent desktops, and the desktop <i>must</i> be set to <i>Refresh at log off</i>. Delete or refresh the machine on log off. Example:</p><p><img></img></p></li><li>After logging off with View set to <i>Refresh Immediately</i>, the desktop goes into maintenance mode.  If there is only one machine in the pool, the pool will not be available until that machine has completed the refresh. </li></ul></li>        </ul>
<ul>            <li>The first time a user logs into his/her desktop,  a User Layer  is created for the him/her.</li>            <li>If  there is problem loading the elastically assigned Layers for the user, they will still receive their User Layer. </li>            <li>If you rename the user in AD, a new directory and User Layer will be created for the new name. To avoid this, rename the directory on the file share and the VHD file in the directory structure to the new AD user name.</li>        </ul>

