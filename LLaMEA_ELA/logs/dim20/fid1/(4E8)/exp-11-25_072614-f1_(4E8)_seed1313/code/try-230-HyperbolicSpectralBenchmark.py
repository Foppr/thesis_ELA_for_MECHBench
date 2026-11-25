import numpy as np

class HyperbolicSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sine chaotic sequence for dynamic weighting
        self.sine_sequence = np.array([0.8, 0.2, 0.9, 0.1, 0.7, 0.3, 0.6, 0.4, 0.5, 0.5])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sine chaotic map dynamics with spectral decomposition
        sine_term = 0.0
        for i in range(self.dim):
            # Sine tent map: f(x) = mu * sin(x) if x < 0.5 else mu * sin(1 - x)
            mu = 4.2 + 0.3 * np.cos(0.6 * np.pi * i)
            xi_sine = mu * np.sin(x[i]) if x[i] < 0.5 else mu * np.sin(1 - x[i])
            sine_term += xi_sine * np.cos(2.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        sine_term /= self.dim
        
        # Quaternion-inspired spectral decomposition with multi-dimensional modulation
        quat_spectral_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.4 * np.cos(0.8 * np.pi * i)
            # Using complex-like interaction terms inspired by quaternion algebra
            quat_spectral_term += (np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) + 
                                 np.cos(freq_mod * x[i]) * np.sin(freq_mod * x[i])) * np.exp(-0.05 * x[i]**2)
        quat_spectral_term /= self.dim
        
        # Dynamic elastic net penalty with multi-scale conditioning
        elastic_term = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.6 * np.cos(0.4 * np.pi * i)
            # Elastic net combines L1 and L2 penalties with dynamic weights
            elastic_term += condition_factor * (x[i]**2 + 0.1 * np.abs(x[i])) * np.exp(-0.1 * x[i]**2)
        elastic_term /= self.dim
        
        # Cross-dimensional interaction with sine coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = 0.6 + 0.4 * np.cos(0.3 * (i - j) + 0.2 * np.sum(x))
                # Sine interaction to increase complexity
                cross_term += coupling_factor * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with sine basin modulation
        modal_term = 0.0
        for i in range(self.dim):
            chaotic_amp = 1.0 + 0.4 * np.cos(0.5 * np.pi * i + np.sum(x))
            modal_term += chaotic_amp * np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        modal_term /= self.dim
        
        # Dynamic noise with sine phase coupling
        noise_term = 0.0
        for i in range(self.dim):
            phase = 0.6 * np.sin(0.4 * np.pi * i + 0.3 * np.sum(x))
            noise_term += np.sin(x[i] * np.pi * (1 + 0.1 * x[i] + phase)) * np.exp(-0.08 * x[i]**2)
        noise_term /= self.dim
        
        # Polynomial distortion with sine coefficients
        poly_term = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.3 * np.sin(0.7 * np.pi * i)
            poly_term += coeff * (x[i]**4 - 2.8 * x[i]**3 + 2.5 * x[i]**2) * np.exp(-0.05 * x[i]**2)
        poly_term /= self.dim
        
        # Multi-scale spectral ridge with sine modulation
        spectral_ridge = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.5 * np.sin(0.6 * np.pi * i + 0.4 * np.sum(x))
            spectral_ridge += mod_factor * np.sin(0.6 * np.pi * x[i]) * np.cos(0.6 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        spectral_ridge /= self.dim
        
        # Multi-scale interaction with sine coupling
        multi_scale_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 0.3 + 0.7 * np.sin(0.2 * (i - j) + 0.1 * np.sum(x))
                multi_scale_term += scale_factor * np.cosh(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        multi_scale_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with dynamic weights based on sine chaotic map
        weights = self.sine_sequence[:self.dim] % 1.0
        weights = weights / np.sum(weights)
        
        total = (weights[0] * sine_term + 
                 weights[1] * quat_spectral_term + 
                 weights[2] * elastic_term + 
                 weights[3] * cross_term + 
                 weights[4] * modal_term + 
                 weights[5] * noise_term + 
                 weights[6] * poly_term + 
                 weights[7] * spectral_ridge + 
                 weights[8] * multi_scale_term)
        
        return total