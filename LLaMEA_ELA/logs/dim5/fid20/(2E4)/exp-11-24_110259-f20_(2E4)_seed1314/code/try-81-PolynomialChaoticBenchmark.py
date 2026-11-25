import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients and coupling matrices
        self.poly_coeffs = np.random.rand(dim, 5) * 2 - 1
        self.coupling_matrix = np.random.rand(dim, dim) * 0.5 + 0.5
        self.harmonic_freqs = np.random.rand(dim) * 8 + 2
        self.spatial_weights = np.random.rand(dim) * 2 + 1
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos expansion terms with adaptive coupling
        poly_terms = []
        for i in range(self.dim):
            # Adaptive polynomial basis functions
            coeffs = self.poly_coeffs[i]
            poly_val = (coeffs[0] * x_scaled[i]**2 + 
                       coeffs[1] * x_scaled[i]**3 + 
                       coeffs[2] * x_scaled[i]**4 + 
                       coeffs[3] * x_scaled[i]**5 + 
                       coeffs[4] * x_scaled[i]**6)
            
            # Spatially varying coupling effects
            coupling_effect = 0.0
            for j in range(self.dim):
                coupling_strength = self.coupling_matrix[i][j]
                coupling_effect += coupling_strength * np.sin(self.harmonic_freqs[j] * x_scaled[j])
            
            poly_terms.append(poly_val + coupling_effect * self.spatial_weights[i])
        
        # Harmonic interference patterns with adaptive frequency modulation
        interference_terms = []
        for i in range(self.dim):
            freq = self.harmonic_freqs[i]
            interference = np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
            
            # Multi-scale harmonic mixing
            mix_term = 0.0
            for k in range(1, 4):
                mix_term += (1.0 / k) * np.sin(k * freq * x_scaled[i]) * np.cos(k * freq * x_scaled[i])
            
            interference_terms.append(interference + 0.5 * mix_term)
        
        # Nested harmonic coupling with varying strengths
        nested_coupling = []
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, self.dim):
                strength = self.coupling_matrix[i][j] * 0.3
                coupling_sum += strength * np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
            nested_coupling.append(coupling_sum)
        
        # Adaptive spatial modulation with multi-scale interference
        spatial_modulation = 0.0
        for i in range(self.dim):
            spatial_term = np.sin(self.spatial_weights[i] * x_scaled[i])
            spatial_term += 0.3 * np.sin(2 * self.spatial_weights[i] * x_scaled[i])
            spatial_term += 0.1 * np.sin(4 * self.spatial_weights[i] * x_scaled[i])
            spatial_modulation += spatial_term
        
        # Global structure with polynomial and harmonic components
        global_structure = (np.sum(np.sin(x_scaled) * np.cos(x_scaled)) + 
                          0.5 * np.sum(np.sin(2 * x_scaled) * np.cos(2 * x_scaled)) +
                          0.2 * np.sum(np.sin(4 * x_scaled) * np.cos(4 * x_scaled)))
        
        # Adaptive weighting based on position
        pos_weight = 1.0 + 0.3 * np.sin(np.sum(x_scaled**2))
        pos_weight *= (1.0 + 0.2 * np.cos(np.sum(x_scaled**4)))
        
        # Combine all components with adaptive scaling
        result = (pos_weight * (np.sum(poly_terms) + 0.7 * np.sum(interference_terms) + 
                               0.5 * np.sum(nested_coupling) + 0.3 * spatial_modulation + 
                               0.2 * global_structure))
        
        # Add controlled noise for robustness
        noise = 0.005 * np.random.rand() * (1.0 + 0.5 * np.sin(np.sum(x_scaled**2)))
        return result + noise