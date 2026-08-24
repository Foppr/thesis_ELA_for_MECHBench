import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyper-chaotic modulation with increased frequency parameters and nested structures
        chaotic_term = np.sum(np.sin(317 * np.sin(np.cos(x))) * np.cos(251 * np.cos(np.sin(x))) * 
                             (1 + 0.85 * np.sin(np.sum(x**3.7)) * np.cos(np.sum(x**4.9)) * 
                              np.sin(np.sum(x**5.8)) * np.cos(np.sum(x**6.7)) * 
                              np.sin(np.sum(x**7.9)) * np.cos(np.sum(x**8.6)) * 
                              np.sin(np.sum(x**9.4)) * np.cos(np.sum(x**10.8)) * 
                              np.sin(np.sum(x**11.3)) * np.cos(np.sum(x**12.1)))) / self.dim
        
        # Modified quantum-resonant polynomial with higher exponents and dynamic scaling
        poly_term = np.sum((7.2 + 0.65 * np.sin(self.dim * 1.4)) * x**25 - 
                          (6.8 + 0.61 * np.cos(self.dim * 1.8)) * x**24 + 
                          (6.5 + 0.58 * np.sin(self.dim * 2.2)) * x**23 - 
                          (6.2 + 0.55 * np.cos(self.dim * 2.6)) * x**22 + 
                          (5.9 + 0.52 * np.sin(self.dim * 3.0)) * x**21 - 
                          (5.6 + 0.49 * np.cos(self.dim * 3.4)) * x**20 + 
                          (5.3 + 0.46 * np.sin(self.dim * 3.8)) * x**19 - 
                          (5.0 + 0.43 * np.cos(self.dim * 4.2)) * x**18 + 
                          (4.7 + 0.40 * np.sin(self.dim * 4.6)) * x**17 - 
                          (4.4 + 0.37 * np.cos(self.dim * 5.0)) * x**16 + 
                          (4.1 + 0.34 * np.sin(self.dim * 5.4)) * x**15 - 
                          (3.8 + 0.31 * np.cos(self.dim * 5.8)) * x**14 + 
                          (3.5 + 0.28 * np.sin(self.dim * 6.2)) * x**13 - 
                          (3.2 + 0.25 * np.cos(self.dim * 6.6)) * x**12 + 
                          (2.9 + 0.22 * np.sin(self.dim * 7.0)) * x**11 - 
                          (2.6 + 0.19 * np.cos(self.dim * 7.4)) * x**10 + 
                          (2.3 + 0.16 * np.sin(self.dim * 7.8)) * x**9 - 
                          (2.0 + 0.13 * np.cos(self.dim * 8.2)) * x**8 + 
                          (1.7 + 0.10 * np.sin(self.dim * 8.6)) * x**7 - 
                          (1.4 + 0.07 * np.cos(self.dim * 9.0)) * x**6 + 
                          (1.1 + 0.04 * np.sin(self.dim * 9.4)) * x**5 - 
                          (0.8 + 0.01 * np.cos(self.dim * 9.8)) * x**4) / self.dim
        
        # Enhanced multi-dimensional quantum barrier with more complex interference patterns
        barrier_term = np.sum(np.exp(-x**2 / (5.2 + 2.8 * np.sin(self.dim * 0.9))) * 
                             np.sin(16.3 * x + 1.2 * np.cos(self.dim * 1.3)) * 
                             np.cos(7.8 * x + 0.6 * np.sin(self.dim * 1.6)) * 
                             np.sin(x/6.1 + 0.35 * np.cos(self.dim * 1.9)) * 
                             np.cos(x/8.4 + 0.34 * np.sin(self.dim * 2.2)) * 
                             np.sin(x/11.2 + 0.31 * np.cos(self.dim * 2.5)) * 
                             np.cos(x/13.8 + 0.29 * np.sin(self.dim * 2.8)) * 
                             np.sin(x/16.5 + 0.26 * np.cos(self.dim * 3.1)) * 
                             np.cos(x/19.2 + 0.23 * np.sin(self.dim * 3.4)) * 
                             np.sin(x/22.1 + 0.20 * np.cos(self.dim * 3.7)) * 
                             np.cos(x/25.0 + 0.17 * np.sin(self.dim * 4.0))) / self.dim
        
        # Enhanced hyper-fractal attractor with more complex nested structures
        attractor_term = np.sum(np.sin(np.exp(x/4.8 + 0.45 * np.sin(self.dim * 1.0))) * 
                               np.cos(np.exp(-x/7.2 + 0.42 * np.cos(self.dim * 1.2))) * 
                               np.sin(x/6.8 + 0.30 * np.sin(self.dim * 1.4)) * 
                               np.cos(x/10.3 + 0.28 * np.cos(self.dim * 1.6)) * 
                               np.sin(x/9.5 + 0.25 * np.sin(self.dim * 1.8)) * 
                               np.cos(x/14.2 + 0.22 * np.cos(self.dim * 2.0)) * 
                               np.sin(x/12.8 + 0.19 * np.sin(self.dim * 2.2)) * 
                               np.cos(x/17.5 + 0.16 * np.cos(self.dim * 2.4)) * 
                               np.sin(x/15.7 + 0.13 * np.sin(self.dim * 2.6)) * 
                               np.cos(x/20.8 + 0.10 * np.cos(self.dim * 2.8)) * 
                               np.sin(x/19.3 + 0.08 * np.sin(self.dim * 3.0)) * 
                               np.cos(x/24.1 + 0.06 * np.cos(self.dim * 3.2))) / self.dim
        
        # Advanced adaptive cross-dimensional coupling with modified weights and exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 5.1 + 0.9 * np.sin(i + self.dim * 1.5)  # Increased weight modulation
                cross_term += weight * np.abs(x[i] - x[i+1])**(5.2 + 0.9 * np.sin(i + 1.3 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel hierarchical fractal noise with enhanced components
        noise = (0.058 * np.random.rand() + 
                0.035 * np.sin(np.sum(x**2.9)) + 
                0.028 * np.cos(np.sum(x**3.7)) + 
                0.021 * np.sin(np.sum(x**4.5)) * np.cos(np.sum(x**5.3)) + 
                0.016 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.011 * np.cos(np.sum(x**6.7)) * np.sin(np.sum(x**7.9)) + 
                0.008 * np.sin(np.sum(x**8.4)) * np.cos(np.sum(x**9.6)) + 
                0.005 * np.cos(np.sum(x**10.3)) * np.sin(np.sum(x**11.7)) + 
                0.004 * np.sin(np.sum(x**12.4)) * np.cos(np.sum(x**13.8)) + 
                0.003 * np.cos(np.sum(x**14.3)) * np.sin(np.sum(x**15.7)) + 
                0.002 * np.sin(np.sum(x**16.2)) * np.cos(np.sum(x**17.6)) + 
                0.001 * np.cos(np.sum(x**18.1)) * np.sin(np.sum(x**19.5)))
        
        # Enhanced dynamic weighting with modified factors
        weights = [0.71 + 0.21 * np.sin(self.dim * 1.2),  # Increased weight modulation
                  0.66 + 0.19 * np.cos(self.dim * 1.4), 
                  0.61 + 0.17 * np.sin(self.dim * 1.6), 
                  0.56 + 0.15 * np.cos(self.dim * 1.8), 
                  0.51 + 0.13 * np.sin(self.dim * 2.0)]
        
        # Combine all terms with modified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise