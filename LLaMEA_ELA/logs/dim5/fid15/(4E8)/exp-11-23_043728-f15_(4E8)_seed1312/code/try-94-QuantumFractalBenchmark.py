import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_exponent = 1.8
        self.quantum_coeff = 0.7
        self.coupling_strength = 0.3
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Quantum interference pattern using sine and cosine waves
        quantum_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            freq = 2 ** (i % 5) * self.quantum_coeff
            quantum_pattern[i] = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Fractal energy distribution using fractional Brownian motion approximation
        fractal_energy = np.zeros(self.dim)
        for i in range(self.dim):
            scale = 2 ** (i % 3)
            freq = 1.5 * scale
            fractal_energy[i] = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5) * (1 + 0.3 * np.sin(3 * x_norm[i]))
        
        # Combine quantum and fractal patterns
        combined_pattern = quantum_pattern + 0.6 * fractal_energy
        
        # Add dynamic coupling between dimensions with time-like progression
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += self.coupling_strength * (x_norm[i] - x_norm[i+1])**2 * np.sin(0.5 * (i + 1) * np.pi)
        
        # Create complex curvature with polynomial and exponential terms
        curvature = np.sum(combined_pattern**3) + 0.2 * np.sum(np.exp(np.abs(combined_pattern)) - 1)
        
        # Add non-smooth features for increased difficulty
        nonsmooth = 0.15 * np.sum(np.abs(x_norm)**1.3)
        
        # Introduce dimensionality-dependent penalty
        penalty = 0.02 * self.dim * np.mean(np.abs(x_norm))
        
        # Adaptive scaling factor
        scale_factor = 1.0 + 0.005 * np.log(self.dim + 1)
        
        return scale_factor * (curvature + coupling_term + nonsmooth + penalty)