# awesome-holography

A curated list of resources on holographic displays, inspired by [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision).

## Disclaimer

This list is compiled during my paper survey about holographic displays, and is not meant to be exhuastive. The list is organized for me to easily navigate different topics in holography. I would like to thank the authors of the following papers for providing great references:

- [Neural Holography with Camera-in-the-loop Training](https://www.computationalimaging.org/publications/neuralholography/) (Peng et al. 2020)
- [Learned Hardware-in-the-loop Phase Retrieval for Holographic Near-Eye Displays](https://light.princeton.edu/publication/hil-holography/) (Chakravarthula et al. 2020)

## Table of Contents
- [Background, Theory, and Survey](#background-theory-and-survey)
- [Computer Generated Holography (CGH)](#computer-generated-holography-cgh)
    - [Traditional Heuristic Methods](#traditional-heuristic-methods)
    - [Iterative Methods](#iterative-methods)
    - [Data-driven (Learning-based) Methods](#data-driven-learning-based-methods)
- [Holographic Display Architectures and Optics](#holographic-display-architectures-and-optics)
- [Etendue, Eyebox, Pupil Related](#etendue-eyebox-pupil-related)
- [Labs and Researchers](#labs-and-researchers)

## Background, Theory, and Survey
### Background and Theory
- [Introduction to Fourier Optics](https://books.google.com.tw/books/about/Introduction_to_Fourier_Optics.html?id=QllRAAAAMAAJ&redir_esc=y) by Joseph W. Goodman is a great book to learn the basics of wave propagation and holography.

### Survey Papers
- [Toward the next-generation VR/AR optics: a review of holographic near-eye displays from a human-centric perspective](https://opg.optica.org/optica/fulltext.cfm?uri=optica-7-11-1563&id=442336) (Chang et al. 2020)
- [Deep learning in holography and coherent imaging](https://www.nature.com/articles/s41377-019-0196-0) (Rivenson et al. 2019)

## Computer Generated Holography (CGH)

### Traditional Heuristic Methods

#### Point-based Methods

Some methods are based on the double phase encoding scheme, where two phase-only modulation patterns are interleaved on a single SLM:

- [Computer-generated double-phase holograms](https://opg.optica.org/ao/abstract.cfm?uri=ao-17-24-3874) (Hsueh et al. 1978) proposed to decompose a complex field into two phase-only components to generate holograms using a single phase-only SLM.
- [Holographic Near-Eye Displays for Virtual and Augmented Reality](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/holo_author.pdf) (Maimone et al. 2017) proposed a holographic near-eye display system based on the double phase encoding scheme.

Others methods include:
- [Near-eye Light Field Holographic Rendering with Spherical Waves for Wide Field of View Interactive 3D Computer Graphics](https://people.csail.mit.edu/liangs/papers/ToG17.pdf) (Shi et al. 2017)

#### Polygon/Mesh-based Methods
- [Computer-generated holograms of 3-D objects composed of tilted planar segments](https://opg.optica.org/ao/abstract.cfm?uri=ao-27-14-3020) (Leseberg et al. 1988)
- [Computer-generated holograms of tilted planes by a spatial frequency approach](https://opg.optica.org/josaa/ViewMedia.cfm?uri=josaa-10-2-299&seq=0&guid=37d8e19b-51f8-478e-936a-7a3c8c405b54) (Tommasi et al. 1993) 
- [Computer-generated holograms for three-dimensional surface objects with shade and texture](https://opg.optica.org/ao/abstract.cfm?uri=ao-44-22-4607) (Matsushima 2005)
- [Extremely high-definition full-parallax computer-generated hologram created by the polygon-based method](https://opg.optica.org/ao/fulltext.cfm?uri=ao-48-34-H54&id=186427) (Matsushima et al. 2009)
- [Silhouette method for hidden surface removal in computer holography and its acceleration using the switch-back technique](https://opg.optica.org/oe/fulltext.cfm?uri=oe-22-20-24450&id=301771) (Matsushima et al. 2014)
- [Computer generated holograms from three dimensional meshes using an analytic light transport model](https://opg.optica.org/ao/abstract.cfm?uri=ao-47-10-1567) (Ahrenberg et al. 2008)
- [Fast and effective occlusion culling for 3D holographic displays by inverse orthographic projection with low angular sampling](https://opg.optica.org/ao/abstract.cfm?uri=ao-53-27-6287) (Jia et al. 2014)

#### Layer-based Methods
- [Computer-generated hologram with occlusion effect using layer-based processing](https://opg.optica.org/ao/abstract.cfm?uri=ao-56-13-F138) (Zhang et al. 2017)
- [Accurate calculation of computer-generated holograms using angular-spectrum layer-oriented method](https://opg.optica.org/oe/fulltext.cfm?uri=oe-23-20-25440&id=326909) (Zhao et al. 2015)
- [Improved layer-based method for rapid hologram generation and real-time interactive holographic display applications](https://opg.optica.org/oe/fulltext.cfm?uri=oe-23-14-18143&id=321638) (Chen et al. 2015)
- [Computer generated hologram with geometric occlusion using GPU-accelerated depth buffer rasterization for three-dimensional display](https://opg.optica.org/ao/abstract.cfm?uri=ao-48-21-4246) (Chen et al. 2009)

#### Holographic Stereograms
- [Holographic near-eye displays based on overlap-add stereograms](http://www.computationalimaging.org/publications/holographic-near-eye-displays-based-on-overlap-add-stereograms-siggraph-asia-2019/) (Padmanaban et al. 2019)
- [Layered holographic stereogram based on inverse Fresnel diffraction](https://opg.optica.org/ao/abstract.cfm?uri=ao-55-3-A154) (Zhang et al. 2016)
- [Fully computed holographic stereogram based algorithm for computer-generated holograms with accurate depth cues](https://opg.optica.org/oe/fulltext.cfm?uri=oe-23-4-3901&id=311865) (Zhang et al. 2015)

### Iterative Methods
A family of iterative methods is based on the **Gerchberg-Saxton (GS) Algorithm** where the phase and amplitute patterns at two planes are updated iteratively as the wave propagates back and forth between the two planes:

- [A practical algorithm for the determination of phase from image and diffraction plane pictures](http://www.u.arizona.edu/~ppoon/GerchbergandSaxton1972.pdf) (Gerchberg et al. 1972) proposed the **Gerchberg-Saxton (GS) Algorithm**
- [Mix-and-Match Holography](http://www.cs.ubc.ca/labs/imager/tr/2017/MixMatchHolography/MixMatchHolography_YPeng_SA17_LowRes.pdf) (Peng et al. 2017) proposed an interative phase-retrieval method built upon GS
- [Fresnel ping-pong algorithm for two-plane computer-generated hologram display](https://opg.optica.org/ao/ViewMedia.cfm?uri=ao-33-5-869&seq=0&guid=cd9375f1-824e-4719-a271-624d5c09ccca&html=true) (Dorsch et al. 1994) 

Other optimization based methods leverage gradient descent or non-convex optimization techniques to optimize the phase pattern of the SLM:

- [Hogel-free Holography](https://dl.acm.org/doi/pdf/10.1145/3516428)(Chakravarthula et al. 2022)
- [Multi-depth hologram generation using stochastic gradient descent algorithm with complex loss function](https://opg.optica.org/oe/fulltext.cfm?uri=oe-29-10-15089&id=450644) (Chen et al. 2021)
- [Realistic Defocus Blur for Multiplane Computer-Generated Holography](https://arxiv.org/abs/2205.07030) (Kavaklı et al. 2021) proposed a novel loss function aimed to synthesize high quality defocus blur, and can be intergated in various iterative (GS, gradient-descent) and non-iterative (double phase encoding) methods. 
- [Wirtinger Holography for Near-Eye Displays](https://www.cs.princeton.edu/~fheide/wirtingerholography) (Chakravarthula et al. 2019) optimizes the phase-only SLM pattern using closed-form Wirtinger complex derivatives in gradient descent.
- [3D computer-generated holography by non-convex optimization](https://opg.optica.org/optica/fulltext.cfm?uri=optica-4-10-1306&id=375391) (Zhang et al. 2017)
   
Unfortunately, iterative methods are inherently slow and thus not suitble for real-time CGH.

### Data-driven (Learning-based) Methods

A major focus in deep learning for CGH is using camera-in-the-loop (CITL) training to learn an accurate free space wave propagation and optical hardware model for holographic displays:
- [Neural Holography with Camera-in-the-loop Training](https://www.computationalimaging.org/publications/neuralholography/) (Peng et al. 2020) is the first to use **camera-in-the-loop training (CITL)** to optimize a parameterized wave propagation model, where optical aberrations, SLM non-linearities, and etc are learned from data. A CNN is also proposed to synthesize 2D and 3D holograms in real-time. 
- [Neural 3D Holography: Learning Accurate Wave Propagation Models for 3D Holographic Virtual and Augmented Reality Displays](https://www.computationalimaging.org/publications/neuralholography3d/) (Choi et al. 2021) uses two CNNs to directly model optical aberrations, SLM non-linearities, and etc, at the input plane and **multiple** target planes. The usage of two CNNs introduces more degrees of freedom than that of the parameterized propagation model proposed in Peng et al. 2020, such that higher quality 3D holograms can be achieved.
- [Time-multiplexed Neural Holography: A Flexible Framework for Holographic Near-eye Displays with Fast Heavily-quantized Spatial Light Modulators](https://www.computationalimaging.org/publications/time-multiplexed-neural-holography/) (Choi et al. 2022) leveraged time-multiplexed quantized SLM patterns to synthesize high quality defocus blur. 
- [Learned Hardware-in-the-loop Phase Retrieval for Holographic Near-Eye Displays](https://light.princeton.edu/publication/hil-holography/) (Chakravarthula et al. 2020) uses CITL to learn an aberration approximator that models the residual between holograms generated from ideal wave propagation (i.e. ASM) and real-world wave propagation models. An adversarial loss is used in addition to reconstruction loss to optimize the synthesized holograms.
   
Instead of using a predetermined convolution kernel to compute wave propagation (i.e. the angular spectrum method), [Learned holographic light transport](https://arxiv.org/pdf/2108.08253.pdf) (Kavaklı et al. 2021) learns the wave propagation convolution kernel directly from images captured by a physical holographic display.

Previous works assume a naive wave propagation model (i.e. the angular spectrum method), and directly regresses complex holograms using different CNN architectures:
- [Towards real-time photorealistic 3D holography with deep neural networks](https://cdfg.mit.edu/publications/tensor-holography) (Shi et al. 2021) 
- [DeepCGH: 3D computer-generated holography using deep learning](https://opg.optica.org/oe/fulltext.cfm?uri=oe-28-18-26636&id=437573) (Eybposh et al. 2020) uses a CNN to estimate a complex field at a fixed plane from a set of 3D target multiplane inputs; the complex field is then reverse propagated to the SLM plane to generate a phase pattern.
- [Deep neural network for multi-depth hologram generation and its training strategy](https://opg.optica.org/oe/fulltext.cfm?uri=oe-28-18-27137&id=437709) (Lee et al. 2020) directly estimates the SLM phase pattern from 3D target multiplane inputs using a CNN.
- [Deep-learning-generated holography](https://opg.optica.org/ao/abstract.cfm?uri=ao-57-14-3859) (Horisaki et al. 2018)
- [Phase recovery and holographic image reconstruction using deep learning in neural networks](https://www.nature.com/articles/lsa2017141) (Rivenson et al. 2018)


## Holographic Display Architectures and Optics

Most CGH display frameworks use coherent light source (laser) and a single phase-only SLM. The following works explore alternatives to the current paradigm, such as using partially-coherent light sources, amplitude SLMs, and adding additional optical elements.
   
Partially-coherent light sources are used to reduce speckle artifacts:
- [Speckle-free holography with partially coherent light sources and camera-in-the-loop calibration](https://www.computationalimaging.org/publications/partiallycoherentholography/) (Peng et al. 2021) uses partially coherent light sources and camera-in-the-loop optimization to reduce speckle artifacts.
- [Light source optimization for partially coherent holographic displays with consideration of speckle contrast, resolution, and depth of field](https://www.nature.com/articles/s41598-020-75947-0)
- [Holographic head-mounted display with RGB light emitting diode light source](https://opg.optica.org/oe/fulltext.cfm?uri=oe-22-6-6526&id=281866) (Moon et al. 2014)

Special optical elements are used to improve the holographic display quality:
- [Monocular 3D see-through head-mounted display via complex amplitude modulation](https://opg.optica.org/oe/fulltext.cfm?uri=oe-24-15-17372&id=348011) (Gao et al. 2016)
- [Optimizing image quality for holographic near-eye displays with Michelson Holography](https://opg.optica.org/optica/fulltext.cfm?uri=optica-8-2-143&id=446984) (Choi et al. 2021)
- [Holographic Optics for Thin and Lightweight Virtual Reality](https://dl.acm.org/doi/abs/10.1145/3386569.3392416) (Maimone et al. 2020)
- [Retinal 3D: augmented reality near-eye display via pupil-tracked light field projection on retina](https://dl.acm.org/doi/10.1145/3130800.3130889) (Jang et al. 2017)
- [Holographic display for see-through augmented reality using mirror-lens holographic optical element](https://opg.optica.org/ol/abstract.cfm?uri=ol-41-11-2486) (Li et al. 2016)
- [3D holographic head mounted display using holographic optical elements with astigmatism aberration compensation](https://opg.optica.org/oe/fulltext.cfm?uri=oe-23-25-32025&id=333174) (Yeom et al. 2015)
   
Bulky headsets hamper the development of AR/VR. Reducing the size of holographic displays are important:
- [Holographic Glasses for Virtual Reality](https://research.nvidia.com/publication/2022-08_holographic-glasses-virtual-reality) (Kim et al. 2022) presents a holographic display system with eyeglasses-like form factor. An optical stack of 2.5mm is achieved by combining pupil-replicating waveguide, SLMs, and geometric phase lenses.


## Etendue, Eyebox, Pupil Related
- [Pupil-aware Holography](https://arxiv.org/pdf/2203.14939.pdf) (Chakravarthula et al. 2022)
- [Neural Etendue Expander for Ultra-Wide-Angle High-Fidelity Holographic Display](https://arxiv.org/abs/2109.08123) (Baek et al. 2022)
- [High Resolution étendue expansion for holographic displays](https://dl.acm.org/doi/abs/10.1145/3386569.3392414) (Kuo et al. 2020)
- [Holographic Near-eye Display with Expanded Eye-box](https://dl.acm.org/doi/10.1145/3272127.3275069) (Jang et al. 2018)

## Labs and Researchers
- [Computational Imaging Lab, Stanford University](https://www.computationalimaging.org)
- [Computational Imaging Lab, Princeton University](https://light.princeton.edu)
- [Computational Biophotonics Laboratory, UNC Chapel Hill](http://www.nicolaspegard.com/index.php)
- [Graphics and Virtual Reality Group, UNC Chapel Hill](https://telepresence.web.unc.edu)
- [Computational Light Laboratory, University College London](https://complightlab.com)
- [Computational Imaging Group, KAUST](https://vccimaging.org/publications.html)
- [Optical Engineering and Quantum Electronics Lab, Seoul National University](http://oeqelab.snu.ac.kr)
- [NVIDIA Research](https://www.nvidia.com/en-us/research/)

## Reference
- Ref Link: [https://github.com/bchao1/awesome-holography](https://github.com/bchao1/awesome-holography)