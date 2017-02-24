[Publish Layered Images](layered_images_publish_co4)
 > Citrix XenServer
#Publish Layered Images (XenServer)
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Pre"> Prerequisites</a>                        </p>                        <p><a href="#Pub"> Publish a Layered Image</a>                        </p>                    </td>                </tr>            </tbody>        </table>
A Layered Image is a virtual machine that Unidesk has composited from the Layers and settings specified in an Image Template. You can publish one or more Layered Images to XenServer and add each one to a collection, provisioning service, or other method for provisioning your systems.
##Prerequisites<a name="Pre"></a>
To publish a Layered Image, you need:
<ul>            <li>One or more Image Templates. </li>        </ul>
##Publish a Layered Image<a name="Pub"></a>
<ol>            <li>                <p>In the Images module, select one or more Image Templates to publish.</p>            </li>            <li>                <p>From the Action menu, select <b>Publish Layered Image</b>.</p>            </li>            <li>                <p>On the Confirm and Complete page, select <b>Publish Layered Images</b>. For each template, this starts a task called, <i>Publishing Layered Image</i>. When each task completes, the task description provides the information you need to navigate to the image in your environment.</p>            </li>            <li>                <p>Use the information in the expanded Packaging Disk Task shown above to navigate to the location in XenServer where the Layered Image has been published.</p>            </li>        </ol>
Next you can move the image to a collection or other location for provisioning servers.


