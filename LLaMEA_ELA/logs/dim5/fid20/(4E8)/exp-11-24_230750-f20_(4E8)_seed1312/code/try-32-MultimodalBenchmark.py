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
        for i in range(min(5, self.dim)):
            center = np.sin(i) * 3.0
            width = 0.5 + 0.5 * np.cos(i)
            rbfs += np.exp(-0.5 * ((x - center) / width)**2)
        
        # Dynamic conditioning with exponential decay and trigonometric modulation
        dynamic_cond = np.sum(np.exp(-0.1 * x**2) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Adaptive polynomial cross-terms with higher-order interactions
        poly_cross = 0.0
        for i in range(self.dim - 2):
            poly_cross += 0.1 * (x[i]**5 * x[i+1]**3 + x[i]**3 * x[i+1]**5 + x[i+1]**4 * x[i+2]**2)
        
        # Additional harmonic terms with irrational frequency ratios for increased complexity
        irrational_terms = 0.05 * np.sum(np.sin(np.pi * x) * np.cos(np.e * x) + np.sin(np.sqrt(2) * x) * np.cos(np.sqrt(3) * x))
        
        # Combined function value
        return chaotic_terms + rbfs + dynamic_cond + poly_cross + irrational_terms