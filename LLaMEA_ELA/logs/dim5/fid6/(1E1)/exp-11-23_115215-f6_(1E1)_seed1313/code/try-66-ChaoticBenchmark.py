import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for enhanced complexity
        self.r_values = np.linspace(3.5, 3.9, dim)
        self.phase_shifts = np.linspace(0, 2*np.pi, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f_val = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x)))
        
        # Nested logistic map components with phase coupling
        for i in range(self.dim):
            # Outer chaotic dynamics with inner feedback
            if i == 0:
                logistic_val = x[i]
            else:
                logistic_val = self.r_values[i] * x[i-1] * (1 - x[i-1])
            
            # Inner logistic map with phase modulation
            inner_logistic = 3.8 * logistic_val * (1 - logistic_val)
            f_val += 0.4 * np.sin(inner_logistic * 17 + self.phase_shifts[i]) * \
                     np.cos(inner_logistic * 9 + self.phase_shifts[i])
            
        # Dynamic radial basis functions with time-varying centers and widths
        for i in range(self.dim):
            center = 2.5 * np.sin(i * 0.6 + np.sum(x) * 0.1)
            width = 0.4 + 0.6 * np.cos(i * 0.3 + np.sum(x) * 0.2)
            f_val += 0.3 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.2 * np.sin(i * 0.5))
            
        # Non-local coupling with exponentially weighted interactions
        for i in range(self.dim):
            for j in range(i+2, min(i+4, self.dim)):
                weight = np.exp(-0.15 * (j - i)) * np.cos(x[i] + x[j])
                f_val += 0.2 * weight * (x[i]**2) * (x[j]**2)
                
        # Asymmetric higher-order coupling terms
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.25 * (diff**4 + 0.5 * np.abs(diff)**2.5) + \
                         0.1 * np.sin(x[i]) * np.cos(x[i-1])
                
        # Multi-scale sinusoidal modulations with dynamic frequencies
        for i in range(self.dim):
            freq = 1.5 + 2.5 * np.sin(i * 0.3)
            f_val += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + \
                     0.15 * np.sin(4 * freq * x[i]) * np.cos(3 * freq * x[i])
                     
        # Polynomial coupling with chaotic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight generation using logistic map
                chaotic_weight = self.r_values[(i+j) % len(self.r_values)] * 0.6 * (1 - 0.6)
                f_val += chaotic_weight * (x[i]**3) * (x[j]**2) + \
                         0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Time-delayed chaotic coupling with dynamic phase
        for i in range(self.dim):
            if i > 2:
                delayed_term = np.sin(x[i-3] + 0.4 * x[i-2] + 0.2 * x[i-1])
                phase_mod = np.cos(i * 0.4 + np.sum(x))
                f_val += 0.15 * delayed_term * phase_mod * np.cos(x[i])
                
        # Add final high-dimensional non-linear transformation
        f_val += 0.2 * np.sin(np.sum(x**4)) + 0.1 * np.cos(np.prod(x)) + \
                 0.05 * np.sin(np.sum(np.abs(x)))
        
        return f_val