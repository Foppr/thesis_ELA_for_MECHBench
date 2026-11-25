import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired oscillatory component with adaptive frequencies and amplitude modulation
        quantum_osc = 0
        for i in range(self.dim):
            freq = (i + 1) * np.pi / (self.dim + 1)
            amp_mod = 1 + 0.3 * np.sin(i * np.pi / 3) * np.cos(i * np.pi / 5)
            quantum_osc += amp_mod * np.sin(x[i] * freq) * np.cos(x[i] * freq * np.e) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive polynomial potential with dynamic exponents and shifting centers
        poly_pot = 0
        for i in range(self.dim):
            exponent = 2 + 0.5 * np.sin(i * np.pi / 4)
            center = 1.5 * np.sin(i * np.pi / 6) + 1.5 * np.cos(i * np.pi / 6)
            poly_pot += (x[i] - center)**exponent * (1 + 0.2 * np.sin(i * np.pi / 2))
        
        # Saddle-point landscape with dynamic curvature and directional bias
        saddle = 0
        for i in range(self.dim):
            curvature = 0.5 + 0.3 * np.sin(i * np.pi / 8)
            direction = np.cos(i * np.pi / 4) if i % 2 == 0 else np.sin(i * np.pi / 4)
            saddle += curvature * x[i]**2 * direction + 0.1 * x[i]**4
        
        # Dynamic weighting based on dimensionality and spatial correlation
        weight1 = 0.7 + 0.1 * np.sin(self.dim * np.pi / 10)
        weight2 = 0.3 + 0.2 * np.cos(self.dim * np.pi / 8)
        weight3 = 0.2 + 0.15 * np.sin(self.dim * np.pi / 6)
        
        # Combine components with global scaling and noise injection
        result = weight1 * quantum_osc + weight2 * poly_pot + weight3 * saddle
        
        # Add a global shift term and dimensionality-dependent offset
        global_shift = 2.0 * self.dim + 0.5 * np.sum(np.sin(x * np.pi / 4))
        result += global_shift
        
        # Add controlled noise to increase complexity
        noise = 0.01 * np.sum(np.random.randn(self.dim) * np.abs(x))
        
        return result + noise