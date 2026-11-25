import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine map component with dynamic coupling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(3.0 * x[i]) * np.sin(7.0 * x[i]) + \
                      0.5 * np.sin(5.0 * x[i]) * np.cos(9.0 * x[i]) + \
                      0.3 * np.sin(2.0 * x[i]) * np.sin(11.0 * x[i])
        
        # Multi-modal radial basis function with time-delayed feedback
        rbfs = 0.0
        for i in range(self.dim):
            if i > 0:
                delay_term = 0.2 * np.exp(-0.5 * ((x[i] - x[i-1])**2))
            else:
                delay_term = 0.0
            
            rbfs += np.exp(-0.5 * ((x[i] - 0.5)**2 + (x[i] + 0.5)**2)) + \
                   0.3 * np.exp(-0.5 * ((x[i] - 1.0)**2 + (x[i] + 1.0)**2)) + \
                   delay_term
        
        # Non-separable trigonometric interactions with dynamic coupling
        trigonometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = 0.5 + 0.5 * np.sin(0.2 * (i + j))
                trigonometric += coupling_strength * (
                    np.sin(4.0 * x[i]) * np.cos(6.0 * x[j]) + 
                    np.cos(5.0 * x[i]) * np.sin(7.0 * x[j])
                )
        
        # Enhanced polynomial terms with variable exponents
        polynomial = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.sin(i)
            polynomial += (x[i]**exp_factor) + 0.1 * (x[i]**(exp_factor + 1)) + \
                         0.01 * (x[i]**(exp_factor + 2))
        
        # Correlation and interaction terms with dynamic weights
        correlation = 0.0
        for i in range(self.dim - 1):
            weight = 0.3 + 0.2 * np.sin(0.5 * i)
            correlation += weight * (x[i] - x[i+1])**2 * np.sin(3.0 * x[i])
        
        # Additional multi-modal component with chaotic feedback
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.4 * np.sin(8.0 * x[i]) * np.cos(9.0 * x[i]) + \
                         0.2 * np.sin(13.0 * x[i]) * np.cos(14.0 * x[i]) + \
                         0.1 * np.sin(15.0 * x[i]) * np.cos(16.0 * x[i])
        
        # Dynamic scaling factor based on dimension and chaotic behavior
        dynamic_scale = 1.0 + 0.2 * np.log(self.dim + 1) + \
                       0.1 * np.sin(self.dim * 0.3) + \
                       0.05 * np.cos(self.dim * 0.7)
        
        # Combine all components with dynamic weights
        total = dynamic_scale * (0.2 * polynomial + 
                                0.3 * chaotic + 
                                0.25 * rbfs + 
                                0.15 * trigonometric + 
                                0.1 * correlation + 
                                0.1 * multimodal)
        
        return total