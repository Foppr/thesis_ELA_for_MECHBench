import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay potential with multiple peaks
        exp_potential = 0.0
        for i in range(self.dim):
            exp_potential += np.exp(-2 * np.abs(x_norm[i])) * np.cos(5 * np.pi * x_norm[i])
        
        # Trigonometric coupling with varying interaction strengths
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(2 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(3 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Gradient-based attraction fields with varying scales
        gradient_field = 0.0
        for i in range(self.dim):
            gradient_field += (x_norm[i]**2) * np.sin(4 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Ruggedness through high-frequency sinusoids and cubic terms
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += np.sin(15 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i]) + 0.3 * x_norm[i]**3
        
        # Cross-dimensional interaction with Gaussian kernels
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.exp(-0.5 * ((x_norm[i] - x_norm[j])**2)) * np.sin(6 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Add noise term for additional challenge
        noise = 0.01 * np.random.random()
        
        return 1.2 * exp_potential + 0.8 * trig_coupling + 0.6 * gradient_field + 0.9 * ruggedness + 0.7 * cross_interaction + noise