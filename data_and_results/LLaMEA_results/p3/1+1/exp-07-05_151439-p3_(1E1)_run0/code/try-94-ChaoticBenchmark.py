import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyper-chaotic modulation with fractal coupling and multi-scale sinusoids
        chaotic_term = np.sum(np.sin(317 * np.sin(np.cos(x))) * np.cos(251 * np.cos(np.sin(x))) * 
                             (1 + 0.85 * np.sin(np.sum(x**3.7)) * np.cos(np.sum(x**4.9)) * 
                              np.sin(np.sum(x**5.8)) * np.cos(np.sum(x**6.7)) * 
                              np.sin(np.sum(x**7.9)) * np.cos(np.sum(x**8.3)) * 
                              np.sin(np.sum(x**9.6)) * np.cos(np.sum(x**10.4)) * 
                              np.sin(np.sum(x**11.2)) * np.cos(np.sum(x**12.1)))) / self.dim
        
        # Quantum-resonant polynomial with increased complexity and dynamic scaling
        poly_term = np.sum((7.2 + 0.65 * np.sin(self.dim * 1.5)) * x**23 - 
                          (6.8 + 0.61 * np.cos(self.dim * 1.9)) * x**22 + 
                          (6.5 + 0.58 * np.sin(self.dim * 2.3)) * x**21 - 
                          (6.2 + 0.55 * np.cos(self.dim * 2.7)) * x**20 + 
                          (5.9 + 0.52 * np.sin(self.dim * 3.1)) * x**19 - 
                          (5.6 + 0.49 * np.cos(self.dim * 3.5)) * x**18 + 
                          (5.3 + 0.46 * np.sin(self.dim * 3.9)) * x**17 - 
                          (5.0 + 0.43 * np.cos(self.dim * 4.3)) * x**16 + 
                          (4.7 + 0.40 * np.sin(self.dim * 4.7)) * x**15 - 
                          (4.4 + 0.37 * np.cos(self.dim * 5.1)) * x**14 + 
                          (4.1 + 0.34 * np.sin(self.dim * 5.5)) * x**13 - 
                          (3.8 + 0.31 * np.cos(self.dim * 5.9)) * x**12 + 
                          (3.5 + 0.28 * np.sin(self.dim * 6.3)) * x**11 - 
                          (3.2 + 0.25 * np.cos(self.dim * 6.7)) * x**10 + 
                          (2.9 + 0.22 * np.sin(self.dim * 7.1)) * x**9 - 
                          (2.6 + 0.19 * np.cos(self.dim * 7.5)) * x**8 + 
                          (2.3 + 0.16 * np.sin(self.dim * 7.9)) * x**7 - 
                          (2.0 + 0.13 * np.cos(self.dim * 8.3)) * x**6 + 
                          (1.7 + 0.10 * np.sin(self.dim * 8.7)) * x**5 - 
                          (1.4 + 0.07 * np.cos(self.dim * 9.1)) * x**4 + 
                          (1.1 + 0.04 * np.sin(self.dim * 9.5)) * x**3) / self.dim
        
        # Multi-dimensional quantum interference with higher-order coupling
        barrier_term = np.sum(np.exp(-x**2 / (5.1 + 2.7 * np.sin(self.dim * 0.9))) * 
                             np.sin(16.3 * x + 1.2 * np.cos(self.dim * 1.3)) * 
                             np.cos(7.8 * x + 0.6 * np.sin(self.dim * 1.6)) * 
                             np.sin(x/6.1 + 0.35 * np.cos(self.dim * 1.9)) * 
                             np.cos(x/8.4 + 0.38 * np.sin(self.dim * 2.2)) * 
                             np.sin(x/11.0 + 0.32 * np.cos(self.dim * 2.5)) * 
                             np.cos(x/13.7 + 0.29 * np.sin(self.dim * 2.8)) * 
                             np.sin(x/16.5 + 0.25 * np.cos(self.dim * 3.1)) * 
                             np.cos(x/19.3 + 0.21 * np.sin(self.dim * 3.4)) * 
                             np.sin(x/22.1 + 0.18 * np.cos(self.dim * 3.7)) * 
                             np.cos(x/25.0 + 0.15 * np.sin(self.dim * 4.0))) / self.dim
        
        # Fractal attractor with enhanced chaotic dynamics and multi-scale interference
        attractor_term = np.sum(np.sin(np.exp(x/4.7 + 0.45 * np.sin(self.dim * 1.0))) * 
                               np.cos(np.exp(-x/7.2 + 0.42 * np.cos(self.dim * 1.2))) * 
                               np.sin(x/6.8 + 0.30 * np.sin(self.dim * 1.4)) * 
                               np.cos(x/10.2 + 0.28 * np.cos(self.dim * 1.6)) * 
                               np.sin(x/9.4 + 0.25 * np.sin(self.dim * 1.8)) * 
                               np.cos(x/14.3 + 0.22 * np.cos(self.dim * 2.0)) * 
                               np.sin(x/12.6 + 0.18 * np.sin(self.dim * 2.2)) * 
                               np.cos(x/17.5 + 0.15 * np.cos(self.dim * 2.4)) * 
                               np.sin(x/15.8 + 0.12 * np.sin(self.dim * 2.6)) * 
                               np.cos(x/20.5 + 0.09 * np.cos(self.dim * 2.8)) * 
                               np.sin(x/18.9 + 0.06 * np.sin(self.dim * 3.0)) * 
                               np.cos(x/23.4 + 0.03 * np.cos(self.dim * 3.2))) / self.dim
        
        # Enhanced cross-dimensional coupling with adaptive weights and fractal exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 4.8 + 0.9 * np.sin(i + self.dim * 1.5)
                cross_term += weight * np.abs(x[i] - x[i+1])**(5.2 + 0.9 * np.sin(i + 1.4 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Fractal noise with hierarchical multi-scale components
        noise = (0.055 * np.random.rand() + 
                0.033 * np.sin(np.sum(x**2.9)) + 
                0.026 * np.cos(np.sum(x**3.7)) + 
                0.020 * np.sin(np.sum(x**4.5)) * np.cos(np.sum(x**5.3)) + 
                0.015 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.010 * np.cos(np.sum(x**6.7)) * np.sin(np.sum(x**7.9)) + 
                0.007 * np.sin(np.sum(x**8.4)) * np.cos(np.sum(x**9.6)) + 
                0.005 * np.cos(np.sum(x**10.3)) * np.sin(np.sum(x**11.7)) + 
                0.004 * np.sin(np.sum(x**12.4)) * np.cos(np.sum(x**13.8)) + 
                0.003 * np.cos(np.sum(x**14.5)) * np.sin(np.sum(x**15.9)) + 
                0.002 * np.sin(np.sum(x**16.6)) * np.cos(np.sum(x**17.9)) + 
                0.001 * np.cos(np.sum(x**18.2)) * np.sin(np.sum(x**19.5)))
        
        # Dynamic weighting with enhanced complexity
        weights = [0.70 + 0.21 * np.sin(self.dim * 1.2), 
                  0.65 + 0.20 * np.cos(self.dim * 1.4), 
                  0.60 + 0.19 * np.sin(self.dim * 1.6), 
                  0.55 + 0.18 * np.cos(self.dim * 1.8), 
                  0.50 + 0.17 * np.sin(self.dim * 2.0)]
        
        # Combine all terms with enhanced weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise