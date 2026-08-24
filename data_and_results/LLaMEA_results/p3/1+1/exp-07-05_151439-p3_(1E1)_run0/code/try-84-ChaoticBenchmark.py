import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyper-chaotic modulation with nested sinusoidal structures and dynamic phase locking
        chaotic_term = np.sum(np.sin(257 * np.sin(np.cos(x))) * np.cos(173 * np.cos(np.sin(x))) * 
                             (1 + 0.81 * np.sin(np.sum(x**3.7)) * np.cos(np.sum(x**4.9)) * 
                              np.sin(np.sum(x**5.8)) * np.cos(np.sum(x**6.7)) * 
                              np.sin(np.sum(x**7.3)) * np.cos(np.sum(x**8.2)) * 
                              np.sin(np.sum(x**9.1)) * np.cos(np.sum(x**10.4)))) / self.dim
        
        # Quantum-resonant polynomial with dynamic scaling and multi-frequency harmonic interactions
        poly_term = np.sum((7.2 + 0.63 * np.sin(self.dim * 1.5)) * x**23 - 
                          (6.8 + 0.57 * np.cos(self.dim * 1.9)) * x**22 + 
                          (6.5 + 0.54 * np.sin(self.dim * 2.3)) * x**21 - 
                          (6.2 + 0.51 * np.cos(self.dim * 2.7)) * x**20 + 
                          (5.9 + 0.48 * np.sin(self.dim * 3.1)) * x**19 - 
                          (5.6 + 0.45 * np.cos(self.dim * 3.5)) * x**18 + 
                          (5.3 + 0.42 * np.sin(self.dim * 3.9)) * x**17 - 
                          (5.0 + 0.39 * np.cos(self.dim * 4.3)) * x**16 + 
                          (4.7 + 0.36 * np.sin(self.dim * 4.7)) * x**15 - 
                          (4.4 + 0.33 * np.cos(self.dim * 5.1)) * x**14 + 
                          (4.1 + 0.30 * np.sin(self.dim * 5.5)) * x**13 - 
                          (3.8 + 0.27 * np.cos(self.dim * 5.9)) * x**12 + 
                          (3.5 + 0.24 * np.sin(self.dim * 6.3)) * x**11 - 
                          (3.2 + 0.21 * np.cos(self.dim * 6.7)) * x**10 + 
                          (2.9 + 0.18 * np.sin(self.dim * 7.1)) * x**9 - 
                          (2.6 + 0.15 * np.cos(self.dim * 7.5)) * x**8 + 
                          (2.3 + 0.12 * np.sin(self.dim * 7.9)) * x**7 - 
                          (2.0 + 0.09 * np.cos(self.dim * 8.3)) * x**6 + 
                          (1.7 + 0.06 * np.sin(self.dim * 8.7)) * x**5 - 
                          (1.4 + 0.03 * np.cos(self.dim * 9.1)) * x**4 + 
                          (1.1 + 0.01 * np.sin(self.dim * 9.5)) * x**3) / self.dim
        
        # Multi-dimensional quantum barrier with complex interference and dynamic scaling
        barrier_term = np.sum(np.exp(-x**2 / (5.1 + 2.7 * np.sin(self.dim * 0.9))) * 
                             np.sin(15.3 * x + 1.1 * np.cos(self.dim * 1.3)) * 
                             np.cos(7.2 * x + 0.6 * np.sin(self.dim * 1.6)) * 
                             np.sin(x/5.9 + 0.4 * np.cos(self.dim * 1.9)) * 
                             np.cos(x/7.8 + 0.35 * np.sin(self.dim * 2.2)) * 
                             np.sin(x/10.5 + 0.3 * np.cos(self.dim * 2.5)) * 
                             np.cos(x/12.7 + 0.25 * np.sin(self.dim * 2.8)) * 
                             np.sin(x/15.3 + 0.2 * np.cos(self.dim * 3.1)) * 
                             np.cos(x/18.1 + 0.15 * np.sin(self.dim * 3.4))) / self.dim
        
        # Hyper-fractal attractor with non-integer exponents and dynamic scaling
        attractor_term = np.sum(np.sin(np.exp(x/4.3 + 0.5 * np.sin(self.dim * 1.0))) * 
                               np.cos(np.exp(-x/6.7 + 0.42 * np.cos(self.dim * 1.2))) * 
                               np.sin(x/6.2 + 0.3 * np.sin(self.dim * 1.4)) * 
                               np.cos(x/9.8 + 0.28 * np.cos(self.dim * 1.6)) * 
                               np.sin(x/8.9 + 0.25 * np.sin(self.dim * 1.8)) * 
                               np.cos(x/13.4 + 0.22 * np.cos(self.dim * 2.0)) * 
                               np.sin(x/11.7 + 0.18 * np.sin(self.dim * 2.2)) * 
                               np.cos(x/16.3 + 0.15 * np.cos(self.dim * 2.4)) * 
                               np.sin(x/14.2 + 0.12 * np.sin(self.dim * 2.6)) * 
                               np.cos(x/19.8 + 0.1 * np.cos(self.dim * 2.8))) / self.dim
        
        # Advanced adaptive cross-dimensional coupling with dynamic weights, fractional exponents, and multi-scale interactions
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 4.5 + 0.8 * np.sin(i + self.dim * 1.4)
                cross_term += weight * np.abs(x[i] - x[i+1])**(5.1 + 0.9 * np.sin(i + 1.3 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel hierarchical fractal noise with multi-frequency components and dynamic scaling
        noise = (0.052 * np.random.rand() + 
                0.031 * np.sin(np.sum(x**2.9)) + 
                0.024 * np.cos(np.sum(x**3.8)) + 
                0.019 * np.sin(np.sum(x**4.5)) * np.cos(np.sum(x**5.3)) + 
                0.015 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.011 * np.cos(np.sum(x**6.7)) * np.sin(np.sum(x**7.9)) + 
                0.008 * np.sin(np.sum(x**8.4)) * np.cos(np.sum(x**9.6)) + 
                0.006 * np.cos(np.sum(x**10.3)) * np.sin(np.sum(x**11.8)) + 
                0.004 * np.sin(np.sum(x**12.5)) * np.cos(np.sum(x**13.9)) + 
                0.003 * np.cos(np.sum(x**14.4)) * np.sin(np.sum(x**15.8)) + 
                0.002 * np.sin(np.sum(x**16.2)) * np.cos(np.sum(x**17.6)))
        
        # Enhanced dynamic weighting with multi-scale factors, dimensionality-dependent adjustments, and chaotic modulation
        weights = [0.68 + 0.21 * np.sin(self.dim * 1.2), 
                  0.63 + 0.19 * np.cos(self.dim * 1.4), 
                  0.57 + 0.17 * np.sin(self.dim * 1.6), 
                  0.52 + 0.15 * np.cos(self.dim * 1.8), 
                  0.47 + 0.13 * np.sin(self.dim * 2.0)]
        
        # Combine all terms with enhanced weighting and added interaction effects
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise