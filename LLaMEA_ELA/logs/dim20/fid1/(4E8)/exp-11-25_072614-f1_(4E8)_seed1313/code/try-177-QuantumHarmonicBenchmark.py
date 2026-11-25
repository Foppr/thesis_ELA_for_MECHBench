import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator potential terms
        quantum_term = np.sum((x**2 + 1.0) * np.cos(2.0 * x) * np.exp(-0.1 * x**2)) / self.dim
        
        # Radial basis function with dynamic width and adaptive scaling
        rbf_term = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = (x[i] - x[j])**2
                width = 0.5 + 0.3 * np.abs(x[j])  # Adaptive width based on coordinate value
                rbf_sum += np.exp(-distance / (2.0 * width**2))
            rbf_term += rbf_sum
        rbf_term /= self.dim
        
        # Dynamic phase-coupled sine interactions with time-varying coupling strength
        phase_term = 0.0
        for i in range(self.dim):
            coupling_strength = 1.0 + 0.5 * np.sin(0.3 * x[i])
            phase_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_sum += np.sin(coupling_strength * (x[i] - x[j]))
            phase_term += phase_sum**2
        phase_term /= self.dim
        
        # Adaptive conditioning with exponential scaling factor
        cond_factor = 1.0 + 0.8 * np.mean(np.abs(x))  # Increased conditioning effect
        adaptive_term = np.sum((x**3) * np.sin(0.5 * x) * cond_factor) / (self.dim * 2.0)
        
        # Multi-scale fractal-like cosine interactions with varying frequencies
        fractal_term = 0.0
        for i in range(self.dim):
            freq_sum = 0.0
            for k in range(1, 6):  # Up to 5 frequency scales
                freq_sum += np.cos(k * np.pi * x[i]) / (k**1.5)
            fractal_term += freq_sum**2
        fractal_term /= self.dim
        
        # Asymmetric polynomial distortion with cross-dimensional interactions
        poly_term = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                poly_sum += (x[i] - x[j])**4 * np.sin(x[i] + x[j])
            poly_term += x[i]**5 + 2.0 * x[i]**3 + 0.5 * x[i] + poly_sum
        poly_term /= self.dim
        
        # Combined weighted sum of all terms
        total = 0.21 * quantum_term + 0.18 * rbf_term + 0.19 * phase_term + 0.16 * adaptive_term + 0.15 * fractal_term + 0.11 * poly_term
        
        return total