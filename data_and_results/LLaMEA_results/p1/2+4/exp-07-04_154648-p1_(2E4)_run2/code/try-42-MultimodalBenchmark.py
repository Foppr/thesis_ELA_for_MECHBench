import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 20)
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with frequency modulation
        sin_term = 0.0
        for i in range(8):
            freq = 2**(i+1) * (1 + 0.3 * np.sin(0.5 * x_norm.sum()))
            sin_term += np.sin(freq * x_norm) * np.cos(freq * x_norm**1.3)
        
        # Enhanced multi-modal RBF with dynamic widths
        rbf_sum = 0.0
        for i in range(20):
            diff = x_norm - self.rbf_centers[i]
            # Dynamic width based on position and time
            dynamic_width = self.rbf_widths[i] * (1 + 0.2 * np.sin(x_norm.sum() + self.time_phase[i%self.dim]))
            rbf_sum += np.exp(-0.5 * np.sum((diff / dynamic_width)**2))
        
        # Time-dependent noise with chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i] * 7 + self.time_phase[i]) * np.cos(x_norm[i] * 5 + self.time_phase[i])
        noise *= 0.2 * (1 + 0.5 * np.sin(x_norm.sum() * 3))
        
        # Complex cross-dimensional coupling with polynomial interactions
        cross_interaction = 0.0
        for i in range(self.dim - 2):
            term = (x_norm[i]**4 + x_norm[i+1]**4 + x_norm[i+2]**4) * np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1] + x_norm[i+2]))
            cross_interaction += term * np.cos(0.5 * x_norm[i] * x_norm[i+1])
        
        # Polynomial and exponential components for increased complexity
        poly_term = np.sum(x_norm**6) * 0.05
        exp_term = np.sum(np.exp(-x_norm**2) * np.sin(x_norm))
        
        # Global minimum at origin with additional scaling
        return sin_term + rbf_sum + noise + cross_interaction + poly_term + exp_term + 0.01 * np.sum(np.abs(x_norm)**3.5)