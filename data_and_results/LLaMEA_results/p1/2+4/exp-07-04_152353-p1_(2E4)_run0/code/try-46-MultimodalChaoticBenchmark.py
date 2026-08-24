import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Multimodal component with exponentially decaying correlation
        multimodal = 0
        for i in range(self.dim):
            # Create multiple local minima using sinusoidal modulation
            multimodal += np.sin(x_norm[i] * 10) * np.exp(-0.1 * np.abs(x_norm[i]))
            
        # Correlation decay component with varying scale
        correlation = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying correlation between variables
                correlation += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.cos(x_norm[i] * x_norm[j])
                
        # Sinusoidal modulation with varying frequency
        modulation = 0
        for i in range(self.dim):
            modulation += np.sin(x_norm[i] * (1 + 0.5 * np.sin(i))) * np.cos(x_norm[i] * (2 + 0.3 * np.cos(i)))
            
        # Heavy-tailed noise component
        noise = 0
        for i in range(self.dim):
            # Use Cauchy-like distribution for heavy tails
            noise += np.random.standard_cauchy() * np.exp(-0.2 * np.abs(x_norm[i]))
            
        # Interaction terms with polynomial scaling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_norm[i]**3) * (x_norm[j]**2) * np.sin(x_norm[i] + x_norm[j])
                
        # Combine components with adaptive weights
        result = 0.4 * quadratic + 0.3 * multimodal + 0.15 * correlation + 0.1 * modulation + 0.05 * interaction
        
        return result