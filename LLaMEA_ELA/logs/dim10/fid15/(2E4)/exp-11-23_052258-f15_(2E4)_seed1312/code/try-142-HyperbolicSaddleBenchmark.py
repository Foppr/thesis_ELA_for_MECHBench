import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos parameters with increased complexity
        self.poly_orders = [3 + int(4 * np.sin(i * 0.5)) for i in range(dim)]
        self.saddle_strengths = [1.5 + 1.2 * np.cos(i * 0.6) for i in range(dim)]
        self.temporal_modulation = [0.8 + 0.5 * np.sin(i * 0.9) for i in range(dim)]
        # Additional parameters for enhanced complexity
        self.well_depths = [2.0 + 1.0 * np.sin(1.1 * i) for i in range(dim)]
        self.asymmetries = [0.3 + 0.4 * np.cos(0.8 * i) for i in range(dim)]
        # New parameters for increased complexity
        self.frequency_components = [1.5 + 2.0 * np.sin(i * 0.7) for i in range(dim)]
        self.coupling_strengths = [0.5 + 0.3 * np.cos(i * 0.4) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic saddle point component with modified interactions
        saddle_term = 0.0
        for i in range(self.dim):
            poly_order = self.poly_orders[i % len(self.poly_orders)]
            # Enhanced nonlinearity in saddle term
            saddle_term += (np.tanh(x[i]) * np.sinh(x[i])**3) * self.saddle_strengths[i % len(self.saddle_strengths)]
            
        # Modified polynomial chaos interaction terms with stronger cross-dimension coupling
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Stronger polynomial interactions with additional trigonometric components
                poly_interaction = (x[i]**5 + x[j]**5) * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
                chaos_term += poly_interaction
                
        # Improved temporal gradient modulation with enhanced time-varying components
        temporal_term = 0.0
        for i in range(self.dim):
            mod_factor = self.temporal_modulation[i % len(self.temporal_modulation)]
            # Enhanced temporal modulation with additional frequency components
            temporal_term += mod_factor * np.cos(4 * x[i]) * np.sin(5 * x[i]) * np.tanh(x[i]**2)
            
        # Multi-scale harmonic landscape with increased frequency diversity
        harmonic_term = 0.0
        freqs = [1.0, 3.0, 5.0, 8.0, 12.0, 15.0]
        for i in range(self.dim):
            for freq in freqs:
                harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.15 * abs(x[i]))
                
        # Enhanced asymmetric hyperbolic wells with modified depth and nonlinearity
        well_term = 0.0
        for i in range(self.dim):
            depth = self.well_depths[i % len(self.well_depths)]
            asymmetry = self.asymmetries[i % len(self.asymmetries)]
            # More complex well structure with additional nonlinear components
            well_term += depth * (np.tanh(x[i] - asymmetry) * np.sinh(x[i])**3)
            
        # Strengthened cross-dimensional coupling with novel interaction patterns
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling with multi-scale interactions
                coupling_strength = self.coupling_strengths[i % len(self.coupling_strengths)]
                cross_coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (x[i]**4 + x[j]**4) * np.exp(-0.08 * (x[i]**2 + x[j]**2)) * coupling_strength
                
        # New multimodal enhancement with increased complexity and varied scales
        multimodal_term = 0.0
        for i in range(self.dim):
            # More complex multimodal structure with multiple frequency components
            freq_comp = self.frequency_components[i % len(self.frequency_components)]
            multimodal_term += np.sin(freq_comp * x[i]) * np.cos(freq_comp * x[i]) * np.tanh(x[i]) * (1 + 0.3 * np.sin(i * 0.6))
            
        # Combine all terms with adjusted weights for improved balance
        weights = [0.28, 0.22, 0.19, 0.16, 0.13, 0.07, 0.05]
        total = (weights[0] * saddle_term + 
                weights[1] * chaos_term + 
                weights[2] * temporal_term + 
                weights[3] * harmonic_term + 
                weights[4] * well_term +
                weights[5] * cross_coupling +
                weights[6] * multimodal_term)
                
        # Enhanced dimensionality-based scaling with additional nonlinearity
        scale = 1.0 + 0.5 * np.log(self.dim + 1) + 0.12 * np.sum(np.abs(x)**2.5)
        
        return scale * total