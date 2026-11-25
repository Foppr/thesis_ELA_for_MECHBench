import numpy as np

class AdaptiveHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive frequency modulators and harmonic coefficients
        self.freq_modulators = np.random.rand(dim) * 2 + 1
        self.harmonic_coeffs = np.random.rand(dim, 4) * 0.5 + 0.5
        self.interference_patterns = np.random.rand(dim, dim) * 2 - 1
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base trigonometric polynomial with adaptive frequencies
        result = np.zeros_like(x_scaled)
        for i in range(self.dim):
            freq_mod = self.freq_modulators[i]
            # Adaptive frequency modulation based on position
            adaptive_freq = freq_mod * (1.0 + 0.5 * np.sin(x_scaled[i]))
            
            # Polynomial harmonic components
            h1 = np.sin(adaptive_freq * x_scaled[i])
            h2 = np.sin(2 * adaptive_freq * x_scaled[i])
            h3 = np.sin(3 * adaptive_freq * x_scaled[i])
            h4 = np.sin(4 * adaptive_freq * x_scaled[i])
            
            # Combine harmonics with learned coefficients
            result[i] = (self.harmonic_coeffs[i][0] * h1 + 
                        self.harmonic_coeffs[i][1] * h2 + 
                        self.harmonic_coeffs[i][2] * h3 + 
                        self.harmonic_coeffs[i][3] * h4)
        
        # Spatially varying harmonic interference
        interference = np.zeros(self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                # Spatial coupling with interference pattern coefficients
                coupling = self.interference_patterns[i][j]
                interference[i] += coupling * np.cos(x_scaled[i] + x_scaled[j])
        
        # Multi-scale modulation with position-dependent amplitude
        amplitude_mod = 1.0 + 0.3 * np.sin(2 * np.sum(x_scaled**2))
        amplitude_mod *= (1.0 + 0.2 * np.cos(3 * np.sum(x_scaled**2)))
        
        # Combine all components
        total_result = amplitude_mod * (np.sum(result) + 0.5 * np.sum(interference))
        
        # Add multi-modal structure through nested polynomial terms
        nested_terms = 0.0
        for i in range(self.dim):
            # Nested polynomial with increasing degree
            poly_val = x_scaled[i]**2 + 0.3 * x_scaled[i]**4 + 0.1 * x_scaled[i]**6
            nested_terms += np.sin(poly_val)
        
        total_result += 0.3 * nested_terms
        
        # Add noise for non-deterministic boundary behavior
        noise = 0.01 * np.random.rand() * (1.0 + np.sin(np.sum(x_scaled**2)))
        
        return total_result + noise