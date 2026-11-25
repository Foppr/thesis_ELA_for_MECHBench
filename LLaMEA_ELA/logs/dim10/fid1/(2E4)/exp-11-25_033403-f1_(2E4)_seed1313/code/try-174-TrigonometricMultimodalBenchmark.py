import numpy as np

class TrigonometricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random frequencies, amplitudes, and phases for each dimension
        self.frequencies = np.random.uniform(1.0, 15.0, dim)
        self.amplitudes = np.random.uniform(0.3, 2.5, dim)
        self.phases = np.random.uniform(0.0, 2 * np.pi, dim)
        # Additional parameters for creating complex interactions
        self.interaction_coefficients = np.random.uniform(-2.0, 2.0, (dim, dim))
        self.bias_terms = np.random.uniform(-1.0, 1.0, dim)
        # Dynamic modulation parameters
        self.modulation_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.modulation_amplitudes = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base trigonometric function with varying parameters and dynamic modulation
        result = 0.0
        for i in range(self.dim):
            # Compose multiple trigonometric terms with different frequencies and amplitudes
            term = (self.amplitudes[i] * np.sin(self.frequencies[i] * x[i] + self.phases[i]) +
                   0.5 * self.amplitudes[i] * np.cos(2 * self.frequencies[i] * x[i] + self.phases[i]) +
                   0.3 * self.amplitudes[i] * np.sin(3 * self.frequencies[i] * x[i] + self.phases[i]) +
                   0.1 * self.amplitudes[i] * np.cos(4 * self.frequencies[i] * x[i] + self.phases[i]))
            
            # Add dynamic modulation based on other dimensions
            dynamic_mod = 0.0
            for j in range(self.dim):
                if i != j:
                    dynamic_mod += (self.interaction_coefficients[i, j] * 
                                  np.sin(x[j] * self.modulation_frequencies[i]) * 
                                  np.cos(x[j] * self.modulation_frequencies[i] * 0.7))
            
            term += dynamic_mod
            # Add bias term
            term += self.bias_terms[i]
            result += term**2
            
        # Add interaction terms between dimensions with adaptive coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create adaptive coupling based on distance and interaction coefficients
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)  # Avoid division by zero
                coupling = (self.interaction_coefficients[i, j] * 
                           np.sin(dist * self.frequencies[i]) * 
                           np.cos(dist * self.frequencies[j]))
                
                # Add chaotic modulation to interaction terms
                chaotic_mod = np.sin(x[i] * x[j] * 0.1) * np.cos(x[i] + x[j])
                coupling *= (1.0 + 0.3 * chaotic_mod)
                
                interaction += coupling
                
        # Add multi-scale periodic modulation with varying amplitudes
        periodic_modulation = 0.0
        for i in range(self.dim):
            # Multiple frequency components for richer structure
            freq1 = self.modulation_frequencies[i]
            freq2 = self.modulation_frequencies[i] * 1.5
            freq3 = self.modulation_frequencies[i] * 2.0
            
            periodic_modulation += (self.modulation_amplitudes[i] * 
                                  np.sin(x[i] * freq1) * 
                                  np.cos(x[i] * freq2) * 
                                  np.sin(x[i] * freq3))
            
        # Combine all components with optimized weights
        total = 0.35 * result + 0.35 * interaction + 0.3 * periodic_modulation
        
        # Add noise-like perturbation to increase complexity
        noise_perturbation = 0.01 * np.sum(np.sin(x * 7.0))
        total += noise_perturbation
        
        return total