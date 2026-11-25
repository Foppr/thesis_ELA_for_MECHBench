import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2.5 * x) * np.cos(1.7 * x) * np.sin(0.9 * x))
        
        # Polynomial potential terms with mixed degrees
        poly_term = np.sum(x**4 + 0.5 * x**3 - 0.3 * x**2 + 0.1 * x)
        
        # Radial gradient component with exponential decay
        r_squared = np.sum(x**2)
        radial_grad = r_squared * np.exp(-0.1 * r_squared) * (1 + 0.2 * np.sin(0.5 * r_squared))
        
        # Non-linear coupling between dimensions using chaotic logistic map-like interactions
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += x[i] * x[i+1] * np.sin(3.1 * x[i]) * np.cos(2.3 * x[i+1])
        
        # Chaotic component with multi-modal structure from nested trigonometric functions
        chaotic_term = np.sum(np.sin(4.0 * x) * np.cos(3.0 * x) * np.sin(2.0 * x) * np.cos(x))
        
        # Add a small random perturbation for increased complexity and irregularity
        noise = 0.01 * np.random.rand()
        
        # Combined function with carefully tuned weights
        return 0.3 * sin_term + 0.25 * poly_term + 0.2 * radial_grad + 0.15 * coupling_term + 0.1 * chaotic_term + noise