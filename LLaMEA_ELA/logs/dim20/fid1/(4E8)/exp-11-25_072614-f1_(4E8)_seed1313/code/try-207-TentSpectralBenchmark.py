import numpy as np

class TentSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic tent map sequence for dynamic weighting
        self.tent_sequence = np.array([0.3, 0.9, 0.7, 0.1, 0.3, 0.9, 0.7, 0.1, 0.3, 0.9])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics with spectral decomposition
        tent_term = 0.0
        for i in range(self.dim):
            # Tent map: f(x) = mu * x if x < 0.5 else mu * (1 - x)
            mu = 3.8 + 0.2 * np.sin(0.5 * np.pi * i)
            xi_tent = mu * x[i] if x[i] < 0.5 else mu * (1 - x[i])
            tent_term += xi_tent * np.cos(2.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        tent_term /= self.dim
        
        # Spectral decomposition with frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(0.7 * np.pi * i)
            spectral_term += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) * np.exp(-0.05 * x[i]**2)
        spectral_term /= self.dim
        
        # Adaptive ridge penalty with dynamic conditioning
        ridge_term = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.5 * np.sin(0.3 * np.pi * i)
            ridge_term += condition_factor * x[i]**2 * np.exp(-0.1 * x[i]**2)
        ridge_term /= self.dim
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = 0.5 + 0.5 * np.sin(0.2 * (i - j) + 0.1 * np.sum(x))
                cross_term += coupling_factor * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with chaotic basin modulation
        modal_term = 0.0
        for i in range(self.dim):
            chaotic_amp = 1.0 + 0.3 * np.sin(0.4 * np.pi * i + np.sum(x))
            modal_term += chaotic_amp * np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        modal_term /= self.dim
        
        # Dynamic noise with spectral phase coupling
        noise_term = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.3 * np.pi * i + 0.2 * np.sum(x))
            noise_term += np.sin(x[i] * np.pi * (1 + 0.1 * x[i] + phase)) * np.exp(-0.08 * x[i]**2)
        noise_term /= self.dim
        
        # Polynomial distortion with chaotic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.2 * np.sin(0.6 * np.pi * i)
            poly_term += coeff * (x[i]**4 - 2.5 * x[i]**3 + 2.0 * x[i]**2) * np.exp(-0.05 * x[i]**2)
        poly_term /= self.dim
        
        # Adaptive spectral ridge with chaotic modulation
        spectral_ridge = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.4 * np.sin(0.5 * np.pi * i + 0.3 * np.sum(x))
            spectral_ridge += mod_factor * np.sin(0.5 * np.pi * x[i]) * np.cos(0.5 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        spectral_ridge /= self.dim
        
        # Combine all terms with dynamic weights based on tent map
        weights = self.tent_sequence[:self.dim] % 1.0
        weights = weights / np.sum(weights)
        
        total = (weights[0] * tent_term + 
                 weights[1] * spectral_term + 
                 weights[2] * ridge_term + 
                 weights[3] * cross_term + 
                 weights[4] * modal_term + 
                 weights[5] * noise_term + 
                 weights[6] * poly_term + 
                 weights[7] * spectral_ridge)
        
        return total