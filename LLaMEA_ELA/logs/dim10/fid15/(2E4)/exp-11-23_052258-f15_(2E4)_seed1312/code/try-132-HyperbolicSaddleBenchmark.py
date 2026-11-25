import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos parameters with enhanced complexity
        self.poly_orders = [2 + int(3 * np.sin(i * 0.4)) for i in range(dim)]
        self.saddle_strengths = [1.2 + 0.9 * np.cos(i * 0.5) for i in range(dim)]
        self.temporal_modulation = [0.6 + 0.4 * np.sin(i * 0.8) for i in range(dim)]
        # Additional parameters for enhanced landscape complexity
        self.asymmetry_params = [0.4 + 0.3 * np.sin(i * 0.6) for i in range(dim)]
        self.frequency_modulators = [1.5 + 0.5 * np.cos(i * 0.7) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic saddle point component with modified interactions
        saddle_term = 0.0
        for i in range(self.dim):
            poly_order = self.poly_orders[i % len(self.poly_orders)]
            # Enhanced hyperbolic structure with asymmetry
            asymmetry = self.asymmetry_params[i % len(self.asymmetry_params)]
            saddle_term += (np.tanh(x[i] - asymmetry) * x[i]**poly_order) * self.saddle_strengths[i % len(self.saddle_strengths)]
            
        # Modified polynomial chaos interaction terms with stronger cross-dimension coupling
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                # Enhanced polynomial interactions with frequency modulation
                freq_mod_i = self.frequency_modulators[i % len(self.frequency_modulators)]
                freq_mod_j = self.frequency_modulators[j % len(self.frequency_modulators)]
                poly_interaction = (x[i]**3 + x[j]**3) * np.sin(freq_mod_i * x[i] * freq_mod_j * x[j])
                chaos_term += poly_interaction
                
        # Adaptive temporal gradient modulation with enhanced variation
        temporal_term = 0.0
        for i in range(self.dim):
            mod_factor = self.temporal_modulation[i % len(self.temporal_modulation)]
            # Enhanced temporal component with multiple frequency interactions
            temporal_term += mod_factor * (np.cos(2 * x[i]) * np.sin(3 * x[i]) + 0.5 * np.sin(5 * x[i]))
            
        # Multi-scale harmonic landscape with adaptive frequencies
        harmonic_term = 0.0
        freqs = [1.0, 2.0, 3.0, 6.0, 12.0]  # Extended frequency range
        for i in range(self.dim):
            for freq in freqs:
                freq_mod = self.frequency_modulators[i % len(self.frequency_modulators)]
                harmonic_term += np.sin(freq_mod * freq * x[i]) * np.cos(freq_mod * freq * x[i])
                
        # Enhanced asymmetric hyperbolic wells with varying depth and shape
        well_term = 0.0
        for i in range(self.dim):
            # Varying well depths, asymmetries, and shapes
            depth = 1.5 + 0.4 * np.sin(0.9 * i)
            asymmetry = self.asymmetry_params[i % len(self.asymmetry_params)]
            shape_factor = 1.0 + 0.2 * np.cos(0.7 * i)
            well_term += depth * (np.tanh(x[i] - asymmetry) * x[i]**shape_factor)
            
        # Enhanced cross-dimensional coupling with additional interaction terms
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # More complex cross-dimensional interactions
                cross_coupling += (np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) + 
                                 0.3 * np.sin(2 * x[i]) * np.cos(2 * x[j]))
                
        # Additional complexity terms for improved benchmark difficulty
        additional_term = 0.0
        for i in range(self.dim):
            # Hyperbolic cosine and sine combinations for added complexity
            additional_term += np.cosh(x[i]) * np.sinh(x[i]) + 0.5 * np.cos(x[i]**2)
            
        # Combine all terms with adjusted weights for better balance
        weights = [0.22, 0.18, 0.20, 0.23, 0.16, 0.07, 0.04]
        total = (weights[0] * saddle_term + 
                weights[1] * chaos_term + 
                weights[2] * temporal_term + 
                weights[3] * harmonic_term + 
                weights[4] * well_term +
                weights[5] * cross_coupling +
                weights[6] * additional_term)
                
        # Add dimensionality-based scaling with enhanced hyperbolic adjustment
        scale = 1.0 + 0.4 * np.log(self.dim + 1) + 0.08 * np.sum(np.abs(x)**1.7)
        
        return scale * total