import numpy as np

class LogisticQuaternionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for dynamic weighting
        self.logistic_sequence = np.array([0.3, 0.7, 0.2, 0.8, 0.4, 0.6, 0.1, 0.9, 0.5, 0.5])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic dynamics with spectral decomposition
        log_term = 0.0
        for i in range(self.dim):
            # Logistic map: f(x) = r * x * (1 - x)
            r = 3.9 + 0.2 * np.sin(0.7 * np.pi * i)
            xi_log = r * x[i] * (1 - x[i])
            log_term += xi_log * np.sin(2.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        log_term /= self.dim
        
        # Quaternion-inspired spectral decomposition with multi-dimensional modulation
        quat_spectral_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.cos(0.9 * np.pi * i)
            # Using quaternion-like interaction terms
            quat_spectral_term += (np.sin(freq_mod * x[i]) * np.sin(freq_mod * x[i]) + 
                                  np.cos(freq_mod * x[i]) * np.cos(freq_mod * x[i])) * np.exp(-0.05 * x[i]**2)
        quat_spectral_term /= self.dim
        
        # Adaptive elastic net penalty with multi-scale conditioning
        elastic_term = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.5 * np.cos(0.5 * np.pi * i)
            # Elastic net combines L1 and L2 penalties with adaptive weights
            elastic_term += condition_factor * (x[i]**2 + 0.15 * np.abs(x[i])) * np.exp(-0.1 * x[i]**2)
        elastic_term /= self.dim
        
        # Cross-dimensional interaction with logistic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = 0.5 + 0.5 * np.cos(0.4 * (i - j) + 0.3 * np.sum(x))
                # Logistic cosine interaction to increase complexity
                cross_term += coupling_factor * np.cos(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with logistic basin modulation
        modal_term = 0.0
        for i in range(self.dim):
            chaotic_amp = 1.0 + 0.3 * np.cos(0.6 * np.pi * i + np.sum(x))
            modal_term += chaotic_amp * np.tan(1.5 * np.pi * x[i]) * np.sin(2.5 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        modal_term /= self.dim
        
        # Adaptive noise with logistic phase coupling
        noise_term = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.tan(0.3 * np.pi * i + 0.2 * np.sum(x))
            noise_term += np.cos(x[i] * np.pi * (1 + 0.1 * x[i] + phase)) * np.exp(-0.08 * x[i]**2)
        noise_term /= self.dim
        
        # Polynomial distortion with logistic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.2 * np.tan(0.6 * np.pi * i)
            poly_term += coeff * (x[i]**4 - 2.5 * x[i]**3 + 2.2 * x[i]**2) * np.exp(-0.05 * x[i]**2)
        poly_term /= self.dim
        
        # Multi-scale spectral ridge with logistic modulation
        spectral_ridge = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.4 * np.tan(0.5 * np.pi * i + 0.3 * np.sum(x))
            spectral_ridge += mod_factor * np.sin(0.5 * np.pi * x[i]) * np.sin(0.5 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        spectral_ridge /= self.dim
        
        # Multi-scale interaction with logistic coupling
        multi_scale_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 0.4 + 0.6 * np.tan(0.3 * (i - j) + 0.2 * np.sum(x))
                multi_scale_term += scale_factor * np.cos(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        multi_scale_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with dynamic weights based on logistic map
        weights = self.logistic_sequence[:self.dim] % 1.0
        weights = weights / np.sum(weights)
        
        total = (weights[0] * log_term + 
                 weights[1] * quat_spectral_term + 
                 weights[2] * elastic_term + 
                 weights[3] * cross_term + 
                 weights[4] * modal_term + 
                 weights[5] * noise_term + 
                 weights[6] * poly_term + 
                 weights[7] * spectral_ridge + 
                 weights[8] * multi_scale_term)
        
        return total