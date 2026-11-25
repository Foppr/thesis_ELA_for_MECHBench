import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Sinusoidal wave components with varying frequencies
        wave1 = np.sum(np.sin(2 * np.pi * x / 2.0))
        wave2 = np.sum(np.sin(4 * np.pi * x / 3.0))
        wave3 = np.sum(np.sin(6 * np.pi * x / 4.0))
        
        # Polynomial penalty terms to create conditioning variations
        poly1 = np.sum(x**4) * 0.01
        poly2 = np.sum(np.abs(x)**3) * 0.05
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(min(5, self.dim)):
            if i > 0:
                chaotic += np.sin(x[i-1] * x[i]) * np.cos(x[i-1] + x[i])
        
        # Combine all components with different weights
        result = -0.5 * wave1 - 0.3 * wave2 - 0.2 * wave3 + poly1 + poly2 + 0.1 * chaotic
        
        # Add small random noise to prevent exact replication
        noise = np.random.normal(0, 0.001)
        
        return result + noise