import numpy as np

class FractalRecursivePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial landscape with enhanced recursive fractal structure
        result = 0.0
        for i in range(self.dim):
            # Enhanced recursive polynomial terms with increased complexity
            poly_term = x[i]**2 + 0.8 * x[i]**3 + 0.25 * x[i]**4 + 0.05 * x[i]**5
            
            # Intensified fractal self-similarity through higher frequency modulation
            scale_factor = 1.0
            for j in range(6):  # Increased recursion depth
                if i + j < self.dim:
                    scale_factor *= (1.0 + 0.6 * np.sin(x[i] * (j + 1) * 3.0))  # Higher frequency modulation
            
            result += poly_term * scale_factor
        
        # Augmented noise injection at multiple scales with chaotic patterns
        noise = 0.0
        for i in range(self.dim):
            # Enhanced multi-scale noise with increased complexity and chaos
            freq1 = 8.0 + 4.0 * np.sin(i * 0.9)  # Increased base frequency
            freq2 = 5.0 + 3.0 * np.cos(i * 0.4)  # Different frequency pattern
            freq3 = 7.0 + 2.5 * np.sin(i * 0.6)  # Additional frequency component
            noise += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                     0.7 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]) +
                     0.4 * np.sin(freq3 * x[i]) * np.cos(freq1 * x[i]))  # Higher amplitude coupling
        
        # Extended cross-dimensional coupling with dynamic strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended coupling range
                # Stronger fractal coupling with dynamic structure
                coupling_strength = 2.0 + 0.5 * np.sin(i * 0.5)  # Dynamic weight adjustment
                coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * coupling_strength
        
        # Enhanced basin boundary complexity with smoother transitions
        basin_term = 0.0
        for i in range(self.dim):
            # Enhanced basin boundaries using stronger transitions and sharper edges
            boundary = np.abs(x[i]) - 1.5  # Shifted boundary
            smooth_boundary = np.tanh(boundary * 8.0)  # Increased transition sharpness
            basin_term += smooth_boundary**2
        
        # Final combined landscape with modified weights and enhanced scaling
        total = 0.3 * result + 0.5 * noise + 0.15 * cross_term + 0.05 * basin_term
        
        # Enhanced global scaling factor for increased complexity and difficulty
        scaling = 1.0 + 0.25 * self.dim
        
        return total * scaling