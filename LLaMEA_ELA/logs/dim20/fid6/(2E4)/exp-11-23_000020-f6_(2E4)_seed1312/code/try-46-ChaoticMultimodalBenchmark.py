import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants for chaotic behavior with more variation
        self.r_values = np.linspace(3.6, 4.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced logistic map chaos component with longer transient and more sensitive dependence
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Initialize chaotic sequence with more iterations to settle
            xi = 0.5 + 0.01 * np.random.rand()  # Slightly perturbed initial condition
            for _ in range(50):  # Let it settle longer
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution with multiple steps and sensitivity to initial conditions
            for _ in range(20):
                xi = r * xi * (1 - xi)
            chaos += xi
        
        # Enhanced trigonometric wave interference with higher frequencies and amplitude modulation
        wave = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) + 
                      np.sin(9 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) +
                      np.sin(13 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) +
                      np.sin(17 * np.pi * x_norm) * np.cos(19 * np.pi * x_norm))
        
        # Polynomial coupling with quartic term for increased complexity and smoother gradients
        poly = np.sum(x_norm**4 + 0.7 * x_norm**3 + 0.5 * x_norm**2 + 0.3 * x_norm + 0.1)
        
        # Coupling between dimensions using product of higher-order sinusoids with varying frequencies
        coupling = np.prod(np.sin(0.9 * np.pi * x_norm) + np.cos(0.9 * np.pi * x_norm) + 
                          np.sin(1.3 * np.pi * x_norm) * np.cos(1.3 * np.pi * x_norm))
        
        # Novel radial basis function component with adaptive bandwidth and phase modulation
        rbf = np.sum(np.exp(-0.25 * x_norm**2) * np.sin(25 * x_norm) * np.cos(6 * x_norm))
        
        # Additional hyperbolic tangent modulation with different parameters
        tanh_mod = np.sum(np.tanh(3 * x_norm) * np.cos(15 * x_norm) * np.sin(4 * x_norm))
        
        # Combine all components with varying weights optimized for better algorithm discrimination
        return 0.25 * chaos + 0.25 * wave + 0.18 * poly + 0.12 * coupling + 0.09 * rbf + 0.08 * tanh_mod + 2.5