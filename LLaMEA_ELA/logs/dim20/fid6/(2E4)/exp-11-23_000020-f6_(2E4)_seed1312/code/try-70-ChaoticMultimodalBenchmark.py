import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants with higher chaos parameter variation and nested fractal structure
        self.r_values = np.linspace(3.8, 4.0, dim)
        # Add fractal scaling factor for nested chaos
        self.fractal_scale = 1.0 + 0.5 * np.sin(np.arange(dim) * np.pi / dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced logistic map chaos component with nested fractal structure and dynamic phase modulation
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i] * self.fractal_scale[i]
            # Initialize chaotic sequence with quaternion perturbation for higher sensitivity
            xi = 0.5 + 0.01 * np.random.rand()
            for _ in range(100):  # Even longer transient to ensure chaos
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution with multiple steps and sensitivity to initial conditions
            for _ in range(30):
                xi = r * xi * (1 - xi)
            chaos += xi
        
        # Multi-frequency trigonometric wave interference with complex amplitude modulation and dynamic phase
        wave = 0.0
        frequencies = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
        for i in range(0, len(frequencies), 2):
            if i + 1 < len(frequencies):
                wave += np.sin(frequencies[i] * np.pi * x_norm) * np.cos(frequencies[i+1] * np.pi * x_norm)
        
        # Adaptive polynomial coupling with variable coefficients and higher-order terms
        poly = np.sum(x_norm**6 + 0.7 * x_norm**5 + 0.4 * x_norm**4 + 0.3 * x_norm**3 + 0.2 * x_norm**2 + 0.1 * x_norm + 0.05)
        
        # Coupling between dimensions using quaternion-based sinusoidal products with dynamic phase modulation
        coupling = np.prod(np.sin(1.0 * np.pi * x_norm) * np.cos(1.0 * np.pi * x_norm) + 
                          np.sin(1.5 * np.pi * x_norm) * np.cos(1.5 * np.pi * x_norm) +
                          np.sin(2.0 * np.pi * x_norm) * np.cos(2.0 * np.pi * x_norm) +
                          np.sin(2.5 * np.pi * x_norm) * np.cos(2.5 * np.pi * x_norm))
        
        # Novel quaternion-based radial basis function component with adaptive bandwidth and phase modulation
        rbf = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(40 * x_norm) * np.cos(10 * x_norm) * 
                    np.cos(15 * x_norm) * np.sin(25 * x_norm) * np.cos(30 * x_norm))
        
        # Additional exponential modulation with complex base and frequency, now including dynamic scaling
        exp_mod = np.sum(np.exp(-0.6 * x_norm**2) * np.cos(20 * x_norm) * np.sin(10 * x_norm) *
                        np.sin(30 * x_norm) * np.cos(5 * x_norm) * np.sin(35 * x_norm))
        
        # Add dynamic phase modulation to enhance multimodality
        phase_mod = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm) * np.sin(9 * x_norm))
        
        # Combine all components with optimized weights for maximum algorithm discrimination
        return 0.2 * chaos + 0.3 * wave + 0.2 * poly + 0.1 * coupling + 0.1 * rbf + 0.08 * exp_mod + 0.05 * phase_mod + 2.5