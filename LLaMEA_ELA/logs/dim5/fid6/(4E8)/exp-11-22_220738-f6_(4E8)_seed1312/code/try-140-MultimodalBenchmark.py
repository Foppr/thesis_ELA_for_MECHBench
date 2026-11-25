import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = min(6, dim)
        self.phase_coupling_strength = 2.0
        self.noise_resilience_factor = 0.8
        self.adaptive_scaling = np.linspace(1.0, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Hyperchaotic fractal component with adaptive scaling
        for i in range(self.fractal_depth):
            scale = self.adaptive_scaling[i % self.dim]
            f_val += 0.3 * np.sin(scale * x[i % self.dim]) * np.cos(scale * x[i % self.dim])
            f_val += 0.2 * np.tanh(scale * x[i % self.dim]) * np.sin(scale * x[i % self.dim]**2)
        
        # Dynamic phase coupling with time-varying parameters
        for i in range(self.dim):
            phase_sum = 0.0
            for j in range(i + 1, min(i + 4, self.dim)):
                phase_diff = x[i] - x[j]
                phase_sum += np.sin(phase_diff * (j - i + 1)) * np.cos(phase_diff * (j - i + 2))
            f_val += self.phase_coupling_strength * phase_sum
        
        # Enhanced logarithmic barrier regions with dynamic spacing
        for i in range(self.dim):
            barrier = 0.0
            for j in range(1, 8):
                center = 2.5 + 0.5 * np.sin(j * 0.7)
                barrier += np.log(np.abs(x[i] - center) + 0.05)
            f_val += 2.5 * barrier
        
        # Multi-scale Gaussian peaks with dynamic widths and heights
        peak_centers = np.linspace(-4.8, 4.8, min(9, self.dim))
        for i, center in enumerate(peak_centers):
            width = 0.3 + 0.4 * np.sin(i * 0.5)
            height = 1.2 + 0.8 * np.cos(i * 0.3)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Asymmetric exponential potentials with adaptive parameters
        for i in range(self.dim):
            if x[i] < 0:
                f_val += 1.5 * np.exp(-0.4 * x[i]) * np.sin(0.8 * x[i])
            else:
                f_val += 1.5 * np.exp(-0.6 * x[i]) * np.cos(0.8 * x[i])
        
        # Hyperbolic tangent modulation with dynamic frequency
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)
            f_val += 0.3 * np.tanh(2.5 * x[i]) * np.sin(freq * x[i]**2)
        
        # Cross-dimensional interference with adaptive weights
        weight_sum = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                weight = 0.5 + 0.3 * np.cos(i + j)
                diff = x[i] - x[j]
                weight_sum += weight * np.sin(diff * 4.0) * np.cos(diff * 3.0)
        f_val += 0.6 * weight_sum
        
        # Add noise resilience component
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += 0.1 * np.sin(x[i] * 10.0) * np.cos(x[i] * 7.0)
        f_val += self.noise_resilience_factor * noise_component
        
        return f_val