import numpy as np

class ChaoticGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic weighting
        self.chaotic_seq = np.array([0.1, 0.9, 0.3, 0.7, 0.2, 0.8, 0.4, 0.6, 0.5, 0.5])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave dynamics with Gaussian RBF interpolation
        chaotic_term = 0.0
        for i in range(self.dim):
            # Chaotic sine-wave: sin(omega * x + phi) where omega and phi are dynamically adjusted
            omega = 2.0 + 0.5 * np.sin(0.4 * np.pi * i)
            phi = 0.3 * np.pi * i + 0.1 * np.sum(x)
            chaotic_term += np.sin(omega * x[i] + phi) * np.exp(-0.1 * x[i]**2)
        chaotic_term /= self.dim
        
        # Multi-scale Gaussian radial basis function with adaptive widths
        rbf_term = 0.0
        for i in range(self.dim):
            # Varying width based on dimension index and global sum
            width = 0.8 + 0.4 * np.sin(0.5 * np.pi * i + 0.2 * np.sum(x))
            rbf_term += np.exp(-0.5 * (x[i] / width)**2) * np.cos(3.0 * x[i])
        rbf_term /= self.dim
        
        # Adaptive penalty with condition-based scaling
        penalty_term = 0.0
        for i in range(self.dim):
            # Condition factor that varies with dimension and global sum
            condition_factor = 1.2 + 0.3 * np.sin(0.2 * np.pi * i + 0.1 * np.sum(x))
            penalty_term += condition_factor * (x[i]**2 + 0.2 * np.abs(x[i])) * np.exp(-0.08 * x[i]**2)
        penalty_term /= self.dim
        
        # Enhanced cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling factor based on chaotic sequence and dimension difference
                coupling_factor = 0.4 + 0.6 * np.sin(0.3 * (i - j) + 0.2 * np.sum(x))
                cross_term += coupling_factor * np.exp(-0.15 * (x[i] - x[j])**2) * np.cos(0.7 * (x[i] + x[j]))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with chaotic basin modulation
        modal_term = 0.0
        for i in range(self.dim):
            # Chaotic amplitude modulation based on dimension and global sum
            chaotic_amp = 1.0 + 0.4 * np.sin(0.5 * np.pi * i + 0.3 * np.sum(x))
            modal_term += chaotic_amp * np.tanh(x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.12 * x[i]**2)
        modal_term /= self.dim
        
        # Enhanced noise component with chaotic phase coupling
        noise_term = 0.0
        for i in range(self.dim):
            # Phase based on chaotic sequence and global sum
            phase = 0.4 * np.tanh(0.2 * np.pi * i + 0.15 * np.sum(x))
            noise_term += np.sin(x[i] * (1.0 + 0.15 * x[i] + phase)) * np.exp(-0.1 * x[i]**2)
        noise_term /= self.dim
        
        # Polynomial distortion with chaotic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            # Chaotic coefficient modulation
            coeff = 1.1 + 0.2 * np.tanh(0.3 * np.pi * i + 0.1 * np.sum(x))
            poly_term += coeff * (x[i]**4 - 2.0 * x[i]**3 + 1.5 * x[i]**2 + 0.3 * x[i]) * np.exp(-0.06 * x[i]**2)
        poly_term /= self.dim
        
        # Multi-scale ridge with chaotic modulation
        ridge_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation factor
            mod_factor = 1.0 + 0.3 * np.tanh(0.3 * np.pi * i + 0.2 * np.sum(x))
            ridge_term += mod_factor * np.sin(x[i]) * np.cos(x[i]) * np.exp(-0.1 * x[i]**2)
        ridge_term /= self.dim
        
        # Multi-scale interaction with chaotic coupling
        multi_scale_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic scale factor based on dimension and global sum
                scale_factor = 0.3 + 0.7 * np.tanh(0.2 * (i - j) + 0.1 * np.sum(x))
                multi_scale_term += scale_factor * np.exp(-0.08 * (x[i] - x[j])**2) * np.cos(0.4 * (x[i] + x[j]))
        multi_scale_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with dynamic weights based on chaotic sequence
        weights = self.chaotic_seq[:self.dim] % 1.0
        weights = weights / np.sum(weights)
        
        total = (weights[0] * chaotic_term + 
                 weights[1] * rbf_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_term + 
                 weights[4] * modal_term + 
                 weights[5] * noise_term + 
                 weights[6] * poly_term + 
                 weights[7] * ridge_term + 
                 weights[8] * multi_scale_term)
        
        return total