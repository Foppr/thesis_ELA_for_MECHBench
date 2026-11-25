import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms with varying degrees
        poly_term = np.sum(x**4 + 0.5 * x**3 + 0.2 * x**2)
        
        # Sinusoidal oscillations with chaotic frequency modulation
        sin_term = np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * np.sin(0.7 * x))
        
        # Cross-dimensional coupling with exponential decay
        cross_term = np.sum(np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Logarithmic barrier near the origin to increase conditioning
        r_squared = np.sum(x**2)
        barrier_term = -np.log(1e-10 + r_squared / 25.0)
        
        # Chaotic component with irrational frequency ratios
        chaotic_term = np.sum(np.sin(np.pi * np.sqrt(2) * x) * np.cos(np.pi * np.sqrt(3) * x))
        
        # Additional multimodal component with saddle point structure
        saddle_term = np.sum(x**2 * np.sin(1.0 / (1e-10 + np.abs(x))))
        
        # Combine all terms with carefully tuned weights
        return 0.3 * poly_term + 0.25 * sin_term + 0.2 * cross_term + 0.15 * barrier_term + 0.05 * chaotic_term + 0.05 * saddle_term