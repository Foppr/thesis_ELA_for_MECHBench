import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic harmonic component with time-varying frequencies
        result = np.sum(np.sin(10 * x) * np.cos(15 * x)) + 0.5 * np.sum(np.sin(25 * x**2))
        
        # Saddle-point attraction mechanism with varying strength
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i]**2 - 25.0) * np.exp(-0.1 * x[i]**2)
        result += 0.3 * saddle_term
        
        # Time-varying harmonic modulation with dynamic phase shifts
        time_mod = 0.0
        for i in range(self.dim):
            phase = np.sin(0.5 * i) * np.cos(0.3 * i)
            time_mod += np.sin(20 * x[i] + phase) * np.cos(15 * x[i] + phase)
        result += 0.2 * time_mod
        
        # Exponentially decaying cross-dimensional couplings
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling_term += np.exp(-dist) * np.sin(10 * (x[i] + x[j]))
        result += 0.15 * coupling_term
        
        # Adaptive gradient modulation with oscillating penalty
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.abs(np.sin(20 * x[i]) * np.cos(15 * x[i]))
        result += 0.25 * grad_mod * np.sin(0.1 * np.sum(x**2))
        
        # Multi-scale fractal-like structure with recursive harmonic components
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(30 * x[i]) * np.cos(25 * x[i]) * np.sin(20 * x[i])
        result += 0.1 * fractal_term
        
        # Add noise-like perturbations with varying amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(50 * x[i]) * np.cos(40 * x[i]) * (1.0 + 0.1 * np.random.rand())
        result += 0.05 * noise
        
        return result