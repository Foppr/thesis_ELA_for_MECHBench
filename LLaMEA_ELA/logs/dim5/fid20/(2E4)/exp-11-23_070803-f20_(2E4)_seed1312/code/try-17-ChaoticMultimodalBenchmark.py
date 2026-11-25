import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Enhanced polynomial basin term with mixed powers and cross-terms
        basin_term = 0.2 * np.sum(x_norm**6) + 0.3 * np.sum(x_norm**4) + 0.25 * np.sum(x_norm**2)
        
        # Enhanced chaotic sinusoidal component with higher frequency cross-terms and phase shifts
        chaotic_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_term += (np.sin(20 * x_norm[i] * x_norm[j]) * np.cos(10 * (x_norm[i] + x_norm[j])) + 
                               np.cos(15 * x_norm[i] * x_norm[j]) * np.sin(9 * (x_norm[i] - x_norm[j])) +
                               np.sin(25 * x_norm[i]**2 * x_norm[j]) * np.cos(12 * x_norm[i] * x_norm[j]**2))
        
        # Enhanced multimodal component with more complex frequency interactions and nested terms
        multimodal_term = 0
        for i in range(self.dim):
            multimodal_term += (np.sin(30 * x_norm[i]) * np.cos(25 * x_norm[i]) + 
                              np.sin(40 * x_norm[i]**2) * np.cos(35 * x_norm[i]**2) +
                              np.sin(50 * x_norm[i]**3) * np.cos(45 * x_norm[i]**3) +
                              np.sin(35 * x_norm[i]**4) * np.cos(30 * x_norm[i]**4))
        
        # Additional coupling term between dimensions with more complex interaction
        coupling_term = 0
        for i in range(self.dim):
            coupling_term += (np.sin(12 * x_norm[i]) * np.cos(12 * x_norm[(i+1) % self.dim]) +
                            np.sin(8 * x_norm[i] * x_norm[(i+2) % self.dim]) * 
                            np.cos(6 * x_norm[i] * x_norm[(i+2) % self.dim]))
        
        # Combine all terms with different weights
        result = basin_term + chaotic_term + multimodal_term + 0.4 * coupling_term
        
        # Add small random noise to make it non-deterministic
        noise = np.random.normal(0, 0.001)
        
        return result + noise