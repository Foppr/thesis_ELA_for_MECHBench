import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        np.random.seed(42)
        self.chaos_params = np.random.uniform(0.5, 2.0, dim)
        self.oscillation_freq = np.random.uniform(1.0, 5.0, dim)
        self.modulation_freq = np.random.uniform(0.1, 0.5, dim)
        self.scale_factors = np.random.uniform(0.1, 2.0, dim)
        self.nested_depth = max(1, dim // 4)
        self.gradient_strength = 1.5
        self.constraint_strength = 2.0
        self.dynamic_shift = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply scaling and dynamic shifts
        x_shifted = x + self.dynamic_shift
        
        # Base quadratic term
        f_val = np.sum(x_shifted**2)
        
        # Add chaotic gradient contributions
        gradient_contrib = 0.0
        for i in range(self.dim):
            # Multi-scale oscillations
            oscillation = np.sin(self.oscillation_freq[i] * x_shifted[i])
            modulation = np.cos(self.modulation_freq[i] * x_shifted[i])
            gradient_contrib += self.chaos_params[i] * oscillation * modulation * x_shifted[i]
            
        f_val += self.gradient_strength * gradient_contrib
        
        # Add nested minima structure
        nested_term = 0.0
        for i in range(self.nested_depth):
            scale = 1.0 / (i + 1)
            nested_contrib = 0.0
            for j in range(self.dim):
                nested_contrib += np.sin(scale * self.oscillation_freq[j] * x_shifted[j]) * np.cos(scale * self.modulation_freq[j] * x_shifted[j])
            nested_term += scale * nested_contrib**2
            
        f_val += nested_term
        
        # Add implicit constraint landscape
        constraint_term = 0.0
        for i in range(self.dim):
            constraint_term += self.constraint_strength * (np.sin(x_shifted[i]) - 0.5 * np.sin(2 * x_shifted[i]))**2
            
        f_val += constraint_term
        
        # Add multi-scale interaction terms
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(self.scale_factors[i] * x_shifted[i]) * np.cos(self.scale_factors[j] * x_shifted[j])
                interaction_term += interaction * np.exp(-0.1 * (x_shifted[i] - x_shifted[j])**2)
                
        f_val += interaction_term
        
        # Add dynamic fitness landscape with time-like parameter
        time_param = np.sum(np.sin(x_shifted)) / self.dim
        dynamic_factor = 1.0 + 0.5 * np.sin(time_param)
        f_val *= dynamic_factor
        
        return f_val