import numpy as np

class QuantumTensorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Quantum-inspired oscillator parameters
        self.osc_freqs = np.random.uniform(1.0, 4.0, dim)
        self.osc_ampls = np.random.uniform(0.5, 2.0, dim)
        self.osc_phases = np.random.uniform(0.0, 2*np.pi, dim)
        
        # Tensor interaction coefficients
        self.tensor_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim, dim))
        
        # Dynamic penalty parameters
        self.penalty_strengths = np.random.uniform(0.5, 3.0, dim)
        self.penalty_centers = np.random.uniform(-4.0, 4.0, dim)
        self.penalty_widths = np.random.uniform(0.5, 2.0, dim)
        
        # Coupling strength between dimensions
        self.coupling_strengths = np.random.uniform(0.1, 1.0, dim)
        
        # Multi-scale harmonic components
        self.harmonic_orders = np.random.randint(2, 6, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Quantum oscillator components
        for i in range(self.dim):
            oscillator = self.osc_ampls[i] * np.sin(self.osc_freqs[i] * x_norm[i] + self.osc_phases[i])
            f_val += 0.25 * oscillator**4
        
        # Tensor-based interactions
        for i in range(self.dim):
            tensor_sum = 0.0
            for j in range(self.dim):
                for k in range(self.dim):
                    tensor_sum += self.tensor_coeffs[i, j, k] * x_norm[j] * x_norm[k]
            f_val += 0.15 * tensor_sum**2
        
        # Dynamic penalty terms
        for i in range(self.dim):
            penalty = self.penalty_strengths[i] * np.exp(-0.5 * ((x_norm[i] - self.penalty_centers[i]) / self.penalty_widths[i])**2)
            f_val += 0.3 * penalty**2
        
        # Cross-dimensional coupling with tensor structure
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i] * np.sin(x_norm[i] * x_norm[j])
            f_val += 0.2 * coupling_sum**3
        
        # Multi-scale harmonic components
        for i in range(self.dim):
            harmonic_sum = 0.0
            for order in range(1, self.harmonic_orders[i] + 1):
                harmonic_sum += np.sin(order * x_norm[i])
            f_val += 0.1 * harmonic_sum**2
        
        # Global shaping with quartic terms
        f_val += 0.2 * np.sum(x_norm**4)
        
        return f_val