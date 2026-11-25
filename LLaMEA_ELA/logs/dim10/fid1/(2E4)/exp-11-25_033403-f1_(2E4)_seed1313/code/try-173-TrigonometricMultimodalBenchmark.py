import numpy as np

class TrigonometricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random frequencies, amplitudes, and phases for each dimension
        self.frequencies = np.random.uniform(1.0, 15.0, dim)
        self.amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.phases = np.random.uniform(0.0, 2 * np.pi, dim)
        # Additional parameters for creating complex interactions
        self.interaction_coefficients = np.random.uniform(-2.0, 2.0, (dim, dim))
        self.bias_terms = np.random.uniform(-1.0, 1.0, dim)
        # Chaos-inducing parameter
        self.chaos_factor = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base trigonometric function with varying parameters and chaos factor
        result = 0.0
        for i in range(self.dim):
            # Compose multiple trigonometric terms with different frequencies and amplitudes
            term = (self.amplitudes[i] * np.sin(self.frequencies[i] * x[i] + self.phases[i]) +
                   0.5 * self.amplitudes[i] * np.cos(2 * self.frequencies[i] * x[i] + self.phases[i]) +
                   0.3 * self.amplitudes[i] * np.sin(3 * self.frequencies[i] * x[i] + self.phases[i]) +
                   0.1 * self.amplitudes[i] * np.cos(4 * self.frequencies[i] * x[i] + self.phases[i]))
            # Add bias term and chaos modulation
            term += self.bias_terms[i]
            term *= (1 + self.chaos_factor[i] * np.sin(x[i] * 0.1))
            result += term**2
            
        # Add interaction terms between dimensions with dynamic coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create coupling based on distance and interaction coefficients with phase modulation
                dist = np.abs(x[i] - x[j])
                phase_diff = np.abs(np.sin(x[i]) - np.cos(x[j]))
                interaction += (self.interaction_coefficients[i, j] * 
                              np.sin(dist * self.frequencies[i] + phase_diff) * 
                              np.cos(dist * self.frequencies[j] + phase_diff) *
                              np.exp(-0.1 * dist))
                
        # Add periodic modulation to the overall function with chaotic influence
        periodic_modulation = 0.0
        for i in range(self.dim):
            periodic_modulation += (np.sin(x[i] * self.frequencies[i] * 0.5) * 
                                  np.cos(x[i] * self.frequencies[i] * 0.3) *
                                  (1 + 0.2 * np.sin(x[i] * self.chaos_factor[i])))
            
        # Add higher-order cross-terms for increased non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (self.interaction_coefficients[i, j] * 
                              np.sin(x[i] + x[j]) * 
                              np.cos(x[i] - x[j]))
        
        # Combine all components with appropriate weights
        total = 0.3 * result + 0.3 * interaction + 0.2 * periodic_modulation + 0.2 * cross_term
        
        return total