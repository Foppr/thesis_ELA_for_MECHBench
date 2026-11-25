import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rotation_matrix = np.random.rand(dim, dim) * 2 - 1
        self.rotation_matrix = np.linalg.qr(self.rotation_matrix)[0]
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Rotate input for orientation independence
        x_rot = self.rotation_matrix @ x
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 4)
            sin_component += np.sin(freq * x_rot[i]) * np.cos(freq * x_rot[i] ** 2)
        
        # Radial basis function component with multiple centers
        rbf_component = 0.0
        centers = np.linspace(-3, 3, min(5, self.dim))
        for i in range(len(centers)):
            if i < self.dim:
                rbf_component += np.exp(-0.5 * (x_rot[i] - centers[i % len(centers)]) ** 2)
        
        # Gradient attraction field component
        grad_field = 0.0
        for i in range(self.dim):
            grad_field += (x_rot[i] ** 4 - 10 * x_rot[i] ** 2 + 5) * np.exp(-0.1 * x_rot[i] ** 2)
        
        # Cross-term interaction component
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.sin(x_rot[i] * x_rot[i+1]) * (1 + 0.1 * (x_rot[i] ** 2 + x_rot[i+1] ** 2))
        
        # Combined landscape with adaptive weights
        return 0.5 * sin_component + 0.3 * rbf_component + 0.7 * grad_field + 0.4 * cross_term