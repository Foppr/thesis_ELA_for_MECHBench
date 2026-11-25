import numpy as np

class QuantumInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired interference terms with complex amplitude modulation
        quantum_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                quantum_term += np.sin(distance * np.pi) * np.cos(distance * np.pi) * np.exp(-0.1 * distance**2)
        quantum_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Radial basis function with adaptive width and height
        rbfs = 0.0
        for i in range(self.dim):
            rbfs += np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i] + 2.0)**2) / 1.5**2)
        rbfs /= self.dim
        
        # Dynamic dimension coupling with frequency modulation
        coupling_term = 0.0
        for i in range(self.dim):
            coupling_term += np.sin(2.0 * x[i]) * np.cos(0.5 * x[i]) * (1.0 + 0.3 * np.sin(0.7 * x[i]))
        coupling_term /= self.dim
        
        # Asymmetric polynomial distortion with varying exponents (modified)
        poly_term = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                poly_term += 1.0 * x[i]**3 - 1.8 * x[i]**2 + 0.9 * x[i]  # Modified exponents and coefficients
            else:
                poly_term += 1.5 * x[i]**3 + 1.1 * x[i]**2 - 0.7 * x[i]
        poly_term /= self.dim
        
        # Multi-scale sinusoidal modulation with varying frequencies
        mod_term = 0.0
        for i in range(self.dim):
            mod_term += np.sin(3.0 * x[i]) * np.cos(1.5 * x[i]) * np.sin(0.5 * x[i])
        mod_term /= self.dim
        
        # Fractal-like self-similarity with recursive scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(x[i] * np.pi / 2.0) * np.cos(x[i] * np.pi / 4.0)
        fractal_term /= self.dim
        
        # Cross-dimensional interaction with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.2 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with carefully tuned weights (slightly modified)
        total = 0.20 * quantum_term + 0.20 * rbfs + 0.16 * coupling_term + 0.15 * poly_term + 0.12 * mod_term + 0.11 * fractal_term + 0.16 * cross_term
        
        return total