import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with chaotic sine modulations and adaptive Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 3.0 * (i + 1) / self.dim
            freq2 = 1.5 * (i + 1) / self.dim
            # Chaotic modulation with varying frequencies
            chaotic_mod = np.sin(freq1 * np.pi * x[i]) ** 5 + 0.3 * np.exp(-0.5 * (x[i] / 1.5)**2) * np.cos(freq2 * np.pi * x[i]) ** 3
            multimodal += chaotic_mod
        
        # Enhanced polynomial interaction terms with dynamic exponents and cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic exponents based on dimensionality
                exp_i = 2.5 + 0.3 * (i + 1)
                exp_j = 3.0 + 0.2 * (j + 1)
                polynomial += 0.12 * (x[i] ** exp_i) * (x[j] ** exp_j)
        
        # Adaptive scaling based on dimensionality and interaction strength
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Dynamic global shift with non-linear transformation
        shift = 0.8 * np.sum(np.abs(x) ** 1.2)
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.2 * multimodal + 0.05 * polynomial) + shift