import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map parameters for dimension coupling
        np.random.seed(42)
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        self.logistic_states = np.random.rand(dim) * 0.5 + 0.25  # Initialize logistic states
        # Perturbation scales
        self.perturbation_scale = 0.1
        self.frequency_scale = 1.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Apply chaotic logistic map for dimension coupling
        logistic_vals = np.zeros(self.dim)
        for i in range(self.dim):
            self.logistic_states[i] = self.r_values[i] * self.logistic_states[i] * (1 - self.logistic_states[i])
            logistic_vals[i] = self.logistic_states[i]
        
        # Add sinusoidal terms with varying frequencies and amplitudes
        for i in range(self.dim):
            # Use logistic state to modulate frequency and amplitude
            freq = 2.0 + 3.0 * logistic_vals[i]
            amp = 1.0 + 2.0 * logistic_vals[i]
            f_val += amp * np.sin(freq * x[i]) + 0.5 * amp * np.sin(2.0 * freq * x[i])
            
        # Add cross-dimensional interaction terms
        for i in range(self.dim - 1):
            f_val += 0.3 * np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
            
        # Add perturbed quartic term
        f_val += 0.02 * np.sum((x**4) * (1.0 + self.perturbation_scale * np.sin(10.0 * x)))
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.5
        
        return f_val