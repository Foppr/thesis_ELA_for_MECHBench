import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = min(5, dim)
        self.barrier_strength = 3.0
        self.quantum_phase_shift = np.pi / 4
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Fractal component with self-similar patterns
        for i in range(self.fractal_depth):
            scale = 2.0**(i + 1)
            f_val += 0.5 * np.sin(scale * x[i % self.dim]) * np.cos(scale * x[i % self.dim])
        
        # Logarithmic barrier regions
        for i in range(self.dim):
            barrier = 0.0
            for j in range(1, 6):
                barrier += np.log(np.abs(x[i] - (2.5 + 0.5 * np.sin(j))) + 0.1)
            f_val += self.barrier_strength * barrier
        
        # Quantum phase interference pattern
        quantum_sum = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                phase_diff = x[i] - x[j]
                quantum_sum += np.sin(phase_diff * 2.0 + self.quantum_phase_shift) * np.cos(phase_diff * 3.0)
        f_val += 0.8 * quantum_sum
        
        # Multi-scale Gaussian peaks with varying heights and widths
        peak_centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i, center in enumerate(peak_centers):
            width = 0.5 + 0.3 * np.sin(i)
            height = 1.5 + 0.5 * np.cos(i)
            f_val += height * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
        
        # Asymmetric exponential potentials
        for i in range(self.dim):
            if x[i] < 0:
                f_val += 1.2 * np.exp(-0.3 * x[i]) * np.sin(0.7 * x[i])
            else:
                f_val += 1.2 * np.exp(-0.5 * x[i]) * np.cos(0.7 * x[i])
        
        # Hyperbolic tangent modulation
        for i in range(self.dim):
            f_val += 0.4 * np.tanh(3.0 * x[i]) * np.sin(0.5 * x[i]**2)
        
        return f_val