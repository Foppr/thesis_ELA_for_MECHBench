import numpy as np

class ChaoticGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic weighting
        self.chaotic_seq = np.array([0.1, 0.9, 0.4, 0.6, 0.2, 0.8, 0.3, 0.7, 0.5, 0.5])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave dynamics with Gaussian RBF interpolation
        chaotic_term = 0.0
        for i in range(self.dim):
            # Chaotic map: x_{n+1} = sin(r * x_n) * (1 - x_n^2)
            r = 3.5 + 0.4 * np.cos(0.7 * np.pi * i)
            x_chaos = np.sin(r * x[i]) * (1 - x[i]**2)
            chaotic_term += x_chaos * np.exp(-0.15 * x[i]**2)
        chaotic_term /= self.dim
        
        # Multi-scale Gaussian RBF with adaptive widths
        gaussian_term = 0.0
        for i in range(self.dim):
            # Varying width based on dimension index
            width = 0.8 + 0.7 * np.cos(0.5 * np.pi * i)
            gaussian_term += np.exp(-0.5 * (x[i] / width)**2) * np.sin(3.0 * x[i])
        gaussian_term /= self.dim
        
        # Adaptive penalty with condition-based scaling
        penalty_term = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.5 * np.cos(0.4 * np.pi * i)
            penalty_term += condition_factor * (x[i]**2 + 0.2 * np.abs(x[i])) * np.exp(-0.08 * x[i]**2)
        penalty_term /= self.dim
        
        # Cross-dimensional interaction with chaotic coupling - MUTATED
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased coupling strength and modified phase
                coupling_factor = 0.6 + 0.8 * np.cos(0.4 * (i - j) + 0.5 * np.sum(x))
                cross_term += coupling_factor * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(0.8 * (x[i] + x[j]))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with chaotic basin modulation
        modal_term = 0.0
        for i in range(self.dim):
            chaotic_amp = 1.0 + 0.4 * np.cos(0.5 * np.pi * i + 0.3 * np.sum(x))
            modal_term += chaotic_amp * np.tanh(x[i]) * np.sin(2.0 * x[i]) * np.exp(-0.12 * x[i]**2)
        modal_term /= self.dim
        
        # Dynamic noise with chaotic phase coupling
        noise_term = 0.0
        for i in range(self.dim):
            phase = 0.3 * np.tanh(0.4 * np.pi * i + 0.1 * np.sum(x))
            noise_term += np.cos(x[i] * (1 + 0.15 * x[i] + phase)) * np.exp(-0.1 * x[i]**2)
        noise_term /= self.dim
        
        # Polynomial distortion with chaotic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.3 * np.tanh(0.6 * np.pi * i)
            poly_term += coeff * (x[i]**5 - 3.0 * x[i]**4 + 2.5 * x[i]**3) * np.exp(-0.07 * x[i]**2)
        poly_term /= self.dim
        
        # Multi-scale ridge with chaotic modulation
        ridge_term = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.3 * np.tanh(0.5 * np.pi * i + 0.2 * np.sum(x))
            ridge_term += mod_factor * np.sin(x[i]) * np.sin(x[i]) * np.exp(-0.1 * x[i]**2)
        ridge_term /= self.dim
        
        # Multi-scale interaction with chaotic coupling - MUTATED
        multi_scale_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased scale factor and modified phase
                scale_factor = 0.4 + 0.8 * np.tanh(0.3 * (i - j) + 0.3 * np.sum(x))
                multi_scale_term += scale_factor * np.exp(-0.12 * (x[i] - x[j])**2) * np.sin(0.5 * (x[i] + x[j]))
        multi_scale_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with dynamic weights based on chaotic sequence
        weights = self.chaotic_seq[:self.dim] % 1.0
        weights = weights / np.sum(weights)
        
        total = (weights[0] * chaotic_term + 
                 weights[1] * gaussian_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_term + 
                 weights[4] * modal_term + 
                 weights[5] * noise_term + 
                 weights[6] * poly_term + 
                 weights[7] * ridge_term + 
                 weights[8] * multi_scale_term)
        
        return total