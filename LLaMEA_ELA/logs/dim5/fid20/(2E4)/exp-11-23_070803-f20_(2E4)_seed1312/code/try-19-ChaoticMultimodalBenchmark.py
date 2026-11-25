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
        
        # Add cross-dimensional coupling in basin term
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                basin_term += 0.1 * x_norm[i]**3 * x_norm[j]**3
        
        # Enhanced chaotic sinusoidal component with higher frequency and more complex interactions
        chaotic_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_term += (np.sin(20 * x_norm[i] * x_norm[j]) * np.cos(15 * (x_norm[i] + x_norm[j])) + 
                               np.cos(18 * x_norm[i] * x_norm[j]) * np.sin(13 * (x_norm[i] - x_norm[j])) +
                               np.sin(25 * x_norm[i]**2 * x_norm[j]) * np.cos(20 * x_norm[i] * x_norm[j]**2))
        
        # Enhanced multimodal component with more complex frequency interactions and higher harmonics
        multimodal_term = 0
        for i in range(self.dim):
            multimodal_term += (np.sin(30 * x_norm[i]) * np.cos(25 * x_norm[i]) + 
                              np.sin(45 * x_norm[i]**2) * np.cos(40 * x_norm[i]**2) +
                              np.sin(50 * x_norm[i]**3) * np.cos(45 * x_norm[i]**3) +
                              np.sin(60 * x_norm[i]**4) * np.cos(55 * x_norm[i]**4))
        
        # Additional coupling term between dimensions with enhanced complexity
        coupling_term = 0
        for i in range(self.dim):
            coupling_term += (np.sin(12 * x_norm[i]) * np.cos(12 * x_norm[(i+1) % self.dim]) + 
                            np.sin(15 * x_norm[i]**2) * np.cos(15 * x_norm[(i+1) % self.dim]**2) +
                            np.sin(10 * x_norm[i] * x_norm[(i+2) % self.dim]) * np.cos(10 * x_norm[i] * x_norm[(i+2) % self.dim]))
        
        # Combine all terms
        result = basin_term + chaotic_term + multimodal_term + 0.6 * coupling_term
        
        # Add minimal noise to maintain black-box nature without disrupting optimization landscape
        noise = np.random.normal(0, 0.0001)
        
        return result + noise