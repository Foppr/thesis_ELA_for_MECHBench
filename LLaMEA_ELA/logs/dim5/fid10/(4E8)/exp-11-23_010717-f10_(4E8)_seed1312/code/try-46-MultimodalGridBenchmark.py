import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like quadratic basin with varying curvature and enhanced complexity
        basin = 0.1 * np.sum((x**2) * (1 + 0.3 * np.sin(3 * x) * np.cos(2 * x)) * (1 + 0.1 * np.sin(5 * x)))
        
        # Chaotic grid of global minima with fractal-like interactions and increased complexity
        grid_minima = 0.0
        for i in range(self.dim):
            # Use chaotic sine-cosine combinations with varying frequencies and amplitudes
            grid_minima += 3.5 * np.sin(0.9 * x[i]) * np.cos(0.6 * x[i]) * np.sin(0.4 * x[i]**2) * np.cos(0.15 * x[i]**3)
            
        # Enhanced cross-dimensional coupling terms for increased complexity and non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use more complex interaction functions with combined trigonometric terms and additional polynomial factors
                cross_term += 0.9 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] + x[j]))
                
        # Add a more complex chaotic noise component with fractal-like structure and higher frequency
        noise = 0.06 * np.sum(np.sin(25 * x) * np.cos(12 * x) * np.sin(7 * x) * np.cos(3 * x))
        
        return basin + grid_minima + cross_term + noise