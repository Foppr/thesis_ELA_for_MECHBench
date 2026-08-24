import numpy as np

class DynamicPhaseRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for phase shifts
        self.phase_shifts = np.linspace(0, 2*np.pi, dim, endpoint=False)
        # Additional tuning parameters for better conditioning
        self.rbf_width = 3.0
        self.poly_degree = 4
        self.phase_modulation = 1.5
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced Radial Basis Function component with varied widths
        centers = np.linspace(-0.6, 0.6, self.dim)
        rbf = np.sum(np.exp(-self.rbf_width * (x_norm - centers)**2))
        
        # Modified polynomial interaction term with higher degree
        poly_term = np.sum((x_norm**self.poly_degree + 0.3 * x_norm**3 - 0.4 * x_norm**2 + 0.1 * x_norm)**2)
        
        # Adaptive phase shift component with enhanced modulation
        phase_shift = np.sin(self.phase_shifts + self.phase_modulation * np.sum(x_norm))
        phase_term = np.sum(np.cos(3 * np.pi * x_norm + phase_shift) * 
                           np.exp(-0.3 * np.sum(x_norm**2)))
        
        # Enhanced cross-term interaction with non-linear coupling
        cross_term = np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * 
                           np.sin(4 * (x_norm[:-1] + x_norm[1:])))
        
        # Improved adaptive conditioning based on input magnitude
        conditioning = 1 + 0.3 * np.abs(x_norm) + 0.1 * x_norm**2
        cond_term = np.sum(conditioning * x_norm**5)
        
        # Additional chaotic component for increased complexity
        chaotic_term = np.sum(np.sin(5 * x_norm) * np.cos(2 * x_norm) * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Combine all components with optimized weights
        return 1.2 * rbf + 0.9 * poly_term + 1.0 * phase_term + 0.7 * cross_term + 1.1 * cond_term + 0.5 * chaotic_term