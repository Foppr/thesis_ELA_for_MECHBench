import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants for chaotic behavior
        self.r_values = np.linspace(3.5, 4.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Logistic map chaos component
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Initialize chaotic sequence
            xi = 0.5
            for _ in range(10):  # Let it settle
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution
            for _ in range(5):
                xi = r * xi * (1 - xi)
            chaos += xi
        
        # Trigonometric wave interference
        wave = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) + 
                      np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Polynomial coupling with cross-terms
        poly = np.sum(x_norm**3 + 0.3 * x_norm**2 + 0.1 * x_norm)
        
        # Coupling between dimensions using product of sinusoids
        coupling = np.prod(np.sin(0.5 * np.pi * x_norm) + np.cos(0.5 * np.pi * x_norm))
        
        # Exponential modulation term
        exp_mod = np.sum(np.exp(-x_norm**2) * np.sin(10 * x_norm))
        
        # Combine all components with varying weights
        return 0.3 * chaos + 0.4 * wave + 0.2 * poly + 0.05 * coupling + 0.05 * exp_mod + 3.0