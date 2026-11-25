import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants for chaotic behavior with more variation
        self.r_values = np.linspace(3.8, 4.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced logistic map chaos component with longer transient
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Initialize chaotic sequence with more iterations to settle
            xi = 0.5
            for _ in range(20):  # Let it settle
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution with multiple steps
            for _ in range(10):
                xi = r * xi * (1 - xi)
            chaos += xi
        
        # Enhanced trigonometric wave interference with higher frequencies
        wave = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) + 
                      np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) +
                      np.sin(11 * np.pi * x_norm) * np.cos(13 * np.pi * x_norm))
        
        # Polynomial coupling with quartic term for increased complexity
        poly = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.3 * x_norm**2 + 0.1 * x_norm)
        
        # Coupling between dimensions using product of higher-order sinusoids
        coupling = np.prod(np.sin(0.7 * np.pi * x_norm) + np.cos(0.7 * np.pi * x_norm))
        
        # Radial basis function component for irregular landscape
        rbf = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(15 * x_norm))
        
        # Additional exponential modulation with different base
        exp_mod = np.sum(np.exp(-0.3 * x_norm**2) * np.cos(8 * x_norm))
        
        # Combine all components with varying weights
        return 0.25 * chaos + 0.35 * wave + 0.2 * poly + 0.1 * coupling + 0.05 * rbf + 0.05 * exp_mod + 2.5