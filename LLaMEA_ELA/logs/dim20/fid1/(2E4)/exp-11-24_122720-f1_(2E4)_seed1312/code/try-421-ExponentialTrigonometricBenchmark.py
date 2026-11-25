import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Exponential decay parameters
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.decay_offsets = np.random.uniform(-1.0, 1.0, dim)
        # Trigonometric coupling coefficients
        self.coupling_amplitudes = np.random.uniform(0.5, 2.0, (dim, dim))
        self.coupling_frequencies = np.random.randint(1, 6, (dim, dim))
        # Gradient field parameters
        self.gradient_magnitudes = np.random.uniform(0.5, 3.0, dim)
        self.gradient_directions = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive scaling factor
        self.adaptive_scale = np.random.uniform(0.5, 2.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component
        exp_sum = 0
        for i in range(self.dim):
            xi = x[i]
            exp_term = np.exp(-self.decay_rates[i] * np.abs(xi)) + self.decay_offsets[i]
            exp_sum += exp_term
        
        # Trigonometric coupling component
        trig_sum = 0
        for i in range(self.dim):
            xi = x[i]
            coupling_term = 0
            for j in range(self.dim):
                if i != j:
                    coupling_term += (self.coupling_amplitudes[i][j] * 
                                    np.sin(self.coupling_frequencies[i][j] * x[j]) *
                                    np.cos(xi))
            trig_sum += coupling_term
        
        # Gradient field component
        grad_sum = 0
        for i in range(self.dim):
            xi = x[i]
            grad_term = 0
            for j in range(self.dim):
                grad_term += self.gradient_magnitudes[i] * self.gradient_directions[i][j] * (xi - x[j])
            grad_sum += grad_term
        
        # Combine all components with adaptive scaling
        result = (0.6 * exp_sum + 
                 1.0 * trig_sum + 
                 0.8 * grad_sum) * self.adaptive_scale
        
        return result