import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced quadratic basin term with dimension-dependent scaling
        quadratic_term = 0.3 * np.sum(x_normalized**2) * (1 + 0.1 * self.dim)
        
        # Hybrid chaotic sinusoidal components with multi-exponential decay
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 15 * (1.7 ** i)
            decay = np.exp(-0.3 * i) * np.exp(-0.05 * i**2)
            chaotic_term += np.sin(freq * x_normalized[i]) * decay * (1 + 0.3 * np.sin(3 * x_normalized[i]))
        
        # Dynamic cross-dimensional interactions with variable coupling and phase shifts
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 * (1 - np.exp(-0.2 * (i + j))) * np.sin(0.5 * np.pi * (i / self.dim))
                phase_shift = np.cos(2 * np.pi * x_normalized[i]) * np.sin(2 * np.pi * x_normalized[j])
                cross_term += coupling * np.sin(10 * np.pi * x_normalized[i]) * np.cos(8 * np.pi * x_normalized[j]) * phase_shift
        
        # Dynamic global minimum shift with dimension-dependent magnitude and chaotic modulation
        shift = 0.4 * (self.dim / 15.0) * np.sin(0.2 * self.dim)
        shift_term = 0.9 * np.sum((x_normalized - shift)**4) + 0.1 * np.sum(np.abs(x_normalized - shift))
        
        # Add a global noise component to increase landscape complexity
        noise = 0.05 * np.random.rand()
        
        return quadratic_term + chaotic_term + cross_term + shift_term + noise