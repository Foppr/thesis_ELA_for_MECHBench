import numpy as np

class HyperbolicSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractional Brownian motion sequence for dynamic weighting
        self.fbm_sequence = np.array([0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5, 0.5])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional Brownian motion inspired term with neural gradient flow
        fbm_term = 0.0
        for i in range(self.dim):
            # Fractional Brownian motion with Hurst parameter modulation
            hurst = 0.3 + 0.4 * np.sin(0.5 * np.pi * i)
            # Neural-inspired gradient flow component
            grad_flow = np.tanh(x[i] * (1.0 + 0.2 * np.sin(0.7 * np.pi * i)))
            fbm_term += grad_flow * np.cos(1.5 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        fbm_term /= self.dim
        
        # Neural network-inspired spectral decomposition
        nn_spectral_term = 0.0
        for i in range(self.dim):
            # Adaptive frequency modulation inspired by neural networks
            freq_mod = 1.0 + 0.5 * np.cos(0.6 * np.pi * i)
            nn_spectral_term += (np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) + 
                               np.cos(freq_mod * x[i]) * np.sin(freq_mod * x[i])) * np.exp(-0.08 * x[i]**2)
        nn_spectral_term /= self.dim
        
        # Adaptive multi-scale harmonic penalty with dynamic conditioning
        harmonic_term = 0.0
        for i in range(self.dim):
            # Scale-dependent condition factor
            scale_factor = 1.0 + 0.7 * np.cos(0.3 * np.pi * i)
            # Harmonic penalty combining multiple frequencies
            harmonic_term += scale_factor * (x[i]**2 + 0.15 * np.abs(x[i]) + 0.05 * x[i]**3) * np.exp(-0.1 * x[i]**2)
        harmonic_term /= self.dim
        
        # Cross-dimensional interaction with fractional coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractional coupling strength based on dimension difference
                coupling_factor = 0.5 + 0.5 * np.cos(0.2 * (i - j) + 0.3 * np.sum(x))
                cross_term += coupling_factor * np.sinh(x[i] * x[j]) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with fractional basin modulation
        modal_term = 0.0
        for i in range(self.dim):
            # Fractional amplitude modulation
            frac_amp = 1.0 + 0.5 * np.cos(0.4 * np.pi * i + np.sum(x))
            modal_term += frac_amp * np.tanh(3.0 * np.pi * x[i]) * np.sin(2.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        modal_term /= self.dim
        
        # Neural noise with fractional phase coupling
        noise_term = 0.0
        for i in range(self.dim):
            # Fractional phase modulation
            phase = 0.5 * np.cos(0.3 * np.pi * i + 0.2 * np.sum(x))
            noise_term += np.sinh(x[i] * np.pi * (1.0 + 0.15 * x[i] + phase)) * np.exp(-0.09 * x[i]**2)
        noise_term /= self.dim
        
        # Polynomial distortion with fractional coefficients
        poly_term = 0.0
        for i in range(self.dim):
            # Fractional coefficient modulation
            coeff = 1.0 + 0.4 * np.cos(0.8 * np.pi * i)
            poly_term += coeff * (x[i]**4 - 3.0 * x[i]**3 + 2.8 * x[i]**2) * np.exp(-0.06 * x[i]**2)
        poly_term /= self.dim
        
        # Fractional spectral ridge with multi-scale modulation
        spectral_ridge = 0.0
        for i in range(self.dim):
            # Multi-scale modulation factor
            mod_factor = 1.0 + 0.6 * np.cos(0.5 * np.pi * i + 0.3 * np.sum(x))
            spectral_ridge += mod_factor * np.sinh(0.7 * np.pi * x[i]) * np.cos(0.7 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        spectral_ridge /= self.dim
        
        # Multi-scale interaction with fractional coupling
        multi_scale_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractional scale factor
                scale_factor = 0.4 + 0.6 * np.cos(0.25 * (i - j) + 0.15 * np.sum(x))
                multi_scale_term += scale_factor * np.cosh(x[i] * x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
        multi_scale_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with dynamic weights based on fractional Brownian motion
        weights = self.fbm_sequence[:self.dim] % 1.0
        weights = weights / np.sum(weights)
        
        total = (weights[0] * fbm_term + 
                 weights[1] * nn_spectral_term + 
                 weights[2] * harmonic_term + 
                 weights[3] * cross_term + 
                 weights[4] * modal_term + 
                 weights[5] * noise_term + 
                 weights[6] * poly_term + 
                 weights[7] * spectral_ridge + 
                 weights[8] * multi_scale_term)
        
        return total