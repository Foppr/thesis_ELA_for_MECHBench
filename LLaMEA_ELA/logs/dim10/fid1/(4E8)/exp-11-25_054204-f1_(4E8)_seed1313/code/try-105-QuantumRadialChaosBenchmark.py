import numpy as np

class QuantumRadialChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.uniform(0.5, 2.0, dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        # Chaos parameters for temporal dynamics
        self.chaos_a = np.random.uniform(3.5, 4.0, dim)
        self.chaos_b = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator potential
        quantum_potential = 0.0
        for i in range(self.dim):
            quantum_potential += 0.5 * self.omega[i]**2 * x[i]**2
        
        # Radial basis function components
        rbf_sum = 0.0
        for i in range(self.dim):
            rbf_term = 0.0
            for j in range(self.dim):
                diff = x[j] - self.rbf_centers[i, j]
                rbf_term += np.exp(-0.5 * (diff / self.rbf_widths[i])**2)
            rbf_sum += rbf_term
        
        # Temporal chaos component with logistic map dynamics
        chaos_component = 0.0
        for i in range(self.dim):
            if i == 0:
                chaos_val = x[i]
            else:
                chaos_val = self.chaos_a[i-1] * x[i-1] * (1 - x[i-1]) + self.chaos_b[i-1]
            chaos_component += chaos_val * np.sin(x[i])
        
        # Mixed polynomial and trigonometric terms with varying exponents
        mixed_terms = 0.0
        for i in range(self.dim):
            if i % 4 == 0:
                mixed_terms += x[i]**3 * np.cos(x[i])
            elif i % 4 == 1:
                mixed_terms += x[i]**4 * np.sin(x[i])
            elif i % 4 == 2:
                mixed_terms += x[i]**2.5 * np.tan(x[i] / 2.0)
            else:
                mixed_terms += x[i]**3.5 * np.exp(-x[i]**2)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross_coupling += np.exp(-dist) * np.sin(x[i] + x[j])
        
        # Global conditioning factor based on dimensionality
        condition_factor = 1.0 + 0.1 * (self.dim - 1)
        
        # Combine all components with adaptive weighting
        result = condition_factor * (quantum_potential + rbf_sum + chaos_component + mixed_terms + cross_coupling)
        
        return result