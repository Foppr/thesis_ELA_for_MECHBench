import numpy as np

class GradientTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random coefficients for trigonometric components
        self.coeffs = np.random.uniform(-2.0, 2.0, dim)
        # Precompute radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gradient-based attraction field component
        grad_field = 0.0
        for i in range(self.dim):
            grad_field += (x[i] - self.coeffs[i])**2 * np.sin(x[i])**2
        
        # Trigonometric coupling between dimensions
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(x[i] * x[j]) * np.cos((x[i] + x[j])**2)
        
        # Fractal-like radial basis function component with multiple centers
        rbf_sum = 0.0
        for i in range(10):
            rbf_sum += self.rbf_widths[i] * np.exp(-0.5 * np.sum((x - self.rbf_centers[i])**2) / (self.rbf_widths[i]**2))
        
        # Polynomial and harmonic mixing component
        poly_harmonic = 0.0
        for i in range(self.dim):
            poly_harmonic += (x[i]**3 + x[i]**5) * np.cos(x[i] / (i+1)) + 0.5 * np.sin(x[i])**4
        
        # Cross-dimensional interaction with varying weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_interaction += (x[i] - x[j])**2 * np.exp(-0.1 * abs(x[i] - x[j]))
        
        # Add a noise modulation term to increase conditioning
        noise = 0.1 * np.sum(np.sin(x * np.pi / 4.0))
        
        # Combine all components with different weights
        return grad_field + trig_coupling + rbf_sum + poly_harmonic + cross_interaction + noise