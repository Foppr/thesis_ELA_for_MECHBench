import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for stability
        self.chaotic_params = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient component with time-delayed feedback
        chaotic_sum = 0.0
        for i in range(self.dim):
            # Polynomial chaos expansion terms
            poly_term = (x_norm[i]**2 + 0.3 * x_norm[i]**3 + 0.1 * x_norm[i]**4)
            
            # Chaotic modulation with delayed feedback
            delay_feedback = 0.0
            if i > 0:
                delay_feedback = 0.5 * np.sin(self.chaotic_params[i-1] * x_norm[i-1])
            
            chaotic_sum += poly_term + delay_feedback
            
        # Saddle-point region with mixed curvature
        saddle_sum = 0.0
        for i in range(self.dim):
            # Create regions with both positive and negative curvatures
            if i % 2 == 0:
                saddle_sum += (x_norm[i]**2 - 0.5 * x_norm[i]**4)  # Quadratic + quartic
            else:
                saddle_sum += (0.3 * x_norm[i]**3 - 0.1 * x_norm[i]**5)  # Cubic + quintic
        
        # Cross-dimensional coupling with asymmetric interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction terms
                asym_interaction = (np.sin(x_norm[i] * x_norm[j]) * 
                                  np.exp(-0.5 * (x_norm[i] - x_norm[j])**2))
                coupling += asym_interaction
        
        # Add noise-like chaotic perturbations with varying amplitudes
        noise = 0.0
        for i in range(self.dim):
            noise += 0.2 * np.sin(10 * x_norm[i]) * np.cos(8 * x_norm[i]) + \
                     0.1 * np.sin(15 * x_norm[i]) * np.cos(12 * x_norm[i])
        
        # Combine all components
        result = chaotic_sum + 0.5 * saddle_sum + 0.3 * coupling + 0.1 * noise
        
        return result