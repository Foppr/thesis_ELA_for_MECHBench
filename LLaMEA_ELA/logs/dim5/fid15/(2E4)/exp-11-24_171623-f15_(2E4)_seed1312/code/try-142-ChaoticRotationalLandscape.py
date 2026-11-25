import numpy as np

class ChaoticRotationalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logarithmic barrier components with chaotic modulation
        log_sum = 0.0
        for i in range(self.dim):
            # Add small perturbation to avoid singularities
            val = np.abs(x_norm[i]) + 1e-8
            log_sum += np.log(val) * np.sin(x_norm[i] * np.pi * (i + 1))
        
        # Polynomial coupling with chaotic coefficients
        poly_sum = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            poly_sum += coeff * (x_norm[i]**3) * np.cos(x_norm[i] * 2.0)
            
        # Rotational components inspired by quaternions
        rot_sum = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                # 2D rotational component
                x1, x2 = x_norm[i], x_norm[i+1]
                rot_sum += (x1**2 + x2**2) * np.sin(x1 * x2 * 3.0)
                
        # Chaotic attractor-like structure with multiple local minima
        chaos_sum = 0.0
        for i in range(self.dim):
            # Logistic map inspired term
            chaos_term = np.sin(x_norm[i] * 5.0) * np.cos(x_norm[i] * 2.0)
            chaos_sum += chaos_term * (1.0 + 0.3 * np.sin(i * 2.0))
            
        # Cross-dimensional interaction with exponential decay
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < len(x_norm) and j < len(x_norm):
                    dist = np.abs(x_norm[i] - x_norm[j])
                    cross_sum += np.exp(-dist * 2.0) * np.sin(x_norm[i] + x_norm[j])
        
        # Adaptive conditioning factor
        cond_factor = 1.0 + 0.4 * np.sin(self.dim * 0.3)
        
        # Combine all components
        result = 0.25 * log_sum + 0.3 * poly_sum + 0.2 * rot_sum + 0.2 * chaos_sum + 0.05 * cross_sum
        
        # Add final transformation to increase complexity
        result = result * cond_factor * (1.0 + 0.2 * np.sum(np.abs(x_norm)))
        
        return result