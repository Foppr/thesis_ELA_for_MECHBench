import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Base quadratic term with conditioning
        quadratic = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 2)  # Increased frequency range
            amp = 1.8 + 1.0 * np.sin(i * 0.6)  # Increased amplitude variation
            sinusoidal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.3 * (x_normalized[i] - 0.2)**2)
        
        # Add a complex penalty term with multiple local minima and higher-order terms
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.5 * (x_normalized[i]**10 - 5 * x_normalized[i]**8 + 10 * x_normalized[i]**6 - 10 * x_normalized[i]**4 + 5 * x_normalized[i]**2 - 1)
            
        # Add a global minimum at origin with additional penalty terms
        global_penalty = 0.0
        for i in range(self.dim):
            global_penalty += 0.2 * np.sin(15 * np.pi * x_normalized[i]) * np.exp(-0.15 * x_normalized[i]**2)
            
        # Add a highly oscillatory term to increase complexity with cross-dimension interactions
        oscillatory = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                oscillatory += 0.25 * np.sin(25 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(20 * np.pi * (x_normalized[i] - x_normalized[j]))
                
        # Add a central repulsion term to challenge basin attraction
        center_repulsion = 0.0
        dist_from_origin = np.sqrt(np.sum(x_normalized**2))
        center_repulsion = 2.5 * np.exp(-0.5 * dist_from_origin**2) * (1.0 + 0.6 * np.sin(12 * dist_from_origin))
        
        # Add a new chaotic component for increased complexity with modified parameters
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.25 * np.sin(45 * np.pi * x_normalized[i]) * np.cos(35 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Add a new term to improve fitness score and reduce bias
        bias_reduction = 0.0
        for i in range(self.dim):
            bias_reduction += 0.06 * np.sin(8 * np.pi * x_normalized[i]) * np.cos(6 * np.pi * x_normalized[i])
            
        # Add a new term to increase basin of attraction complexity
        basin_complexity = 0.0
        for i in range(self.dim):
            basin_complexity += 0.15 * np.sin(20 * np.pi * x_normalized[i]) * np.cos(15 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Add new cross-dimensional exponential interaction term
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += 0.2 * np.exp(-1.5 * (x_normalized[i]**2 + x_normalized[j]**2)) * np.sin(30 * np.pi * (x_normalized[i] - x_normalized[j]))
        
        # Add a new term to balance the landscape and reduce bias
        balance_term = 0.0
        for i in range(self.dim):
            balance_term += 0.1 * np.sin(18 * np.pi * x_normalized[i]) * np.cos(12 * np.pi * x_normalized[i]) * np.exp(-0.1 * x_normalized[i]**2)
        
        # Add a new interaction term with adaptive frequency modulation
        adaptive_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                adaptive_interaction += 0.15 * np.sin(20 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(15 * np.pi * (x_normalized[i] - x_normalized[j])) * np.exp(-0.1 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        return quadratic + sinusoidal + penalty + global_penalty + oscillatory + center_repulsion + chaotic + bias_reduction + basin_complexity + cross_exp + balance_term + adaptive_interaction