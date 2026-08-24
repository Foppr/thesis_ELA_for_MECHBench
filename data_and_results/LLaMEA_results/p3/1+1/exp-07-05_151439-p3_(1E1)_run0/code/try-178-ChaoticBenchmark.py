import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyper-chaotic modulation with increased frequency components and dynamic phase locking
        chaotic_term = np.sum(np.sin(317 * np.sin(np.cos(x))) * np.cos(251 * np.cos(np.sin(x))) * 
                             (1 + 0.87 * np.sin(np.sum(x**3.7)) * np.cos(np.sum(x**4.9)) * 
                              np.sin(np.sum(x**5.8)) * np.cos(np.sum(x**6.7)) * 
                              np.sin(np.sum(x**7.9)) * np.cos(np.sum(x**8.6)) * 
                              np.sin(np.sum(x**9.4)) * np.cos(np.sum(x**10.8)) * 
                              np.sin(np.sum(x**11.2)) * np.cos(np.sum(x**12.5)))) / self.dim
        
        # Quantum-resonant polynomial with intensified exponents and dynamic scaling
        poly_term = np.sum((7.2 + 0.65 * np.sin(self.dim * 1.5)) * x**25 - 
                          (6.8 + 0.61 * np.cos(self.dim * 1.9)) * x**24 + 
                          (6.5 + 0.58 * np.sin(self.dim * 2.3)) * x**23 - 
                          (6.2 + 0.55 * np.cos(self.dim * 2.7)) * x**22 + 
                          (5.9 + 0.52 * np.sin(self.dim * 3.1)) * x**21 - 
                          (5.6 + 0.49 * np.cos(self.dim * 3.5)) * x**20 + 
                          (5.3 + 0.46 * np.sin(self.dim * 3.9)) * x**19 - 
                          (5.0 + 0.43 * np.cos(self.dim * 4.3)) * x**18 + 
                          (4.7 + 0.40 * np.sin(self.dim * 4.7)) * x**17 - 
                          (4.4 + 0.37 * np.cos(self.dim * 5.1)) * x**16 + 
                          (4.1 + 0.34 * np.sin(self.dim * 5.5)) * x**15 - 
                          (3.8 + 0.31 * np.cos(self.dim * 5.9)) * x**14 + 
                          (3.5 + 0.28 * np.sin(self.dim * 6.3)) * x**13 - 
                          (3.2 + 0.25 * np.cos(self.dim * 6.7)) * x**12 + 
                          (2.9 + 0.22 * np.sin(self.dim * 7.1)) * x**11 - 
                          (2.6 + 0.19 * np.cos(self.dim * 7.5)) * x**10 + 
                          (2.3 + 0.16 * np.sin(self.dim * 7.9)) * x**9 - 
                          (2.0 + 0.13 * np.cos(self.dim * 8.3)) * x**8 + 
                          (1.7 + 0.10 * np.sin(self.dim * 8.7)) * x**7 - 
                          (1.4 + 0.07 * np.cos(self.dim * 9.1)) * x**6 + 
                          (1.1 + 0.04 * np.sin(self.dim * 9.5)) * x**5 - 
                          (0.8 + 0.01 * np.cos(self.dim * 9.9)) * x**4) / self.dim
        
        # Multi-dimensional quantum barrier with intensified interference and scaling
        barrier_term = np.sum(np.exp(-x**2 / (5.2 + 2.8 * np.sin(self.dim * 0.9))) * 
                             np.sin(16.3 * x + 1.2 * np.cos(self.dim * 1.3)) * 
                             np.cos(7.8 * x + 0.6 * np.sin(self.dim * 1.6)) * 
                             np.sin(x/6.1 + 0.35 * np.cos(self.dim * 1.9)) * 
                             np.cos(x/8.3 + 0.34 * np.sin(self.dim * 2.2)) * 
                             np.sin(x/11.0 + 0.30 * np.cos(self.dim * 2.5)) * 
                             np.cos(x/13.7 + 0.26 * np.sin(self.dim * 2.8)) * 
                             np.sin(x/16.5 + 0.22 * np.cos(self.dim * 3.1)) * 
                             np.cos(x/19.3 + 0.18 * np.sin(self.dim * 3.4)) * 
                             np.sin(x/22.1 + 0.14 * np.cos(self.dim * 3.7)) * 
                             np.cos(x/25.0 + 0.10 * np.sin(self.dim * 4.0))) / self.dim
        
        # Hyper-fractal attractor with intensified exponents and scaling
        attractor_term = np.sum(np.sin(np.exp(x/4.5 + 0.45 * np.sin(self.dim * 1.0))) * 
                               np.cos(np.exp(-x/6.8 + 0.42 * np.cos(self.dim * 1.2))) * 
                               np.sin(x/6.5 + 0.30 * np.sin(self.dim * 1.4)) * 
                               np.cos(x/10.0 + 0.28 * np.cos(self.dim * 1.6)) * 
                               np.sin(x/9.2 + 0.25 * np.sin(self.dim * 1.8)) * 
                               np.cos(x/13.8 + 0.22 * np.cos(self.dim * 2.0)) * 
                               np.sin(x/12.3 + 0.18 * np.sin(self.dim * 2.2)) * 
                               np.cos(x/17.2 + 0.15 * np.cos(self.dim * 2.4)) * 
                               np.sin(x/15.7 + 0.12 * np.sin(self.dim * 2.6)) * 
                               np.cos(x/20.5 + 0.09 * np.cos(self.dim * 2.8)) * 
                               np.sin(x/19.0 + 0.06 * np.sin(self.dim * 3.0)) * 
                               np.cos(x/24.0 + 0.03 * np.cos(self.dim * 3.2))) / self.dim
        
        # Advanced adaptive cross-dimensional coupling with intensified weights and exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 5.2 + 1.1 * np.sin(i + self.dim * 1.6)  # Increased weight modulation
                cross_term += weight * np.abs(x[i] - x[i+1])**(5.2 + 1.0 * np.sin(i + 1.4 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel hierarchical fractal noise with intensified components
        noise = (0.058 * np.random.rand() + 
                0.035 * np.sin(np.sum(x**2.9)) + 
                0.028 * np.cos(np.sum(x**3.7)) + 
                0.024 * np.sin(np.sum(x**4.5)) * np.cos(np.sum(x**5.3)) + 
                0.019 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.015 * np.cos(np.sum(x**6.7)) * np.sin(np.sum(x**7.9)) + 
                0.011 * np.sin(np.sum(x**8.4)) * np.cos(np.sum(x**9.6)) + 
                0.008 * np.cos(np.sum(x**10.4)) * np.sin(np.sum(x**11.8)) + 
                0.006 * np.sin(np.sum(x**12.5)) * np.cos(np.sum(x**13.9)) + 
                0.004 * np.cos(np.sum(x**14.4)) * np.sin(np.sum(x**15.8)) + 
                0.003 * np.sin(np.sum(x**16.3)) * np.cos(np.sum(x**17.7)) + 
                0.002 * np.cos(np.sum(x**18.1)) * np.sin(np.sum(x**19.5)) + 
                0.001 * np.sin(np.sum(x**20.0)) * np.cos(np.sum(x**21.4)))
        
        # Enhanced dynamic weighting with intensified factors
        weights = [0.72 + 0.21 * np.sin(self.dim * 1.25),  # Increased weight modulation
                  0.67 + 0.20 * np.cos(self.dim * 1.45), 
                  0.62 + 0.18 * np.sin(self.dim * 1.65), 
                  0.57 + 0.16 * np.cos(self.dim * 1.85), 
                  0.52 + 0.14 * np.sin(self.dim * 2.05)]
        
        # Combine all terms with intensified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise