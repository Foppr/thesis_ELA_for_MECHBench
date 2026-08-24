import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyper-chaotic modulation with multi-scale sinusoidal nesting and dynamic phase locking
        chaotic_term = np.sum(np.sin(317 * np.sin(np.cos(x))) * np.cos(251 * np.cos(np.sin(x))) * 
                             (1 + 0.81 * np.sin(np.sum(x**3.7)) * np.cos(np.sum(x**4.9)) * 
                              np.sin(np.sum(x**5.8)) * np.cos(np.sum(x**6.7)) * 
                              np.sin(np.sum(x**7.9)) * np.cos(np.sum(x**8.6)) * 
                              np.sin(np.sum(x**9.4)) * np.cos(np.sum(x**10.8)) * 
                              np.sin(np.sum(x**11.3)) * np.cos(np.sum(x**12.1)) * 
                              np.sin(np.sum(x**13.7)) * np.cos(np.sum(x**14.5)) * 
                              np.sin(np.sum(x**15.2)) * np.cos(np.sum(x**16.9)) * 
                              np.sin(np.sum(x**17.4)) * np.cos(np.sum(x**18.6)) * 
                              np.sin(np.sum(x**19.1)) * np.cos(np.sum(x**20.3)))) / self.dim
        
        # Quantum-resonant polynomial with higher-order exponents and dynamic scaling
        poly_term = np.sum((7.2 + 0.63 * np.sin(self.dim * 1.4)) * x**25 - 
                          (6.8 + 0.59 * np.cos(self.dim * 1.8)) * x**24 + 
                          (6.5 + 0.56 * np.sin(self.dim * 2.2)) * x**23 - 
                          (6.2 + 0.53 * np.cos(self.dim * 2.6)) * x**22 + 
                          (5.9 + 0.50 * np.sin(self.dim * 3.0)) * x**21 - 
                          (5.6 + 0.47 * np.cos(self.dim * 3.4)) * x**20 + 
                          (5.3 + 0.44 * np.sin(self.dim * 3.8)) * x**19 - 
                          (5.0 + 0.41 * np.cos(self.dim * 4.2)) * x**18 + 
                          (4.7 + 0.38 * np.sin(self.dim * 4.6)) * x**17 - 
                          (4.4 + 0.35 * np.cos(self.dim * 5.0)) * x**16 + 
                          (4.1 + 0.32 * np.sin(self.dim * 5.4)) * x**15 - 
                          (3.8 + 0.29 * np.cos(self.dim * 5.8)) * x**14 + 
                          (3.5 + 0.26 * np.sin(self.dim * 6.2)) * x**13 - 
                          (3.2 + 0.23 * np.cos(self.dim * 6.6)) * x**12 + 
                          (2.9 + 0.20 * np.sin(self.dim * 7.0)) * x**11 - 
                          (2.6 + 0.17 * np.cos(self.dim * 7.4)) * x**10 + 
                          (2.3 + 0.14 * np.sin(self.dim * 7.8)) * x**9 - 
                          (2.0 + 0.11 * np.cos(self.dim * 8.2)) * x**8 + 
                          (1.7 + 0.08 * np.sin(self.dim * 8.6)) * x**7 - 
                          (1.4 + 0.05 * np.cos(self.dim * 9.0)) * x**6 + 
                          (1.1 + 0.02 * np.sin(self.dim * 9.4)) * x**5) / self.dim
        
        # Multi-dimensional quantum barrier with enhanced interference and scaling
        barrier_term = np.sum(np.exp(-x**2 / (5.2 + 2.8 * np.sin(self.dim * 0.9))) * 
                             np.sin(16.3 * x + 1.2 * np.cos(self.dim * 1.3)) * 
                             np.cos(7.5 * x + 0.6 * np.sin(self.dim * 1.6)) * 
                             np.sin(x/6.1 + 0.35 * np.cos(self.dim * 1.9)) * 
                             np.cos(x/8.3 + 0.38 * np.sin(self.dim * 2.2)) * 
                             np.sin(x/11.2 + 0.31 * np.cos(self.dim * 2.5)) * 
                             np.cos(x/13.8 + 0.27 * np.sin(self.dim * 2.8)) * 
                             np.sin(x/16.7 + 0.23 * np.cos(self.dim * 3.1)) * 
                             np.cos(x/19.4 + 0.19 * np.sin(self.dim * 3.4)) * 
                             np.sin(x/22.1 + 0.15 * np.cos(self.dim * 3.7)) * 
                             np.cos(x/25.3 + 0.11 * np.sin(self.dim * 4.0))) / self.dim
        
        # Hyper-fractal attractor with increased complexity and scaling
        attractor_term = np.sum(np.sin(np.exp(x/4.7 + 0.45 * np.sin(self.dim * 1.0))) * 
                               np.cos(np.exp(-x/7.2 + 0.42 * np.cos(self.dim * 1.2))) * 
                               np.sin(x/6.8 + 0.30 * np.sin(self.dim * 1.4)) * 
                               np.cos(x/10.3 + 0.28 * np.cos(self.dim * 1.6)) * 
                               np.sin(x/9.5 + 0.25 * np.sin(self.dim * 1.8)) * 
                               np.cos(x/14.1 + 0.22 * np.cos(self.dim * 2.0)) * 
                               np.sin(x/12.7 + 0.18 * np.sin(self.dim * 2.2)) * 
                               np.cos(x/17.3 + 0.15 * np.cos(self.dim * 2.4)) * 
                               np.sin(x/15.8 + 0.12 * np.sin(self.dim * 2.6)) * 
                               np.cos(x/20.4 + 0.09 * np.cos(self.dim * 2.8)) * 
                               np.sin(x/18.9 + 0.06 * np.sin(self.dim * 3.0)) * 
                               np.cos(x/23.7 + 0.03 * np.cos(self.dim * 3.2))) / self.dim
        
        # Advanced adaptive cross-dimensional coupling with increased complexity and modified weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 4.8 + 0.9 * np.sin(i + self.dim * 1.5)
                cross_term += weight * np.abs(x[i] - x[i+1])**(5.2 + 0.9 * np.sin(i + 1.4 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel hierarchical fractal noise with enhanced components
        noise = (0.052 * np.random.rand() + 
                0.031 * np.sin(np.sum(x**2.9)) + 
                0.024 * np.cos(np.sum(x**3.7)) + 
                0.019 * np.sin(np.sum(x**4.5)) * np.cos(np.sum(x**5.3)) + 
                0.015 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.011 * np.cos(np.sum(x**6.7)) * np.sin(np.sum(x**7.9)) + 
                0.008 * np.sin(np.sum(x**8.4)) * np.cos(np.sum(x**9.6)) + 
                0.005 * np.cos(np.sum(x**10.3)) * np.sin(np.sum(x**11.7)) + 
                0.004 * np.sin(np.sum(x**12.4)) * np.cos(np.sum(x**13.8)) + 
                0.003 * np.cos(np.sum(x**14.3)) * np.sin(np.sum(x**15.7)) + 
                0.002 * np.sin(np.sum(x**16.2)) * np.cos(np.sum(x**17.5)) + 
                0.001 * np.cos(np.sum(x**18.1)) * np.sin(np.sum(x**19.4)) + 
                0.0005 * np.sin(np.sum(x**20.2)) * np.cos(np.sum(x**21.6)) + 
                0.0003 * np.cos(np.sum(x**22.3)) * np.sin(np.sum(x**23.8)) + 
                0.0001 * np.sin(np.sum(x**24.5)) * np.cos(np.sum(x**25.9)))
        
        # Enhanced dynamic weighting with modified factors
        weights = [0.68 + 0.21 * np.sin(self.dim * 1.2), 
                  0.63 + 0.20 * np.cos(self.dim * 1.4), 
                  0.58 + 0.19 * np.sin(self.dim * 1.6), 
                  0.53 + 0.18 * np.cos(self.dim * 1.8), 
                  0.48 + 0.17 * np.sin(self.dim * 2.0)]
        
        # Combine all terms with modified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise