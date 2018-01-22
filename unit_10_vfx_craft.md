Unit 10: VFX CRAFT
=============
<!--Abstract
The processes and art of a particular department, such as animation, lighting, FX or rigging
The particular standards of a department and the challenges they face
-->
From my experience at Double Negative, I haven't worked very closely with any one *creative* department in particular, but instead I have picked up a more basic (although broader) understanding of the challenges and responsibilities of a wide range of departments. So here I will give a brief overview of each of major roles, which will exist in almost every large VFX house.

Step 1: Concept Design
-------------
Concept Design is always a vital first step of any visual creative project that requires cooperation, whether a marketing campaign, a computer game or, more importantly, visual effects. In feature films, this is where many of the sets, costumes, and creatures are often first visualized, after only previously existing as words in a screenplay and in the imagination of the director.

Concept artists might be involved from the client side, the VFX house or even both, depending on the nature of the project. They often have a wide range of creative skills, as concept might include 3D sculpts, 2D digital art and sketches.

Artists in this area are able to have a lot of creative impact, as concept work will be used time and time again as reference in the work of many other artists.

Step 2: Build (Asset Specific Work)
-------------
In this section I will cover the main departments involved in asset design.

### Modelling

![Model of Motorbike](./images/wireframe_bike.jpg)

*image: https://seraphinacorazza.wordpress.com/2012/12/28/*

Modellers create pretty much all of the 3d assets (with the exception of 3d geometry created by FX TDs) required by a project. They have to meet not just artistic goals set by a combination of client notes and reference, but also technical specifications, some likely examples being:

##### Correct and consistent detail level (or LOD for Level of Detail)

Models will often be created with a number of LODS, so that the full detailed object doesn't always need to be rendered when it isn't required, for example when it is in the far distance of a shot. One workflow for creating these models is by starting from reference (or, if fortunate enough, a LIDAR scan) and, starting from a simple shape, building in progressively more detail, so that the highest LOD is the last to be created.

##### Efficient UVs, so that the ratio between UV space area and 3D surface area is consistent throughout the model.

Unless some parts of the model are more likely to have attention paid to than other parts. e.g. character models, where faces often have higher resolution textures.

##### Efficient mesh topology, so its structure deforms well.

This is very important in the games industry. They don't have the luxury of being able to sub-divide their meshes until they deform well, as the resource cost is exponentially expensive with each iteration.


#### Types of Modelling

Modelling is normally split into two categories: Hard surface and organic modelling.

Organic modelling encompasses anything with an irregular shape, or something that is mathematically hard to express. Some examples include plants, poop and most characters & animals. Sculpting is the preferred modelling method for organic modelling, which means using a program with specialised brushes that push, pull or otherwise deform parts of a model. ZBrush and Mudbox are both popular software packages that are used at studios.

Hard surface modelling is the skill of creating models that are *not too difficult to express mathematically*\*. But this does not in any way mean that they are any more difficult create than organic models. Hard surface modelling tasks include buildings, rigid props from bottles to mobile phones, and most furniture. These shapes can be created using the more traditional and mathematical modelling tools, such as extruding and adding edge loops. Programs used to create these models include Autodesk Maya and SideFX Houdini.

These models are then passed of to texturing and rigging (if they are to be animated).

\**Not an exact definition, but this was the result of reading lots of artists' individual opinions*

### Rigging

![Portal Rig](./images/portal_rig.jpg)

*image: James Ball - http://ballzy247saeblog.blogspot.co.uk/2015/02/*

A Rigger, sometimes called a Rigging TD, builds controllable rigs for models that require animation, such as vehicles and characters. For characters, this can involve building a skeleton which they bind to the mesh. Per-vertex weights are then painted for each skeletal bone, which define how much influence that bone has on the vertex. These bones are normally hidden and more user-friendly controls are created. The most commonly used software package for this is Autodesk Maya.

### texture & shader design

![Logan Ref/Lookdev](./images/logan_lookdev.jpg)

*image: Image Engine*

<!-- Texture artists use a variety of software, platforms, and rendering environments to create textures for environments, characters, objects, and props for animated films, television shows, and video games. Some of the most common types of software, platforms, and rendering environments used in animation include Photoshop, 3D Paint, UV Layout/Editing, RenderMan, Mental Ray, Maya, Shaders, and Houdini. Texture artists also use digital matte painting techniques to create textures and they work with advanced surface types, subsurface scattering, and global illumination. -->

Step 3: Shot Specific Work
-------------
Brief overview.

### Matchmove

![Matchmove pic](./images/matchmove.jpg)

*image: QLBEANS*

<!-- Match Moving or Camera Tracking is a technique that allows the integration of computer generated (CGI) VFX into live action footage. The process allows for the correct position, scale, orientation, and motion of the CGI relative to the real world captured in the shot.

Although Match Moving is traditionally an entry level job into 3D VFX, it is a crucial part of the 3D/CGI pipeline. Matchmoving describing the world inside a computer in 3D, what the original live action camera saw. -->

### Animation

![Matchmove pic](./images/anim_poses.jpg)

*image: Digital Domain*

<!-- Computer Animators produce images which, when recorded in sequence and projected, create the illusion of movement.

In character animation, they may be cast, like actors, for their special talents - comedy, dialogue, song and dance, action, men, women, children, animals, simplicity, etc. On other projects, they may be selected for their particular technical skills and ability.

In principle, the role of Animator is the same for all techniques of animation. The differences are in the tools used, and in some of the skills required. -->

### FX

![Houdini FX Sim](./images/fx.jpg)

*image: Carlos Parmentier*

FX TDs (short for Effects Technical Directors) are

<!--
Effects Technical Directors (FX TDs) are the digital versions of the traditional on-set special effects crew. They are in charge of creating things that are too complex to animate manually, and need to be run as computer simulations instead, including fire, destruction, dust, water, cloth, smoke and magic. They take animation and geometry data from other departments, and set up simulations to interact with them, for example bringing in a building model and destroying it, or taking a roto animated (sometimes called ‘body tracked’) model of a character casting a spell and adding the magic swirls that will then be rendered and composited over footage of the real actor. The data produced by the simulations is sometimes lit and rendered out by the FX department, but is usually sent to the Lighting Artists/TDs to create the final images.

Sometimes the simulations are carefully designed to mirror the laws of physics, and sometimes a more creative approach to reality is called for, depending on the effect needed. Because of this an FX TD needs to be able to adapt, and not get stuck in only one way of approaching a problem. As with all aspects of filmmaking, the director and VFX supervisor need to gauge the balance of achieving realism versus cinematic impact.
-->

### Lighting

![Lighting Before/After](./images/lighting_before_after.jpg)

*image: Dylan Sisson*

<!-- A lighter's role is to ignite stuff

Lighting TDs/Lighters make sure there is consistency in lighting, colour balance and mood between the various elements of a shot or scene. When appropriate, they ensure the computer-generated imagery looks photorealistic to match the live action plates.

Lighting TDs/Lighters add the lighting that creates atmosphere, increasing realism, tone and depth in a scene and clarifying location, weather and time of day. They balance individual elements to enable the compositors to produce a convincing image. They refer to the production designs and apply that visual style as faithfully as possible, taking care to maintain continuity.

They match technical skill with aesthetic judgement to create images that not only look good but are easy to render (i.e. output; translating computer data into images). -->

Step 4: 2D
-------------
brief overview

### Roto

![roto example](./images/roto_before_after.jpg)

*image + in-depth tutorial: https://pirayaganjanakulnon.wordpress.com/2016/01/12/module-01-assignment-01-rotoscope-shot/*

Roto artists are responsible for creating alpha mattes from scans which isolate certain features. Ideally, a key would be easier and more efficient, but it is not always possible or practical to shoot in front of an evenly lit screen. The most common way this is done is by trying to break down the movement of the desired element in a way it can be defined by as few 2d spline-shapes as possible. Then these shapes are transformed and translated to follow the movement in the scan. Compositors can then take these elements and layer them over CG elements or combine them with other scans.

### Prep/Paint

![prep example](./images/prep_before_after.jpg)

*image: http://www.btlnews.com/crafts/visual-fx/level-256-produces-126-vfx-shots-for-the-bourne-legacy/*

Prep have the job of cleaning up scans, ready for comp, mainly by painting. Painting, in the context of Prep, refers to the skill of believably reconstructing detail in a part of a scan that has been partially or completely occluded, by sampling from similar areas on the same or surrounding frames, or reference images. Some common paint removal tasks are required for:

- Dust shadows from footage shot on physical film.
- Wires from actor harnesses.
- Accidental or unavoidable boom poles, camera rigs and film crew members.
- Items that conflict with latest creative decisions or that create continuity issues.


### Comp

![Mad Max Fury Road Comp](./images/mad_max_fx.jpg)

*image: Iloura*

A comper's role is to combine the work of all of the earlier artists departments into a final shot. This involves combining any CG elements, DMP (Digital Matte Painting) work, prep elements and roto mattes with live action scans, in a way that looks believable enough to fool a viewer that it was shot once, through the lens of a single real camera.

An organised example of a Nuke node graph:

![Example Node Graph](./images/nuke_node_graph.jpg)

*image: http://www.jinguanghuang.com/compositing*

The most commonly used industry compositing software package is currently Nuke, which has been developed by The Foundry since 2007. It uses a node-based system, rather than the layer-based system found in compositing software such as the also very popular Adobe After Effects. One significant advantage of the node-based workflow is that it makes collaboration much easier. You can easily get an idea of what is happening in a well-organised nuke scene by zooming out and looking at the entire node graph, something that is much more difficult to do in a layer based system, especially when you are dealing with very large scene's (which is very likely in a VFX studio).

