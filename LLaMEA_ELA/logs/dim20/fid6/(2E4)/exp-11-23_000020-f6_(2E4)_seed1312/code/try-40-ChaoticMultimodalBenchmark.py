import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants for even more chaotic behavior
        self.r_values = np.linspace(3.9, 4.0, dim)
        # Fractional Brownian motion-like scaling factors
        self.hurst = 0.7
        self.frac_factors = np.array([np.power(i + 1, 2 * self.hurst - 1) for i in range(dim)])
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced logistic map chaos with longer transient and more iterations
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            xi = 0.5
            # Let it settle with more iterations
            for _ in range(30):
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution with multiple steps and fractional scaling
            for _ in range(15):
                xi = r * xi * (1 - xi)
            chaos += xi * self.frac_factors[i]
        
        # Multi-scale trigonometric interference with higher frequencies and more terms
        wave = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) + 
                      np.sin(9 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) +
                      np.sin(13 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) +
                      np.sin(17 * np.pi * x_norm) * np.cos(19 * np.pi * x_norm))
        
        # Higher-order polynomial coupling with mixed terms
        poly = np.sum(x_norm**5 + 0.6 * x_norm**4 + 0.4 * x_norm**3 + 0.2 * x_norm**2 + 0.1 * x_norm)
        
        # Coupling between dimensions using product of higher-order sinusoids with phase shifts
        coupling = np.prod(np.sin(0.9 * np.pi * x_norm + 0.2) + np.cos(0.9 * np.pi * x_norm - 0.3))
        
        # Enhanced radial basis function component with multiple centers and varying widths
        rbf = np.sum(np.exp(-0.3 * x_norm**2) * np.sin(20 * x_norm) + 
                     np.exp(-0.1 * x_norm**2) * np.cos(25 * x_norm))
        
        # Additional exponential modulation with multiple bases and frequency components
        exp_mod = np.sum(np.exp(-0.2 * x_norm**2) * np.cos(10 * x_norm) + 
                         np.exp(-0.4 * x_norm**2) * np.sin(12 * x_norm))
        
        # Fractional Brownian motion-like interference component
        fbm = np.sum(np.sin(2 * np.pi * x_norm * self.frac_factors) * np.cos(3 * np.pi * x_norm * self.frac_factors))
        
        # Combine all components with varying weights and add a global scaling factor
        return 0.2 * chaos + 0.3 * wave + 0.15 * poly + 0.1 * coupling + 0.08 * rbf + 0.07 * exp_mod + 0.05 * fbm + 3.0