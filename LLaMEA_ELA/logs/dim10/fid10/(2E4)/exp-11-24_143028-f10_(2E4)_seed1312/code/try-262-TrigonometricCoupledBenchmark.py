import numpy as np

class TrigonometricCoupledBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for trigonometric components
        self.frequencies = np.random.uniform(1.0, 15.0, dim)
        self.phase_shifts = np.random.uniform(0.0, 2 * np.pi, dim)
        self.amplitudes = np.random.uniform(0.5, 4.0, dim)
        self.coupling_coeffs = np.random.uniform(0.1, 3.0, (dim, dim))
        self.harmonic_orders = np.random.randint(2, 8, dim)
        # Add chaotic modulation parameter
        self.chaos_params = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base trigonometric terms with varying frequencies and phases
        base_terms = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i]
            phase = self.phase_shifts[i]
            amp = self.amplitudes[i]
            order = self.harmonic_orders[i]
            
            # Construct complex trigonometric combinations with chaotic modulation
            chaotic_mod = 1.0 + self.chaos_params[i] * np.sin(2.0 * x[i])
            term = amp * np.sin(freq * x[i] + phase) * chaotic_mod + \
                   0.5 * np.cos(freq * x[i] + phase) * chaotic_mod + \
                   0.3 * np.sin(order * freq * x[i] + phase) * chaotic_mod
            base_terms += term**2
        
        # Adaptive coupling between dimensions with time-varying interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Time-varying coupling coefficient based on dimension values
                    coeff = self.coupling_coeffs[i, j] * (1.0 + 0.5 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[j]))
                    coupling_term += coeff * np.sin(0.5 * (x[i] + x[j])) * \
                                    np.cos(0.3 * (x[i] - x[j]))
        
        # Add periodic penalty terms to increase multimodality with adaptive scaling
        penalty_term = 0.0
        for i in range(self.dim):
            # Multiple periodic penalties with different periods and adaptive weights
            penalty_term += 2.5 * np.sin(3.0 * x[i]) + \
                           1.8 * np.cos(4.0 * x[i]) + \
                           1.0 * np.sin(7.0 * x[i]) + \
                           0.5 * np.cos(9.0 * x[i])
        
        # Add a global scaling factor and combine terms
        result = 0.6 * base_terms + 0.25 * coupling_term + 0.15 * penalty_term
        
        return result