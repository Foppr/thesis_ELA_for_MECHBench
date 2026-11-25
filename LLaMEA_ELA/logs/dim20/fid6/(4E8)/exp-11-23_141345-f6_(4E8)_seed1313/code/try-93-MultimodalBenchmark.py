import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillations with chaotic frequency modulation
        sin_term = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.sin(1.5 * x) * np.cos(0.8 * x))
        
        # Higher-order polynomial potential with mixed degrees and interaction terms
        poly_term = np.sum(x**6 + 0.7 * x**5 - 0.4 * x**4 + 0.2 * x**3 - 0.1 * x**2 + 0.05 * x)
        
        # Radial gradient component with multi-scale exponential decay and trigonometric modulation
        r_squared = np.sum(x**2)
        radial_grad = r_squared * np.exp(-0.15 * r_squared) * (1 + 0.3 * np.sin(0.7 * r_squared) + 0.2 * np.cos(0.4 * r_squared))
        
        # Non-linear coupling between dimensions using chaotic logistic map-like interactions with sine/cosine mixing
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += x[i] * x[i+1] * np.sin(4.2 * x[i]) * np.cos(3.5 * x[i+1]) * np.tan(1.3 * x[i] + 0.5 * x[i+1])
        
        # Chaotic component with multi-modal structure from nested trigonometric functions and exponential scaling
        chaotic_term = np.sum(np.sin(5.0 * x) * np.cos(4.0 * x) * np.sin(3.0 * x) * np.cos(2.0 * x) * np.sin(x) * np.exp(-0.05 * r_squared))
        
        # Additional cross-dimensional interaction with fractal-like structure
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_term += (x[i]**2 + x[j]**2) * np.sin(2.5 * x[i] * x[j]) * np.cos(1.8 * x[i] * x[j])
        
        # Add a small random perturbation for increased complexity and irregularity
        noise = 0.01 * np.random.rand()
        
        # Combined function with carefully tuned weights
        return 0.25 * sin_term + 0.2 * poly_term + 0.25 * radial_grad + 0.15 * coupling_term + 0.1 * chaotic_term + 0.05 * fractal_term + noise