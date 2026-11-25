import numpy as np

class RidgeGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic ridge component with varying frequencies
        ridge = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            ridge += np.sin(freq * x[i]) * np.cos(freq * x[i]) * (x[i]**2 + 1.0)
        
        # Gaussian peaks with varying heights and widths
        gaussian = 0
        peak_positions = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            pos = peak_positions[i]
            height = 2.0 + 1.5 * np.sin(i * 0.5)
            width = 0.5 + 0.3 * np.cos(i * 0.4)
            gaussian += height * np.exp(-0.5 * ((x[i % self.dim] - pos) / width)**2)
        
        # Cross-dimensional correlation component
        correlation = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.3 + 0.2 * np.sin(0.2 * (i + j))
                correlation += weight * x[i] * x[j] * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Asymmetric saddle with variable conditioning
        saddle = 0
        for i in range(self.dim):
            condition = 1.0 + 0.4 * np.sin(i * 0.6)
            saddle += (x[i] - 1.0)**2 * (x[i] + 1.0)**4 * condition
        
        # Multi-scale oscillation with dynamic phase shifts
        oscillation = 0
        scales = [0.2, 0.5, 1.0, 2.0]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            phase_shift = 0.1 * np.sin(i * 0.3)
            oscillation += np.sin(scale * x[i] + phase_shift) * np.cos(1.5 * scale * x[i] + phase_shift)
        
        # Symmetry-breaking term
        symmetry_break = 0
        for i in range(self.dim):
            symmetry_break += (x[i]**3 - 0.5 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Combine all components with carefully tuned weights
        return (ridge * 0.3 +
                gaussian * 0.4 +
                correlation * 0.25 +
                saddle * 0.35 +
                oscillation * 0.2 +
                symmetry_break * 0.15)