import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos parameters with increased complexity
        self.poly_orders = [2 + int(3 * np.sin(i * 0.4)) for i in range(dim)]
        self.saddle_strengths = [1.2 + 0.9 * np.cos(i * 0.5) for i in range(dim)]
        self.temporal_modulation = [0.6 + 0.4 * np.sin(i * 0.8) for i in range(dim)]
        # Additional parameters for enhanced complexity
        self.well_depths = [1.5 + 0.7 * np.sin(0.9 * i) for i in range(dim)]
        self.asymmetries = [0.2 + 0.3 * np.cos(0.7 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic saddle point component with modified interactions
        saddle_term = 0.0
        for i in range(self.dim):
            poly_order = self.poly_orders[i % len(self.poly_orders)]
            # Enhanced nonlinearity in saddle term
            saddle_term += (np.tanh(x[i]) * np.sinh(x[i])**2) * self.saddle_strengths[i % len(self.saddle_strengths)]
            
        # Modified polynomial chaos interaction terms with stronger cross-dimension coupling
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Stronger polynomial interactions with additional trigonometric components
                poly_interaction = (x[i]**4 + x[j]**4) * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                chaos_term += poly_interaction
                
        # Improved temporal gradient modulation with enhanced time-varying components
        temporal_term = 0.0
        for i in range(self.dim):
            mod_factor = self.temporal_modulation[i % len(self.temporal_modulation)]
            # Enhanced temporal modulation with additional frequency components
            temporal_term += mod_factor * np.cos(3 * x[i]) * np.sin(4 * x[i]) * np.tanh(x[i])
            
        # Multi-scale harmonic landscape with increased frequency diversity
        harmonic_term = 0.0
        freqs = [1.0, 2.5, 3.5, 6.0, 10.0]
        for i in range(self.dim):
            for freq in freqs:
                harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * abs(x[i]))
                
        # Enhanced asymmetric hyperbolic wells with modified depth and nonlinearity
        well_term = 0.0
        for i in range(self.dim):
            depth = self.well_depths[i % len(self.well_depths)]
            asymmetry = self.asymmetries[i % len(self.asymmetries)]
            # More complex well structure with additional nonlinear components
            well_term += depth * (np.tanh(x[i] - asymmetry) * np.sinh(x[i])**2)
            
        # Strengthened cross-dimensional coupling with novel interaction patterns
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling with multi-scale interactions
                cross_coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (x[i]**3 + x[j]**3) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # New multimodal enhancement with increased complexity and varied scales
        multimodal_term = 0.0
        for i in range(self.dim):
            # More complex multimodal structure with multiple frequency components
            multimodal_term += np.sin(6 * x[i]) * np.cos(8 * x[i]) * np.tanh(x[i]) * (1 + 0.2 * np.sin(i * 0.5))
            
        # Combine all terms with adjusted weights for improved balance
        weights = [0.25, 0.20, 0.18, 0.15, 0.12, 0.08, 0.02]
        total = (weights[0] * saddle_term + 
                weights[1] * chaos_term + 
                weights[2] * temporal_term + 
                weights[3] * harmonic_term + 
                weights[4] * well_term +
                weights[5] * cross_coupling +
                weights[6] * multimodal_term)
                
        # Enhanced dimensionality-based scaling with additional nonlinearity
        scale = 1.0 + 0.4 * np.log(self.dim + 1) + 0.08 * np.sum(np.abs(x)**2.0)
        
        return scale * total