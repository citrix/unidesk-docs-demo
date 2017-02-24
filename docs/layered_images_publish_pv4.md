[Publish Layered Images](layered_images_publish_co4)
 > Citrix PVS
#Publish Layered Images (Citrix PVS)
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Pre"> Prerequisites</a>                        </p>                        <p><a href="#Pub"> Publish a Layered Image</a>                        </p>                        <p><a href="#Assign"> Assign the new vDisk to the targeted devices</a>                        </p>                    </td>                </tr>            </tbody>        </table>
A Layered Image is a virtual machine that Unidesk has composited from the Layers and settings specified in an Image Template. You can publish one or more Layered Images  to PVS, and stream them to the systems you want to provision.
##Prerequisites<a name="Pre"></a>
To publish a Layered Image, you need:
<ul>            <li>One or more Image Templates.  </li>        </ul>
##Publish a Layered Image<a name="Pub"></a>
To use an Image Template to publish a Layered Image:
<ol>            <li>Log into the UMC.</li>            <li>Select the <b>Images</b> modules. </li>            <li>Select one or more Image Templates, then click  <b>Publish Layered Image</b>.</li>            <li>On the Confirm and Complete tab, click the <b>Publish Layered Image</b> button.  This starts a task called, <i>Publishing Layered Image</i>. When the task completes, the task description provides the information you need to navigate to the image in your environment.</li>            <li>Use the information in the expanded Packaging Disk Task to navigate to the location in PVS where the Layered Image has been published.</li>        </ol>
Next you can assign the new disk to the targeted devices.
##Assign the new vDisk to the targeted devices<a name="Assign"></a>
<ol>            <li>Log into the PVSConsole.</li>            <li>Access the target PVS server. The new vDisk should appear under the targeted PVS store (refresh may be required).</li>            <li>Assign the new vDisk to the targeted devices.</li>            <li>Using Citrix PVS best practices, test the new vDisk to ensure that the image streams to the server as expected.</li>        </ol>

