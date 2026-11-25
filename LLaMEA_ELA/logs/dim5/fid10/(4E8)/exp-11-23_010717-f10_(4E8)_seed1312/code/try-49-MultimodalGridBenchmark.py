import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like quadratic basin with increased curvature and chaotic interactions
        basin = 0.15 * np.sum((x**2) * (1 + 0.3 * np.sin(4 * x) * np.cos(3 * x)))
        
        # Chaotic grid of global minima with modified frequencies and amplitude scaling
        grid_minima = 0.0
        for i in range(self.dim):
            # Use altered sine-cosine combinations with higher frequency components
            grid_minima += 5.0 * np.sin(1.0 * x[i]) * np.cos(0.6 * x[i]) * np.sin(0.4 * x[i]**2) * np.cos(0.15 * x[i]**3)
            
        # Enhanced cross-dimensional coupling with additional trigonometric interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add cubic interaction and modified cross-term scaling
                cross_term += 1.2 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] + x[j]))
                
        # Perturbed noise component with higher frequency chaotic structure
        noise = 0.08 * np.sum(np.sin(25 * x) * np.cos(15 * x) * np.sin(7 * x))
        
        return basin + grid_minima + cross_term + noise