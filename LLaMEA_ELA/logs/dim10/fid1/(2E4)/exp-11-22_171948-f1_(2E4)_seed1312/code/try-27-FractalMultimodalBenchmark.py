import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal-like self-similar structure using recursive scaling
        for i in range(self.dim):
            # Base fractal component with multi-scale periodicity
            scale_factor = 1.0 + 0.3 * np.sin(0.5 * x[i])
            result += scale_factor * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
            # Chaotic frequency modulation based on golden ratio
            freq_mod = 1.618 + 0.4 * np.sin(x[i])
            result += 0.5 * np.sin(freq_mod * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale harmonic interactions with varying amplitudes
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                # Distance-based interaction with fractal scaling
                dist = np.abs(x[i] - x[j])
                interaction = np.sin(2 * np.pi * dist) * np.exp(-0.5 * dist**2)
                result += 0.3 * interaction * (1 + 0.2 * np.sin(5 * x[i]))
        
        # Cross-dimensional polynomial coupling with fractal-like behavior
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**3 - x[j]**2) * np.sin(x[i] + x[j])
        
        result += 0.4 * poly_coupling / (self.dim * (self.dim - 1) / 2)
        
        # Add chaotic logistic map component with fractal scaling
        logistic_sum = 0.0
        for i in range(self.dim):
            # Normalize input to [0,1] for logistic map
            norm_x = (x[i] + 5.0) / 10.0
            logistic_val = 4 * norm_x * (1 - norm_x)
            logistic_sum += np.sin(2 * np.pi * logistic_val) * np.cos(3 * np.pi * logistic_val)
        
        result += 0.2 * logistic_sum
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result