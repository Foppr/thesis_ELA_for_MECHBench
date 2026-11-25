import numpy as np

class LogisticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map parameters
        self.r_values = 3.9 + 0.1 * np.sin(np.linspace(0, 2*np.pi, dim))
        self.spectral_coeffs = np.random.randn(dim) * 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic dynamics component
        logistic_term = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Use previous dimension's value for chaotic coupling
            if i > 0:
                x_prev = x[i-1] if i > 0 else x[0]
                logistic_term += (r * x_prev * (1 - x_prev)) * np.sin(x[i])
            else:
                logistic_term += r * x[i] * (1 - x[i])
        logistic_term /= self.dim
        
        # Spectral decomposition with adaptive frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * np.pi / (self.dim + 1)) + 0.3 * np.cos(x[i])
            spectral_term += self.spectral_coeffs[i] * np.sin(freq * x[i]) * np.cos(freq * x[i])
        spectral_term /= self.dim
        
        # Adaptive ridge penalty with dynamic conditioning
        ridge_term = 0.0
        for i in range(self.dim):
            # Dynamic ridge coefficient based on dimension and value
            ridge_coeff = 0.5 + 0.3 * np.sin(i * np.pi / self.dim) + 0.1 * np.abs(x[i])
            ridge_term += ridge_coeff * x[i]**2
        ridge_term /= self.dim
        
        # Cross-dimensional interaction with chaotic coupling and hyperbolic terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling between dimensions
                chaotic_coupling = np.sin(x[i] * x[j]) + 0.2 * np.tanh(x[i] - x[j])
                cross_term += chaotic_coupling * np.exp(-0.5 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale temporal dynamics with phase locking
        temporal_term = 0.0
        for i in range(self.dim):
            # Phase-locked oscillators with different frequencies
            freq = 1.0 + 0.4 * np.sin(i * np.pi / self.dim) + 0.2 * np.cos(x[i])
            phase = freq * x[i] + 0.5 * np.sin(freq * x[i])
            temporal_term += np.sin(phase) * np.cos(2.0 * phase) + 0.3 * np.sin(3.0 * phase)
        temporal_term /= self.dim
        
        # Asymmetric distortion with logistic map transformation
        asym_term = 0.0
        for i in range(self.dim):
            # Apply logistic map to input for asymmetric effect
            logistic_val = self.r_values[i] * x[i] * (1 - x[i])
            asym_term += np.abs(logistic_val) + 0.5 * logistic_val**2
        asym_term /= self.dim
        
        # Dynamic conditioning factor with chaotic modulation
        cond_factor = 1.0 + 0.4 * np.sin(np.mean(np.abs(x))) + 0.2 * np.cos(self.dim * np.pi / 3.0)
        
        # Combine all terms with dynamic weights based on chaotic parameters
        total = (0.25 * logistic_term + 
                0.20 * spectral_term + 
                0.15 * ridge_term + 
                0.15 * cross_term + 
                0.15 * temporal_term + 
                0.10 * asym_term) * cond_factor
        
        return total