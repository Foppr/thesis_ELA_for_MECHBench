import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial distance component with exponential barrier
        r = np.sqrt(np.sum(x_norm**2))
        barrier = np.exp(-r**2 / 2.0) * (1.0 + 0.5 * np.sin(10 * r))
        
        # Nested saddle point structure with varying curvature
        saddle = np.sum((x_norm**2 - 1.0)**2 * (x_norm**2 + 1.0))
        
        # Multi-scale sinusoidal modulation with chaotic frequency
        freq_mod = np.sum(np.sin(2 * np.pi * (x_norm + 0.1 * np.sin(5 * x_norm))) + 
                          0.5 * np.sin(4 * np.pi * (x_norm + 0.2 * np.cos(3 * x_norm))))
        
        # Coupled oscillatory terms with adaptive phase shifts
        phase_shifts = np.sin(np.linspace(0, 2 * np.pi, self.dim) * 0.5)
        coupled_osc = np.sum(np.sin(x_norm * (1 + 0.3 * phase_shifts)) * 
                             np.cos(x_norm * (1 + 0.2 * phase_shifts)))
        
        # Exponential decay interaction between dimensions
        decay_interaction = np.sum(np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Combine all components with adaptive weights
        return barrier + 0.2 * saddle + 0.15 * freq_mod + 0.1 * coupled_osc + 0.05 * decay_interaction