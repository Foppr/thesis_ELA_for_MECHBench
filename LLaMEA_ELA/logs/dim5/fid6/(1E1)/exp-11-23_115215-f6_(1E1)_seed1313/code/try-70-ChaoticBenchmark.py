import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for enhanced complexity
        self.r_values = np.linspace(3.5, 4.0, dim)
        self.phase_shifts = np.linspace(0, 2*np.pi, dim)
        self.memory_weights = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling and memory effect
        memory_factor = np.mean(np.sin(x * self.memory_weights))
        f_val = np.sum(x**2) * (1.0 + 0.1 * np.sin(np.sum(x)) + 0.05 * memory_factor)
        
        # Nested logistic map components with phase coupling and fractal recursion
        for i in range(self.dim):
            # Outer chaotic dynamics with inner feedback
            if i == 0:
                logistic_val = x[i]
            else:
                logistic_val = self.r_values[i] * x[i-1] * (1 - x[i-1])
            
            # Inner logistic map with phase modulation and fractal scaling
            inner_logistic = 3.9 * logistic_val * (1 - logistic_val)
            fractal_scale = 1.0 + 0.2 * np.sin(i * 0.5) * np.cos(np.sum(x))
            f_val += 0.4 * np.sin(inner_logistic * 15 + self.phase_shifts[i]) * \
                     np.cos(inner_logistic * 8 + self.phase_shifts[i]) * fractal_scale
            
        # Dynamic radial basis functions with time-varying centers, widths and memory
        for i in range(self.dim):
            center = 3.0 * np.sin(i * 0.7 + np.sum(x) * 0.1 + memory_factor)
            width = 0.3 + 0.7 * np.cos(i * 0.4 + np.sum(x) * 0.2 + memory_factor)
            f_val += 0.3 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.2 * np.sin(i * 0.6 + memory_factor))
            
        # Non-local coupling with exponentially weighted interactions and memory
        for i in range(self.dim):
            for j in range(i+2, min(i+5, self.dim)):
                weight = np.exp(-0.2 * (j - i)) * np.cos(x[i] + x[j]) * (1 + 0.1 * memory_factor)
                f_val += 0.2 * weight * (x[i]**2) * (x[j]**2)
                
        # Asymmetric higher-order coupling terms with memory dependencies
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                mem_term = np.sin(i * 0.3 + memory_factor)
                f_val += 0.25 * (diff**4 + 0.5 * np.abs(diff)**2.5) * (1 + 0.1 * mem_term) + \
                         0.1 * np.sin(x[i]) * np.cos(x[i-1]) * (1 + 0.05 * mem_term)
                
        # Multi-scale sinusoidal modulations with dynamic frequencies and memory
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * 0.3 + memory_factor)
            f_val += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + \
                     0.15 * np.sin(4 * freq * x[i]) * np.cos(3 * freq * x[i])
                     
        # Polynomial coupling with chaotic weights and memory effects
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight generation using logistic map with memory
                chaotic_weight = self.r_values[(i+j) % len(self.r_values)] * 0.5 * (1 - 0.5)
                mem_weight = 1.0 + 0.1 * np.sin(i * 0.2 + j * 0.3 + memory_factor)
                f_val += chaotic_weight * mem_weight * (x[i]**3) * (x[j]**2) + \
                         0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Time-delayed chaotic coupling with dynamic phase and memory
        for i in range(self.dim):
            if i > 2:
                delayed_term = np.sin(x[i-3] + 0.3 * x[i-2] + 0.1 * x[i-1])
                phase_mod = np.cos(i * 0.5 + np.sum(x) + memory_factor)
                f_val += 0.15 * delayed_term * phase_mod * np.cos(x[i])
                
        # Add final high-dimensional non-linear transformation with memory
        f_val += 0.2 * np.sin(np.sum(x**4)) + 0.1 * np.cos(np.prod(x)) + \
                 0.05 * np.sin(np.sum(np.abs(x))) + \
                 0.03 * np.sin(memory_factor * 10)
        
        # Add a self-similar fractal component with recursive scaling
        if self.dim >= 4:
            fractal_component = 0.05 * np.sum(np.sin(x * 2**np.arange(self.dim)) * (1 + 0.1 * np.sin(memory_factor)))
            f_val += fractal_component
            
        return f_val