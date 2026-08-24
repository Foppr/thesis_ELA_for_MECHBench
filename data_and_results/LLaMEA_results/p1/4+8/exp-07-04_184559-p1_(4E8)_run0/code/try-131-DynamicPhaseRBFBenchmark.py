import numpy as np

class DynamicPhaseRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for phase shifts
        self.phase_shifts = np.linspace(0, 2*np.pi, dim, endpoint=False)
        # Chaos parameter for enhanced complexity
        self.chaos_factor = 0.7
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced Radial Basis Function with chaotic modulation
        centers = np.linspace(-0.5, 0.5, self.dim)
        rbf = np.sum(np.exp(-5 * (x_norm - centers)**2) * 
                    (1 + self.chaos_factor * np.sin(3 * np.pi * x_norm)))
        
        # Polynomial interaction term with varying degrees and cosine modulation
        poly_term = np.sum((x_norm**3 + 0.5 * x_norm**2 - 0.3 * x_norm + 
                           0.1 * np.cos(2 * x_norm))**2)
        
        # Dynamic phase shift component with spiral coupling
        phase_shift = np.sin(self.phase_shifts + np.sum(x_norm))
        phase_term = np.sum(np.cos(2 * np.pi * x_norm + phase_shift) * 
                           np.exp(-0.5 * np.sum(x_norm**2)) * 
                           (1 + 0.3 * np.sin(4 * np.pi * x_norm)))
        
        # Novel chaotic cross-terms with spiral coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_norm[i]**2 + x_norm[i+1]**2) * \
                         np.sin(3 * (x_norm[i] + x_norm[i+1]) + 
                               self.chaos_factor * np.sin(5 * x_norm[i]))
        
        # Adaptive conditioning with enhanced nonlinearity
        conditioning = 1 + 0.3 * np.abs(x_norm) + 0.1 * np.sin(3 * x_norm)
        cond_term = np.sum(conditioning * x_norm**4)
        
        # Additional sinusoidal modulation to increase multimodality
        mod_term = np.sum(np.sin(5 * x_norm) * np.cos(2 * x_norm) * 
                         np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Combine all components with optimized weights
        return 1.8 * rbf + 1.0 * poly_term + 1.5 * phase_term + 0.8 * cross_term + 1.2 * cond_term + 0.5 * mod_term