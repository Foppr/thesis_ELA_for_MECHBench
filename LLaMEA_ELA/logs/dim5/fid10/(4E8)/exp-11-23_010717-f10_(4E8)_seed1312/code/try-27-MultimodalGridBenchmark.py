import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like quadratic basin with varying curvature
        basin = 0.05 * np.sum((x**2) * (1 + 0.1 * np.sin(3 * x)))
        
        # Chaotic grid of global minima with fractal-like interactions
        grid_minima = 0.0
        for i in range(self.dim):
            # Use chaotic sine-cosine combinations with varying frequencies
            grid_minima += 3.0 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i]) * np.sin(0.2 * x[i]**2)
            
        # Cross-dimensional coupling terms for increased complexity
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.5 * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
                
        # Add a chaotic noise component with fractal-like structure
        noise = 0.02 * np.sum(np.sin(15 * x) * np.cos(7 * x))
        
        return basin + grid_minima + cross_term + noise