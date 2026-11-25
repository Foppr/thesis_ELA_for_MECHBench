import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial component with mixed degrees
        poly_term = np.sum(0.5 * x_scaled**6 + 0.3 * x_scaled**4 + 0.7 * x_scaled**2)
        
        # Trigonometric component with varying frequencies and amplitudes
        trig_term = np.sum(2.0 * np.sin(3 * np.pi * x_scaled) + 1.5 * np.cos(5 * np.pi * x_scaled) + 
                          0.8 * np.sin(7 * np.pi * x_scaled))
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rb_term = 0.0
        for i in range(len(centers)):
            if i < self.dim:
                rb_term += np.exp(-5.0 * (x_scaled[i] - centers[i%len(centers)])**2)
        
        # Interaction term between all dimensions with varying coupling strengths
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.3 * np.sin(np.pi * (x_scaled[i] - x_scaled[j])) * np.cos(2 * np.pi * (x_scaled[i] + x_scaled[j]))
        
        # Cross-term component with mixed interactions
        cross_term = np.sum(x_scaled[:-1]**2 * x_scaled[1:] + 0.5 * x_scaled[:-1] * x_scaled[1:]**3)
        
        # Add noise-like perturbation to increase complexity
        noise = 0.1 * np.random.rand()
        
        return poly_term + trig_term + rb_term + interaction_term + cross_term + noise