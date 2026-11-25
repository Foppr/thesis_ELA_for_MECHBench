import numpy as np

class FractalRecursivePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial landscape with recursive fractal structure
        result = 0.0
        for i in range(self.dim):
            # Modified recursive polynomial terms with altered coefficients
            poly_term = x[i]**2 + 0.7 * x[i]**3 + 0.15 * x[i]**4
            
            # Fractal-like self-similarity through recursive scaling
            scale_factor = 1.0
            for j in range(4):  # Increased recursion depth
                if i + j < self.dim:
                    scale_factor *= (1.0 + 0.4 * np.sin(x[i] * (j + 1) * 2.5))  # Higher frequency modulation
            
            result += poly_term * scale_factor
        
        # Enhanced noise injection at multiple scales
        noise = 0.0
        for i in range(self.dim):
            # Modified multi-scale noise with increased frequency variation
            freq1 = 6.0 + 3.0 * np.sin(i * 0.7)  # Increased base frequency
            freq2 = 4.0 + 2.0 * np.cos(i * 0.3)  # Different frequency pattern
            noise += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                     0.6 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]))  # Higher amplitude coupling
        
        # Increased cross-dimensional coupling strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling range
                # Stronger fractal coupling with modified structure
                coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * 1.5  # Increased strength
        
        # Basin boundary complexity with enhanced smoothness
        basin_term = 0.0
        for i in range(self.dim):
            # Enhanced basin boundaries using stronger transitions
            boundary = np.abs(x[i]) - 1.2  # Shifted boundary
            smooth_boundary = np.tanh(boundary * 6.0)  # Increased transition sharpness
            basin_term += smooth_boundary**2
        
        # Final combined landscape with modified weights
        total = 0.25 * result + 0.45 * noise + 0.25 * cross_term + 0.05 * basin_term
        
        # Enhanced global scaling factor for increased complexity
        scaling = 1.0 + 0.15 * self.dim
        
        return total * scaling