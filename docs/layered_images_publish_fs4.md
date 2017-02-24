[Publish Layered Images](layered_images_publish_co4)
 > Network file share
#Publish Layered Images (Network File Share)
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Pre"> Prerequisites</a>                        </p>                        <p><a href="#Pub"> Publish a Layered Image</a>                        </p>                        <p><a href="#Next"> Next Step</a>                        </p>                    </td>                </tr>            </tbody>        </table>
A Layered Image is a virtual machine that Unidesk has composited from the Layers and settings specified in an Image Template. You can publish one or more Layered Images to  the ELM's Network File Share, copy the Image(s) to your target environment, and use them to provision Session Hosts in your environment. This is especially useful if Unidesk does not yet include Connectors for the platform where you're provisioning systems. 
##Prerequisites<a name="Pre"></a>
To publish a Layered Image, you need:
<ul>            <li>One or more Image Templates.</li>        </ul>
The Image Template you select should have the correct OSLayer and any App Layers you want in the Layered Image.
##Publish a Layered Image<a name="Pub"></a>
To use an Image Template to publish a Layered Image:
<ol>            <li>                <p>In the Images module, select one or more Image Template that you want to publish.</p>            </li>            <li>                <p>From the Action menu, select <b>Publish Layered Image</b>.</p>            </li>            <li>                <p>On the Confirm and Complete page, select <b>Publish Layered Images</b>.  For each Image Template this starts a task called, <i>Publishing Layered Image</i>. When each task completes, the task description provides the information you need to navigate to the image in your environment.</p>            </li>            <li>                <p>Use the information in the expanded Packaging Disk Task shown above to navigate to the location where the Layered Image has been published.</p>                <p><b>IMPORTANT:</b> When publishing a Layered Image to a file share, there will be one VMDK file option, and it will generate two files: <i>layer.vmdk</i> and <i>layer-flat.vmdk</i>. You need to upload both of them.</p>            </li>        </ol>
##Next Step<a name="Next"></a>
Once the Layered Image is published to the file share, you can use the image to provision servers in your environment.


