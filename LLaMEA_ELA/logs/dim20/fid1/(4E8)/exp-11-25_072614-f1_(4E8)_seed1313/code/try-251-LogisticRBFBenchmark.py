import numpy as np

class LogisticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for dynamic weighting
        self.logistic_seq = np.array([0.3, 0.7, 0.2, 0.8, 0.4, 0.6, 0.1, 0.9, 0.5, 0.5])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map dynamics with radial basis function interpolation
        logistic_term = 0.0
        for i in range(self.dim):
            # Logistic map: x_{n+1} = r * x_n * (1 - x_n)
            r = 3.9 + 0.2 * np.sin(0.5 * np.pi * i)
            x_log = r * x[i] * (1 - x[i])
            logistic_term += x_log * np.exp(-0.1 * x[i]**2)
        logistic_term /= self.dim
        
        # Radial basis function with multi-dimensional modulation
        rbf_term = 0.0
        for i in range(self.dim):
            # Radial basis function with varying width
            width = 1.0 + 0.5 * np.sin(0.6 * np.pi * i)
            rbf_term += np.exp(-0.5 * (x[i] / width)**2) * np.cos(2.0 * np.pi * x[i])
        rbf_term /= self.dim
        
        # Adaptive penalty with multi-scale conditioning
        penalty_term = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.4 * np.sin(0.3 * np.pi * i)
            penalty_term += condition_factor * (x[i]**2 + 0.1 * np.abs(x[i])) * np.exp(-0.05 * x[i]**2)
        penalty_term /= self.dim
        
        # Cross-dimensional interaction with enhanced logistic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = 0.5 + 0.5 * np.sin(0.2 * (i - j) + 0.3 * np.sum(x))
                # Enhanced coupling with additional harmonic term
                cross_term += coupling_factor * np.exp(-0.1 * (x[i] - x[j])**2) * np.cos(0.5 * (x[i] + x[j])) * np.sin(0.2 * x[i] * x[j])
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with enhanced logistic basin modulation
        modal_term = 0.0
        for i in range(self.dim):
            chaotic_amp = 1.0 + 0.3 * np.sin(0.4 * np.pi * i + np.sum(x))
            # Enhanced modal structure with additional trigonometric component
            modal_term += chaotic_amp * np.tanh(x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2) * (1.0 + 0.2 * np.sin(0.3 * x[i]))
        modal_term /= self.dim
        
        # Dynamic noise with enhanced logistic phase coupling
        noise_term = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.tanh(0.3 * np.pi * i + 0.2 * np.sum(x))
            # Enhanced noise with additional polynomial component
            noise_term += np.sin(x[i] * (1 + 0.1 * x[i] + phase)) * np.exp(-0.08 * x[i]**2) * (1.0 + 0.1 * x[i]**2)
        noise_term /= self.dim
        
        # Polynomial distortion with enhanced logistic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.2 * np.tanh(0.5 * np.pi * i)
            # Enhanced polynomial with additional cubic term
            poly_term += coeff * (x[i]**4 - 2.5 * x[i]**3 + 2.0 * x[i]**2 + 0.5 * x[i]) * np.exp(-0.05 * x[i]**2)
        poly_term /= self.dim
        
        # Multi-scale ridge with enhanced logistic modulation
        ridge_term = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.4 * np.tanh(0.4 * np.pi * i + 0.3 * np.sum(x))
            # Enhanced ridge with additional interaction term
            ridge_term += mod_factor * np.sin(x[i]) * np.cos(x[i]) * np.exp(-0.1 * x[i]**2) * (1.0 + 0.1 * np.sin(0.5 * x[i]))
        ridge_term /= self.dim
        
        # Multi-scale interaction with enhanced logistic coupling
        multi_scale_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 0.2 + 0.8 * np.tanh(0.1 * (i - j) + 0.1 * np.sum(x))
                # Enhanced multi-scale with additional exponential term
                multi_scale_term += scale_factor * np.exp(-0.05 * (x[i] - x[j])**2) * np.cos(0.3 * (x[i] + x[j])) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        multi_scale_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with dynamic weights based on logistic map
        weights = self.logistic_seq[:self.dim] % 1.0
        weights = weights / np.sum(weights)
        
        total = (weights[0] * logistic_term + 
                 weights[1] * rbf_term + 
                 weights[2] * penalty_term + 
                 weights[3] * cross_term + 
                 weights[4] * modal_term + 
                 weights[5] * noise_term + 
                 weights[6] * poly_term + 
                 weights[7] * ridge_term + 
                 weights[8] * multi_scale_term)
        
        return total