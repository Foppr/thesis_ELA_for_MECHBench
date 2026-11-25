import numpy as np

class NeuralBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential barrier terms to create rugged landscape
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(-10 * np.abs(x_normalized[i])) * (1 + np.sin(5 * x_normalized[i])**2)
        
        # Sinusoidal coupling between variables with adaptive frequency
        coupling = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * 0.5)
            coupling += np.sin(freq * x_normalized[i])
            for j in range(i+1, self.dim):
                coupling += np.sin(freq * (x_normalized[i] + x_normalized[j])) * np.cos(2 * (x_normalized[i] - x_normalized[j]))
        
        # Adaptive conditioning based on position
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 4.0 * (1.0 / (1.0 + np.exp(-x_normalized[i])))
            conditioning += cond_factor * x_normalized[i]**2 * np.cos(3 * x_normalized[i])
        
        # Multi-modal component with Gaussian peaks
        modal = 0.0
        centers = np.linspace(-1, 1, 5)
        for c in centers:
            peak_val = 0.0
            for i in range(self.dim):
                peak_val += (x_normalized[i] - c)**2
            modal += np.exp(-peak_val * 2.0) * np.cos(4 * peak_val)
        
        # Fractal-like self-similarity through recursive sine composition
        fractal = 0.0
        for i in range(self.dim):
            val = x_normalized[i]
            for _ in range(3):
                val = np.sin(val * 5)
            fractal += val**2
        
        # Combined fitness with dynamic weights
        return (0.25 * barrier + 0.3 * coupling + 0.2 * conditioning + 
                0.15 * modal + 0.1 * fractal)