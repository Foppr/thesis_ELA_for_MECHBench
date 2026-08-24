import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyper-chaotic modulation with increased frequency parameters
        chaotic_term = np.sum(np.sin(317 * np.sin(np.cos(x))) * np.cos(251 * np.cos(np.sin(x))) * 
                             (1 + 0.81 * np.sin(np.sum(x**3.7)) * np.cos(np.sum(x**4.9)) * 
                              np.sin(np.sum(x**5.8)) * np.cos(np.sum(x**6.7)) * 
                              np.sin(np.sum(x**7.9)) * np.cos(np.sum(x**8.6)) * 
                              np.sin(np.sum(x**9.4)) * np.cos(np.sum(x**10.8)))) / self.dim
        
        # Modified quantum-resonant polynomial with altered exponents and scaling
        poly_term = np.sum((7.2 + 0.63 * np.sin(self.dim * 1.4)) * x**23 - 
                          (6.8 + 0.57 * np.cos(self.dim * 1.8)) * x**22 + 
                          (6.5 + 0.54 * np.sin(self.dim * 2.2)) * x**21 - 
                          (6.2 + 0.51 * np.cos(self.dim * 2.6)) * x**20 + 
                          (5.9 + 0.48 * np.sin(self.dim * 3.0)) * x**19 - 
                          (5.6 + 0.45 * np.cos(self.dim * 3.4)) * x**18 + 
                          (5.3 + 0.42 * np.sin(self.dim * 3.8)) * x**17 - 
                          (5.0 + 0.39 * np.cos(self.dim * 4.2)) * x**16 + 
                          (4.7 + 0.36 * np.sin(self.dim * 4.6)) * x**15 - 
                          (4.4 + 0.33 * np.cos(self.dim * 5.0)) * x**14 + 
                          (4.1 + 0.30 * np.sin(self.dim * 5.4)) * x**13 - 
                          (3.8 + 0.27 * np.cos(self.dim * 5.8)) * x**12 + 
                          (3.5 + 0.24 * np.sin(self.dim * 6.2)) * x**11 - 
                          (3.2 + 0.21 * np.cos(self.dim * 6.6)) * x**10 + 
                          (2.9 + 0.18 * np.sin(self.dim * 7.0)) * x**9 - 
                          (2.6 + 0.15 * np.cos(self.dim * 7.4)) * x**8 + 
                          (2.3 + 0.12 * np.sin(self.dim * 7.8)) * x**7 - 
                          (2.0 + 0.09 * np.cos(self.dim * 8.2)) * x**6 + 
                          (1.7 + 0.06 * np.sin(self.dim * 8.6)) * x**5 - 
                          (1.4 + 0.03 * np.cos(self.dim * 9.0)) * x**4 + 
                          (1.1 + 0.01 * np.sin(self.dim * 9.4)) * x**3) / self.dim
        
        # Enhanced multi-dimensional quantum barrier with modified interference
        barrier_term = np.sum(np.exp(-x**2 / (5.1 + 2.7 * np.sin(self.dim * 0.9))) * 
                             np.sin(16.3 * x + 1.1 * np.cos(self.dim * 1.3)) * 
                             np.cos(7.8 * x + 0.55 * np.sin(self.dim * 1.6)) * 
                             np.sin(x/6.2 + 0.35 * np.cos(self.dim * 1.9)) * 
                             np.cos(x/8.1 + 0.34 * np.sin(self.dim * 2.2)) * 
                             np.sin(x/11.3 + 0.30 * np.cos(self.dim * 2.5)) * 
                             np.cos(x/13.7 + 0.26 * np.sin(self.dim * 2.8)) * 
                             np.sin(x/16.4 + 0.22 * np.cos(self.dim * 3.1)) * 
                             np.cos(x/19.2 + 0.18 * np.sin(self.dim * 3.4))) / self.dim
        
        # Enhanced hyper-fractal attractor with modified exponents and scaling
        attractor_term = np.sum(np.sin(np.exp(x/4.5 + 0.45 * np.sin(self.dim * 1.0))) * 
                               np.cos(np.exp(-x/6.8 + 0.42 * np.cos(self.dim * 1.2))) * 
                               np.sin(x/6.4 + 0.30 * np.sin(self.dim * 1.4)) * 
                               np.cos(x/9.9 + 0.28 * np.cos(self.dim * 1.6)) * 
                               np.sin(x/9.1 + 0.25 * np.sin(self.dim * 1.8)) * 
                               np.cos(x/13.5 + 0.22 * np.cos(self.dim * 2.0)) * 
                               np.sin(x/11.9 + 0.18 * np.sin(self.dim * 2.2)) * 
                               np.cos(x/16.4 + 0.15 * np.cos(self.dim * 2.4)) * 
                               np.sin(x/14.4 + 0.12 * np.sin(self.dim * 2.6)) * 
                               np.cos(x/19.9 + 0.09 * np.cos(self.dim * 2.8))) / self.dim
        
        # Modified adaptive cross-dimensional coupling with enhanced weights and exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 4.8 + 0.9 * np.sin(i + self.dim * 1.5)  # Increased weight modulation
                cross_term += weight * np.abs(x[i] - x[i+1])**(5.1 + 0.9 * np.sin(i + 1.3 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Enhanced hierarchical fractal noise with modified components
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
                0.002 * np.sin(np.sum(x**16.2)) * np.cos(np.sum(x**17.5)))
        
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