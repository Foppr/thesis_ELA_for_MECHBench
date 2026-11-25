import numpy as np

class FractalRecursivePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial landscape with recursive fractal structure
        result = 0.0
        for i in range(self.dim):
            # Recursive polynomial terms with varying degrees
            poly_term = x[i]**2 + 0.5 * x[i]**3 + 0.1 * x[i]**4
            
            # Fractal-like self-similarity through recursive scaling
            scale_factor = 1.0
            for j in range(3):  # 3 levels of recursion
                if i + j < self.dim:
                    scale_factor *= (1.0 + 0.3 * np.sin(x[i] * (j + 1) * 2.0))
            
            result += poly_term * scale_factor
        
        # Adaptive noise injection at multiple scales
        noise = 0.0
        for i in range(self.dim):
            # Multi-scale noise with varying frequencies and amplitudes
            freq1 = 5.0 + 2.0 * np.sin(i)
            freq2 = 3.0 + 1.5 * np.cos(i * 0.5)
            noise += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                     0.5 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]))
        
        # Cross-dimensional coupling with fractal interaction patterns
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for fractal effect
                # Fractal coupling with recursive structure
                coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                cross_term += coupling
        
        # Basin boundary complexity with piecewise smoothness
        basin_term = 0.0
        for i in range(self.dim):
            # Create complex basin boundaries using step functions and smooth transitions
            boundary = np.abs(x[i]) - 1.0
            smooth_boundary = np.tanh(boundary * 5.0)
            basin_term += smooth_boundary**2
        
        # Final combined landscape with adaptive weights
        total = 0.3 * result + 0.4 * noise + 0.2 * cross_term + 0.1 * basin_term
        
        # Add global scaling factor based on dimensionality for increased complexity
        scaling = 1.0 + 0.1 * self.dim
        
        return total * scaling