import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-like interference terms with phase modulation
        quantum_terms = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x) * 
                              np.exp(-0.5 * np.abs(x)) * np.sin(0.5 * np.pi * np.sum(x**2)))
        
        # Radial basis functions with dynamically shifted centers and time-varying widths
        rbfs = 0.0
        for i in range(self.dim):
            center = 4.0 * np.sin(i * 0.3) + 1.0 * np.cos(i * 0.7)
            width = 0.5 + 0.3 * np.sin(i * 0.4)
            rbfs += np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
        
        # Fractional polynomial cross-terms with mixed exponents
        poly_cross = 0.0
        for i in range(self.dim - 1):
            poly_cross += (x[i]**1.5 * x[i+1]**2.5 + x[i]**2.5 * x[i+1]**1.5)
        
        # Chaotic sine waves with varying frequencies and amplitude modulation
        chaotic_terms = np.sum(np.sin(5.0 * np.sin(x)) * np.cos(4.0 * np.cos(x)) * 
                              np.exp(-0.2 * np.abs(x)) * np.sin(1.3 * x))
        
        # Harmonic coupling terms with adaptive phase shifts
        harmonic_terms = 0.3 * np.sum(np.sin(2.7 * x) * np.cos(4.1 * x) * 
                                     np.exp(-0.1 * x**2) + 
                                     np.sin(6.8 * x) * np.cos(8.9 * x) * 
                                     np.exp(-0.15 * x**2))
        
        # Combined function value with additional coupling terms
        return quantum_terms + rbfs + poly_cross + chaotic_terms + harmonic_terms + 0.1 * np.sum(np.sin(10.0 * x) * np.cos(12.0 * x))