import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-2 * np.abs(x_norm)) * np.sin(5 * x_norm))
        
        # Trigonometric interference pattern with non-uniform frequencies
        trig_interference = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            trig_interference += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Asymmetric polynomial potential with mixed even/odd powers
        asym_poly = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                asym_poly += 0.6 * x_norm[i]**4 + 0.3 * x_norm[i]**2
            else:
                asym_poly += 0.5 * x_norm[i]**5 + 0.4 * x_norm[i]**3
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                cross_coupling += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Saddle-like structure with hyperbolic tangent components
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(2 * x_norm[i]) * x_norm[i]**2
        
        # Add a small random noise component for added complexity
        noise = 0.01 * np.random.random()
        
        return 1.5 * exp_decay + 0.8 * trig_interference + 0.6 * asym_poly + 0.4 * cross_coupling + 0.3 * saddle + noise