import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis functions with varying widths and additional sinusoidal components
        rbf_sum = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.3 * np.sin(i * 0.5)  # Varying widths with different frequency
            rbf_sum += (np.exp(-width * (x[i] - 1.0)**2) + 
                       np.exp(-width * (x[i] + 1.0)**2) + 
                       0.5 * np.sin(3.0 * x[i]))  # Additional sinusoidal modulation
        
        # Enhanced cosine modulation with frequency variation
        cos_modulation = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.cos(i)  # Varying frequencies
            cos_modulation += np.cos(freq * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Modified quadratic basin term with dimension-dependent scaling
        quadratic = 0.0
        for i in range(self.dim):
            quadratic += (0.03 + 0.02 * np.sin(i)) * x[i]**2
        
        # Enhanced cross-terms with non-linear interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-linear interaction with sine and cosine
                cross_terms += 0.03 * np.sin(x[i] + x[j]) * np.cos(2.0 * x[i] - x[j])
        
        # Additional global structure term to create more challenging landscape
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += 0.01 * (x[i]**4 - 2*x[i]**2)
        
        return rbf_sum + cos_modulation + quadratic + cross_terms + global_structure