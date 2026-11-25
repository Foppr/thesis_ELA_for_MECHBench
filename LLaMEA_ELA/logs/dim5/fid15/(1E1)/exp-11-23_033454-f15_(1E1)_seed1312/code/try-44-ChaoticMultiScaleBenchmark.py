import numpy as np

class ChaoticMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.freqs = np.random.uniform(1, 10, dim)
        self.amps = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.basin_degree = 3 + np.random.randint(0, 3)  # Random polynomial degree
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term - creates a smooth, curved landscape
        basin_term = np.sum((x / 5.0)**self.basin_degree) * 0.5
        
        # Chaotic sinusoidal component - creates irregular, high-frequency oscillations
        chaotic_term = 0.0
        for i in range(self.dim):
            # Multi-scale sinusoidal waves with different frequencies and amplitudes
            wave = self.amps[i] * np.sin(self.freqs[i] * x[i] + self.phase_shifts[i])
            # Add higher harmonics for more complexity
            wave += 0.5 * self.amps[i] * np.sin(2 * self.freqs[i] * x[i] + self.phase_shifts[i])
            chaotic_term += wave
        
        # Cross-term interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * 0.1
                
        # Add a global scaling factor to control difficulty
        difficulty_factor = 1.0 + 0.5 * np.random.random()
        
        return difficulty_factor * (basin_term - chaotic_term + cross_term)