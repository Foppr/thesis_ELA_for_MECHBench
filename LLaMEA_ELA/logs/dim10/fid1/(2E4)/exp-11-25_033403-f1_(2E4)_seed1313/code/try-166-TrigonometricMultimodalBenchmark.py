import numpy as np

class TrigonometricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random frequencies, amplitudes, and phases for each dimension
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phases = np.random.uniform(0.0, 2 * np.pi, dim)
        # Additional parameters for creating complex interactions
        self.interaction_coefficients = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.bias_terms = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base trigonometric function with varying parameters
        result = 0.0
        for i in range(self.dim):
            # Compose multiple trigonometric terms with different frequencies and amplitudes
            term = (self.amplitudes[i] * np.sin(self.frequencies[i] * x[i] + self.phases[i]) +
                   0.5 * self.amplitudes[i] * np.cos(2 * self.frequencies[i] * x[i] + self.phases[i]) +
                   0.3 * self.amplitudes[i] * np.sin(3 * self.frequencies[i] * x[i] + self.phases[i]))
            # Add bias term
            term += self.bias_terms[i]
            result += term**2
            
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create coupling based on distance and interaction coefficients
                dist = np.abs(x[i] - x[j])
                interaction += (self.interaction_coefficients[i, j] * 
                              np.sin(dist * self.frequencies[i]) * 
                              np.cos(dist * self.frequencies[j]))
                
        # Add periodic modulation to the overall function
        periodic_modulation = 0.0
        for i in range(self.dim):
            periodic_modulation += np.sin(x[i] * self.frequencies[i] * 0.5) * np.cos(x[i] * self.frequencies[i] * 0.3)
            
        # Combine all components with appropriate weights
        total = 0.4 * result + 0.3 * interaction + 0.3 * periodic_modulation
        
        return total