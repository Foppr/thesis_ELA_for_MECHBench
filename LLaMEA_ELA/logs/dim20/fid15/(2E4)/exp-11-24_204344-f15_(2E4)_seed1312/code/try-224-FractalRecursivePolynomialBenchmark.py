import numpy as np

class FractalRecursivePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial landscape with enhanced recursive fractal structure
        result = 0.0
        for i in range(self.dim):
            # Enhanced recursive polynomial terms with modified coefficients
            poly_term = x[i]**2 + 0.8 * x[i]**3 + 0.2 * x[i]**4 + 0.05 * x[i]**5
            
            # Enhanced fractal-like self-similarity through recursive scaling
            scale_factor = 1.0
            for j in range(8):  # Increased recursion depth
                if i + j < self.dim:
                    scale_factor *= (1.0 + 0.6 * np.sin(x[i] * (j + 1) * 4.0))  # Higher frequency modulation
            
            result += poly_term * scale_factor
        
        # Enhanced noise injection at multiple scales with chaotic components
        noise = 0.0
        for i in range(self.dim):
            # Multi-scale noise with increased frequency variation and chaotic elements
            freq1 = 10.0 + 5.0 * np.sin(i * 1.1)  # Increased base frequency
            freq2 = 6.0 + 4.0 * np.cos(i * 0.5)   # Different frequency pattern
            freq3 = 7.0 + 3.0 * np.sin(i * 0.7)   # Additional chaotic frequency
            
            noise += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                     0.8 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]) +
                     0.3 * np.sin(freq3 * x[i]))  # Higher amplitude coupling with chaotic component
        
        # Stronger cross-dimensional coupling strength with extended range
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+9, self.dim)):  # Extended coupling range
                # Stronger fractal coupling with modified structure
                coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * 3.0  # Increased strength
                cross_term += coupling
        
        # Enhanced basin boundary complexity with smoother transitions
        basin_term = 0.0
        for i in range(self.dim):
            # Enhanced basin boundaries using stronger transitions
            boundary = np.abs(x[i]) - 2.0  # Shifted boundary
            smooth_boundary = np.tanh(boundary * 10.0)  # Increased transition sharpness
            basin_term += smooth_boundary**2
        
        # Novel asymmetric energy wells with dynamic frequency modulation and chaotic perturbations
        well_term = 0.0
        for i in range(self.dim):
            # Asymmetric wells with dynamic modulation and chaotic perturbation
            well = (x[i] - 1.5)**2 * (x[i] + 1.5)**2 * np.sin(x[i] * 7.0)  # Asymmetric well with higher frequency
            chaotic_perturbation = 0.2 * np.sin(x[i] * 15.0) * np.cos(x[i] * 8.0)  # Chaotic perturbation
            well_term += well + chaotic_perturbation
        
        # Additional chaotic perturbation layer for increased complexity
        chaos_layer = 0.0
        for i in range(self.dim):
            chaos_layer += 0.15 * np.sin(x[i] * 20.0) * np.cos(x[i] * 12.0) * np.sin(x[i] * 3.0)
        
        # Final combined landscape with modified weights
        total = 0.25 * result + 0.35 * noise + 0.25 * cross_term + 0.1 * basin_term + 0.05 * well_term + 0.05 * chaos_layer
        
        # Enhanced global scaling factor for increased complexity
        scaling = 1.0 + 0.3 * self.dim
        
        return total * scaling