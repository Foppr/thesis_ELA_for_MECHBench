import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation decay factors
        self.decay_factors = np.exp(-np.arange(dim) * 0.1)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Multimodal component with periodic forcing
        multimodal = 0
        for i in range(self.dim):
            # Create multiple local minima using sine and cosine
            multimodal += (np.sin(x_norm[i] * 3) + np.cos(x_norm[i] * 2)) * np.exp(-0.5 * x_norm[i]**2)
            
        # Correlated variables with exponential decay
        correlated = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying correlation
                corr = self.decay_factors[j-i] * x_norm[i] * x_norm[j]
                correlated += corr**2
                
        # Periodic forcing with varying frequencies
        periodic = 0
        for i in range(self.dim):
            # Add periodic components with different frequencies
            freq = 1 + 0.5 * np.sin(i * 0.3)
            periodic += np.sin(x_norm[i] * freq * 2 * np.pi) * np.cos(x_norm[i] * freq * 3 * np.pi)
            
        # Asymmetric saddle point regions
        saddle = 0
        for i in range(self.dim):
            # Create asymmetric regions using sign and polynomial terms
            saddle += x_norm[i]**3 * np.sign(x_norm[i]) * np.exp(-0.1 * np.abs(x_norm[i]))
            
        # Add interaction terms with varying coupling strengths
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = 0.5 + 0.5 * np.sin(i * 0.2 + j * 0.3)
                interaction += coupling * (x_norm[i] - x_norm[j])**4
                
        # Combine components with different weights
        result = 0.3 * quadratic + 0.25 * multimodal + 0.2 * correlated + 0.15 * periodic + 0.08 * saddle + 0.02 * interaction
        
        # Add noise to increase difficulty
        noise = 0.01 * np.sum(np.sin(x_norm * 10) * np.cos(x_norm * 7))
        result += noise
        
        return result