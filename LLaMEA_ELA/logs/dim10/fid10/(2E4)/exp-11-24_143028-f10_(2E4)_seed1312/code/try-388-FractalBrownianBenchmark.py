import numpy as np

class FractalBrownianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for enhanced complexity
        self.chaos_factors = np.random.uniform(0.5, 2.0, dim)
        self.frequency_modulators = np.random.uniform(0.8, 1.5, dim)
        self.coupling_strengths = np.random.uniform(0.3, 1.2, dim)
        # Cross-dimensional coupling with chaotic interaction
        self.coupling_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.coupling_matrix[i, j] = np.random.uniform(-0.8, 0.8) * np.exp(-abs(i-j)/max(1, dim/3))
        # Adaptive basin parameters
        self.basin_parameters = np.random.uniform(0.2, 1.0, dim)
        # Additional chaotic modulation for improved fitness
        self.modulation_factors = np.random.uniform(0.1, 0.5, dim)
        # New: Enhanced fractal structure with modified harmonic components
        self.harmonic_weights = np.random.uniform(0.5, 1.5, dim)
        self.fractal_exponents = np.random.uniform(0.3, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for fractal computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute chaotic sine wave components with adaptive frequencies
        chaotic_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Chaotic sine wave with frequency modulation and new harmonic structure
            base_freq = 2 * np.pi * self.frequency_modulators[i]
            chaos_factor = self.chaos_factors[i]
            
            # Multiple chaotic contributions with modified harmonic structure
            chaotic_sum = 0.0
            num_terms = min(15, max(5, int(self.basin_parameters[i] * 7)))
            for n in range(1, num_terms + 1):
                freq = base_freq * n * (1.0 + 0.2 * np.sin(n * normalized_x[i] * 3.0))
                amplitude = chaos_factor / (n * (n + 1.0)) * self.harmonic_weights[i]
                chaotic_sum += amplitude * np.sin(freq * normalized_x[i])
            
            # Add coupling effects with modified interaction
            coupling_effect = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_effect += self.coupling_matrix[i, j] * np.sin(2.5 * normalized_x[j] + 0.5 * np.cos(normalized_x[i]))
            
            chaotic_values[i] = chaotic_sum + coupling_effect
            
        # Add cross-dimensional basin interactions with self-similarity and new fractal components
        fitness = 0.0
        for i in range(self.dim):
            # Enhanced polynomial and exponential terms with fractal modification
            term1 = 0.4 * chaotic_values[i]**2
            term2 = 0.15 * np.abs(chaotic_values[i])**3
            term3 = 0.25 * np.exp(-0.3 * chaotic_values[i]**2)
            
            # Fractal basin interaction with modified distance metric
            basin_interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(chaotic_values[i] - chaotic_values[j])
                    # Modified fractal distance with exponent
                    fractal_dist = dist ** self.fractal_exponents[i]
                    basin_interaction += 0.25 * np.exp(-fractal_dist / (0.15 * self.basin_parameters[i]))
            
            # Add adaptive coupling strength and chaotic modulation
            coupling_term = self.coupling_strengths[i] * np.sin(2.0 * chaotic_values[i]) * (1.0 + self.modulation_factors[i] * np.sin(3.0 * normalized_x[i]))
            
            fitness += term1 + term2 + term3 + basin_interaction + coupling_term
        
        # Normalize and add global scaling
        fitness = fitness / self.dim
        # Add chaotic noise for robustness
        noise = np.random.uniform(-0.002, 0.002) * np.mean(np.abs(chaotic_values))
        return fitness + noise