import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize dimension-specific parameters for ruggedness and modulation
        self.ruggedness_factors = np.random.uniform(0.5, 2.0, dim)
        self.modulation_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.interference_strengths = np.random.uniform(0.1, 1.0, (dim, dim))
        self.adaptation_parameters = np.random.uniform(0.8, 1.5, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base rugged energy term with sinusoidal modulations
        energy_term = 0.0
        for i in range(self.dim):
            ruggedness = self.ruggedness_factors[i]
            freq = self.modulation_frequencies[i]
            # Sinusoidal modulation with varying amplitude and frequency
            energy_term += (1.0 + ruggedness * np.sin(freq * x_norm[i])) * \
                          np.exp(-0.5 * (x_norm[i] ** 2)) * \
                          (1.0 + 0.2 * np.cos(3 * freq * x_norm[i]))
        
        # Cross-dimensional interference with adaptive coupling
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = self.interference_strengths[i][j]
                # Adaptive coupling based on dimension indices and input values
                coupling = strength * np.sin(x_norm[i] * x_norm[j]) * \
                          np.exp(-0.2 * (x_norm[i] - x_norm[j])**2) * \
                          np.cos(2 * (x_norm[i] + x_norm[j]))
                interference_term += coupling
        
        # Adaptive difficulty scaling based on input position
        difficulty_scale = 1.0
        for i in range(self.dim):
            difficulty_scale *= (1.0 + self.adaptation_parameters[i] * np.sin(x_norm[i]))
        
        # Additional high-frequency oscillation component
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) * \
                             np.exp(-0.3 * (x_norm[i] ** 2))
        
        # Combine all terms with appropriate scaling
        combined = energy_term + interference_term + high_freq_term
        
        # Add a global bias term that varies with problem dimensionality
        global_bias = 0.1 * self.dim * np.sum(np.sin(x_norm) * np.cos(x_norm))
        
        # Apply final adaptive scaling and return
        return difficulty_scale * combined + global_bias