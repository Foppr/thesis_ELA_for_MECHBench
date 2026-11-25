import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths
        np.random.seed(42)
        self.centers = np.random.uniform(-1, 1, (dim, 5))
        self.widths = np.random.uniform(0.5, 2.0, 5)
        # Precompute attraction points for gradient fields
        self.attraction_points = np.random.uniform(-1, 1, (dim, 3))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.3 * i)
            amp = 1.5 + 0.5 * np.cos(0.4 * i)
            phase = 0.5 * np.sin(0.6 * i)
            f1 += amp * np.sin(freq * x_norm[i] + phase) * np.exp(-0.2 * x_norm[i]**2)
        
        # Radial basis function component with multiple centers
        f2 = 0.0
        for i in range(self.dim):
            rb_value = 0.0
            for j in range(5):
                diff = x_norm[i] - self.centers[i, j]
                rb_value += self.widths[j] * np.exp(-0.5 * diff**2)
            f2 += rb_value
        
        # Gradient attraction fields with varying strengths
        f3 = 0.0
        for i in range(self.dim):
            attraction = 0.0
            for j in range(3):
                diff = x_norm[i] - self.attraction_points[i, j]
                strength = 1.0 + 0.5 * np.sin(0.7 * j)
                attraction += strength * np.exp(-0.3 * diff**2)
            f3 += attraction
        
        # Mixed polynomial and trigonometric component with coupling
        f4 = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i]**6 + 0.8 * x_norm[i]**4 + 0.3 * x_norm[i]**2
            trig_term = np.sin(3.0 * x_norm[i]) + 0.7 * np.cos(2.5 * x_norm[i])
            f4 += poly_term * trig_term
        
        # Cross-dimensional coupling with chaotic interaction
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x_norm[i] + x_norm[j])) * np.cos(0.3 * (x_norm[i] - x_norm[j]))
                chaos_factor = 0.8 + 0.4 * np.sin(0.9 * (i + j))
                f5 += coupling * chaos_factor
        
        # Combine all components with dynamic weights
        weights = [1.2, 0.8, 1.0, 0.6, 0.9]
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5