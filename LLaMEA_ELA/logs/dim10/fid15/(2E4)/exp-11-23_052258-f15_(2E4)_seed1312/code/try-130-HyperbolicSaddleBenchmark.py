import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos parameters with slight modifications
        self.poly_orders = [3 + int(np.sin(i * 0.5)) for i in range(dim)]
        self.saddle_strengths = [1.0 + 0.8 * np.cos(i * 0.3) for i in range(dim)]
        self.temporal_modulation = [0.5 + 0.5 * np.sin(i * 0.7) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic saddle point component with modified polynomial interactions
        saddle_term = 0.0
        for i in range(self.dim):
            # Modified hyperbolic tangent-based saddle structure
            poly_order = self.poly_orders[i % len(self.poly_orders)]
            saddle_term += (np.tanh(x[i]) * x[i]**poly_order) * self.saddle_strengths[i % len(self.saddle_strengths)]
            
        # Polynomial chaos interaction terms with altered cross-dimension coupling
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range
                # Modified higher-order polynomial interactions
                poly_interaction = (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])  # Changed to sine
                chaos_term += poly_interaction
                
        # Temporal gradient modulation with modified time-varying components
        temporal_term = 0.0
        for i in range(self.dim):
            # Modified modulation factor
            mod_factor = self.temporal_modulation[i % len(self.temporal_modulation)]
            temporal_term += mod_factor * np.cos(2 * x[i]) * np.sin(x[i])  # Swapped sin/cos
            
        # Multi-scale harmonic landscape with modified frequencies
        harmonic_term = 0.0
        freqs = [1.0, 2.0, 3.0, 5.0]  # Slightly shifted frequencies
        for i in range(self.dim):
            for freq in freqs:
                harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i])  # Swapped sin/cos
                
        # Asymmetric hyperbolic wells with modified depth and asymmetry
        well_term = 0.0
        for i in range(self.dim):
            # Modified well depths and asymmetries
            depth = 1.0 + 0.3 * np.sin(0.8 * i)
            asymmetry = 0.1 + 0.2 * np.cos(0.6 * i)
            well_term += depth * (np.tanh(x[i] - asymmetry) * x[i]**2)  # Changed to x^2
            
        # Combine all terms with altered weights
        weights = [0.25, 0.20, 0.25, 0.15, 0.15]  # Modified weight distribution
        total = (weights[0] * saddle_term + 
                weights[1] * chaos_term + 
                weights[2] * temporal_term + 
                weights[3] * harmonic_term + 
                weights[4] * well_term)
                
        # Add dimensionality-based scaling with modified hyperbolic adjustment
        scale = 1.0 + 0.20 * np.log(self.dim + 1) + 0.05 * np.sum(np.abs(x)**1.5)  # Changed exponent
        
        return scale * total