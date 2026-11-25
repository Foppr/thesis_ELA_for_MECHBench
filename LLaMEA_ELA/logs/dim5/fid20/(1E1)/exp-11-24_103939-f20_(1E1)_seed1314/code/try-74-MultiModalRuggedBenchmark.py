import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and exponential growth
        f1 = np.sum(np.power(np.abs(x_scaled), 4) + 0.3 * np.power(np.abs(x_scaled), 3) - 0.2 * np.power(np.abs(x_scaled), 2) + 0.05 * np.abs(x_scaled))
        
        # Nested trigonometric components with exponentially increasing frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq_factor = 2 ** (i % 5)
            f2 += np.sin(freq_factor * x_scaled[i]) * np.cos(freq_factor * x_scaled[i] * 1.5) * np.sin(freq_factor * x_scaled[i] * 0.7)
        
        # Fractal-like radial basis functions with self-similar structure
        f3 = 0.0
        for i in range(min(8, self.dim)):
            center = np.sin(i * np.pi / 4) * 0.5
            width = 0.1 + 0.05 * np.cos(i)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**(2 + i % 3))
        
        # Chaotic cross-dimensional interaction terms with non-linear coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_scaled[i] * x_scaled[j]) * np.cos(x_scaled[i] + x_scaled[j])
                f4 += coupling * (i + j) / (self.dim * (self.dim - 1) / 2)
        
        # Asymmetric saddle point structure with exponential decay
        f5 = np.sum(np.power(x_scaled**2 - 0.3, 3) * np.exp(-0.5 * np.abs(x_scaled)))
        
        # High-frequency oscillation with exponentially increasing complexity
        f6 = 0.0
        for i in range(self.dim):
            freq = 10 * (i + 1)
            f6 += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.8) * np.sin(freq * x_scaled[i] * 0.3)
        
        # Combined penalty for boundary avoidance with exponential weighting
        f7 = 0.5 * np.sum(np.power(np.abs(x_scaled), 3.5) + np.power(np.abs(x_scaled), 2.5))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7