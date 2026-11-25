import numpy as np

class TrigonometricCoupledBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for trigonometric components
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.phase_shifts = np.random.uniform(0.0, 2 * np.pi, dim)
        self.amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.coupling_coeffs = np.random.uniform(0.1, 2.0, (dim, dim))
        self.harmonic_orders = np.random.randint(2, 6, dim)
        
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
            
            # Construct complex trigonometric combinations
            term = amp * np.sin(freq * x[i] + phase) + \
                   0.5 * np.cos(freq * x[i] + phase) + \
                   0.3 * np.sin(order * freq * x[i] + phase)
            base_terms += term**2
        
        # Coupling between dimensions with varying interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coeff = self.coupling_coeffs[i, j]
                    coupling_term += coeff * np.sin(0.5 * (x[i] + x[j])) * \
                                    np.cos(0.3 * (x[i] - x[j]))
        
        # Add periodic penalty terms to increase multimodality
        penalty_term = 0.0
        for i in range(self.dim):
            # Multiple periodic penalties with different periods
            penalty_term += 2.0 * np.sin(3.0 * x[i]) + \
                           1.5 * np.cos(4.0 * x[i]) + \
                           0.8 * np.sin(7.0 * x[i])
        
        # Add a global scaling factor and combine terms
        result = 0.5 * base_terms + 0.3 * coupling_term + 0.2 * penalty_term
        
        return result