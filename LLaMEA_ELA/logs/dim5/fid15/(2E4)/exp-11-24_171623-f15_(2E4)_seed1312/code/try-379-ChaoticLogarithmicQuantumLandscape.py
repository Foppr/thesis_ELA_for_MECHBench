import numpy as np

class ChaoticLogarithmicQuantumLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic logarithmic barrier parameters
        self.barrier_centers = -2.0 + 4.0 * np.random.rand(dim)
        self.barrier_strengths = 1.0 + 3.0 * np.random.rand(dim)
        self.barrier_widths = 0.2 + 1.8 * np.random.rand(dim)
        # Polynomial coupling coefficients with varying degrees
        self.poly_coupling_coeffs = 0.5 + 2.5 * np.random.rand(dim, dim)
        self.poly_coupling_degrees = 2 + 4 * np.random.randint(1, 5, (dim, dim))
        # Quantum-inspired oscillatory components
        self.oscillation_amplitudes = 1.5 + 3.5 * np.random.rand(dim)
        self.oscillation_frequencies = 2.0 + 8.0 * np.random.rand(dim)
        self.oscillation_phases = 2.0 * np.pi * np.random.rand(dim)
        # Asymmetric exponential terms
        self.exp_exponents = 1.0 + 4.0 * np.random.rand(dim)
        self.exp_coefficients = 0.5 + 2.0 * np.random.rand(dim)
        # Global conditioning parameters
        self.conditioning_factors = 0.5 + 2.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logarithmic barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i] - self.barrier_centers[i])
            if dist < self.barrier_widths[i]:
                barrier_sum += self.barrier_strengths[i] * np.log(1.0 + dist / (self.barrier_widths[i] * 0.5))
        
        # Polynomial coupling component
        poly_coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_coupling_sum += self.poly_coupling_coeffs[i, j] * (x_norm[i]**self.poly_coupling_degrees[i, j]) * (x_norm[j]**2)
        
        # Quantum-inspired oscillatory component
        quantum_sum = 0.0
        for i in range(self.dim):
            quantum_sum += self.oscillation_amplitudes[i] * np.sin(self.oscillation_frequencies[i] * x_norm[i] + self.oscillation_phases[i]) * np.cos(x_norm[i])
        
        # Asymmetric exponential component
        exp_sum = 0.0
        for i in range(self.dim):
            exp_sum += self.exp_coefficients[i] * np.exp(-self.exp_exponents[i] * np.abs(x_norm[i]))
        
        # Global conditioning and scaling
        conditioning_sum = 0.0
        for i in range(self.dim):
            conditioning_sum += self.conditioning_factors[i] * x_norm[i]**2
        
        # Combine all components with varying weights
        result = 0.25 * barrier_sum + 0.30 * poly_coupling_sum + 0.20 * quantum_sum + 0.15 * exp_sum + 0.10 * conditioning_sum
        
        # Add high-order polynomial penalty term
        penalty = 0.10 * np.sum(np.abs(x_norm)**6)
        
        return result + penalty