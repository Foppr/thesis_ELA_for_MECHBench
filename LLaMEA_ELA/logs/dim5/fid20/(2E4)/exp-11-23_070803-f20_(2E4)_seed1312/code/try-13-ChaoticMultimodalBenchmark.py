import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Polynomial basin term with exponential damping
        basin_term = 0.3 * np.sum(np.exp(2 * np.abs(x_norm)) - 1) + 0.2 * np.sum(x_norm**4)
        
        # Chaotic sinusoidal component with fractal-like cross-terms
        chaotic_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like interaction with multiple frequencies
                chaotic_term += (np.sin(15 * x_norm[i] * x_norm[j]) * 
                                np.cos(10 * (x_norm[i]**2 + x_norm[j]**2)) *
                                np.exp(-0.5 * (x_norm[i] - x_norm[j])**2))
        
        # Multimodal component with exponential modulation
        multimodal_term = 0
        for i in range(self.dim):
            # Combine multiple frequencies with exponential weights
            multimodal_term += (np.sin(25 * x_norm[i]) * np.cos(20 * x_norm[i]) * 
                               np.exp(-0.1 * np.abs(x_norm[i])) + 
                               np.sin(35 * x_norm[i]**3) * np.cos(30 * x_norm[i]**3) * 
                               np.exp(-0.05 * np.abs(x_norm[i]**3)))
        
        # Add a global chaotic modulation term
        global_modulation = np.sum(np.sin(50 * x_norm) * np.cos(40 * x_norm)) * 0.1
        
        # Combine all terms
        result = basin_term + chaotic_term + multimodal_term + global_modulation
        
        # Add structured noise to increase ruggedness
        noise = 0.001 * np.sum(np.sin(100 * x_norm) * np.cos(90 * x_norm))
        
        return result + noise