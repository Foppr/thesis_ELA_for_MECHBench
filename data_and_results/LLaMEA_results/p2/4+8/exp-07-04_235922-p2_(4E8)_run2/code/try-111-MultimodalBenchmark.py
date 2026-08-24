import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar components with multiple scales
        fractal_term = 0.0
        for i in range(1, 6):
            scale = 2 ** i
            fractal_term += 0.2 / scale * np.sum(np.sin(scale * x) * np.cos(scale * x / 2) * np.exp(-0.05 * np.abs(x)))
        
        # Quantum-like interference patterns
        quantum_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                quantum_term += 0.1 * np.sin(10 * distance) * np.cos(5 * distance) * np.exp(-0.1 * distance**2)
        
        # Dynamic saddle-point landscape
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.3 * (x[i]**4 - 6 * x[i]**2 + 9) * np.sin(2 * x[i])
        
        # Multi-scale sinusoidal coupling with varying amplitudes
        coupling_term = 0.0
        for k in range(1, 4):
            coupling_term += 0.15 * np.sum(np.sin(k * x) * np.cos(k * x / 3) * np.exp(-0.02 * np.abs(x)**(1.5 + k/2)))
        
        # Adaptive exponential decay with periodic modulation
        decay_term = 0.0
        for i in range(self.dim):
            decay_term += 0.25 * np.exp(-0.5 * (x[i] - np.sin(0.5 * x[i]))**2) * np.cos(15 * x[i])
        
        # Add a complex interaction between all dimensions
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += 0.05 * np.sin(3 * (x[i] - x[j])) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Combine all terms
        result = fractal_term + quantum_term + saddle_term + coupling_term + decay_term + interaction_term
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result