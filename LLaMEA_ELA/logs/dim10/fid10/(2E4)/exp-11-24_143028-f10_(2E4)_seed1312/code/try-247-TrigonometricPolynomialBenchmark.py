import numpy as np

class TrigonometricPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive frequency parameters
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize coupling coefficients
        self.coupling_strength = np.random.uniform(0.1, 1.0, dim)
        # Initialize hierarchical penalty parameters
        self.penalty_levels = [np.random.uniform(1.0, 5.0) for _ in range(3)]
        self.penalty_weights = np.random.uniform(0.5, 2.0, 3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric polynomial component
        trig_term = 0.0
        for i in range(self.dim):
            # Evaluate trigonometric polynomial with multiple harmonics
            harmonic_sum = 0.0
            for j in range(1, 4):  # up to 3rd harmonic
                freq = self.frequencies[i] * j
                amp = self.amplitudes[i] / j  # decay with frequency
                phase = self.phase_shifts[i]
                harmonic_sum += amp * np.sin(freq * x[i] + phase)
            trig_term += harmonic_sum**2
            
        # Cross-dimensional coupling term
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling based on trigonometric interaction
                coupling = np.sin(self.coupling_strength[i] * x[i]) * np.cos(self.coupling_strength[j] * x[j])
                coupling_term += coupling * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Hierarchical penalty landscape
        penalty_term = 0.0
        for i in range(self.dim):
            penalty = 0.0
            for level, (weight, exponent) in enumerate(zip(self.penalty_weights, self.penalty_levels)):
                scale = 2**level
                scaled_x = x[i] / scale
                penalty += weight * (np.abs(scaled_x)**exponent) * np.exp(-0.02 * scaled_x**2)
            penalty_term += penalty
            
        # Adaptive scaling based on dimensionality
        adaptive_scale = np.sqrt(self.dim) + 1.0
        
        # Combine all components with dynamic weights
        result = adaptive_scale * trig_term + 0.3 * coupling_term + 0.7 * penalty_term
        
        return result