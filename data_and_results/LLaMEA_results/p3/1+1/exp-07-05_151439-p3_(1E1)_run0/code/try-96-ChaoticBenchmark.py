import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyper-chaotic modulation with modified nested sinusoidal structures and dynamic phase locking
        chaotic_term = np.sum(np.sin(233 * np.sin(np.cos(x))) * np.cos(197 * np.cos(np.sin(x))) * 
                             (1 + 0.73 * np.sin(np.sum(x**3.1)) * np.cos(np.sum(x**4.2)) * 
                              np.sin(np.sum(x**5.4)) * np.cos(np.sum(x**6.1)) * 
                              np.sin(np.sum(x**7.8)) * np.cos(np.sum(x**8.5)) * 
                              np.sin(np.sum(x**9.3)) * np.cos(np.sum(x**10.7)))) / self.dim
        
        # Quantum-resonant polynomial with modified exponents and dynamic scaling
        poly_term = np.sum((6.8 + 0.59 * np.sin(self.dim * 1.3)) * x**21 - 
                          (6.4 + 0.53 * np.cos(self.dim * 1.7)) * x**20 + 
                          (6.1 + 0.50 * np.sin(self.dim * 2.1)) * x**19 - 
                          (5.8 + 0.47 * np.cos(self.dim * 2.5)) * x**18 + 
                          (5.5 + 0.44 * np.sin(self.dim * 2.9)) * x**17 - 
                          (5.2 + 0.41 * np.cos(self.dim * 3.3)) * x**16 + 
                          (4.9 + 0.38 * np.sin(self.dim * 3.7)) * x**15 - 
                          (4.6 + 0.35 * np.cos(self.dim * 4.1)) * x**14 + 
                          (4.3 + 0.32 * np.sin(self.dim * 4.5)) * x**13 - 
                          (4.0 + 0.29 * np.cos(self.dim * 4.9)) * x**12 + 
                          (3.7 + 0.26 * np.sin(self.dim * 5.3)) * x**11 - 
                          (3.4 + 0.23 * np.cos(self.dim * 5.7)) * x**10 + 
                          (3.1 + 0.20 * np.sin(self.dim * 6.1)) * x**9 - 
                          (2.8 + 0.17 * np.cos(self.dim * 6.5)) * x**8 + 
                          (2.5 + 0.14 * np.sin(self.dim * 6.9)) * x**7 - 
                          (2.2 + 0.11 * np.cos(self.dim * 7.3)) * x**6 + 
                          (1.9 + 0.08 * np.sin(self.dim * 7.7)) * x**5 - 
                          (1.6 + 0.05 * np.cos(self.dim * 8.1)) * x**4 + 
                          (1.3 + 0.02 * np.sin(self.dim * 8.5)) * x**3) / self.dim
        
        # Multi-dimensional quantum barrier with modified interference and scaling
        barrier_term = np.sum(np.exp(-x**2 / (4.9 + 2.5 * np.sin(self.dim * 0.8))) * 
                             np.sin(14.7 * x + 1.0 * np.cos(self.dim * 1.2)) * 
                             np.cos(6.9 * x + 0.5 * np.sin(self.dim * 1.5)) * 
                             np.sin(x/5.7 + 0.3 * np.cos(self.dim * 1.8)) * 
                             np.cos(x/7.6 + 0.32 * np.sin(self.dim * 2.1)) * 
                             np.sin(x/10.2 + 0.28 * np.cos(self.dim * 2.4)) * 
                             np.cos(x/12.4 + 0.24 * np.sin(self.dim * 2.7)) * 
                             np.sin(x/15.0 + 0.20 * np.cos(self.dim * 3.0)) * 
                             np.cos(x/17.8 + 0.16 * np.sin(self.dim * 3.3))) / self.dim
        
        # Hyper-fractal attractor with modified exponents and scaling
        attractor_term = np.sum(np.sin(np.exp(x/4.1 + 0.4 * np.sin(self.dim * 0.9))) * 
                               np.cos(np.exp(-x/6.4 + 0.40 * np.cos(self.dim * 1.1))) * 
                               np.sin(x/6.0 + 0.28 * np.sin(self.dim * 1.3)) * 
                               np.cos(x/9.5 + 0.26 * np.cos(self.dim * 1.5)) * 
                               np.sin(x/8.7 + 0.23 * np.sin(self.dim * 1.7)) * 
                               np.cos(x/13.1 + 0.20 * np.cos(self.dim * 1.9)) * 
                               np.sin(x/11.5 + 0.16 * np.sin(self.dim * 2.1)) * 
                               np.cos(x/16.0 + 0.13 * np.cos(self.dim * 2.3)) * 
                               np.sin(x/14.0 + 0.10 * np.sin(self.dim * 2.5)) * 
                               np.cos(x/19.5 + 0.08 * np.cos(self.dim * 2.7))) / self.dim
        
        # Advanced adaptive cross-dimensional coupling with modified weights and exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 4.2 + 0.7 * np.sin(i + self.dim * 1.3)
                cross_term += weight * np.abs(x[i] - x[i+1])**(4.8 + 0.8 * np.sin(i + 1.2 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel hierarchical fractal noise with modified components
        noise = (0.049 * np.random.rand() + 
                0.029 * np.sin(np.sum(x**2.7)) + 
                0.022 * np.cos(np.sum(x**3.5)) + 
                0.017 * np.sin(np.sum(x**4.3)) * np.cos(np.sum(x**5.1)) + 
                0.013 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.009 * np.cos(np.sum(x**6.4)) * np.sin(np.sum(x**7.6)) + 
                0.006 * np.sin(np.sum(x**8.1)) * np.cos(np.sum(x**9.3)) + 
                0.004 * np.cos(np.sum(x**10.1)) * np.sin(np.sum(x**11.5)) + 
                0.003 * np.sin(np.sum(x**12.2)) * np.cos(np.sum(x**13.6)) + 
                0.002 * np.cos(np.sum(x**14.1)) * np.sin(np.sum(x**15.5)) + 
                0.001 * np.sin(np.sum(x**16.0)) * np.cos(np.sum(x**17.3)))
        
        # Enhanced dynamic weighting with modified factors
        weights = [0.65 + 0.19 * np.sin(self.dim * 1.1), 
                  0.60 + 0.18 * np.cos(self.dim * 1.3), 
                  0.55 + 0.16 * np.sin(self.dim * 1.5), 
                  0.50 + 0.14 * np.cos(self.dim * 1.7), 
                  0.45 + 0.12 * np.sin(self.dim * 1.9)]
        
        # Combine all terms with modified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise