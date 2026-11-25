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
            for j in range(8):  # Increased recursion depth
                if i + j < self.dim:
                    scale_factor *= (1.0 + 0.6 * np.sin(x[i] * (j + 1) * 4.0))  # Higher frequency modulation
            
            result += poly_term * scale_factor
        
        # Enhanced noise injection at multiple scales
        noise = 0.0
        for i in range(self.dim):
            # Modified multi-scale noise with increased frequency variation
            freq1 = 10.0 + 5.0 * np.sin(i * 1.1)  # Increased base frequency
            freq2 = 6.0 + 4.0 * np.cos(i * 0.5)  # Different frequency pattern
            noise += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                     0.8 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]))  # Higher amplitude coupling
        
        # Increased cross-dimensional coupling strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+9, self.dim)):  # Extended coupling range
                # Stronger fractal coupling with modified structure
                coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * 3.0  # Increased strength
                cross_term += coupling
        
        # Basin boundary complexity with enhanced smoothness
        basin_term = 0.0
        for i in range(self.dim):
            # Enhanced basin boundaries using stronger transitions
            boundary = np.abs(x[i]) - 2.0  # Shifted boundary
            smooth_boundary = np.tanh(boundary * 10.0)  # Increased transition sharpness
            basin_term += smooth_boundary**2
        
        # Novel asymmetric energy wells with dynamic frequency modulation
        well_term = 0.0
        for i in range(self.dim):
            # Asymmetric wells with dynamic modulation - slightly modified
            well = (x[i] - 1.5)**2 * (x[i] + 1.5)**2 * np.sin(x[i] * 7.0)  # Asymmetric well
            # Slight modification to well structure for increased difficulty
            well += 0.3 * np.cos(x[i] * 12.0) * np.exp(-0.5 * x[i]**2)
            well_term += well
        
        # Final combined landscape with modified weights
        total = 0.25 * result + 0.45 * noise + 0.25 * cross_term + 0.06 * basin_term + 0.04 * well_term
        
        # Enhanced global scaling factor for increased complexity
        scaling = 1.0 + 0.3 * self.dim
        
        return total * scaling