import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Polynomial basin term
        basin_term = 0.5 * np.sum(x_norm**4) + 0.3 * np.sum(x_norm**2)
        
        # Chaotic sinusoidal component with cross-terms (modified frequencies and added cubic terms)
        chaotic_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_term += np.sin(15 * x_norm[i] * x_norm[j]) * np.cos(7 * (x_norm[i] + x_norm[j])) + \
                               0.3 * np.sin(8 * x_norm[i]**3 * x_norm[j]**2) * np.cos(6 * x_norm[i] * x_norm[j]**3)
        
        # Additional multimodal component with varying frequencies
        multimodal_term = 0
        for i in range(self.dim):
            multimodal_term += np.sin(25 * x_norm[i]) * np.cos(20 * x_norm[i]) + \
                              np.sin(35 * x_norm[i]**2) * np.cos(30 * x_norm[i]**2)
        
        # Combine all terms
        result = basin_term + chaotic_term + multimodal_term
        
        # Add small random noise to make it non-deterministic
        noise = np.random.normal(0, 0.001)
        
        return result + noise