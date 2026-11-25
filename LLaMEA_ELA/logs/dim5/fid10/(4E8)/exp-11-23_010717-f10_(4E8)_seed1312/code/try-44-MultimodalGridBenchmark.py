import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like quadratic basin with varying curvature and enhanced complexity
        basin = 0.1 * np.sum((x**2) * (1 + 0.2 * np.sin(3 * x) * np.cos(2 * x)))
        
        # Chaotic grid of global minima with fractal-like interactions and increased complexity
        grid_minima = 0.0
        for i in range(self.dim):
            # Use chaotic sine-cosine combinations with varying frequencies and amplitudes
            grid_minima += 4.0 * np.sin(0.8 * x[i]) * np.cos(0.5 * x[i]) * np.sin(0.3 * x[i]**2) * np.cos(0.1 * x[i]**3)
            
        # Enhanced cross-dimensional coupling terms for increased complexity and non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use more complex interaction functions with combined trigonometric terms
                cross_term += 0.8 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * (x[i]**2 + x[j]**2)
                
        # Add a more complex chaotic noise component with fractal-like structure and higher frequency
        noise = 0.05 * np.sum(np.sin(20 * x) * np.cos(10 * x) * np.sin(5 * x))
        
        # Perturbed global minimum to increase algorithmic challenge while preserving a clear global optimum
        perturbation = 0.01 * np.sum((x - 0.5)**4)
        
        # Add a novel hyper-chaotic term with multiple interacting frequencies for enhanced complexity
        hyper_chaos = 0.02 * np.sum(np.sin(10 * x) * np.cos(7 * x) * np.sin(3 * x) * np.cos(x))
        
        return basin + grid_minima + cross_term + noise + perturbation + hyper_chaos