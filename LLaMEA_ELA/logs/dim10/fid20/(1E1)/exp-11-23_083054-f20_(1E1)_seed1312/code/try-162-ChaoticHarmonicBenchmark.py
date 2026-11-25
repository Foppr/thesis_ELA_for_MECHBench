import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r_values = np.array([3.5 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        self.step_widths = np.array([0.1 + 0.2 * np.cos(i * 0.6) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic logistic map component
        chaotic_sum = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            x_logistic = 0.5
            for _ in range(10):  # Iterate to reach chaotic regime
                x_logistic = r * x_logistic * (1 - x_logistic)
            chaotic_sum += x_logistic * np.sin(x_norm[i] * 3.0) * np.cos(x_norm[i] * 2.0)
        
        # Spherical harmonics component with varying degrees
        sph_harm_sum = 0.0
        for i in range(self.dim):
            degree = 2 + i % 3
            order = -degree + (i % (2 * degree + 1))
            sph_harm_sum += np.sin(degree * x_norm[i]) * np.cos(order * x_norm[i]) * (1.0 + 0.2 * np.sin(x_norm[i]))
        
        # Asymmetric step functions
        step_sum = 0.0
        for i in range(self.dim):
            step_width = self.step_widths[i]
            if x_norm[i] > 0:
                step_sum += (x_norm[i] - step_width) ** 2 * np.exp(-x_norm[i]**2)
            else:
                step_sum += (x_norm[i] + step_width) ** 2 * np.exp(-x_norm[i]**2)
        
        # Combine components with dynamic weights
        weights = [0.4 + 0.1 * np.sin(0.5 * i) for i in range(3)]
        return weights[0] * chaotic_sum + weights[1] * sph_harm_sum + weights[2] * step_sum