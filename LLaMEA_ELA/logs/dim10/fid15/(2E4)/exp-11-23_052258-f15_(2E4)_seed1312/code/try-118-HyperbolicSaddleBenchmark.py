import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos parameters with slight modifications
        self.poly_orders = [4 + int(np.sin(i * 0.6)) for i in range(dim)]
        self.saddle_strengths = [1.2 + 0.9 * np.cos(i * 0.4) for i in range(dim)]
        self.temporal_modulation = [0.6 + 0.4 * np.sin(i * 0.8) for i in range(dim)]
        
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
            for j in range(i+1, min(i+4, self.dim)):
                # Altered higher-order polynomial interactions
                poly_interaction = (x[i]**4 + x[j]**2) * np.cos(x[i] * x[j])
                chaos_term += poly_interaction
                
        # Temporal gradient modulation with modified time-varying components
        temporal_term = 0.0
        for i in range(self.dim):
            # Modified time-dependent modulation factor
            mod_factor = self.temporal_modulation[i % len(self.temporal_modulation)]
            temporal_term += mod_factor * np.sin(3 * x[i]) * np.cos(2 * x[i])
            
        # Multi-scale harmonic landscape with varying frequencies and amplitudes
        harmonic_term = 0.0
        freqs = [1.5, 2.5, 4.5, 8.5]
        for i in range(self.dim):
            for freq in freqs:
                harmonic_term += np.cos(freq * x[i]) * np.sin(freq * x[i])
                
        # Asymmetric hyperbolic wells with modified depth and asymmetry
        well_term = 0.0
        for i in range(self.dim):
            # Modified well depths and asymmetries
            depth = 1.2 + 0.4 * np.sin(0.9 * i)
            asymmetry = 0.2 + 0.3 * np.cos(0.7 * i)
            well_term += depth * (np.tanh(x[i] - asymmetry) * x[i]**3)
            
        # Combine all terms with modified weights
        weights = [0.22, 0.25, 0.15, 0.20, 0.18]
        total = (weights[0] * saddle_term + 
                weights[1] * chaos_term + 
                weights[2] * temporal_term + 
                weights[3] * harmonic_term + 
                weights[4] * well_term)
                
        # Add dimensionality-based scaling with modified hyperbolic adjustment
        scale = 1.0 + 0.25 * np.log(self.dim + 1) + 0.08 * np.sum(np.abs(x)**1.7)
        
        return scale * total