import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with condition number scaling
        base = np.sum(x_norm**2)
        
        # Chaotic sine wave component with dynamic frequency modulation
        chaotic = 0.0
        for i in range(self.dim):
            freq = 10 * (1 + 0.5 * np.sin(i * 0.5))
            chaotic += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Multi-scale Gaussian peaks with varying amplitudes and widths
        peaks = 0.0
        scales = [0.5, 1.0, 1.5, 2.0]
        for i in range(self.dim):
            for s in scales:
                peaks += 2.0 * np.exp(-0.5 * ((x_norm[i] - s) / 0.3)**2) + 1.5 * np.exp(-0.5 * ((x_norm[i] + s) / 0.3)**2)
        
        # Adaptive penalty based on distance from center with dynamic scaling
        penalty = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i])
            penalty += 5.0 * (dist**4 - 2 * dist**2 + 1) * np.exp(-0.3 * dist**2)
        
        # Cross-dimensional interaction with variable coupling strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling += 0.3 * np.sin(20 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(15 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Dynamic exponential interaction with adaptive decay
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                exp_interaction += 0.2 * np.exp(-5.0 * dist) * np.sin(30 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric oscillatory component with phase shift
        asym_osc = 0.0
        for i in range(self.dim):
            asym_osc += 0.4 * np.sin(25 * np.pi * x_norm[i]) * np.cos(20 * np.pi * x_norm[i]) * (1 + 0.3 * np.sin(i * 0.7))
        
        # Adaptive basin complexity with varying depth
        basin = 0.0
        for i in range(self.dim):
            basin += 0.25 * (x_norm[i]**6 - 3 * x_norm[i]**4 + 3 * x_norm[i]**2 - 1)**2
        
        # Final combined function with dimensionality-dependent scaling
        total = base + 0.5 * chaotic + 0.3 * peaks + 0.4 * penalty + 0.2 * coupling + 0.3 * exp_interaction + 0.3 * asym_osc + 0.2 * basin
        
        return total