import numpy as np

class FractalRecursivePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial landscape with enhanced fractal structure
        result = 0.0
        for i in range(self.dim):
            # Enhanced recursive polynomial terms with dynamic exponents
            exponent = 2 + 0.5 * np.sin(i) + 0.3 * np.cos(i * 1.5)
            poly_term = x[i]**exponent + 0.4 * x[i]**(exponent + 1) + 0.05 * x[i]**(exponent + 2)
            
            # Fractal-like self-similarity with dynamic scaling factors
            scale_factor = 1.0
            for j in range(4):  # Increased recursion depth
                if i + j < self.dim:
                    freq = (j + 1) * 1.5 + np.sin(i * 0.7)
                    scale_factor *= (1.0 + 0.2 * np.cos(x[i] * freq))
            
            result += poly_term * scale_factor
        
        # Enhanced adaptive noise injection with dynamic frequencies
        noise = 0.0
        for i in range(self.dim):
            # Dynamic frequency modulation based on dimension index
            freq1 = 4.0 + 3.0 * np.sin(i * 0.5)
            freq2 = 2.5 + 2.0 * np.cos(i * 0.3)
            freq3 = 3.5 + 1.8 * np.sin(i * 0.8)
            
            noise += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                     0.6 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]) +
                     0.3 * np.sin(freq3 * x[i]) * np.cos(freq1 * x[i]))
        
        # Cross-dimensional coupling with enhanced fractal interaction patterns
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended range for stronger coupling
                # Enhanced coupling with dynamic strength based on dimension
                strength = 1.0 + 0.3 * np.sin(i * 0.5) * np.cos(j * 0.3)
                coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j] * strength)
                cross_term += coupling
        
        # Basin boundary complexity with dynamic smooth transitions
        basin_term = 0.0
        for i in range(self.dim):
            # Dynamic boundary creation with varying thresholds
            threshold = 1.0 + 0.2 * np.sin(i * 0.7)
            boundary = np.abs(x[i]) - threshold
            smooth_boundary = np.tanh(boundary * 6.0)  # Increased steepness
            basin_term += smooth_boundary**2
        
        # Additional fractal complexity through nested trigonometric functions
        trig_term = 0.0
        for i in range(self.dim):
            # Nested sine-cosine combinations with varying frequencies
            freq1 = 2.0 + np.sin(i * 0.4)
            freq2 = 1.5 + np.cos(i * 0.6)
            trig_term += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        
        # Final combined landscape with adaptive weights
        total = 0.25 * result + 0.35 * noise + 0.25 * cross_term + 0.15 * basin_term + 0.05 * trig_term
        
        # Enhanced global scaling factor based on dimensionality
        scaling = 1.0 + 0.15 * self.dim + 0.02 * np.sin(self.dim * 0.3)
        
        return total * scaling