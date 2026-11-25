import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with random bifurcation control
        self.r_params = np.random.rand(dim) * 2.5 + 3.5
        self.noise_levels = np.random.rand(dim) * 0.1 + 0.05
        self.correlation_matrix = np.random.rand(dim, dim) * 0.3 + 0.1
        np.fill_diagonal(self.correlation_matrix, 1.0)
        
    def f(self, x):
        # Scale input to [0, 1] range for logistic map
        x_scaled = (x + 5.0) / 10.0
        
        # Generate chaotic sequences using logistic maps
        chaotic_values = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_params[i]
            x_i = x_scaled[i]
            # Iterate logistic map for several steps to reach chaotic regime
            for _ in range(10):
                x_i = r * x_i * (1 - x_i)
            chaotic_values[i] = x_i
            
        # Apply spatial correlation through matrix multiplication
        correlated_values = self.correlation_matrix @ chaotic_values
        
        # Compute multimodal components with varying amplitudes
        result = 0.0
        for i in range(self.dim):
            # Multiple harmonic components with different frequencies
            freq1 = 2 * np.pi * (i + 1)
            freq2 = 4 * np.pi * (i + 1)
            freq3 = 6 * np.pi * (i + 1)
            
            term = (
                0.5 * np.sin(freq1 * correlated_values[i]) +
                0.3 * np.sin(freq2 * correlated_values[i]) +
                0.2 * np.sin(freq3 * correlated_values[i])
            )
            
            # Add amplitude modulation based on position
            amp_mod = 1.0 + 0.5 * np.sin(3 * correlated_values[i])
            result += amp_mod * term
            
        # Add cross-dimensional coupling terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (
                    np.sin(2 * np.pi * (correlated_values[i] + correlated_values[j])) *
                    np.cos(2 * np.pi * (correlated_values[i] - correlated_values[j]))
                )
                
        # Add noise with position-dependent strength
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_levels[i] * np.random.rand() * np.exp(-np.sum(x_scaled**2))
            
        return result + 0.1 * coupling + noise