import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic gradient component with nested sinusoids
        chaotic_grad = 0.0
        for i in range(self.dim):
            chaotic_grad += np.sin(10.0 * x_scaled[i]) * np.cos(7.0 * x_scaled[i]) * np.sin(3.0 * x_scaled[i])
        
        # Nested multi-scale sinusoidal modulations
        nested_mod = 0.0
        for i in range(self.dim):
            nested_mod += (1.0 + 0.5 * np.sin(20.0 * x_scaled[i])) * \
                         (1.0 + 0.3 * np.cos(15.0 * x_scaled[i])) * \
                         (1.0 + 0.4 * np.sin(8.0 * x_scaled[i]))
        
        # Dynamic scaling factor based on distance from center
        r = np.sqrt(np.sum(x_scaled**2))
        dynamic_scale = 1.0 + 0.8 * np.exp(-r**2 / 2.0) + 0.3 * np.sin(5.0 * r)
        
        # Adaptive penalty with multiple constraint violations
        penalty = 0.0
        for i in range(self.dim):
            if abs(x_scaled[i]) > 0.8:
                penalty += 10.0 * (abs(x_scaled[i]) - 0.8)**2
            if x_scaled[i] * x_scaled[(i+1) % self.dim] < -0.5:
                penalty += 5.0 * (x_scaled[i] * x_scaled[(i+1) % self.dim] + 0.5)**2
        
        # Multi-modal structure with varying amplitude and frequency
        modal_structure = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.7 * np.sin(12.0 * x_scaled[i])
            freq = 5.0 + 3.0 * np.cos(8.0 * x_scaled[i])
            modal_structure += amp * np.sin(freq * x_scaled[i] + 2.0 * np.cos(4.0 * x_scaled[i]))
        
        # Cross-dimensional coupling with dynamic weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = 0.5 + 0.5 * np.sin(2.0 * dist)
                cross_coupling += weight * np.sin(15.0 * dist) * np.cos(10.0 * dist)
        
        # Combine all components with dynamic weighting
        result = (dynamic_scale * 
                 (0.6 * chaotic_grad + 0.3 * nested_mod + 0.4 * modal_structure + 0.2 * cross_coupling) + 
                 0.1 * penalty)
        
        return result