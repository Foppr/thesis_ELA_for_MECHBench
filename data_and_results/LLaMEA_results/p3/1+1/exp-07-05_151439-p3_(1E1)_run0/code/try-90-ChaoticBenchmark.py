import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyper-chaotic modulation with multi-scale sinusoidal coupling
        chaotic_term = np.sum(np.sin(317 * np.sin(np.cos(x))) * np.cos(251 * np.cos(np.sin(x))) * 
                             (1 + 0.85 * np.sin(np.sum(x**3.7)) * np.cos(np.sum(x**4.9)) * 
                              np.sin(np.sum(x**5.8)) * np.cos(np.sum(x**6.7)) * 
                              np.sin(np.sum(x**7.9)) * np.cos(np.sum(x**8.3)) * 
                              np.sin(np.sum(x**9.1)) * np.cos(np.sum(x**10.5)) * 
                              np.sin(np.sum(x**11.2)) * np.cos(np.sum(x**12.8)))) / self.dim
        
        # Modified quantum-resonant polynomial with higher-order exponents and dynamic scaling
        poly_term = np.sum((8.2 + 0.71 * np.sin(self.dim * 1.5)) * x**25 - 
                          (7.8 + 0.67 * np.cos(self.dim * 1.9)) * x**24 + 
                          (7.5 + 0.64 * np.sin(self.dim * 2.3)) * x**23 - 
                          (7.2 + 0.61 * np.cos(self.dim * 2.7)) * x**22 + 
                          (6.9 + 0.58 * np.sin(self.dim * 3.1)) * x**21 - 
                          (6.6 + 0.55 * np.cos(self.dim * 3.5)) * x**20 + 
                          (6.3 + 0.52 * np.sin(self.dim * 3.9)) * x**19 - 
                          (6.0 + 0.49 * np.cos(self.dim * 4.3)) * x**18 + 
                          (5.7 + 0.46 * np.sin(self.dim * 4.7)) * x**17 - 
                          (5.4 + 0.43 * np.cos(self.dim * 5.1)) * x**16 + 
                          (5.1 + 0.40 * np.sin(self.dim * 5.5)) * x**15 - 
                          (4.8 + 0.37 * np.cos(self.dim * 5.9)) * x**14 + 
                          (4.5 + 0.34 * np.sin(self.dim * 6.3)) * x**13 - 
                          (4.2 + 0.31 * np.cos(self.dim * 6.7)) * x**12 + 
                          (3.9 + 0.28 * np.sin(self.dim * 7.1)) * x**11 - 
                          (3.6 + 0.25 * np.cos(self.dim * 7.5)) * x**10 + 
                          (3.3 + 0.22 * np.sin(self.dim * 7.9)) * x**9 - 
                          (3.0 + 0.19 * np.cos(self.dim * 8.3)) * x**8 + 
                          (2.7 + 0.16 * np.sin(self.dim * 8.7)) * x**7 - 
                          (2.4 + 0.13 * np.cos(self.dim * 9.1)) * x**6 + 
                          (2.1 + 0.10 * np.sin(self.dim * 9.5)) * x**5 - 
                          (1.8 + 0.07 * np.cos(self.dim * 9.9)) * x**4 + 
                          (1.5 + 0.04 * np.sin(self.dim * 10.3)) * x**3) / self.dim
        
        # Multi-dimensional quantum barrier with enhanced interference patterns
        barrier_term = np.sum(np.exp(-x**2 / (5.2 + 2.8 * np.sin(self.dim * 0.9))) * 
                             np.sin(17.3 * x + 1.2 * np.cos(self.dim * 1.4)) * 
                             np.cos(7.8 * x + 0.6 * np.sin(self.dim * 1.7)) * 
                             np.sin(x/6.3 + 0.35 * np.cos(self.dim * 2.0)) * 
                             np.cos(x/8.7 + 0.38 * np.sin(self.dim * 2.3)) * 
                             np.sin(x/11.4 + 0.32 * np.cos(self.dim * 2.6)) * 
                             np.cos(x/13.9 + 0.28 * np.sin(self.dim * 2.9)) * 
                             np.sin(x/16.7 + 0.24 * np.cos(self.dim * 3.2)) * 
                             np.cos(x/19.8 + 0.20 * np.sin(self.dim * 3.5)) * 
                             np.sin(x/23.1 + 0.16 * np.cos(self.dim * 3.8)) * 
                             np.cos(x/26.5 + 0.12 * np.sin(self.dim * 4.1))) / self.dim
        
        # Enhanced hyper-fractal attractor with modified scaling and multi-scale interference
        attractor_term = np.sum(np.sin(np.exp(x/4.7 + 0.45 * np.sin(self.dim * 1.0))) * 
                               np.cos(np.exp(-x/7.2 + 0.42 * np.cos(self.dim * 1.2))) * 
                               np.sin(x/6.8 + 0.30 * np.sin(self.dim * 1.4)) * 
                               np.cos(x/10.3 + 0.28 * np.cos(self.dim * 1.6)) * 
                               np.sin(x/9.6 + 0.25 * np.sin(self.dim * 1.8)) * 
                               np.cos(x/14.2 + 0.22 * np.cos(self.dim * 2.0)) * 
                               np.sin(x/12.7 + 0.18 * np.sin(self.dim * 2.2)) * 
                               np.cos(x/17.5 + 0.15 * np.cos(self.dim * 2.4)) * 
                               np.sin(x/15.8 + 0.12 * np.sin(self.dim * 2.6)) * 
                               np.cos(x/20.3 + 0.09 * np.cos(self.dim * 2.8)) * 
                               np.sin(x/18.9 + 0.06 * np.sin(self.dim * 3.0)) * 
                               np.cos(x/23.7 + 0.03 * np.cos(self.dim * 3.2))) / self.dim
        
        # Advanced adaptive cross-dimensional coupling with modified weights and exponents
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 5.1 + 0.8 * np.sin(i + self.dim * 1.4)
                cross_term += weight * np.abs(x[i] - x[i+1])**(5.3 + 0.9 * np.sin(i + 1.3 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel hierarchical fractal noise with increased complexity and stochastic components
        noise = (0.061 * np.random.rand() + 
                0.037 * np.sin(np.sum(x**2.9)) + 
                0.028 * np.cos(np.sum(x**3.7)) + 
                0.021 * np.sin(np.sum(x**4.5)) * np.cos(np.sum(x**5.3)) + 
                0.016 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.011 * np.cos(np.sum(x**6.7)) * np.sin(np.sum(x**7.9)) + 
                0.008 * np.sin(np.sum(x**8.4)) * np.cos(np.sum(x**9.6)) + 
                0.005 * np.cos(np.sum(x**10.3)) * np.sin(np.sum(x**11.7)) + 
                0.004 * np.sin(np.sum(x**12.4)) * np.cos(np.sum(x**13.8)) + 
                0.003 * np.cos(np.sum(x**14.3)) * np.sin(np.sum(x**15.7)) + 
                0.002 * np.sin(np.sum(x**16.2)) * np.cos(np.sum(x**17.5)) + 
                0.001 * np.cos(np.sum(x**18.1)) * np.sin(np.sum(x**19.4)) + 
                0.0005 * np.sin(np.sum(x**20.2)) * np.cos(np.sum(x**21.6)))
        
        # Enhanced dynamic weighting with modified factors and additional terms
        weights = [0.72 + 0.21 * np.sin(self.dim * 1.2), 
                  0.68 + 0.19 * np.cos(self.dim * 1.4), 
                  0.64 + 0.17 * np.sin(self.dim * 1.6), 
                  0.60 + 0.15 * np.cos(self.dim * 1.8), 
                  0.56 + 0.13 * np.sin(self.dim * 2.0)]
        
        # Combine all terms with modified weighting
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise