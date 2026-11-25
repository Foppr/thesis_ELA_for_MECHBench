import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal component with multi-scale oscillations
        fractal = 0
        for i in range(self.dim):
            # Multi-frequency sine waves with decreasing amplitude
            for freq in [1, 2, 4, 8]:
                fractal += np.sin(freq * x[i]) * np.exp(-freq * 0.1)
        
        # Self-similar interaction terms using distance-based scaling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                # Fractal-like interaction with scale-dependent strength
                interaction += (np.sin(10 * dist) / (dist + 0.1)) * np.exp(-dist * 0.5)
        
        # Add a global quadratic penalty for distance from origin
        penalty = np.sum(x**2) * 0.01
        
        # Combine components with varying weights
        return 3 * fractal + 0.5 * interaction + penalty + self.dim * 2.0