---
title: "Unit 3: RENDER MANAGEMENT"
date: "March 2018"
author: "Hasan Balable"
geometry: margin=2.54cm
---

RENDER MANAGEMENT
=================

<!-- 
Grid computing and its use within VFX render queues - at a basic level
How to balance resource needs within the company’s physical capacity
Render optimisation techniques -->

Rendering high detail, photorealistic images and simulations calls for a lot of computer processing power. VFX houses need to be able to produce these results quickly. To do this, they often have their own in house super-computers, called render farms, which utilize the power of grid and cluster computing. 

What is Grid Computing?
--------------

This describes a shared pool of computing resources used to solve complex tasks. It is a form of distributed computing,  meaning that these tasks utilize the resources of multiple networked machine . In the context of visual effects, there are a number of examples where this can be used.

#### Security

In an industry that constantly deals commercially sensitive data, security is a huge priority. For larger studios, having workstations with access to internal servers and the internet can be risky territory as any breach of security due to malicious attacks would have direct access to this sensitive data. One solution to this that has been adopted by multiple studios it to use remote desktop environments provided by a server with internet access. This  This adds a layer of protection, as any file transfers between a secure workstation and one of these remote environments is can be heavily controlled, which not only decreases the risk of a harmful malicious attack, but also acts as a deterrent against any leaks that might be caused internally.

There are many frameworks that utilize the efficiency of shared computing resources that enable for this type of remote environment. It would not be efficient to keep a virtual environment that isn't being used open, so after a session has been inactive for a period of time it is closed and resources are redistributed. Though it this isn't necessarily classed as grid computing as there is no distribution between networked machines involved.

#### Working Remotely

These virtual environments are used by many companies, and can be very cost-effective. Nvidia Grid is an example of a technology which enables this virtual desktop infrastructure (VDI) to be powerful to be practical for use in VFX production. Sharing resources over a number of Grid-enabled physical GPUs allows for a customised virtual GPU per user, making is possible to work in GPU intensive 3D programs without the need for multiple physical workstations.

#### Rendering

Many VFX studios, especially larger ones, have a number of powerful machines dedicated for rendering, which are called *slaves*. Today, these can often be supplemented, or even fully replaced by, a number of remote machines provided by a cloud services such as YellowDog and Google Cloud. Pixar's Tractor is a system we use at DNEG that enables this distributed rendering. Tractor uses a central server and multiple render machines, called blades. It also provides a number of APIs and a web UI.

### Understanding Tractor

Tractor blades can have multiple slots, and the number of slots describes the number of tasks a blade can run simultaneously. The central server, also called a queue manager, receives render jobs, containing a tree of individual tasks, which it distributes to available slots.  These slots then run their specific tasks, which could be anything from a shell command which renames or moves a number of files to a 500 frame FX cache. After these tasks are completed, the blade will send a signal to the central server, announcing that it is ready for a new task.

Tasks can also be run on workstations, which are often abundant in a VFX studio. This is especially efficient at night, while these machines are not in use.

These tasks can also be given keys which are used by the queue manager to identify important information such as the application being used and the minimum specifications of the machine it can be run on. For example, a heavy lighting render may require a machine with a lot of RAM available and a powerful GPU, while a 2D prep nuke script can be rendered quickly on a machine with a much lower spec.

Job priority levels and limits can also be set too, which enable time-critical jobs to be run quickly while not taking too many slots from the rest of the farm. ```priority``` is a float attribute which is a measure of a jobs importance. The queue manager will allocate slots to tasks of higher priority jobs before lower priority jobs. Jobs in Tractor also have an attribute called ```maxactive```, which defines the maximum number of active tasks available at one time. This would be useful in the case that a high priority job had 1000 tasks in parallel in their default state: ```ready```. Without a max active set on the job, the queue manager would quickly allocate any available slots to this one job and would neglect any lower priority jobs.

##### Chunking

Chunking is when long sequences are split up into multiple tasks. This is a useful technique which speeds up jobs at the cost of CPUs. This is normally done by either splitting render sequences into smaller chunks of frames (e.g. 1 task per 10 frames), or by rendering different segments of an image as multiple tasks, for example splitting frames in half and rendering them as seperate tasks, before having a script stitch them back together. The latter is usually reserved for especially high resolution images, such as those for marketing stills.

#### Render Wrangling

##### Erroring Jobs

One responsibility of a render wrangler (sometimes called a render TD) is to debug failing renders. Failing renders are easy to spot in tractor as the job is coloured bright red and reads "error". Any stack traces, errors or warnings should show in a tasks log, which can be access by right-clicking on a red errored task under the errored job in tractor, and selecting "Log" from the context menu. If the stack trace doesn't make much sense, there should be a scene file you can debug directly. First step would be to try and run the task manually step-by-step and see if you encounter any errors.

##### Slow Jobs

There are many causes for slow or hanging jobs, and sometimes it can be difficult to diagnose a cause, especially when the log isn't showing any actual errors. Memory issues can often be the cause of hanging jobs, and the there are a few solutions for this. Namely:

- Retrying the issue on a slot with a higher RAM allocation.
- Making the scene lighter. e.g. rendering lower LODs of distant assets.
- Chunking the job into smaller tasks.

For lighting renders, you can speed up the tasks by lowering the number of samples, which will result in a render being more noisy, though it can be quicker to render, then fix this noise using 2D tools than to render with a higher sample rate. In some cases, when the 2D noise removal is done well, these results can look very similar to a full-quality render.
