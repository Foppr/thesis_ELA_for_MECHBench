import numpy as np

class SinusoidalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive frequency patterns
        self.freq_patterns = np.random.rand(dim, 6) * 2 + 1
        # Precompute amplitude gradients
        self.amp_gradients = np.random.rand(dim) * 0.5 + 0.5
        # Precompute phase couplings
        self.phase_couplings = np.random.rand(dim, dim) * 0.8 - 0.4
        
    def f(self, x):
        # Scale input to [-pi, pi] range
        x_scaled = (x / 5.0) * np.pi
        
        # Compute base sinusoidal components with varying frequencies and amplitudes
        sin_components = []
        for i in range(self.dim):
            freq_pattern = self.freq_patterns[i]
            amp_grad = self.amp_gradients[i]
            
            # Base sinusoidal terms with adaptive frequency modulation
            term1 = np.sin(freq_pattern[0] * x_scaled[i]) * amp_grad
            term2 = np.sin(freq_pattern[1] * x_scaled[i]) * amp_grad * 0.7
            term3 = np.sin(freq_pattern[2] * x_scaled[i]) * amp_grad * 0.5
            term4 = np.sin(freq_pattern[3] * x_scaled[i]) * amp_grad * 0.3
            term5 = np.sin(freq_pattern[4] * x_scaled[i]) * amp_grad * 0.1
            
            # Add amplitude gradient effects
            gradient_effect = amp_grad * (1.0 + 0.2 * np.sin(x_scaled[i]))
            
            sin_components.append((term1 + term2 + term3 + term4 + term5) * gradient_effect)
        
        # Compute spatial coupling terms with dynamic phase relationships
        coupling_terms = []
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Dynamic phase coupling with spatial distance effects
                    phase_diff = x_scaled[i] - x_scaled[j]
                    coupling_strength = self.phase_couplings[i][j]
                    
                    # Adaptive coupling based on relative positions
                    dist_factor = 1.0 / (1.0 + np.exp(-2.0 * np.abs(x_scaled[i] - x_scaled[j])))
                    coupling_sum += coupling_strength * np.sin(phase_diff) * dist_factor
            
            coupling_terms.append(coupling_sum)
        
        # Compute interference patterns with spatially varying weights
        interference_terms = []
        for i in range(self.dim):
            # Multi-scale interference with different amplitude and frequency components
            interference = 0.0
            
            # Low-frequency interference
            interference += np.sin(0.5 * x_scaled[i]) * np.cos(0.3 * x_scaled[i])
            
            # Medium-frequency interference  
            interference += 0.7 * np.sin(2.0 * x_scaled[i]) * np.cos(1.5 * x_scaled[i])
            
            # High-frequency interference
            interference += 0.4 * np.sin(5.0 * x_scaled[i]) * np.cos(3.5 * x_scaled[i])
            
            # Spatially varying amplitude
            spatial_amp = 1.0 + 0.3 * np.sin(0.8 * x_scaled[i])
            interference *= spatial_amp
            
            interference_terms.append(interference)
        
        # Global structural term with multi-scale modulation
        global_term = 0.0
        global_term += np.sum(np.sin(0.5 * x_scaled) * np.cos(0.3 * x_scaled))
        global_term += 0.7 * np.sum(np.sin(2.0 * x_scaled) * np.cos(1.5 * x_scaled))
        global_term += 0.4 * np.sum(np.sin(5.0 * x_scaled) * np.cos(3.5 * x_scaled))
        
        # Combine all terms with adaptive weighting
        result = (np.sum(sin_components) + 
                 0.6 * np.sum(coupling_terms) + 
                 0.4 * np.sum(interference_terms) + 
                 0.3 * global_term)
        
        # Add controlled noise for enhanced complexity
        noise = 0.001 * np.random.rand() * (1.0 + 0.5 * np.sin(np.sum(x_scaled)))
        noise += 0.0005 * np.random.rand() * np.cos(np.sum(x_scaled**2))
        
        return result + noise