import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation matrix for dimension interactions
        self.correlation = np.random.rand(dim, dim) * 0.3 - 0.15
        np.fill_diagonal(self.correlation, 1.0)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Hyperbolic sine-cosine multimodal component
        hyperbolic = 0.0
        for i in range(self.dim):
            hyperbolic += np.sinh(1.5 * x[i]) * np.cosh(1.2 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Correlated dimension interactions with chaotic behavior
        correlated = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    correlated += self.correlation[i, j] * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Multi-scale periodic modulation with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            periodic += (1.0 * np.sin(3 * x[i]) * np.cos(2 * x[i]) + 
                        0.7 * np.sin(5 * x[i]) * np.cos(4 * x[i]) + 
                        0.5 * np.sin(7 * x[i]) * np.cos(6 * x[i]))
        
        # Asymmetric coupling with exponential decay
        asymmetric = 0.0
        for i in range(self.dim - 1):
            asymmetric += np.exp(-0.2 * x[i]**2) * np.sin(2 * x[i+1]) * np.cos(3 * x[i]) + \
                         np.exp(-0.3 * x[i+1]**2) * np.sin(3 * x[i]) * np.cos(2 * x[i+1])
        
        # Ruggedness through hyperbolic tangent interactions
        rugged = 0.0
        for i in range(self.dim - 1):
            rugged += np.tanh(x[i] + x[i+1]) * np.exp(-0.1 * (x[i] - x[i+1])**2)
        
        # Global modulation with sine-cosine product
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.4 * np.sin(2 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.08 * np.abs(x[i]))
        
        # Combine all components with different weights to create complex landscape
        return base + 1.2 * hyperbolic + 0.9 * correlated + 0.7 * periodic + 0.5 * asymmetric + 0.3 * rugged + 0.2 * global_mod