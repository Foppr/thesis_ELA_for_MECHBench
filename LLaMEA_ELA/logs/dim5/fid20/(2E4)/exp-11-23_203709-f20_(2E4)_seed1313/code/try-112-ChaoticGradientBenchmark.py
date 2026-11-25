import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with varying condition numbers and enhanced chaos
        chaotic_grad = 0
        for i in range(self.dim):
            # Enhanced dynamic condition number with chaotic sine modulation
            cond_num = 15**(0.7 * np.sin(1.2 * i + 0.5) + 1.5)
            # Enhanced gradient-based term with chaotic scaling and additional sine coupling
            chaotic_grad += cond_num * x[i] * np.cos(3.0 * x[i] + 0.8 * np.sin(1.5 * i)) * np.sin(0.6 * x[i])
        
        # Multi-scale periodic modulation with varying frequencies, amplitudes, and coupling
        periodic = 0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.9 * i + 1.0)
            amp = 1.5 + 0.8 * np.cos(1.1 * i + 0.7)
            # Additional coupling term for enhanced multimodality
            coupling = np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0) * np.sin(0.5 * x[i])
            periodic += amp * coupling
        
        # Enhanced saddle point landscape with hyperbolic tangent interactions and cross-dimensional coupling
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced interaction with chaotic coupling
                interaction = np.tanh(x[i]) * np.tanh(x[j]) * np.sin(0.4 * (x[i] + x[j]))
                saddle += interaction * (x[i]**2 + x[j]**2 + 0.5 * x[i] * x[j])
        
        # Variable conditioning with exponential scaling and enhanced chaotic modulation
        variable_cond = 0
        for i in range(self.dim):
            scale_factor = 1.5 + 1.2 * np.sin(0.8 * i + 1.2)
            # Enhanced exponential scaling with chaotic modulation
            variable_cond += scale_factor * np.exp(-0.3 * x[i]**2) * x[i]**5 * np.cos(1.3 * x[i])
        
        # Additional chaotic sine coupling component for enhanced multimodality
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_component += np.sin(2.0 * x[i] + 1.5 * x[j]) * np.cos(1.8 * x[i] - 0.9 * x[j])
        
        # Combined landscape with dynamic weights and enhanced chaotic interactions
        return 0.9 * chaotic_grad + 1.5 * periodic + 1.2 * saddle + 1.3 * variable_cond + 0.8 * coupling_component