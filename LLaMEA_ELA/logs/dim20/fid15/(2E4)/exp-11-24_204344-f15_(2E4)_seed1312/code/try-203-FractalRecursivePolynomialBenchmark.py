import numpy as np

class FractalRecursivePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial landscape with enhanced recursive structure
        result = 0.0
        for i in range(self.dim):
            # Enhanced polynomial terms with increased nonlinearity
            poly_term = x[i]**2 + 0.8 * x[i]**3 + 0.2 * x[i]**4 + 0.05 * x[i]**5
            
            # Fractal self-similarity with dynamic scaling factors
            scale_factor = 1.0
            for j in range(5):  # Increased recursion depth
                if i + j < self.dim:
                    # Higher frequency modulation with chaotic component
                    freq_mod = 7.0 + 2.5 * np.sin(i * 0.8 + j * 1.3)
                    scale_factor *= (1.0 + 0.5 * np.sin(x[i] * freq_mod))
            
            result += poly_term * scale_factor
        
        # Enhanced multi-scale chaotic noise injection
        noise = 0.0
        for i in range(self.dim):
            # Chaotic frequency patterns with adaptive coupling
            freq1 = 8.0 + 4.0 * np.sin(i * 0.6)  # Increased base frequency
            freq2 = 5.0 + 3.0 * np.cos(i * 0.4)  # Different pattern
            noise += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                     0.7 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]) +
                     0.3 * np.sin(freq1 * x[i] * 0.5) * np.cos(freq2 * x[i] * 0.5))  # Additional chaotic component
        
        # Stronger cross-dimensional coupling with fractal structure
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling range
                # Fractal-like coupling with dynamic strength
                coupling_strength = 2.0 + 0.8 * np.sin(i * 0.7 + j * 0.5)
                cross_term += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * coupling_strength
        
        # Adaptive basin boundary complexity with dynamic transitions
        basin_term = 0.0
        for i in range(self.dim):
            # Dynamic boundary with enhanced nonlinearity
            boundary = np.abs(x[i]) - 1.0  # Standard boundary
            smooth_boundary = np.tanh(boundary * 8.0)  # Increased sharpness
            basin_term += smooth_boundary**3  # Cubic smoothing for more complexity
        
        # Final combined landscape with adjusted weights
        total = 0.2 * result + 0.5 * noise + 0.25 * cross_term + 0.05 * basin_term
        
        # Global scaling with enhanced complexity factor
        scaling = 1.0 + 0.2 * self.dim
        
        return total * scaling