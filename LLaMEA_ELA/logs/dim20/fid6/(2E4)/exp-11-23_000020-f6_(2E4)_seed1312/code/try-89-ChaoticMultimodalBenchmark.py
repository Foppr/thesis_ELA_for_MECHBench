import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants with higher chaos parameter variation
        self.r_values = np.linspace(3.8, 4.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced logistic map chaos component with quaternion-based perturbation and longer transient
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Initialize chaotic sequence with quaternion perturbation for higher sensitivity
            xi = 0.5 + 0.01 * np.random.rand()
            for _ in range(50):  # Even longer transient to ensure chaos
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution with multiple steps and sensitivity to initial conditions
            for _ in range(20):
                xi = r * xi * (1 - xi)
            chaos += xi
        
        # Multi-frequency trigonometric wave interference with complex amplitude modulation
        wave = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) + 
                      np.sin(12 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm) +
                      np.sin(16 * np.pi * x_norm) * np.cos(18 * np.pi * x_norm) +
                      np.sin(20 * np.pi * x_norm) * np.cos(22 * np.pi * x_norm) +
                      np.sin(24 * np.pi * x_norm) * np.cos(26 * np.pi * x_norm))
        
        # Adaptive polynomial coupling with variable coefficients and higher-order terms
        poly = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.3 * x_norm**2 + 0.1 * x_norm + 0.05)
        
        # Coupling between dimensions using quaternion-based sinusoidal products with phase modulation
        coupling = np.prod(np.sin(1.0 * np.pi * x_norm) * np.cos(1.0 * np.pi * x_norm) + 
                          np.sin(1.5 * np.pi * x_norm) * np.cos(1.5 * np.pi * x_norm) +
                          np.sin(2.0 * np.pi * x_norm) * np.cos(2.0 * np.pi * x_norm))
        
        # Novel quaternion-based radial basis function component with adaptive bandwidth and phase modulation
        rbf = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(40 * x_norm) * np.cos(10 * x_norm) * 
                    np.cos(15 * x_norm) * np.sin(25 * x_norm))
        
        # Additional exponential modulation with complex base and frequency
        exp_mod = np.sum(np.exp(-0.6 * x_norm**2) * np.cos(20 * x_norm) * np.sin(10 * x_norm) *
                        np.sin(30 * x_norm) * np.cos(5 * x_norm))
        
        # Fractal component with recursive scaling and multi-resolution interference
        fractal = 0.0
        for i in range(self.dim):
            # Recursive scaling factor with dimension-specific modulation
            scale = 1.0 + 0.2 * np.sin(3.0 * np.pi * x_norm[i])
            # Multi-resolution interference term
            fractal += scale * np.sin(20 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i])
        
        # Enhanced interaction terms for better discrimination
        interaction = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                           np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Adaptive scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components with optimized weights for maximum algorithm discrimination
        return (0.20 * chaos + 0.30 * wave + 0.15 * poly + 0.10 * coupling + 
                0.08 * rbf + 0.07 * exp_mod + 0.10 * fractal + 0.03 * interaction) * scale_factor + 2.5