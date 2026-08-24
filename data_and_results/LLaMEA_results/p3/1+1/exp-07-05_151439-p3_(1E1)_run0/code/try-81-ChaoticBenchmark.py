import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Ultra-high frequency chaotic modulation with fractional dimensions and complex phase coupling
        chaotic_term = np.sum(np.sin(127 * np.sin(np.cos(x))) * np.cos(89 * np.cos(np.sin(x))) * 
                             (1 + 0.73 * np.sin(np.sum(x**2.7)) * np.cos(np.sum(x**3.1)) * 
                              np.sin(np.sum(x**4.3)) * np.cos(np.sum(x**5.9)) * 
                              np.sin(np.sum(x**6.2)) * np.cos(np.sum(x**7.4)))) / self.dim
        
        # Extremely high-degree polynomial with dynamic coefficients and multi-scale interactions
        poly_term = np.sum((5.8 + 0.52 * np.sin(self.dim * 1.3)) * x**17 - 
                          (4.9 + 0.41 * np.cos(self.dim * 1.7)) * x**16 + 
                          (4.6 + 0.38 * np.sin(self.dim * 2.1)) * x**15 - 
                          (4.3 + 0.35 * np.cos(self.dim * 2.5)) * x**14 + 
                          (4.1 + 0.32 * np.sin(self.dim * 2.9)) * x**13 - 
                          (3.9 + 0.30 * np.cos(self.dim * 3.3)) * x**12 + 
                          (3.7 + 0.28 * np.sin(self.dim * 3.7)) * x**11 - 
                          (3.5 + 0.26 * np.cos(self.dim * 4.1)) * x**10 + 
                          (3.3 + 0.24 * np.sin(self.dim * 4.5)) * x**9 - 
                          (3.1 + 0.22 * np.cos(self.dim * 4.9)) * x**8 + 
                          (2.9 + 0.20 * np.sin(self.dim * 5.3)) * x**7 - 
                          (2.7 + 0.18 * np.cos(self.dim * 5.7)) * x**6 + 
                          (2.5 + 0.16 * np.sin(self.dim * 6.1)) * x**5 - 
                          (2.3 + 0.14 * np.cos(self.dim * 6.5)) * x**4 + 
                          (2.1 + 0.12 * np.sin(self.dim * 6.9)) * x**3 - 
                          (1.9 + 0.10 * np.cos(self.dim * 7.3)) * x**2 + 
                          (2.4 + 0.13 * np.sin(self.dim * 7.7)) * x) / self.dim
        
        # Multi-phase quantum barrier with complex interference and dynamic scaling
        barrier_term = np.sum(np.exp(-x**2 / (4.2 + 2.1 * np.sin(self.dim * 0.8))) * 
                             np.sin(12.5 * x + 0.8 * np.cos(self.dim * 1.2)) * 
                             np.cos(5.7 * x + 0.5 * np.sin(self.dim * 1.5)) * 
                             np.sin(x/4.8 + 0.3 * np.cos(self.dim * 1.8)) * 
                             np.cos(x/6.3 + 0.25 * np.sin(self.dim * 2.1)) * 
                             np.sin(x/8.7 + 0.2 * np.cos(self.dim * 2.4)) * 
                             np.cos(x/10.2 + 0.15 * np.sin(self.dim * 2.7))) / self.dim
        
        # Ultra-complex multi-scale chaotic attractor with non-integer exponents and dynamic scaling
        attractor_term = np.sum(np.sin(np.exp(x/3.1 + 0.4 * np.sin(self.dim * 0.9))) * 
                               np.cos(np.exp(-x/5.2 + 0.32 * np.cos(self.dim * 1.1))) * 
                               np.sin(x/5.1 + 0.2 * np.sin(self.dim * 1.3)) * 
                               np.cos(x/8.3 + 0.18 * np.cos(self.dim * 1.5)) * 
                               np.sin(x/7.7 + 0.15 * np.sin(self.dim * 1.7)) * 
                               np.cos(x/11.9 + 0.12 * np.cos(self.dim * 1.9)) * 
                               np.sin(x/9.4 + 0.1 * np.sin(self.dim * 2.1)) * 
                               np.cos(x/13.6 + 0.08 * np.cos(self.dim * 2.3))) / self.dim
        
        # Advanced adaptive cross-dimensional coupling with dynamic weights, fractional exponents, and multi-scale interactions
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 3.8 + 0.7 * np.sin(i + self.dim * 1.2)
                cross_term += weight * np.abs(x[i] - x[i+1])**(4.2 + 0.8 * np.sin(i + 1.1 * self.dim))
        cross_term /= (self.dim - 1)
        
        # Novel hierarchical fractal noise with multi-frequency components and dynamic scaling
        noise = (0.045 * np.random.rand() + 
                0.028 * np.sin(np.sum(x**2.5)) + 
                0.021 * np.cos(np.sum(x**3.7)) + 
                0.017 * np.sin(np.sum(x**4.2)) * np.cos(np.sum(x**5.1)) + 
                0.013 * np.sin(self.dim) * np.cos(np.sum(x)) + 
                0.010 * np.cos(np.sum(x**6.3)) * np.sin(np.sum(x**7.4)) + 
                0.007 * np.sin(np.sum(x**8.1)) * np.cos(np.sum(x**9.5)) + 
                0.005 * np.cos(np.sum(x**10.2)) * np.sin(np.sum(x**11.7)) + 
                0.003 * np.sin(np.sum(x**12.3)) * np.cos(np.sum(x**13.8)) + 
                0.002 * np.cos(np.sum(x**14.1)) * np.sin(np.sum(x**15.6)))
        
        # Enhanced dynamic weighting with multi-scale factors, dimensionality-dependent adjustments, and chaotic modulation
        weights = [0.62 + 0.18 * np.sin(self.dim * 1.1), 
                  0.58 + 0.16 * np.cos(self.dim * 1.3), 
                  0.51 + 0.14 * np.sin(self.dim * 1.5), 
                  0.43 + 0.12 * np.cos(self.dim * 1.7), 
                  0.37 + 0.10 * np.sin(self.dim * 1.9)]
        
        # Combine all terms with enhanced weighting and added interaction effects
        result = (weights[0] * chaotic_term + 
                 weights[1] * poly_term + 
                 weights[2] * barrier_term + 
                 weights[3] * attractor_term + 
                 weights[4] * cross_term)
        
        return result + noise