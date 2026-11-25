import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos parameters with substantial modifications
        self.poly_orders = [5 + int(np.sin(i * 0.7)) for i in range(dim)]
        self.saddle_strengths = [1.5 + 1.1 * np.cos(i * 0.5) for i in range(dim)]
        self.temporal_modulation = [0.8 + 0.3 * np.sin(i * 0.9) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic saddle point component with enhanced polynomial interactions
        saddle_term = 0.0
        for i in range(self.dim):
            # Enhanced hyperbolic tangent-based saddle structure
            poly_order = self.poly_orders[i % len(self.poly_orders)]
            saddle_term += (np.tanh(x[i]) * x[i]**poly_order) * self.saddle_strengths[i % len(self.saddle_strengths)]
            
        # Polynomial chaos interaction terms with extended cross-dimension coupling
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling range
                # Enhanced higher-order polynomial interactions
                poly_interaction = (x[i]**5 + x[j]**3) * np.sin(x[i] * x[j])  # Changed to sine
                chaos_term += poly_interaction
                
        # Temporal gradient modulation with enhanced time-varying components
        temporal_term = 0.0
        for i in range(self.dim):
            # Enhanced modulation factor
            mod_factor = self.temporal_modulation[i % len(self.temporal_modulation)]
            temporal_term += mod_factor * np.cos(4 * x[i]) * np.sin(3 * x[i])  # Swapped sin/cos
            
        # Multi-scale harmonic landscape with increased frequency diversity
        harmonic_term = 0.0
        freqs = [2.0, 3.0, 5.0, 9.0, 12.0]  # Significantly shifted frequencies
        for i in range(self.dim):
            for freq in freqs:
                harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i])  # Swapped sin/cos
                
        # Asymmetric hyperbolic wells with enhanced depth and asymmetry
        well_term = 0.0
        for i in range(self.dim):
            # Enhanced well depths and asymmetries
            depth = 1.5 + 0.5 * np.sin(1.1 * i)
            asymmetry = 0.3 + 0.4 * np.cos(0.8 * i)
            well_term += depth * (np.tanh(x[i] - asymmetry) * x[i]**4)  # Changed to x^4
            
        # Additional complex coupling terms with novel interaction patterns
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i]**2 + x[j]**2) * np.exp(-abs(x[i] - x[j]))  # New exponential coupling
                
        # Combine all terms with altered weights
        weights = [0.25, 0.20, 0.15, 0.25, 0.10, 0.05]  # Modified weight distribution
        total = (weights[0] * saddle_term + 
                weights[1] * chaos_term + 
                weights[2] * temporal_term + 
                weights[3] * harmonic_term + 
                weights[4] * well_term +
                weights[5] * coupling_term)
                
        # Add dimensionality-based scaling with enhanced hyperbolic adjustment
        scale = 1.0 + 0.30 * np.log(self.dim + 1) + 0.12 * np.sum(np.abs(x)**2.0)  # Changed exponent
        
        return scale * total