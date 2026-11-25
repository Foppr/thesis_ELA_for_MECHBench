import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine waves with irrational frequency ratios and amplitude modulation
        chaotic_terms = np.sum(np.sin(10.0 * np.sin(x)) * np.cos(7.0 * np.cos(x)) * np.exp(-0.1 * np.abs(x)))
        
        # Radial basis functions with dynamic centers and adaptive widths
        rbfs = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.7) * 4.0
            width = 0.3 + 0.4 * np.sin(i * 0.5)
            rbfs += np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
        
        # Dynamic conditioning with exponential decay and trigonometric modulation
        cond_terms = np.sum(np.exp(-0.3 * x**2) * np.sin(6.0 * x) * np.cos(4.0 * x))
        
        # Augmented polynomial cross-terms with higher-order interactions and mixed exponents
        poly_cross = 0.15 * np.sum(x[:-1]**7 * x[1:]**4 + x[:-1]**4 * x[1:]**7 + x[:-1]**5 * x[1:]**5)
        
        # Additional complex harmonic terms with varying phase shifts and decay
        harmonic_terms = 0.25 * np.sum(np.sin(3.1 * x) * np.cos(5.9 * x) * np.exp(-0.2 * x**2) + 
                                      np.sin(7.2 * x) * np.cos(9.8 * x) * np.exp(-0.15 * x**2))
        
        # Combined function value with additional coupling terms
        return chaotic_terms + rbfs + cond_terms + poly_cross + harmonic_terms + 0.05 * np.sum(np.sin(12.0 * x) * np.cos(15.0 * x))