import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic harmonic component with enhanced nonlinearity
        result = np.sum(np.sin(12 * x) * np.cos(18 * x)) + 0.6 * np.sum(np.sin(30 * x**2))
        
        # Enhanced saddle-point attraction mechanism with stronger basin effects
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i]**2 - 25.0) * np.exp(-0.15 * x[i]**2)
        result += 0.4 * saddle_term
        
        # Modified time-varying harmonic modulation with phase coupling
        time_mod = 0.0
        for i in range(self.dim):
            phase = np.sin(0.6 * i) * np.cos(0.4 * i)
            time_mod += np.sin(25 * x[i] + phase) * np.cos(20 * x[i] + phase)
        result += 0.25 * time_mod
        
        # Enhanced exponentially decaying cross-dimensional couplings with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling_term += np.exp(-dist * 0.5) * np.sin(12 * (x[i] + x[j]))
        result += 0.2 * coupling_term
        
        # Improved adaptive gradient modulation with enhanced penalty
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.abs(np.sin(25 * x[i]) * np.cos(20 * x[i]))
        result += 0.3 * grad_mod * np.sin(0.15 * np.sum(x**2))
        
        # Enhanced multi-scale fractal-like structure with recursive components
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(35 * x[i]) * np.cos(30 * x[i]) * np.sin(25 * x[i])
        result += 0.15 * fractal_term
        
        # Reduced noise perturbations with controlled amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(45 * x[i]) * np.cos(35 * x[i]) * (1.0 + 0.05 * np.random.rand())
        result += 0.03 * noise
        
        return result