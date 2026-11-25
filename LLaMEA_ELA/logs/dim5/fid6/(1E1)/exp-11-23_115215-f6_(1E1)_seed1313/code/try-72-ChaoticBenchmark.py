import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for enhanced complexity
        self.r_values = np.linspace(3.5, 4.0, dim)
        self.phase_shifts = np.linspace(0, 2*np.pi, dim)
        self.fractal_exponents = np.random.uniform(0.3, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling and fractal modulation
        f_val = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x)))
        
        # Nested logistic map components with phase coupling and fractal feedback
        for i in range(self.dim):
            # Outer chaotic dynamics with inner feedback
            if i == 0:
                logistic_val = x[i]
            else:
                logistic_val = self.r_values[i] * x[i-1] * (1 - x[i-1])
            
            # Inner logistic map with phase modulation and fractal scaling
            inner_logistic = 3.9 * logistic_val * (1 - logistic_val)
            fractal_scale = self.fractal_exponents[i]
            f_val += 0.4 * np.sin(inner_logistic * 15 + self.phase_shifts[i]) * \
                     np.cos(inner_logistic * 8 + self.phase_shifts[i]) * \
                     (1.0 + 0.1 * np.sin(fractal_scale * np.sum(x)))
            
        # Dynamic radial basis functions with time-varying centers and widths
        for i in range(self.dim):
            center = 3.0 * np.sin(i * 0.7 + np.sum(x) * 0.1)
            width = 0.3 + 0.7 * np.cos(i * 0.4 + np.sum(x) * 0.2)
            f_val += 0.3 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.2 * np.sin(i * 0.6)) * \
                     (1.0 + 0.1 * np.cos(fractal_scale * x[i]))
            
        # Non-local coupling with exponentially weighted interactions and fractal weights
        for i in range(self.dim):
            for j in range(i+2, min(i+5, self.dim)):
                weight = np.exp(-0.2 * (j - i)) * np.cos(x[i] + x[j]) * \
                         (1.0 + 0.05 * np.sin(fractal_scale * (i+j)))
                f_val += 0.2 * weight * (x[i]**2) * (x[j]**2)
                
        # Asymmetric higher-order coupling terms with fractal modulation
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.25 * (diff**4 + 0.5 * np.abs(diff)**2.5) + \
                         0.1 * np.sin(x[i]) * np.cos(x[i-1]) * \
                         (1.0 + 0.1 * np.cos(fractal_scale * i))
                
        # Multi-scale sinusoidal modulations with dynamic frequencies and fractal harmonics
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * 0.3)
            f_val += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + \
                     0.15 * np.sin(4 * freq * x[i]) * np.cos(3 * freq * x[i]) * \
                     (1.0 + 0.05 * np.sin(fractal_scale * i))
                     
        # Polynomial coupling with chaotic weights and fractal structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight generation using logistic map
                chaotic_weight = self.r_values[(i+j) % len(self.r_values)] * 0.5 * (1 - 0.5)
                f_val += chaotic_weight * (x[i]**3) * (x[j]**2) + \
                         0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                         (1.0 + 0.08 * np.cos(fractal_scale * (i+j)))
                
        # Time-delayed chaotic coupling with dynamic phase and fractal modulation
        for i in range(self.dim):
            if i > 2:
                delayed_term = np.sin(x[i-3] + 0.3 * x[i-2] + 0.1 * x[i-1])
                phase_mod = np.cos(i * 0.5 + np.sum(x))
                f_val += 0.15 * delayed_term * phase_mod * np.cos(x[i]) * \
                         (1.0 + 0.1 * np.sin(fractal_scale * i))
                
        # Add final high-dimensional non-linear transformation with fractal features
        f_val += 0.2 * np.sin(np.sum(x**4)) + 0.1 * np.cos(np.prod(x)) + \
                 0.05 * np.sin(np.sum(np.abs(x))) * \
                 (1.0 + 0.1 * np.cos(fractal_scale * np.sum(x)))
        
        # Add fractal-like self-similarity across scales
        scale_factors = [0.5, 0.7, 1.0, 1.3, 1.5]
        for sf in scale_factors[:min(len(scale_factors), self.dim)]:
            f_val += 0.05 * np.sin(sf * np.sum(x**2)) * \
                     (1.0 + 0.1 * np.cos(sf * np.sum(x)))
        
        return f_val