import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks and valleys
        r = np.sqrt(np.sum(x**2))
        radial = 0.3 * r * np.sin(0.4 * r) + 0.1 * r**2
        
        # Sinusoidal terms in each dimension creating multi-modal structure
        modal_terms = 0.0
        for i in range(self.dim):
            modal_terms += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            modal_terms += 0.5 * np.sin(6.0 * x[i]) * np.cos(4.0 * x[i])
        
        # Cross-term interactions between dimensions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.2 * np.sin(x[i]) * np.cos(x[j])
        
        # Penalty for large values to maintain bounded search space
        penalty = 0.5 * np.sum(np.abs(x)**3)
        
        # Combine all components with different weights
        return radial + 0.8 * modal_terms + 0.3 * cross_terms + penalty