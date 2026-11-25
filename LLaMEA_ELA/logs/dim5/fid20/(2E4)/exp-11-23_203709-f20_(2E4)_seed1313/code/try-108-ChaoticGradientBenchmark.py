import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with varying condition numbers
        chaotic_grad = 0
        for i in range(self.dim):
            # Dynamic condition number based on chaotic sine modulation
            cond_num = 10**(0.5 * np.sin(0.8 * i) + 1.0)
            # Gradient-based term with chaotic scaling
            chaotic_grad += cond_num * x[i] * np.cos(2.0 * x[i] + 0.5 * np.sin(1.2 * i))
        
        # Multi-scale periodic modulation with varying frequencies and amplitudes
        periodic = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.7 * i)
            amp = 1.0 + 0.5 * np.cos(0.9 * i)
            periodic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Saddle point landscape with hyperbolic tangent interactions
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.tanh(x[i]) * np.tanh(x[j])
                saddle += interaction * (x[i]**2 + x[j]**2)
        
        # Variable conditioning with exponential scaling
        variable_cond = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.8 * np.sin(0.6 * i + 1.0)
            variable_cond += scale_factor * np.exp(-0.5 * x[i]**2) * x[i]**4
        
        # Combined landscape with dynamic weights
        return 0.7 * chaotic_grad + 1.2 * periodic + 0.9 * saddle + 1.1 * variable_cond