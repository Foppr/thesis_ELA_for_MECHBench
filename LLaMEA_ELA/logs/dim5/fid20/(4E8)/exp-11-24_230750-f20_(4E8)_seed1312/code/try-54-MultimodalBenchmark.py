import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine waves with irrational frequency ratios and dynamic modulation
        chaotic_terms = np.sum(np.sin(np.pi * np.sin(3.14159 * x)) * np.cos(np.e * np.cos(2.71828 * x)))
        
        # Radial basis functions with adaptive centers, widths, and exponential weighting
        rbfs = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.7) * 4.0
            width = 0.3 + 0.1 * np.sin(i * 0.4)
            rbfs += np.exp(-np.sum((x - center)**2) / (2.0 * width**2)) * np.cos(0.5 * i)
        
        # Dynamic conditioning with enhanced exponential decay and trigonometric modulation
        cond_terms = np.sum(np.exp(-0.3 * x**2) * np.sin(6.0 * x) * np.cos(4.0 * x))
        
        # Novel polynomial cross-terms with higher-order interactions and mixed exponents
        poly_cross = 0.15 * np.sum(x[:-1]**7 * x[1:]**4 + x[:-1]**4 * x[1:]**7 + x[:-1]**5 * x[1:]**5)
        
        # Additional complex harmonic terms with multiple irrational frequency ratios and phase shifts
        harmonic_terms = 0.25 * np.sum(np.sin(3.14159 * x) * np.cos(5.23599 * x) + 
                                      np.sin(7.85398 * x) * np.cos(9.42478 * x) + 
                                      np.sin(1.5708 * x) * np.cos(2.35619 * x))
        
        # Combined function value with weighted components
        return 0.8 * chaotic_terms + 1.2 * rbfs + 0.9 * cond_terms + 0.7 * poly_cross + 1.1 * harmonic_terms