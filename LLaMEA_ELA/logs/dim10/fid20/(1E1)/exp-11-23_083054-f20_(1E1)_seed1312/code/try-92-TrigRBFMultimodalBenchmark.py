import numpy as np

class TrigRBFMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute phase shifts for dynamic modulation
        self.phase_shifts = np.linspace(0, 2*np.pi, dim)
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with dynamic centers
        f1 = 0.0
        for i in range(self.dim):
            center = np.sin(self.phase_shifts[i]) * 0.8
            f1 += np.exp(-10 * (x_norm[i] - center)**2)
        
        # Trigonometric oscillation component with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(self.phase_shifts[i])
            f2 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Polynomial coupling with dynamic exponents
        f3 = 0.0
        for i in range(self.dim):
            exp_factor = 1 + 0.5 * np.cos(self.phase_shifts[i])
            f3 += (x_norm[i]**(2*exp_factor) + 0.5 * x_norm[i]**(4*exp_factor)) * np.sin(2 * x_norm[i])
        
        # Cross-term interactions with dynamic coupling strengths
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.4 * np.sin(self.phase_shifts[i] + self.phase_shifts[j])
                distance = (x_norm[i] - x_norm[j])**2
                f4 += coupling * np.exp(-5 * distance) * np.cos(3 * (x_norm[i] + x_norm[j]))
        
        # Combine components with dynamic weights
        weights = [0.25 + 0.1 * np.sin(self.phase_shifts[i]) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4