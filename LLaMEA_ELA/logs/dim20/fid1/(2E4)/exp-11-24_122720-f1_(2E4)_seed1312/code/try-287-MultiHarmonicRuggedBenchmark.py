import numpy as np

class MultiHarmonicRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize harmonic frequencies and amplitudes for each dimension
        self.frequencies = [np.random.uniform(1.0, 5.0) for _ in range(dim)]
        self.amplitudes = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        # Correlation matrix parameters
        self.corr_matrix = np.random.rand(dim, dim) * 0.5
        self.corr_matrix = (self.corr_matrix + self.corr_matrix.T) / 2.0
        np.fill_diagonal(self.corr_matrix, 1.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Harmonic potential component
        harmonic = 0
        for i in range(self.dim):
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            # Exponentially decaying harmonic terms
            harmonic += amp * np.sin(freq * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Ruggedness through multi-modal interaction
        rugged = 0
        for i in range(self.dim):
            # Add higher-order polynomial terms for increased ruggedness
            rugged += 0.5 * x[i]**4 - 2.0 * x[i]**2
            
        # Dynamic correlation structure
        corr_term = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_term += self.corr_matrix[i, j] * x[i] * x[j]
                    
        # Noise sensitivity modulation
        noise_mod = 1.0 + 0.2 * np.sin(np.sum(x**2))
        
        # Combine components with dynamic weighting
        result = 1.2 * harmonic + 0.8 * rugged + 0.5 * corr_term
        
        # Apply dimensionality scaling and noise modulation
        dim_scaling = np.log(self.dim + 1) * 0.05
        result *= (1.0 + dim_scaling) * noise_mod
        
        return result