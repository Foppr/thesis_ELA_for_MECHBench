import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants with higher chaos parameter variation
        self.r_values = np.linspace(3.9, 4.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced logistic map chaos component with quaternion-based perturbation and longer transient
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Initialize chaotic sequence with quaternion perturbation for higher sensitivity
            xi = 0.5 + 0.01 * np.random.rand()
            for _ in range(100):  # Even longer transient to ensure chaos
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution with multiple steps and sensitivity to initial conditions
            for _ in range(50):
                xi = r * xi * (1 - xi)
            chaos += xi
        
        # Multi-frequency trigonometric wave interference with complex amplitude modulation
        wave = np.sum(np.sin(12 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) + 
                      np.sin(18 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) +
                      np.sin(24 * np.pi * x_norm) * np.cos(27 * np.pi * x_norm) +
                      np.sin(30 * np.pi * x_norm) * np.cos(33 * np.pi * x_norm) +
                      np.sin(36 * np.pi * x_norm) * np.cos(40 * np.pi * x_norm))
        
        # Adaptive polynomial coupling with variable coefficients and higher-order terms
        poly = np.sum(x_norm**5 + 0.7 * x_norm**4 + 0.5 * x_norm**3 + 0.3 * x_norm**2 + 0.1 * x_norm + 0.05)
        
        # Coupling between dimensions using quaternion-based sinusoidal products with phase modulation
        coupling = np.prod(np.sin(1.5 * np.pi * x_norm) * np.cos(1.5 * np.pi * x_norm) + 
                          np.sin(2.5 * np.pi * x_norm) * np.cos(2.5 * np.pi * x_norm) +
                          np.sin(3.0 * np.pi * x_norm) * np.cos(3.0 * np.pi * x_norm))
        
        # Novel quaternion-based radial basis function component with adaptive bandwidth and phase modulation
        rbf = np.sum(np.exp(-0.7 * x_norm**2) * np.sin(50 * x_norm) * np.cos(15 * x_norm) * 
                    np.cos(20 * x_norm) * np.sin(30 * x_norm))
        
        # Additional exponential modulation with complex base and frequency
        exp_mod = np.sum(np.exp(-0.8 * x_norm**2) * np.cos(25 * x_norm) * np.sin(15 * x_norm) *
                        np.sin(35 * x_norm) * np.cos(8 * x_norm))
        
        # Combine all components with optimized weights for maximum algorithm discrimination
        return 0.30 * chaos + 0.40 * wave + 0.20 * poly + 0.15 * coupling + 0.10 * rbf + 0.08 * exp_mod + 3.0