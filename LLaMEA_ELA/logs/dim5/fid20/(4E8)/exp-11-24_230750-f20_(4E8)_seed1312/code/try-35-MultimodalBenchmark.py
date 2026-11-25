import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine waves with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(10.0 * np.sin(x)) * np.cos(7.0 * np.cos(x)))
        
        # Radial basis functions with adaptive centers and widths
        rbfs = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.5) * 3.0
            width = 0.5 + 0.2 * np.sin(i * 0.3)
            rbfs += np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
        
        # Dynamic conditioning with exponential decay and trigonometric modulation
        cond_terms = np.sum(np.exp(-0.5 * x**2) * np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Enhanced polynomial cross-terms with higher-order interactions
        poly_cross = 0.1 * np.sum(x[:-1]**6 * x[1:]**3 + x[:-1]**3 * x[1:]**6)
        
        # Additional complex harmonic terms with irrational frequency ratios
        harmonic_terms = 0.2 * np.sum(np.sin(2.5 * x) * np.cos(4.7 * x) + np.sin(6.3 * x) * np.cos(8.9 * x))
        
        # Combined function value
        return chaotic_terms + rbfs + cond_terms + poly_cross + harmonic_terms