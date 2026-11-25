import numpy as np

class PolynomialSinusoidalAdaptiveLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial coefficients for varying curvature
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 4))
        # Precompute sinusoidal coupling weights and frequencies
        self.sin_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.sin_frequencies = 1.0 + 2.0 * np.random.rand(dim)
        # Precompute adaptive conditioning parameters
        self.condition_params = np.random.uniform(0.5, 2.0, dim)
        # Precompute local minima positions
        self.minima_positions = np.random.uniform(-3.0, 3.0, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial potential component with varying degrees
        poly_sum = 0.0
        for i in range(self.dim):
            poly_val = np.polyval(self.poly_coeffs[i], x_norm[i])
            poly_sum += poly_val * np.exp(-0.1 * x_norm[i]**2)
        
        # Sinusoidal coupling component with adaptive frequencies
        sin_sum = 0.0
        for i in range(self.dim):
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += self.sin_weights[i, j] * np.sin(self.sin_frequencies[i] * (x_norm[i] - x_norm[j]))
            sin_sum += coupling * np.exp(-0.2 * x_norm[i]**2)
        
        # Adaptive conditioning component with dynamic scaling
        cond_sum = 0.0
        for i in range(self.dim):
            condition_factor = self.condition_params[i] * (1.0 + 0.5 * np.sin(x_norm[i] * 2))
            cond_sum += condition_factor * x_norm[i]**4
        
        # Local minima attraction component
        minima_sum = 0.0
        for i in range(self.dim):
            dist_to_min = np.sum((x_norm - self.minima_positions[i])**2)
            minima_sum += np.exp(-dist_to_min) * np.cos(3 * x_norm[i])
        
        # Multi-scale harmonic component
        harm_sum = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * np.pi / self.dim)
            harm_sum += scale * np.sin(7 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Combined landscape with weighted contributions
        result = 0.3 * poly_sum + 0.25 * sin_sum + 0.2 * cond_sum + 0.15 * minima_sum + 0.1 * harm_sum
        
        # Global scaling and noise modulation
        noise = 0.01 * np.sum(np.cos(x_norm * 5))
        return result * (1.0 + 0.2 * np.abs(x_norm).mean()) + noise + 0.03 * np.sum(np.abs(x_norm)**6)