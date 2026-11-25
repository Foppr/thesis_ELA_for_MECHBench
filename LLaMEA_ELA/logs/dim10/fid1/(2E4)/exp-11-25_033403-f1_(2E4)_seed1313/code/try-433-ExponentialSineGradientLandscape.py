import numpy as np

class ExponentialSineGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay parameters for each dimension
        self.exp_rates = np.random.uniform(0.1, 2.0, dim)
        self.exp_amplitudes = np.random.uniform(1.0, 5.0, dim)
        # Initialize sine-wave modulation parameters
        self.sine_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.sine_amplitudes = np.random.uniform(0.5, 3.0, dim)
        # Initialize conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        # Initialize coupling weights between dimensions
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize adaptive scaling parameters
        self.scaling_params = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute exponential decay components
        exp_terms = np.zeros(self.dim)
        for j in range(self.dim):
            exp_terms[j] = self.exp_amplitudes[j] * np.exp(-self.exp_rates[j] * np.abs(x[j]))
        
        # Compute sine-wave modulated gradient components
        sine_terms = np.zeros(self.dim)
        for j in range(self.dim):
            sine_terms[j] = self.sine_amplitudes[j] * np.sin(self.sine_frequencies[j] * x[j])
        
        # Compute conditioning terms
        cond_terms = np.zeros(self.dim)
        for j in range(self.dim):
            cond_terms[j] = self.conditioning_factors[j] * (x[j]**2 + 1.0)
        
        # Compute cross-dimensional coupling terms
        coupling_terms = np.zeros(self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms[i] += self.coupling_weights[i, j] * x[j]
        
        # Compute adaptive scaling terms
        scale_terms = np.zeros(self.dim)
        for j in range(self.dim):
            scale_terms[j] = self.scaling_params[j] * (np.abs(x[j]) + 1.0)
        
        # Combine all components with appropriate weights
        total = 0.0
        for j in range(self.dim):
            total += (exp_terms[j] * sine_terms[j] + 
                     cond_terms[j] * coupling_terms[j] + 
                     scale_terms[j])
        
        return total