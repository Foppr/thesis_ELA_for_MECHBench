import numpy as np

class PolynomialChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coefficients for dynamic modulation
        self.coeffs = np.array([np.sin(i * 0.7) * np.cos(i * 0.9) + 1.0 for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial landscape with varying degrees
        result = 0.0
        for i in range(self.dim):
            # Adaptive degree based on chaotic coefficients
            degree = 2 + int(abs(self.coeffs[i]) * 3) % 4
            result += (x[i] ** degree) * (0.5 + 0.5 * np.sin(i * 0.3))
        
        # Add radial basis function network with adaptive centers and widths
        rb_centers = np.array([np.sin(i * 0.8) * 3.0 for i in range(self.dim)])
        rb_widths = np.array([0.5 + 0.3 * np.cos(i * 0.6) for i in range(self.dim)])
        
        for i in range(self.dim):
            # Dynamic width modulation
            width = rb_widths[i] * (1.0 + 0.2 * np.sin(i * 0.4))
            center = rb_centers[i] * (1.0 + 0.1 * np.cos(i * 0.5))
            result += 0.8 * np.exp(-0.5 * ((x[i] - center) / width) ** 2)
        
        # Add chaotic gradient modulation with polynomial interactions
        for i in range(self.dim):
            # Chaotic gradient coefficient
            grad_coef = 1.0 + 0.3 * np.sin(i * 1.2) * np.cos(i * 1.5)
            result += grad_coef * x[i] * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
        
        # Add multi-dimensional coupling with polynomial chaos terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Polynomial chaos interaction term
                poly_term = (x[i] + x[j]) ** 2 + (x[i] - x[j]) ** 3
                result += 0.3 * poly_term * np.sin(i * 0.6) * np.cos(j * 0.8)
        
        # Add fractal-like noise with chaotic frequency modulation
        noise_freq = np.array([np.sin(i * 0.4) + np.cos(i * 0.7) for i in range(self.dim)])
        fractal_noise = np.sum(np.sin(noise_freq * x) * np.cos(noise_freq * x))
        result += 0.2 * fractal_noise
        
        # Add global conditioning factor with chaotic scaling
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.3)
        result *= condition_factor
        
        return result