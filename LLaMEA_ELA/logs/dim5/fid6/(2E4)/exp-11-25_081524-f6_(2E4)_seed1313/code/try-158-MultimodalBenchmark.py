import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle-point component with logistic map dynamics
        chaotic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]  # Periodic boundary
            else:
                x_prev = x[i-1]
            
            chaotic_term += np.sin(r * x_prev) * np.cos(x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Embedded harmonic potentials with varying frequencies and amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.4 * i)
            amp = 1.0 + 0.3 * np.cos(0.3 * i)
            harmonic_term += amp * (np.sin(freq * x[i]) ** 2) * np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional coupling with polynomial interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i] ** 2) * (x[j] ** 3) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Gradient complexity modifier with adaptive noise
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]) * (1.0 + 0.1 * np.random.rand())
        
        # Global scaling factor based on solution distribution
        mean_x = np.mean(x)
        std_x = np.std(x)
        scale_factor = 1.0 + 0.2 * np.tanh(std_x - 1.0) + 0.1 * np.sin(mean_x)
        
        return (chaotic_term + harmonic_term + coupling_term + noise) * scale_factor