import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants for chaotic behavior with more variation
        self.r_values = np.linspace(3.5, 3.95, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced logistic map chaos component with longer transient and more sensitive dependence
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Initialize chaotic sequence with more iterations to settle
            xi = 0.5 + 0.01 * np.random.rand()  # Slightly perturbed initial condition
            for _ in range(30):  # Let it settle longer
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution with multiple steps and sensitivity to initial conditions
            for _ in range(15):
                xi = r * xi * (1 - xi)
            chaos += xi
        
        # Enhanced trigonometric wave interference with higher frequencies and amplitude modulation
        wave = np.sum(np.sin(6 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) + 
                      np.sin(10 * np.pi * x_norm) * np.cos(12 * np.pi * x_norm) +
                      np.sin(14 * np.pi * x_norm) * np.cos(16 * np.pi * x_norm) +
                      np.sin(18 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm))
        
        # Polynomial coupling with cubic term for increased complexity and smoother gradients
        poly = np.sum(x_norm**3 + 0.4 * x_norm**2 + 0.2 * x_norm + 0.1)
        
        # Coupling between dimensions using product of higher-order sinusoids with varying frequencies
        coupling = np.prod(np.sin(0.8 * np.pi * x_norm) + np.cos(0.8 * np.pi * x_norm) + 
                          np.sin(1.2 * np.pi * x_norm) * np.cos(1.2 * np.pi * x_norm))
        
        # Novel radial basis function component with adaptive bandwidth and phase modulation
        rbf = np.sum(np.exp(-0.3 * x_norm**2) * np.sin(30 * x_norm) * np.cos(7 * x_norm))
        
        # Additional exponential modulation with different base and frequency
        exp_mod = np.sum(np.exp(-0.4 * x_norm**2) * np.cos(15 * x_norm) * np.sin(5 * x_norm))
        
        # Combine all components with varying weights optimized for better algorithm discrimination
        return 0.3 * chaos + 0.3 * wave + 0.15 * poly + 0.1 * coupling + 0.08 * rbf + 0.07 * exp_mod + 2.0