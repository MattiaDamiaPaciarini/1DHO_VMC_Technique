# 1DHO_VMC_Technique
The code has been typed in order to take a bit of confidence with VMC technique. It consists on two different approaches to the solution of the same problem.
In particular, the system taken into account is a 1-D harmonic oscillator in quantum mechanics with a particular potential and the aim of the code is to find its ground state energy with the VMC technique.
## Standard Approach
The energy expectation value can be written as follows:

<img src="https://latex.codecogs.com/svg.image?<E(\alpha)>&space;=&space;\frac{&space;\int&space;|\psi(x,\alpha)|^2&space;E_{loc}(x,\alpha)\,dx}{\int|\psi(x,\alpha)|^2&space;\,dx}" title="<E(\alpha)> = \frac{ \int |\psi(x,\alpha)|^2 E_{loc}(x,\alpha)\,dx}{\int|\psi(x,\alpha)|^2 \,dx}" />

with 

<img src="https://latex.codecogs.com/svg.image?\psi(x,\alpha)&space;=&space;\frac{\sqrt{\alpha}}{\pi^{1/4}&space;}&space;e^{-\frac{\alpha^2&space;x^2}{2}}" title="\psi(x,\alpha) = \frac{\sqrt{\alpha}}{\pi^{1/4} } e^{-\frac{\alpha^2 x^2}{2}}" />

To compute the integral, the positions <img src="https://latex.codecogs.com/svg.image?x" title="x" /> have been sampled from the pdf induced from the wavefunction <img src="https://latex.codecogs.com/svg.image?\psi(x,\alpha)" title="\psi(x,\alpha)" />. The evaluation of <img src="https://latex.codecogs.com/svg.image?E_{loc}(x,\alpha)" title="E_{loc}(x,\alpha)" /> follows.
The computational results are compatible with the theoretical ones of <img src="https://latex.codecogs.com/svg.image?\alpha&space;=&space;1.2389" title="\alpha = 1.2389" /> and <img src="https://latex.codecogs.com/svg.image?E_{min}&space;=&space;-3.1232" title="E_{min} = -3.1232" />, as the outputs shows:

![1DHO](https://user-images.githubusercontent.com/91092038/137986940-73654c9a-81b7-45c4-b3a1-4a07edc81905.png)


## Correlated Sampling Approach 
The second approach follows directly from the Correlated Sampling method. Through this technique, it is possible to sample the positions with only one fixed pdf computed around the minimum of <img src="https://latex.codecogs.com/svg.image?\alpha" title="\alpha" /> and to obtain a smoother behaviour of the energy. 
In particular:

<img src="https://latex.codecogs.com/svg.image?E(\alpha)&space;&space;=&space;\frac{\int&space;|\psi(x,\beta)|^2&space;\frac{|\psi(x,\alpha)|^2}{|\psi(x,\beta)|^2}&space;E_{loc}(x,\alpha)&space;\,dx}{\int&space;|\psi(x,\beta)|^2&space;\frac{|\psi(x,\alpha)|^2}{|\psi(x,\beta)|^2}&space;\,dx}&space;&space;" title="E(\alpha) = \frac{\int |\psi(x,\beta)|^2 \frac{|\psi(x,\alpha)|^2}{|\psi(x,\beta)|^2} E_{loc}(x,\alpha) \,dx}{\int |\psi(x,\beta)|^2 \frac{|\psi(x,\alpha)|^2}{|\psi(x,\be![1DHO_CS](https://user-images.githubusercontent.com/91092038/137986649-f724ae99-13de-4eda-a895-b0a017d19a4e.png)
ta)|^2} \,dx} " />

The resulting simulation offers an easier understanding of the energy behaviour



![1DHO_CS](https://user-images.githubusercontent.com/91092038/137986842-93c44f6b-2248-4654-9c93-a0aeaaf7c42b.png)

