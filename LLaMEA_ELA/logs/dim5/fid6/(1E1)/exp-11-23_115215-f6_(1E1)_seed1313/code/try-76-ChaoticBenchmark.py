import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with time-varying nature
        self.r_values = 4.0 * np.sin(np.linspace(0, np.pi, dim)) + 3.5
        self.phase_shifts = np.linspace(0, 4*np.pi, dim)
        self.time_varying_params = np.random.rand(dim) * 2.0 + 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling and time-varying modulation
        f_val = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x))) * self.time_varying_params[0]
        
        # Nested logistic map components with phase coupling and time-varying r values
        for i in range(self.dim):
            # Outer chaotic dynamics with inner feedback
            if i == 0:
                logistic_val = x[i]
            else:
                logistic_val = self.r_values[i] * x[i-1] * (1 - x[i-1])
            
            # Inner logistic map with phase modulation and dynamic frequency
            inner_logistic = 3.9 * logistic_val * (1 - logistic_val)
            freq_mod = 2 + 2 * np.sin(i * 0.5 + np.sum(x) * 0.1)
            f_val += 0.4 * np.sin(inner_logistic * freq_mod + self.phase_shifts[i]) * \
                     np.cos(inner_logistic * (freq_mod * 0.7) + self.phase_shifts[i])
            
        # Dynamic radial basis functions with time-varying centers, widths and weights
        for i in range(self.dim):
            center = 3.0 * np.sin(i * 0.7 + np.sum(x) * 0.1) * self.time_varying_params[i]
            width = 0.3 + 0.7 * np.cos(i * 0.4 + np.sum(x) * 0.2) * self.time_varying_params[i]
            weight = 0.3 * self.time_varying_params[i] * (1.0 + 0.2 * np.sin(i * 0.6))
            f_val += weight * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.2 * np.sin(i * 0.6))
            
        # Non-local coupling with exponentially weighted interactions and time-varying weights
        for i in range(self.dim):
            for j in range(i+2, min(i+5, self.dim)):
                weight = np.exp(-0.2 * (j - i)) * np.cos(x[i] + x[j]) * self.time_varying_params[i]
                f_val += 0.2 * weight * (x[i]**2) * (x[j]**2)
                
        # Asymmetric higher-order coupling terms with time-varying exponents
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                exp_mod = 4 + 2 * np.sin(i * 0.3)
                f_val += 0.25 * (diff**exp_mod + 0.5 * np.abs(diff)**(exp_mod * 0.7)) + \
                         0.1 * np.sin(x[i]) * np.cos(x[i-1])
                
        # Multi-scale sinusoidal modulations with dynamic frequencies and time-varying amplitudes
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * 0.3) * self.time_varying_params[i]
            amp_mod = 0.3 + 0.1 * np.cos(i * 0.4)
            f_val += amp_mod * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + \
                     0.15 * np.sin(4 * freq * x[i]) * np.cos(3 * freq * x[i])
                     
        # Polynomial coupling with chaotic weights and time-varying exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight generation using logistic map with dynamic r value
                chaotic_weight = self.r_values[(i+j) % len(self.r_values)] * 0.5 * (1 - 0.5)
                exp_i = 3 + np.sin(i * 0.2) * 2
                exp_j = 2 + np.cos(j * 0.3) * 2
                f_val += chaotic_weight * (x[i]**exp_i) * (x[j]**exp_j) + \
                         0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Time-delayed chaotic coupling with dynamic phase and time-varying delays
        for i in range(self.dim):
            if i > 2:
                delayed_term = np.sin(x[i-3] + 0.3 * x[i-2] + 0.1 * x[i-1])
                phase_mod = np.cos(i * 0.5 + np.sum(x)) * self.time_varying_params[i]
                delay_weight = 0.15 * (1 + 0.1 * np.sin(i * 0.4))
                f_val += delay_weight * delayed_term * phase_mod * np.cos(x[i])
                
        # Add final high-dimensional non-linear transformation with chaotic modulation
        f_val += 0.2 * np.sin(np.sum(x**4)) * self.time_varying_params[-1] + \
                 0.1 * np.cos(np.prod(x)) * self.time_varying_params[0] + \
                 0.05 * np.sin(np.sum(np.abs(x))) * self.time_varying_params[1]
        
        # Add a highly oscillatory chaotic term for increased multimodality
        chaotic_oscillation = np.sum(np.sin(20 * x) * np.cos(15 * x))
        f_val += 0.3 * chaotic_oscillation
        
        return f_val