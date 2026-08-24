import numpy as np

class AdaptiveRotatedPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        # Generate random rotation matrix
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Apply rotation
        x_rot = self.rotation_matrix @ x_norm
        
        # Polynomial terms with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x_rot[i] ** (2 + i % 3)) * (1.0 + 0.1 * i)
        
        # Trigonometric components with frequency modulation
        trig_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * i
            trig_term += np.sin(freq * x_rot[i] * np.pi) * np.cos(freq * x_rot[i] * np.pi) * (1.0 + 0.2 * np.sin(i * np.pi / 4))
        
        # Exponential decay with sinusoidal modulation
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-0.5 * x_rot[i]**2) * np.sin(3 * x_rot[i] * np.pi) * (1.0 + 0.15 * np.cos(2 * x_rot[i] * np.pi))
        
        # Cross-dimensional interaction with adaptive conditioning
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                condition = 1.0 + 0.3 * (i + j)
                cross_term += (x_rot[i] * x_rot[j]) * np.exp(-condition * (x_rot[i]**2 + x_rot[j]**2)) * np.sin(2 * x_rot[i] * x_rot[j])
        
        # Multimodal component with multiple peaks
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += np.sin(5 * x_rot[i] * np.pi) * np.cos(4 * x_rot[i] * np.pi) * np.exp(-0.3 * x_rot[i]**2)
        
        # Adaptive weighting based on dimension
        weights = np.array([1.0 + 0.1 * i for i in range(self.dim)])
        weighted_poly = np.sum(weights * (x_rot**2))
        
        # Combine all terms
        return poly_term + 0.5 * trig_term + 0.3 * exp_term + 0.4 * cross_term + 0.2 * multi_term + 0.1 * weighted_poly