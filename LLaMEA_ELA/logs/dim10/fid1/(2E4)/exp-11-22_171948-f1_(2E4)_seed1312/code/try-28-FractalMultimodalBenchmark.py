import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced fractal-like self-similar structure with multi-scale periodicity
        for i in range(self.dim):
            # Base fractal component with dynamic scaling
            scale_factor = 1.0 + 0.4 * np.sin(0.7 * x[i])
            result += scale_factor * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
            # Enhanced chaotic frequency modulation based on golden ratio and sine
            freq_mod = 1.618 + 0.5 * np.sin(x[i] * 0.5)
            result += 0.6 * np.sin(freq_mod * x[i]**2) * np.exp(-0.15 * x[i]**2)
        
        # Multi-scale harmonic interactions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                # Distance-based interaction with enhanced fractal scaling
                dist = np.abs(x[i] - x[j])
                interaction = np.sin(3 * np.pi * dist) * np.exp(-0.3 * dist**2)
                result += 0.4 * interaction * (1 + 0.3 * np.sin(7 * x[i]))
        
        # Cross-dimensional polynomial coupling with enhanced complexity
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # More complex coupling with additional terms
                poly_coupling += (x[i]**3 - x[j]**2 + x[i]*x[j]) * np.sin(x[i] + x[j])
        
        result += 0.5 * poly_coupling / (self.dim * (self.dim - 1) / 2)
        
        # Add enhanced chaotic logistic map component with fractal scaling
        logistic_sum = 0.0
        for i in range(self.dim):
            # Normalize input to [0,1] for logistic map
            norm_x = (x[i] + 5.0) / 10.0
            logistic_val = 4 * norm_x * (1 - norm_x)
            logistic_sum += np.sin(3 * np.pi * logistic_val) * np.cos(4 * np.pi * logistic_val) * np.exp(-0.2 * x[i]**2)
        
        result += 0.3 * logistic_sum
        
        # Add high-frequency oscillation component for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        result += 0.1 * high_freq
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result