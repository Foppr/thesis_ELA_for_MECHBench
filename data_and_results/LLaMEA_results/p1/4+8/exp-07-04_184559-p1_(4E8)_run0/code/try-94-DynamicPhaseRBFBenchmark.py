import numpy as np

class DynamicPhaseRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for phase shifts
        self.phase_shifts = np.linspace(0, 2*np.pi, dim, endpoint=False)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial Basis Function component with dynamic centers
        centers = np.linspace(-0.5, 0.5, self.dim)
        rbf = np.sum(np.exp(-5 * (x_norm - centers)**2))
        
        # Polynomial interaction term with varying degrees
        poly_term = np.sum((x_norm**3 + 0.5 * x_norm**2 - 0.3 * x_norm)**2)
        
        # Dynamic phase shift component creating varying landscape topology
        phase_shift = np.sin(self.phase_shifts + np.sum(x_norm))
        phase_term = np.sum(np.cos(2 * np.pi * x_norm + phase_shift) * 
                           np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Cross-term interaction with non-linear coupling
        cross_term = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                           np.sin(3 * (x_norm[:-1] + x_norm[1:])))
        
        # Adaptive conditioning based on input magnitude
        conditioning = 1 + 0.2 * np.abs(x_norm)
        cond_term = np.sum(conditioning * x_norm**4)
        
        # Combine all components with varying weights
        return 1.5 * rbf + 0.8 * poly_term + 1.2 * phase_term + 0.6 * cross_term + 1.0 * cond_term