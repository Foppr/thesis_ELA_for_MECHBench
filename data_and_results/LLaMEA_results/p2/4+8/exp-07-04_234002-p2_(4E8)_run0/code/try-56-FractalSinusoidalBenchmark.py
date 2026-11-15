import numpy as np

class FractalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Recursive fractal-like structure with sine waves
        for i in range(self.dim):
            # Base fractal component with recursive scaling
            val = x[i]
            scale = 1.0
            for k in range(1, 6):  # Up to 5 levels of recursion
                scale *= 0.5
                val += scale * np.sin(2**k * val)
            
            # Add polynomial conditioning
            result += 0.5 * val**2 + 0.1 * val**3 + 0.02 * val**4
            
        # Cross-dimensional coupling with fractal interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling term
                coupling = np.sin(3.0 * x[i]) * np.cos(2.0 * x[j])
                result += 0.05 * coupling * (1.0 + 0.1 * np.sin(5.0 * (x[i] + x[j])))
                
        # Add a global self-similar scaling factor
        global_scale = 1.0 + 0.3 * np.sum(np.sin(0.5 * x)**2)
        result *= global_scale
        
        return result