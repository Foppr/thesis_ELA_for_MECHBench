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
            # Modified condition number with different sine modulation
            cond_num = 10**(0.7 * np.sin(0.9 * i) + 1.2)
            # Gradient-based term with altered chaotic scaling
            chaotic_grad += cond_num * x[i] * np.cos(2.5 * x[i] + 0.6 * np.sin(1.3 * i))
        
        # Multi-scale periodic modulation with changed frequencies and amplitudes
        periodic = 0
        for i in range(self.dim):
            freq = 2.5 + 1.2 * np.sin(0.8 * i)
            amp = 1.2 + 0.3 * np.cos(1.0 * i)
            periodic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
        
        # Enhanced saddle point landscape with modified hyperbolic tangent interactions
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Changed interaction term with different scaling
                interaction = np.tanh(0.8 * x[i]) * np.tanh(0.7 * x[j])
                saddle += interaction * (x[i]**3 + x[j]**3)
        
        # Variable conditioning with modified exponential scaling
        variable_cond = 0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.6 * np.sin(0.7 * i + 1.5)
            variable_cond += scale_factor * np.exp(-0.3 * x[i]**2) * x[i]**5
        
        # Combined landscape with updated weights
        return 0.8 * chaotic_grad + 1.0 * periodic + 1.0 * saddle + 1.2 * variable_cond