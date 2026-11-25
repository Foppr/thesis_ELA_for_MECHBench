import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term with nonlinearity
        radial = np.sum(x**2) * 0.01 + 0.001 * np.sum(x**4)
        
        # Nested sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(7.0 * x[i]) * np.cos(5.0 * x[i]) + 
                        0.5 * np.sin(12.0 * x[i]) * np.cos(8.0 * x[i]))
        
        # Enhanced cross-term interactions with distance-dependent weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                weight = 1.0 / (1.0 + dist**2)
                cross_term += x[i] * x[j] * weight
        
        # Chaotic component with exponential decay and multi-scale behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15.0 * x[i]) * np.cos(11.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Additional harmonic term to increase landscape complexity
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += np.sin(3.0 * x[i])**3 + np.cos(4.0 * x[i])**2
        
        # Combine all terms with optimized weights
        result = radial + 0.6 * sin_term + 0.4 * cross_term + 0.3 * chaotic + 0.2 * harmonic
        
        # Add structured noise to increase robustness to local optima
        noise = 0.005 * np.sum(np.sin(x * 15.0) * np.cos(x * 7.0))
        
        return result + noise