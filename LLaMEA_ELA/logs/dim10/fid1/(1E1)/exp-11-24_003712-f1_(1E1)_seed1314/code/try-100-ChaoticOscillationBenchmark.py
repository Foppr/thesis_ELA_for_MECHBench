import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random coefficients for chaos
        np.random.seed(42)
        self.coeffs = np.random.uniform(-1.0, 1.0, (10, dim))
        self.freqs = np.random.uniform(0.5, 3.0, (10, dim))
        self.phases = np.random.uniform(0, 2*np.pi, (10, dim))

    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Polynomial basin term
        basin_term = np.sum(x**4, axis=1) * 0.01
        
        # Chaotic sinusoidal oscillation term
        chaotic_term = np.zeros(x.shape[0])
        for i in range(10):
            # Apply chaotic combination of sinusoids with random coefficients
            oscillation = np.sum(
                self.coeffs[i] * np.sin(self.freqs[i] * x + self.phases[i]), 
                axis=1
            )
            chaotic_term += np.exp(-0.1 * (i+1)) * np.abs(oscillation)
        
        # Add random perturbations to create irregularity
        perturbation = np.sum(
            np.random.uniform(0.1, 0.5, x.shape) * np.sin(x), 
            axis=1
        )
        
        return basin_term + chaotic_term + 0.1 * perturbation