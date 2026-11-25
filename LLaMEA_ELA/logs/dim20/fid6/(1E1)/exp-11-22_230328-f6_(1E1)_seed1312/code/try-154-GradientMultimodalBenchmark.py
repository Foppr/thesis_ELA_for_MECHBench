import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize conditioning parameters for each dimension
        self.conditioning = np.random.uniform(0.5, 2.0, dim)
        # Create multiple local minima with varying depths and positions
        self.minima_positions = np.random.uniform(-4.0, 4.0, (10, dim))
        self.minima_depths = np.random.uniform(1.0, 5.0, 10)
        # Saddle point configuration
        self.saddle_positions = np.random.uniform(-3.0, 3.0, (5, dim))
        self.saddle_strengths = np.random.uniform(0.5, 2.0, 5)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        quad_term = np.sum(self.conditioning * x_norm ** 2)
        
        # Multiple local minima attraction
        minima_term = 0.0
        for i in range(10):
            dist = np.sum((x_norm - self.minima_positions[i]) ** 2)
            minima_term += self.minima_depths[i] * np.exp(-dist / (2.0 * (0.5 + 0.3 * np.sin(i))))
        
        # Saddle point repulsion
        saddle_term = 0.0
        for i in range(5):
            dist = np.sum((x_norm - self.saddle_positions[i]) ** 2)
            saddle_term += self.saddle_strengths[i] * np.exp(-dist / (2.0 * (0.3 + 0.2 * np.cos(i))))
        
        # Gradient-based periodic modulation
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Combined fitness with dynamic scaling
        combined = quad_term + minima_term - saddle_term + 0.5 * grad_mod
        
        # Add small random noise for robustness
        noise = 0.01 * np.random.uniform(-1, 1)
        
        return combined + noise