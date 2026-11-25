import numpy as np

class MultiModalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base conditioning term with dimensionally scaled quadratic
        f1 = np.sum(x_norm**2) * (1.0 + 0.1 * self.dim)
        
        # Multi-modal harmonic potentials with exponentially decaying amplitudes
        f2 = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)
            amp = np.exp(-0.1 * i)
            f2 += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Logarithmic barrier terms near boundaries
        f3 = 0.0
        for i in range(self.dim):
            if np.abs(x_norm[i]) > 0.8:
                f3 += 10.0 * np.log(1.0 / (1.0 - np.abs(x_norm[i])))
        
        # Cross-dimensional coupling with varying interaction strengths
        f4 = 0.0
        for i in range(self.dim - 1):
            strength = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            f4 += strength * np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[i+1])
        
        # Asymmetric exponential potentials with random phase shifts
        f5 = 0.0
        for i in range(self.dim):
            phase = np.random.random() * np.pi
            f5 += np.exp(-np.abs(x_norm[i]) ** 1.3) * np.sin(3 * x_norm[i] + phase)
        
        # Dimensionally dependent conditioning with scaling factor
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combined chaotic interaction term with varying weights
        f6 = 0.0
        for i in range(self.dim):
            weight = 0.3 + 0.7 * np.sin(i * np.pi / self.dim)
            f6 += weight * np.tanh(x_norm[i] ** 2.5) * np.exp(-x_norm[i]**2)
        
        # Add noise and scale final result
        noise = 0.005 * np.random.random()
        
        return condition_factor * (0.3 * f1 + 1.2 * f2 + 0.8 * f3 + 0.6 * f4 + 0.9 * f5 + 0.7 * f6) + noise