import numpy as np

class QuantumRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Quantum-inspired oscillator parameters
        self.oscillator_frequencies = np.random.uniform(0.5, 8.0, dim)
        self.oscillator_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.oscillator_phases = np.random.uniform(0, 2*np.pi, dim)
        
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (dim, 10))
        self.rbf_weights = np.random.uniform(-2.0, 2.0, (dim, 10))
        
        # Adaptive noise scaling
        self.noise_amplitudes = np.random.uniform(0.1, 1.5, dim)
        self.noise_frequencies = np.random.uniform(1.0, 10.0, dim)
        
        # Cross-dimensional interaction parameters
        self.cross_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.cross_exponents = np.random.uniform(1.0, 4.0, (dim, dim))
        
        # Polynomial shaping parameters
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coefficients = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Quantum-inspired oscillator components
        for i in range(self.dim):
            oscillator_val = self.oscillator_amplitudes[i] * np.sin(
                self.oscillator_frequencies[i] * x_norm[i] + self.oscillator_phases[i]
            )
            f_val += 0.2 * oscillator_val**2
        
        # Radial basis function couplings
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(10):
                rbf_val = np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2)
                rbf_sum += self.rbf_weights[i, j] * rbf_val
            f_val += 0.3 * rbf_sum**2
        
        # Adaptive noise components
        for i in range(self.dim):
            noise_val = self.noise_amplitudes[i] * np.sin(
                self.noise_frequencies[i] * x_norm[i]
            )
            f_val += 0.15 * noise_val**2
        
        # Cross-dimensional interactions with polynomial coupling
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling = self.cross_weights[i, j] * np.abs(x_norm[i] - x_norm[j])**self.cross_exponents[i, j]
                    cross_sum += coupling
            f_val += 0.25 * cross_sum**2
        
        # Polynomial shaping for conditioning
        for i in range(self.dim):
            poly_val = self.poly_coefficients[i] * (x_norm[i]**self.poly_degrees[i])
            f_val += 0.1 * poly_val**2
        
        # Multi-scale harmonic components with varying amplitudes
        for scale in [0.1, 0.3, 0.7, 1.0]:
            harmonic_sum = 0.0
            for i in range(self.dim):
                harmonic_sum += np.sin(scale * 2 * np.pi * x_norm[i]) * np.cos(scale * 3 * np.pi * x_norm[i])
            f_val += 0.2 * harmonic_sum**2
        
        # Basin boundary irregularity with piecewise nonlinearity
        for i in range(self.dim):
            if x_norm[i] < -0.3:
                f_val += 0.5 * np.exp(-x_norm[i]**2)
            elif x_norm[i] > 0.3:
                f_val += 0.5 * np.exp(-(x_norm[i] - 1.0)**2)
            else:
                f_val += 0.2 * (x_norm[i]**6)  # Higher-order nonlinearity
        
        return f_val