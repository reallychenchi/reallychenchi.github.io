---
layout: post
title: Map J2ME Applications to Content Types with JSR-211 (CHAPI)
date: 2010-11-17 20:00
categories: 编程
tags: Java
---


http://www.devx.com/wireless/Article/21958/1954

If you've been frustrated when trying to write J2ME apps that communicate with other applications, help is at hand. This brand new J2ME API improves the way mobile devices handle content.

<!-- more -->



n July, the Java Community Process released JSR 211, the Content Handler API (also known as CHAPI), for public review. The release counts as one of the most useful and innovative new APIs for J2ME development. In short, the API defines a communication model between applications (either Java/J2ME or native applications), by letting developers specify MIDlets as the content handlers for one or more specific file types.



One of the greatest limitations in writing applications for the current J2ME platform lies in intercommunication with other applications. Except for some very limited mechanisms (such as the platformConnection method introduced with MIDP 2.0), Java applications have no way to exchange data with other applications. Faced with the need to communicate with other processes, the "sandbox" conceptâa good thing when it comes to security in mobile applicationsâsuddenly becomes a major flaw.



                        Although this article focuses on the MIDP platform implementation of JSR 211, the API is designed for use on any J2ME compliant device, such as MIDP 1.0 and 2.0 or the Personal Basis Profile devices.            

JSR 211 to the Rescue

The JSR 211 model is based on the concept of content handlers. Using this execution model, a given MIDlet can register itself into the device's operating system to become the default application responsible for manipulating files of a specific MIME type. For example, you might create a MIDlet to edit/display .png images and register it as the default handler for the image/png MIME type. From successful registration onward, any requests for visualization of a .png file would then automatically activate the MIDlet (regardless of whether that request was initiated by a Java application or an application written in some other language). For example, if the user receives an SMS message with a link to a .png file and then selects the link, the registered Java MIDlet would activate and handle the request. The possibilities and usage scenarios are exciting.



The picture below, borrowed from the CHAPI specification, shows where the API implementation fits on the J2ME architecture. Although it presents a new set of classes for developers to use on their Java Applications, the major changes are focused on the virtual machine's AMS (Application Management System), which is responsible for the interactions between the MIDlets and the underlying operating system.



  Figure 1. JSR 211: The figure shows how JSR 211 (CHAPI) fits into the J2ME architecture.            The invocation of registered content handlers is based on URIs; the MIDlet that invokes a content handler doesn't need to specify the application that should be used. The MIDlet needs to supply only the content's URI (in a manner similar to the platformRequest method on the MIDlet class), the operation to be executed (editing, saving, creating, etc), and any other parameters that may be needed for execution.



It's possible to register more than one content handler for any specific file type (for example, when there are two MP3 players on the device). In this case, the invoking application can specify which application to use to handle the content by specifying its ID. The API also supports execution of chained (sequential) content handlers, which allow more than one application to process the content in sequence, each one handing execution to the next application in the chain. In that case, the first content handler registered for the given type is always the first one executed.



The specification states two possible execution modes for the content handling process, depending on the device's multitasking capabilities. In devices where parallel execution of applications (multitasking) is possible, the API dictates that the content handler can be executed in a higher priority thread, and then send an answer back to the invoker application (which is once again brought to the foreground) without any need to finalize the invoker before the content is handled. This execution model also affects the display usage priority: the API specifies that requests for screen drawing (such as callings to the paint() method or access to the Display object) made by the background application (the invoking application, at the time the request is being handled) have lower priority than similar calls made by the foreground application.



On non-multitasking devices, where only one application can execute at a time, the invoker must be finished before the content handler executes. Similarly, the content handler must finish before the invoker can get a response back.



What's in the Box?

The CHAPI ships as the javax.microedition.content package. It's a small API composed of seven classes (including a general usage exception class). CHAPI includes all the necessary mechanisms for invoking a content handler and getting a response back, registering and unregistering content handlers and looking up installed handlers. The package classes are:

Content Handling in a Nutshell

The examples below are based on the example code included on the CHAPI public specification. They show how to invoke a content handler responsible for opening vcard files, how to handle a request, and how to retrieve a response.



Step 1: Invoking a Content Handler

