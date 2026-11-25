import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos parameters with increased complexity
        self.poly_orders = [2 + int(3 * np.sin(i * 0.4)) for i in range(dim)]
        self.saddle_strengths = [1.2 + 1.0 * np.cos(i * 0.5) for i in range(dim)]
        self.temporal_modulation = [0.3 + 0.7 * np.sin(i * 0.6) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic saddle point component with modified polynomial interactions
        saddle_term = 0.0
        for i in range(self.dim):
            # Modified hyperbolic tangent-based saddle structure
            poly_order = self.poly_orders[i % len(self.poly_orders)]
            saddle_term += (np.tanh(x[i]) * x[i]**poly_order) * self.saddle_strengths[i % len(self.saddle_strengths)]
            
        # Enhanced polynomial chaos interaction terms with increased cross-dimension coupling
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Higher-order polynomial interactions with additional nonlinearity
                poly_interaction = (x[i]**4 + x[j]**4) * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                chaos_term += poly_interaction
                
        # Improved temporal gradient modulation with more complex time-varying components
        temporal_term = 0.0
        for i in range(self.dim):
            # Enhanced time-dependent modulation factor
            mod_factor = self.temporal_modulation[i % len(self.temporal_modulation)]
            temporal_term += mod_factor * np.cos(3 * x[i]) * np.sin(4 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Multi-scale harmonic landscape with varying frequencies and added complexity
        harmonic_term = 0.0
        freqs = [1.0, 2.0, 3.0, 6.0, 12.0]
        for i in range(self.dim):
            for freq in freqs:
                harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * (1 + 0.2 * np.sin(freq * x[i]))
                
        # Enhanced asymmetric hyperbolic wells with varying depth and increased nonlinearity
        well_term = 0.0
        for i in range(self.dim):
            # Varying well depths, asymmetries, and enhanced nonlinearity
            depth = 1.5 + 0.3 * np.sin(0.9 * i)
            asymmetry = 0.2 + 0.3 * np.cos(0.7 * i)
            # Enhanced nonlinearity in well term with additional exponential component
            well_term += depth * (np.tanh(x[i] - asymmetry) * x[i]**4) * np.exp(-0.05 * x[i]**2)
            
        # Improved cross-dimensional coupling and nonlinear interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling with nonlinear interaction and additional trigonometric components
                cross_coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Enhanced multimodal term with increased complexity and varied frequencies
        multimodal_term = 0.0
        freqs_multimodal = [3, 5, 7, 9]
        for i in range(self.dim):
            for freq in freqs_multimodal:
                multimodal_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * (1 + 0.15 * np.sin(i * freq))
                
        # Combine all terms with carefully balanced weights
        weights = [0.25, 0.15, 0.22, 0.18, 0.12, 0.06, 0.02]
        total = (weights[0] * saddle_term + 
                weights[1] * chaos_term + 
                weights[2] * temporal_term + 
                weights[3] * harmonic_term + 
                weights[4] * well_term +
                weights[5] * cross_coupling +
                weights[6] * multimodal_term)
                
        # Add dimensionality-based scaling with enhanced hyperbolic adjustment
        scale = 1.0 + 0.4 * np.log(self.dim + 1) + 0.08 * np.sum(np.abs(x)**1.7)
        
        return scale * total