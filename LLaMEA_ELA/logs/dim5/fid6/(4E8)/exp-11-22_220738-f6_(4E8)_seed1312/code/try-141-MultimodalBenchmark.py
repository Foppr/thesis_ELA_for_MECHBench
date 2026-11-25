import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = min(6, dim)
        self.barrier_strength = 3.5
        self.quantum_phase_shift = np.pi / 3
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Fractal component with self-similar patterns
        for i in range(self.fractal_depth):
            scale = 2.5**(i + 1)
            f_val += 0.6 * np.sin(scale * x[i % self.dim]) * np.cos(scale * x[i % self.dim])
        
        # Logarithmic barrier regions
        for i in range(self.dim):
            barrier = 0.0
            for j in range(1, 7):
                barrier += np.log(np.abs(x[i] - (2.0 + 0.6 * np.sin(j))) + 0.15)
            f_val += self.barrier_strength * barrier
        
        # Quantum phase interference pattern
        quantum_sum = 0.0
        for i in range(self.dim):
            for j in range(i + 1, min(i + 4, self.dim)):
                phase_diff = x[i] - x[j]
                quantum_sum += np.sin(phase_diff * 2.5 + self.quantum_phase_shift) * np.cos(phase_diff * 3.5)
        f_val += 0.9 * quantum_sum
        
        # Multi-scale Gaussian peaks with varying heights and widths
        peak_centers = np.linspace(-4.0, 4.0, min(8, self.dim))
        for i, center in enumerate(peak_centers):
            width = 0.6 + 0.2 * np.sin(i * 0.5)
            height = 1.8 + 0.3 * np.cos(i * 0.5)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Asymmetric exponential potentials
        for i in range(self.dim):
            if x[i] < 0:
                f_val += 1.3 * np.exp(-0.35 * x[i]) * np.sin(0.75 * x[i])
            else:
                f_val += 1.1 * np.exp(-0.45 * x[i]) * np.cos(0.65 * x[i])
        
        # Hyperbolic tangent modulation
        for i in range(self.dim):
            f_val += 0.35 * np.tanh(2.5 * x[i]) * np.sin(0.4 * x[i]**2)
        
        return f_val