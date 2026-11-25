import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal landscape with self-similar structure
        fractal = 0.0
        for i in range(self.dim):
            # Nested sinusoidal terms creating fractal-like behavior
            term = 0.0
            for k in range(1, 6):
                freq = 2 ** k
                term += np.sin(freq * x[i]) / (k ** 1.5)
            fractal += term ** 2
            
        # Dynamic curvature based on dimension and position
        curvature = 0.0
        for i in range(self.dim):
            # Varying curvature strength based on position and dimension
            curv = (x[i] ** 2 + 0.1 * np.sin(x[i])) * (1.0 + 0.3 * np.cos(i * 0.5))
            curvature += curv
            
        # Multi-scale interaction terms with varying weights
        scale_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-dependent interaction with fractal characteristics
                dist = np.abs(x[i] - x[j])
                scale_factor = 1.0 / (1.0 + 0.1 * dist)
                scale_interaction += scale_factor * np.sin(3.0 * (x[i] + x[j]))
                
        # Polynomial with mixed convexity and fractal scaling
        poly = 0.0
        for i in range(self.dim):
            poly += (x[i] ** 4 + 0.5 * x[i] ** 3 + 0.1 * x[i] ** 2) * (1.0 + 0.2 * np.sin(i * 0.7))
            
        # Scale-invariant feature with dimension-dependent normalization
        scale_norm = 1.0 + 0.1 * np.log(self.dim + 1.0)
        
        return scale_norm * (0.3 * poly + 0.4 * curvature + 0.2 * scale_interaction + 0.1 * fractal)