Invoking a content handler is a simple task. The example below is based on the examples included on the CHAPI specification document. In the example, the application requests activation of a content manipulator for the vcard (electronic business card) file type (see http://www.imc.org/pdi/) using an Invocation object instance.



In the preceding code, the invoker specifies the opening action (ContentHandler.ACTION_OPEN) and provides some additional arguments that the content handler can use to perform business-specific operations.



Applications invoke handlers using the Registry.invoke() method. This method returns a Boolean value, which indicates whether the invoker must be closed before the content handling takes place.



The example also includes handling an expected response. You can retrieve the Invocation object containing the result of the processing made by the content handler by calling the Registry.getResponse() method. Then you can access all the Invocation attributes (action, args, url, status, etc.) freely, which makes handling the response a rather simple procedure.



It is important to note that the only mandatory connection model implementation on MIDP 2.0 compliant devices is the HttpConnection; however, it's possible to use other protocols on devices that have specific stack implementations, because CHAPI relies on the Generic Connection Framework model (the standard mechanism for creating connections on J2ME). For example, a device that implements JSR 75 (and thus supports a file system) should be able to request a content handler using the file protocol (e.g. "file:///MMC:/mypicture.gif") when instantiating the Invocation object.



Step 1: Invoking a Content Handler

Invoking a content handler is a simple task. The example below is based on the examples included on the CHAPI specification document. In the example, the application requests activation of a content manipulator for the vcard (electronic business card) file type (see http://www.imc.org/pdi/) using an Invocation object instance.

In the preceding code, the invoker specifies the opening action (ContentHandler.ACTION_OPEN) and provides some additional arguments that the content handler can use to perform business-specific operations.



Applications invoke handlers using the Registry.invoke() method. This method returns a Boolean value, which indicates whether the invoker must be closed before the content handling takes place.



The example also includes handling an expected response. You can retrieve the Invocation object containing the result of the processing made by the content handler by calling the Registry.getResponse() method. Then you can access all the Invocation attributes (action, args, url, status, etc.) freely, which makes handling the response a rather simple procedure.



It is important to note that the only mandatory connection model implementation on MIDP 2.0 compliant devices is the HttpConnection; however, it's possible to use other protocols on devices that have specific stack implementations, because CHAPI relies on the Generic Connection Framework model (the standard mechanism for creating connections on J2ME). For example, a device that implements JSR 75 (and thus supports a file system) should be able to request a content handler using the file protocol (e.g. "file:///MMC:/mypicture.gif") when instantiating the Invocation object.



Step 2: Handling a Request

Handling a request is also a simple task. The example below shows an application which handles a request and then displays the result to users until they press a key to close the content handler.

During the example initialization, the call to the Registry.forClass() method instantiates a ContentHandler object associated with the MIDlet (the attributes of this instance, such as supported types and actions, are determined when the MIDlet is registered as a content handler. I'll discuss the procedure later on this article). Using the instance returned from the Registry.forClass method, you can access the pending requests and process them as desired. The ContentHandler class (and its direct subclass, ContentHandlerServer notifies the MIDlet about pending requests via the invocationNotify() method exposed by the ContentListener class (following the request-response model commonly adopted on other APIs, such as the Wireless Messaging API), and can retrieve the invocation data by calling the getRequest() method.



After accessing the Invocation object, you can retrieve the content as a stream of data using the Generic Connection Framework. The Invocation object also grants access to all the attributes which were configured during the instantiation of the Invocation: action, arguments, status, etc.



Step 3: Getting the Response

When the content handling is completed (in the sample code, that occurs when the user presses the 'ok' softkey, which in turn executes the commandAction() method), the application must invoke the ContentHandler.finish() method. The invoking application is then notified of the completion and can return to the main execution thread (if it is active). The behavior of the finish() method is similar to invoke()âdepending on the implementation, the content handler may need to finalize before the callee can continue execution.



Discovering the Registered Handlers

Several methods of the Registry class allow developers to discover the registered handlers responsible for specific content types. You can also determine which registered content handlers are responsible for specific actions, such as delete, open, or rename for a given file extension (.png, .vcard, .mid, etc), or MIME-type (text/html, image/gif, etc). Finally, you can locate the content handler identified by a specific ID.



Registering a Content Handler

For the VCardViewer MIDlet to be recognized as a content handler, you must register it with the AMS. The most common approach is static registration; as long as the MIDlet declares its content handling attributes in the .jad descriptor, it is registered automatically during installation on the device. The sample code below shows the descriptor for the VCardViewer MIDlet. Content handling is a sensitive system resource and prone to misuse, so MIDlets registered as content handlers must be signed/authorized by the author for them to work. The specification states that you must add the MIDlets into the javax.microedition.content.ContentHandler security domain for them to work properly as content handlers.

Among the attributes on this descriptor, only the ones starting with the prefix "MicroEdition-Handler" deserve a detailed explanation in the context of the sample application:

You can also register MIDlets dynamically. The sample code below registers a MIDlet as the content handler for image/png files and declares that the MIDlet will be responsible for handling opening requests (ContentHandler.ACTION_OPEN) for that file type. The code calls the Registry.register() method to perform the registration. The complementary Registry.unregister() method lets you unregister an application previously defined as a content handler. Content handlers are unregistered automatically when their corresponding MIDlets are removed (uninstalled) from the device.

Before you get too excited about these new capabilities, remember that CHAPI is both optional and not yet final. The final reviews are due to take place in the fourth quarter of this year and should not add many changes to the current API specification. In addition, CHAPI's availability on any particular device depends on whether the device manufacturer implement and include it with their devices' VMs. But because of CHAPI's usefulness and the new level of interaction it brings to the J2ME world, many manufacturers will probably elect to implement it on their MIDP 2.00-compliant devices fairly quickly.

[原文在百度空间已经关闭]

