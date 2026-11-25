import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with directional sensitivity
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-0.5 * (x[i] / 2.0)**2) * np.sin(3.0 * x[i])
        
        # Trigonometric coupling with phase interactions
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_diff = np.abs(np.sin(x[i]) - np.cos(x[j]))
                trig_coupling += np.sin(5.0 * phase_diff) * np.cos(4.0 * phase_diff)
        
        # Adaptive conditioning based on dimension and position
        adaptive_cond = 1.0 + 0.3 * np.sin(0.2 * self.dim) * np.cos(0.1 * np.sum(x**2))
        
        # Plateau region with polynomial smoothing
        plateau = 0.0
        for i in range(self.dim):
            plateau += (x[i]**4 - 6.0 * x[i]**2 + 9.0) * np.exp(-0.1 * x[i]**2)
        
        # Sharp gradient component with multi-directional peaks
        gradients = 0.0
        for i in range(self.dim):
            gradients += np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) + np.tanh(2.0 * x[i])
        
        # Combine all components with dynamic weights
        total = adaptive_cond * (0.25 * exp_decay + 0.35 * trig_coupling + 0.2 * plateau + 0.2 * gradients)
        
        # Add stochastic perturbations for increased complexity
        noise = 0.02 * np.sum(np.random.randn(self.dim) * np.sin(40.0 * x))
        
        return total + noise