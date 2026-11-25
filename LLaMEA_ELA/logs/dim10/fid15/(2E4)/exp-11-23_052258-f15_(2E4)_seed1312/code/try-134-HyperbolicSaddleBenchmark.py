import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos parameters
        self.poly_orders = [3 + int(2 * np.sin(i * 0.5)) for i in range(dim)]
        self.saddle_strengths = [1.5 + 0.8 * np.cos(i * 0.3) for i in range(dim)]
        self.temporal_modulation = [0.5 + 0.5 * np.sin(i * 0.7) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic saddle point component with polynomial interactions
        saddle_term = 0.0
        for i in range(self.dim):
            # Hyperbolic tangent-based saddle structure
            poly_order = self.poly_orders[i % len(self.poly_orders)]
            saddle_term += (np.tanh(x[i]) * x[i]**poly_order) * self.saddle_strengths[i % len(self.saddle_strengths)]
            
        # Polynomial chaos interaction terms with cross-dimension coupling
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Higher-order polynomial interactions
                poly_interaction = (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j])
                chaos_term += poly_interaction
                
        # Temporal gradient modulation with time-varying components
        temporal_term = 0.0
        for i in range(self.dim):
            # Time-dependent modulation factor
            mod_factor = self.temporal_modulation[i % len(self.temporal_modulation)]
            temporal_term += mod_factor * np.cos(2 * x[i]) * np.sin(3 * x[i])
            
        # Multi-scale harmonic landscape with varying frequencies
        harmonic_term = 0.0
        freqs = [1.0, 2.0, 4.0, 8.0]
        for i in range(self.dim):
            for freq in freqs:
                harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
                
        # Asymmetric hyperbolic wells with varying depth and enhanced nonlinearity
        well_term = 0.0
        for i in range(self.dim):
            # Varying well depths and asymmetries with added complexity
            depth = 1.0 + 0.5 * np.sin(0.8 * i)
            asymmetry = 0.3 + 0.2 * np.cos(0.6 * i)
            # Enhanced nonlinearity in well term
            well_term += depth * (np.tanh(x[i] - asymmetry) * x[i]**3)
            
        # Add additional complexity with cross-dimensional coupling and nonlinearity
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling with nonlinear interaction
                cross_coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (x[i]**2 + x[j]**2)
                
        # Add a new term for increased multimodality and complexity
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += np.sin(5 * x[i]) * np.cos(7 * x[i]) * (1 + 0.1 * np.sin(i))
            
        # Combine all terms with carefully balanced weights
        weights = [0.22, 0.18, 0.20, 0.18, 0.15, 0.07, 0.05]
        total = (weights[0] * saddle_term + 
                weights[1] * chaos_term + 
                weights[2] * temporal_term + 
                weights[3] * harmonic_term + 
                weights[4] * well_term +
                weights[5] * cross_coupling +
                weights[6] * multimodal_term)
                
        # Add dimensionality-based scaling with hyperbolic adjustment
        scale = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sum(np.abs(x)**1.5)
        
        return scale * total